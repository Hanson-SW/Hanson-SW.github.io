import yfinance as yf
import numpy as np
import json
import os

# 这是我们在网页端提供的智能联想股票池，保证它们都有最新的本地缓存
tickers_list = [
    'AAPL', 'MSFT', 'NVDA', 'TSLA', 'GOOGL', 'AMZN', 'META', 'SPY', 'QQQ',
    '600519.SS', '000858.SZ', '600036.SS', '601318.SS', '002594.SZ', '300750.SZ', '000300.SS', 'BABA'
]

market_data = {}

print("开始拉取股票数据...")

for ticker in tickers_list:
    try:
        # 拉取过去 1 年的历史数据
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1y")

        if hist.empty:
            print(f"[警告] {ticker} 没有拉取到数据，可能代码有误或退市。")
            continue

        # 提取收盘价，清除空值
        closes = hist['Close'].dropna().values
        if len(closes) < 2:
            continue

        current_price = float(closes[-1])

        # 计算对数收益率
        log_returns = np.log(closes[1:] / closes[:-1])
        mean_return = np.mean(log_returns)
        variance = np.var(log_returns, ddof=1)

        # 年化处理 (按252个交易日计算)
        ann_vol = np.sqrt(variance) * np.sqrt(252)
        ann_mu = mean_return * 252 + (ann_vol ** 2) / 2

        # 存入字典，保留对应的小数位数
        market_data[ticker] = {
            "price": round(current_price, 2),
            "vol": round(ann_vol, 3),
            "mu": round(ann_mu, 3)
        }
        print(f"[成功] {ticker} -> 价格: {current_price:.2f}, 波动率: {ann_vol:.3f}, 收益率: {ann_mu:.3f}")

    except Exception as e:
        print(f"[错误] 处理 {ticker} 时发生异常: {e}")

# 将结果保存为 JSON 文件
output_file = 'market_data.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(market_data, f, indent=4)

print(f"数据已成功保存至 {output_file}，共包含 {len(market_data)} 支股票。")
