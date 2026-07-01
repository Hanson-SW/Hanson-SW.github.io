import json
import os
from datetime import datetime, timedelta, timezone

import akshare as ak
import pandas as pd
import yfinance as yf


DATA_DIR = "data"

# Database tier 1: assets directly useful for the current Markowitz and
# backtest demos. Keep symbols in the same exchange-prefixed format consumed
# by the existing front-end pages.
AKSHARE_INDEX_POOL = {
    "sh000001": {
        "name_zh": "上证指数",
        "name_en": "SSE Composite",
        "asset_class": "equity_index",
        "region": "China A-share",
        "style": "broad_market",
    },
    "sz399001": {
        "name_zh": "深证成指",
        "name_en": "SZSE Component",
        "asset_class": "equity_index",
        "region": "China A-share",
        "style": "broad_market",
    },
    "sz399006": {
        "name_zh": "创业板指",
        "name_en": "ChiNext Index",
        "asset_class": "equity_index",
        "region": "China A-share",
        "style": "growth",
    },
    "sh000300": {
        "name_zh": "沪深300",
        "name_en": "CSI 300",
        "asset_class": "equity_index",
        "region": "China A-share",
        "style": "large_cap",
    },
    "sz399300": {
        "name_zh": "沪深300(深)",
        "name_en": "CSI 300 (SZ)",
        "asset_class": "equity_index",
        "region": "China A-share",
        "style": "large_cap",
    },
    "sh000016": {
        "name_zh": "上证50",
        "name_en": "SSE 50",
        "asset_class": "equity_index",
        "region": "China A-share",
        "style": "mega_cap",
    },
    "sh000905": {
        "name_zh": "中证500",
        "name_en": "CSI 500",
        "asset_class": "equity_index",
        "region": "China A-share",
        "style": "mid_cap",
    },
    "sh000852": {
        "name_zh": "中证1000",
        "name_en": "CSI 1000",
        "asset_class": "equity_index",
        "region": "China A-share",
        "style": "small_cap",
    },
    "sh000688": {
        "name_zh": "科创50",
        "name_en": "STAR 50",
        "asset_class": "equity_index",
        "region": "China A-share",
        "style": "technology_growth",
    },
    "sh000906": {
        "name_zh": "中证800",
        "name_en": "CSI 800",
        "asset_class": "equity_index",
        "region": "China A-share",
        "style": "large_mid_cap",
    },
    "sh000985": {
        "name_zh": "中证全指",
        "name_en": "CSI All Share",
        "asset_class": "equity_index",
        "region": "China A-share",
        "style": "all_share",
    },
    "sh000922": {
        "name_zh": "中证红利",
        "name_en": "CSI Dividend",
        "asset_class": "equity_index",
        "region": "China A-share",
        "style": "dividend",
    },
}

YFINANCE_POOL = {
    "us_oneq": {
        "source_symbol": "ONEQ",
        "name_zh": "纳斯达克综合ETF",
        "name_en": "Fidelity Nasdaq Composite ETF",
        "asset_class": "equity_etf",
        "region": "United States",
        "style": "technology_growth",
    },
    "gold_gld": {
        "source_symbol": "GLD",
        "name_zh": "黄金ETF",
        "name_en": "SPDR Gold Shares",
        "asset_class": "commodity_etf",
        "region": "Global",
        "style": "gold",
    },
    "semi_soxx": {
        "source_symbol": "SOXX",
        "name_zh": "半导体ETF",
        "name_en": "iShares Semiconductor ETF",
        "asset_class": "sector_etf",
        "region": "United States",
        "style": "semiconductor",
    },
    "health_xlv": {
        "source_symbol": "XLV",
        "name_zh": "医药健康ETF",
        "name_en": "Health Care Select Sector SPDR",
        "asset_class": "sector_etf",
        "region": "United States",
        "style": "healthcare",
    },
}


def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)


def now_utc_iso():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def normalize_price_frame(df):
    required_cols = ["date", "open", "close", "low", "high"]
    df = df[required_cols].copy()
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    for col in ["open", "close", "low", "high"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["open", "close", "low", "high"])
    df = df.sort_values(by="date").drop_duplicates(subset=["date"], keep="last")
    return df.reset_index(drop=True)


def build_quality_record(symbol, meta, df, status, error=None):
    if df is None or df.empty:
        return {
            "symbol": symbol,
            "name_zh": meta["name_zh"],
            "status": status,
            "rows": 0,
            "start_date": None,
            "end_date": None,
            "missing_price_rows": None,
            "error": error,
        }

    return {
        "symbol": symbol,
        "name_zh": meta["name_zh"],
        "status": status,
        "rows": int(len(df)),
        "start_date": df["date"].iloc[0],
        "end_date": df["date"].iloc[-1],
        "missing_price_rows": 0,
        "error": error,
    }


def load_existing_json_frame(symbol):
    file_path = os.path.join(DATA_DIR, f"{symbol}.json")
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        payload = json.load(f)
    dates = payload.get("dates", [])
    values = payload.get("values", [])
    rows = []
    for date, value in zip(dates, values):
        if len(value) < 4:
            continue
        rows.append({
            "date": date,
            "open": value[0],
            "close": value[1],
            "low": value[2],
            "high": value[3],
        })
    if not rows:
        return None
    return normalize_price_frame(pd.DataFrame(rows))


def fallback_existing_record(symbol, meta, error):
    df = load_existing_json_frame(symbol)
    if df is None or df.empty:
        return build_quality_record(symbol, meta, None, "failed", error)
    print(f"STALE {symbol}: keeping existing cache after fetch failure")
    return build_quality_record(symbol, meta, df, "stale_cache", error)


