import os
import pandas as pd
import akshare as ak
from datetime import datetime

# 定义数据存储的目录和文件名
DATA_DIR = "data"
FILE_PATH = os.path.join(DATA_DIR, "sh000001.json")

def initialize_or_update_data():
    # 确保 data 文件夹存在
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        
    print("开始获取上证指数真实历史数据...")
    
    # 使用 AkShare 获取上证指数日线数据 (从1990年开始的全部历史数据)
    # stock_zh_index_daily 接口可以获取指数的历史日线
    try:
        df_new = ak.stock_zh_index_daily(symbol="sh000001")
    except Exception as e:
        print(f"数据抓取失败: {e}")
        return

    # 规范化列名，方便前端读取
    # AkShare 返回的列名通常是 ['date', 'open', 'high', 'low', 'close', 'volume']
    df_new = df_new[['date', 'open', 'close', 'low', 'high', 'volume']]
    
    # 将日期格式化为字符串 (YYYY-MM-DD)
    df_new['date'] = pd.to_datetime(df_new['date']).dt.strftime('%Y-%m-%d')

    # 判断本地是否已经存在历史数据文件
    if os.path.exists(FILE_PATH):
        print("检测到已有历史数据，开始执行增量合并...")
        # 读取旧数据
        df_old = pd.read_json(FILE_PATH)
        
        # 合并新旧数据，并根据日期去重，保留最新的数据
        df_combined = pd.concat([df_old, df_new]).drop_duplicates(subset=['date'], keep='last')
        # 按日期排序
        df_combined = df_combined.sort_values(by='date').reset_index(drop=True)
    else:
        print("未检测到本地数据，正在一次性填充全部历史数据...")
        df_combined = df_new.sort_values(by='date').reset_index(drop=True)

    # 转换为前端方便读取的格式 (ECharts K线图推荐的数组嵌套格式，或者标准的JSON对象)
    # 为了减少文件体积，我们将其转换为包含 dates 和 values 的字典
    result = {
        "dates": df_combined['date'].tolist(),
        # ECharts 的 K线图数值顺序通常是: [开盘价, 收盘价, 最低价, 最高价]
        "values": df_combined[['open', 'close', 'low', 'high']].values.tolist()
    }

    # 保存为 JSON 文件
    import json
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False)
        
    print(f"数据更新成功！当前共包含 {len(result['dates'])} 个交易日的数据。")

if __name__ == "__main__":
    initialize_or_update_data()
