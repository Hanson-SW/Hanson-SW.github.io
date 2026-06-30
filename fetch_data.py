import os
import pandas as pd
import akshare as ak
import json
from datetime import datetime

DATA_DIR = "data"

# 我们配置的 10 大核心指数代码池
INDEX_POOL = {
    "sh000001": "sh000001",  # 上证指数
    "sz399001": "sz399001",  # 深证成指
    "sz399006": "sz399006",  # 创业板指
    "sh000300": "sh000300",  # 沪深300
    "sh000016": "sh000016",  # 上证50
    "sh000905": "sh000905",  # 中证500
    "sh000852": "sh000852",  # 中证1000
    "sz399300": "sz399300",  # 沪深300(深)
    "sh000688": "sh000688",  # 科创50
}

def update_index_data(symbol, filename):
    file_path = os.path.join(DATA_DIR, f"{filename}.json")
    print(f"正在获取 [{symbol}] 的全量历史数据...")
    
    try:
        # 直接抓取全量历史日线数据
        df_new = ak.stock_zh_index_daily(symbol=symbol)
        
        # 提取有效列，严格保证索引1是close（前端通过 values[i][1] 读取收盘价）
        df_new = df_new[['date', 'open', 'close', 'low', 'high']]
        
        # 强制将日期转为标准 YYYY-MM-DD 字符串
        df_new['date'] = pd.to_datetime(df_new['date']).dt.strftime('%Y-%m-%d')
        
        # 剔除价格数据为空的交易日
        df_new = df_new.dropna(subset=['open', 'close', 'low', 'high'])
        
        # 全量覆盖逻辑：排序、去重
        df_new = df_new.sort_values(by='date').drop_duplicates(subset=['date'], keep='last').reset_index(drop=True)

        # 格式化并保存
        result = {
            "dates": df_new['date'].tolist(),
            "values": df_new[['open', 'close', 'low', 'high']].values.tolist()
        }
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False)
        print(f"✅ [{symbol}] 更新成功，共保存 {len(df_new)} 个交易日数据！")
        
    except Exception as e:
        print(f"❌ [{symbol}] 数据抓取失败: {e}")

def main():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        
    print(f"开始批量更新数据，时间: {datetime.now()}")
    for symbol, filename in INDEX_POOL.items():
        update_index_data(symbol, filename)
    print("全部数据更新任务完成！")

if __name__ == "__main__":
    main()