def save_index_json(symbol, meta, df, source):
    file_path = os.path.join(DATA_DIR, f"{symbol}.json")
    payload = {
        "meta": {
            "symbol": symbol,
            "name_zh": meta["name_zh"],
            "name_en": meta["name_en"],
            "asset_class": meta["asset_class"],
            "region": meta["region"],
            "style": meta["style"],
            "frequency": "daily",
            "price_type": "index_ohlc",
            "source": source,
            "updated_at": now_utc_iso(),
        },
        "dates": df["date"].tolist(),
        # Preserve the current front-end contract:
        # values[i] = [open, close, low, high]
        "values": df[["open", "close", "low", "high"]].round(6).values.tolist(),
    }
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, separators=(",", ":"))


def update_index_data(symbol, meta):
    print(f"Fetching {symbol} {meta['name_zh']} ...")
    try:
        raw = ak.stock_zh_index_daily(symbol=symbol)
        df = normalize_price_frame(raw)
        if df.empty:
            raise ValueError("empty normalized price frame")
        save_index_json(symbol, meta, df, "AkShare stock_zh_index_daily")
        print(f"OK {symbol}: {len(df)} rows, {df['date'].iloc[0]} -> {df['date'].iloc[-1]}")
        return build_quality_record(symbol, meta, df, "ok")
    except Exception as exc:
        print(f"FAILED {symbol}: {exc}")
        return fallback_existing_record(symbol, meta, str(exc))


def normalize_yfinance_frame(df):
    if df.empty:
        return pd.DataFrame(columns=["date", "open", "close", "low", "high"])

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df.reset_index()
    date_col = "Date" if "Date" in df.columns else "Datetime"
    df = df.rename(columns={
        date_col: "date",
        "Open": "open",
        "Close": "close",
        "Low": "low",
        "High": "high",
    })
    return normalize_price_frame(df)


def download_yfinance_history(source_symbol, end_date):
    return yf.download(
        source_symbol,
        start="1998-01-01",
        end=end_date,
        interval="1d",
        auto_adjust=False,
        progress=False,
        threads=False,
    )


def update_yfinance_data(symbol, meta):
    source_symbol = meta["source_symbol"]
    print(f"Fetching {symbol} {meta['name_zh']} from yfinance:{source_symbol} ...")
    try:
        end_date = (datetime.now(timezone.utc).date() + timedelta(days=1)).isoformat()
        raw = download_yfinance_history(source_symbol, end_date)
        df = normalize_yfinance_frame(raw)
        if df.empty:
            raw = download_yfinance_history(source_symbol, "2025-07-01")
            df = normalize_yfinance_frame(raw)
        if df.empty:
            raise ValueError("empty normalized price frame")
        save_index_json(symbol, meta, df, f"yfinance {source_symbol}")
        print(f"OK {symbol}: {len(df)} rows, {df['date'].iloc[0]} -> {df['date'].iloc[-1]}")
        return build_quality_record(symbol, meta, df, "ok")
    except Exception as exc:
        print(f"FAILED {symbol}: {exc}")
        return fallback_existing_record(symbol, meta, str(exc))


def write_manifest(quality_records):
    usable_symbols = {row["symbol"] for row in quality_records if row["status"] in ("ok", "stale_cache")}
    assets = []
    for symbol, meta in {**AKSHARE_INDEX_POOL, **YFINANCE_POOL}.items():
        if symbol not in usable_symbols:
            continue
        q = next(row for row in quality_records if row["symbol"] == symbol)
        assets.append({
            "symbol": symbol,
            "file": f"data/{symbol}.json",
            "name_zh": meta["name_zh"],
            "name_en": meta["name_en"],
            "asset_class": meta["asset_class"],
            "region": meta["region"],
            "style": meta["style"],
            "frequency": "daily",
            "start_date": q["start_date"],
            "end_date": q["end_date"],
            "rows": q["rows"],
            "status": q["status"],
        })

    manifest = {
        "version": 1,
        "generated_at": now_utc_iso(),
        "source": "AkShare stock_zh_index_daily",
        "assets": assets,
    }
    with open(os.path.join(DATA_DIR, "asset_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)


def write_quality_report(quality_records):
    usable_count = sum(1 for row in quality_records if row["status"] in ("ok", "stale_cache"))
    report = {
        "generated_at": now_utc_iso(),
        "total_assets": len(quality_records),
        "ok_assets": sum(1 for row in quality_records if row["status"] == "ok"),
        "stale_cache_assets": sum(1 for row in quality_records if row["status"] == "stale_cache"),
        "usable_assets": usable_count,
        "failed_assets": sum(1 for row in quality_records if row["status"] not in ("ok", "stale_cache")),
        "records": quality_records,
    }
    with open(os.path.join(DATA_DIR, "quality_report.json"), "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)


def main():
    ensure_data_dir()
    print(f"Starting market database update at {datetime.now()}")

    quality_records = []
    for symbol, meta in AKSHARE_INDEX_POOL.items():
        quality_records.append(update_index_data(symbol, meta))
    for symbol, meta in YFINANCE_POOL.items():
        quality_records.append(update_yfinance_data(symbol, meta))

    write_manifest(quality_records)
    write_quality_report(quality_records)

    stale = [row["symbol"] for row in quality_records if row["status"] == "stale_cache"]
    failed = [row["symbol"] for row in quality_records if row["status"] not in ("ok", "stale_cache")]
    if stale:
        print(f"Completed with stale cache symbols: {', '.join(stale)}")
    if failed:
        print(f"Completed with failed symbols: {', '.join(failed)}")
    else:
        print("Completed successfully. All configured assets are usable.")


if __name__ == "__main__":
    main()
