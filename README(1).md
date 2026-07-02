# Financial Engineering & Quantitative Analysis Portfolio
### 📊 金融工程与量化分析作品集

[![Main Page](https://img.shields.io/badge/Main%20Page-index.md-2563eb?style=for-the-badge&logo=githubpages&logoColor=white)](./index.md)
[![Static Frontend](https://img.shields.io/badge/Architecture-Static%20Frontend-10b981?style=for-the-badge)](#-3-architecture--data-pipeline-项目架构与数据链路)
[![Quant Models](https://img.shields.io/badge/Models-Backtest%20%7C%20MPT%20%7C%20Monte%20Carlo-8b5cf6?style=for-the-badge)](#-2-core-modules-核心模块)

> **Main Portfolio Page / 项目主网页:** [Open `index.md`](./index.md)  
> This repository is designed as a lightweight, GitHub Pages-compatible financial engineering portfolio. It demonstrates front-end quantitative modeling, market data caching, strategy backtesting, and portfolio optimization without requiring a traditional backend server.

---

## 👤 1. Personal Information / 个人信息

| Item / 项目 | Details / 详情 |
| :--- | :--- |
| **Author / 作者** | Shengye (Hanson) Wang / 王盛烨 |
| **Education / 教育背景** | NYU Shanghai · Business & Finance (Business Analytics) <br> 上海纽约大学 · 商业与金融（商业分析方向） |
| **Contact / 联系方式** | 📧 `sw6245@nyu.edu` &nbsp;&nbsp; 📞 `+86 159 0896 3789` |
| **GitHub Profile / GitHub 主页** | [Hanson-SW](https://github.com/Hanson-SW) |
| **Portfolio Homepage / 项目主页** | [`index.md`](./index.md) |

---

## 🚀 2. Core Modules / 核心模块

| Module / 模块 | Core File / 核心文件 | Methodology / 金融工程方法 | Current Functionality / 当前功能 |
| :--- | :--- | :--- | :--- |
| **Portfolio Homepage & Live Quant Engine** <br> 主页与股价路径预测引擎 | [`index.md`](./index.md) | Geometric Brownian Motion, Monte Carlo Simulation <br> 几何布朗运动、蒙特卡洛路径模拟 | Resume/project hub, bilingual interface, price path simulation, probability-density heatmap, export/fullscreen chart tools |
| **A-Share Backtesting System** <br> A股量化策略回测系统 | [`backtest.html`](./backtest.html) | Technical timing, sleeve-based allocation, T+1 execution <br> 双均线、布林带、独立资金池、T+1 执行 | Multi-asset backtest, benchmark comparison, trade records, asset attribution, Data Health panel |
| **Markowitz Asset Allocation Model** <br> Markowitz 资产轮动与量化配置模型 | [`markowitz.html`](./markowitz.html) | Modern Portfolio Theory, robust mean/covariance estimation, QP-style optimization <br> 均值-方差、稳健协方差、组合优化 | Efficient frontier, risk contribution, rolling window rebalancing, stress testing, transaction-cost-aware dynamic mode |

---

## 🛠️ 3. Architecture & Data Pipeline / 项目架构与数据链路

This project follows a **serverless/static-first architecture**. The quant engines run in the browser using vanilla JavaScript and ECharts, while market data is stored as lightweight JSON files that can be updated through GitHub Actions.

本项目采用 **纯前端 / 静态优先架构**。模型运算主要在浏览器端完成，行情数据以轻量 JSON 文件形式存储，并可通过 GitHub Actions 自动更新。

### Frontend / 前端

- **HTML5 + CSS3 + Vanilla JavaScript**: no heavy framework dependency, suitable for GitHub Pages deployment.
- **Apache ECharts**: interactive net value curves, efficient frontier scatter plots, heatmaps, zoom tools, and report-style visualizations.
- **Responsive UI**: mobile-width compatibility has been considered for the homepage, Backtest, and Markowitz pages.
- **Bilingual display**: Chinese/English language switching across the main models.

### Data Layer / 数据层

- `data/asset_manifest.json`: unified asset list for both `backtest.html` and `markowitz.html`.
- `data/quality_report.json`: records asset update status, row count, date coverage, failure reason, and stale-cache status.
- `data/*.json`: compact historical price files using the compatible structure `dates + values`.
- Browser `localStorage` cache: improves cold-start experience and allows fallback when network requests fail.
- Built-in fallback asset pool: prevents the page from becoming blank if the manifest or data files fail to load.

### Data Sources / 数据源

- **AkShare**: A-share indices such as CSI 300, SSE 50, CSI 500, CSI 1000, STAR 50, CSI Dividend, etc.
- **yfinance**: lightweight global ETFs such as ONEQ, GLD, SOXX, and XLV.
- **GitHub Actions**: supports scheduled updates and manual dispatch while keeping the repository deployable as a static site.

---

## 🔍 4. Model Details / 模型说明

### 4.1 Live Quant Engine / 股价路径预测引擎

The homepage includes a Monte Carlo simulation module for price path forecasting. Users can adjust ticker, current price, volatility, expected return, number of paths, and horizon. The model renders simulated paths and a probability-density heatmap to visualize uncertainty over time.

主页内置蒙特卡洛股价路径预测模块，支持调整股票代码、当前价格、波动率、期望收益、模拟路径数和预测天数，并通过概率密度热力图展示未来价格分布的不确定性。

**Current strengths / 当前优势**

- Lightweight and visually intuitive.
- Good for demonstrating stochastic process intuition.
- Suitable for front-end-only implementation.

**Known limitations / 已知限制**

- GBM assumes constant drift and volatility, which is a simplified market assumption.
- It does not yet include volatility clustering, jumps, regime switching, or option-implied volatility surfaces.

### 4.2 A-Share Backtesting System / A股回测系统

The backtesting module evaluates rule-based allocation and timing strategies. It includes dual moving average and Bollinger Band signals, independent asset sleeves, strict T+1 execution logic, cash-pool treatment, benchmark comparison, trade details, and attribution panels.

回测模块用于评估规则型资产配置与择时策略，包含双均线、布林带、逐资产独立资金池、严格 T+1 执行、现金池处理、基准对比、交易明细与资产归因面板。

**Current strengths / 当前优势**

- More credible than a simple chart demo because it records trades, rules, and attribution.
- T+1 execution helps reduce look-ahead bias.
- Data Health makes data availability transparent.

**Known limitations / 已知限制**

- Current strategies are still relatively simple technical rules.
- It does not yet support full order-book simulation, intraday execution, capacity constraints, or benchmark-relative portfolio construction.
- For professional-grade research, more sample-splitting, walk-forward validation, and statistical significance tests should be added.

### 4.3 Markowitz Asset Allocation Model / Markowitz 资产配置模型

The Markowitz module implements modern portfolio theory with robust input estimation. It supports Monte Carlo sampling, QP-style optimization, rolling windows, weight caps, transaction costs, stress scenarios, efficient frontier visualization, and risk contribution display.

Markowitz 模块基于现代投资组合理论，加入了稳健输入估计、蒙特卡洛采样、QP 风格优化、滚动窗口、单资产权重上限、交易成本、压力测试、有效前沿和风险贡献展示。

**Current strengths / 当前优势**

- More robust than a basic mean-variance demo because it includes winsorized returns, mean shrinkage, covariance shrinkage, and risk contribution.
- Efficient frontier and stress testing improve interpretability.
- Rolling mode makes the model closer to real portfolio rebalancing.

**Known limitations / 已知限制**

- Mean-variance optimization is highly sensitive to expected-return assumptions.
- The current front-end environment limits the scale of asset universe and the complexity of solvers.
- A more rigorous version could add bootstrap confidence intervals, out-of-sample evaluation, and alternative risk objectives.

---

## 💻 5. Setup & Deployment / 运行与部署指南

### Option A: GitHub Pages / GitHub Pages 部署

Push the repository to GitHub and enable GitHub Pages. The main page is expected to render from:

```text
./index.md
```

Depending on the GitHub Pages/Jekyll configuration, the public homepage may render as the repository root or as `index.html`.

### Option B: Local Static Server / 本地静态服务器

For the HTML model pages, run:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/backtest.html
http://localhost:8000/markowitz.html
```

For the Jekyll-style `index.md` homepage, GitHub Pages rendering is recommended. If local homepage rendering is required, use a Jekyll-compatible local environment or convert/copy the page into `index.html`.

---

## 🧪 6. Validation & Engineering Notes / 验证与工程说明

Implemented improvements include:

- Backtest T+1 execution and sleeve-based cash logic.
- Trade detail panel and asset attribution panel.
- Markowitz robust input estimation: return winsorization, mean shrinkage, covariance shrinkage, and risk contribution.
- Efficient frontier visualization with zoom/export controls.
- Manifest-based asset universe, data quality report, stale-cache protection, and browser cache fallback.
- Mobile layout checks around narrow screen widths.
- Syntax checks for inline JavaScript in `backtest.html` and `markowitz.html`.

This project is intended for **educational, research demonstration, and portfolio presentation purposes**. It is not investment advice and should not be used as a production trading system without further validation.

---

## 🧭 7. Roadmap / 未来拓展方向

The following features are feasible under the current GitHub Pages + lightweight JSON data constraint:

| Priority / 优先级 | Feature / 功能 | Why It Fits / 为什么适合当前架构 |
| :--- | :--- | :--- |
| High | **Factor Model Dashboard** <br> 多因子分析面板 | Uses daily returns and factor proxies; small JSON size; strong finance-research value |
| High | **Risk Parity / ERC Optimizer** <br> 风险平价 / 等风险贡献模型 | Extends Markowitz naturally; low data requirement; visually explainable through risk contribution |
| High | **Black-Litterman Allocation** <br> Black-Litterman 配置模型 | Adds investor views and prior equilibrium returns; strong upgrade from pure mean-variance |
| Medium | **VaR / CVaR Risk Engine** <br> VaR / CVaR 风险测算 | Can run from daily returns; useful for risk-management storytelling |
| Medium | **Pairs Trading Demo** <br> 配对交易演示 | Requires only two price series; can show spread, z-score, entry/exit signals |
| Medium | **Performance Tear Sheet** <br> 策略绩效报告页 | Reuses existing backtest output; adds monthly returns, drawdown table, rolling Sharpe |
| Medium | **Regime Detection Panel** <br> 市场状态识别 | Can use moving volatility, trend filters, or simple HMM-like approximation in front-end |
| Low | **Options Greeks Calculator** <br> 期权希腊值计算器 | No large database needed; good financial-engineering signal, but less connected to existing data pipeline |

---

## 🎨 8. UI/UX Improvement Direction / 美术与交互优化方向

- Build a unified design system: shared color tokens, spacing scale, card radius, shadows, chart theme, and button states.
- Add a project navigation bar so users can jump between homepage, Backtest, Markowitz, and future modules without relying only on buttons.
- Improve chart storytelling: add short interpretation cards beside each chart explaining what the metric means and how to read it.
- Add a dark mode for a more professional quant-terminal feel.
- Reduce visual noise in dense panels by separating “inputs,” “charts,” and “diagnostics” more clearly.
- Add skeleton loading states instead of only spinners, especially when manifest/data files are being fetched.
- Add a model credibility badge area: data coverage, latest update date, sample size, transaction cost assumption, and look-ahead-bias control.

---

## 📌 9. Repository Structure / 推荐目录结构

```text
.
├── index.md                  # Main portfolio homepage / 项目主网页
├── README.md                 # Project documentation / 项目说明文档
├── backtest.html             # A-share backtesting system / A股回测模型
├── markowitz.html            # Markowitz allocation model / 资产配置模型
├── data/
│   ├── asset_manifest.json   # Unified asset universe / 统一资产清单
│   ├── quality_report.json   # Data quality report / 数据质量报告
│   └── *.json                # Historical price files / 历史行情数据
├── fetch_data.py             # Data update script / 数据抓取脚本
└── .github/workflows/
    └── update_data.yml       # Scheduled data update workflow / 自动更新工作流
```

---

## 📄 License & Disclaimer / 许可与免责声明

This project is for academic demonstration and personal portfolio presentation only. All model outputs are simplified research tools and should not be interpreted as trading recommendations, investment advice, or production-level risk management systems.

本项目仅用于学术展示与个人作品集展示。所有模型输出均为简化研究工具，不构成交易建议、投资建议或生产级风险管理系统。
