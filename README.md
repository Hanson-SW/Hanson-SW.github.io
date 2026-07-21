# Financial Engineering & Quantitative Analysis Portfolio
### 📊 金融工程与量化分析作品集

---

## 👤 Personal Information (个人信息)

| Item (项目) | Details (详情) |
| :--- | :--- |
| **Author (作者)** | Shengye (Hanson) Wang (王盛烨) |
| **Education (教育背景)** | NYU Shanghai · Business & Finance (Business Analytics) <br> 上海纽约大学 · 商业与金融（商业分析方向） |
| **Contact (联系方式)** | 📧 `sw6245@nyu.edu` &nbsp;&nbsp; 📞 `+86 159 0896 3789` |
| **Profiles (主页链接)** | [🌐 GitHub Portfolio](https://github.com/Hanson-SW) |

---

## 🚀 1. Project Overview (项目概览)

This repository contains a browser-based **Financial Engineering, Portfolio Analytics & Statement Analysis Lab**. It combines static market data, data-health reporting, strategy backtesting, multi-method portfolio allocation, and financial statement analysis in a **Serverless Front-end (无后端/全客户端)** application that can run directly on GitHub Pages.

### 📦 Key Modules Matrix (核心模块矩阵)

| Module Name (模块名称) | Core File (核心文件) | Mathematical Base (数学/金融基础) | Key Metrics (核心指标) |
| :--- | :--- | :--- | :--- |
| **Live Quant Engine** <br> (实盘蒙特卡洛预测引擎) | `index.md` | Geometric Brownian Motion (GBM) <br> 几何布朗运动 / 随机微分方程 | Implied Volatility ($\sigma$), <br> Expected Return ($\mu$) |
| **A-Share Backtesting System** <br> (A股量化策略回测系统) | `backtest.html` | Momentum & Mean Reversion <br> 双均线择时 / 布林带通道 | CAGR, Sharpe, Calmar, MaxDD, <br> VaR/CVaR, Trade History, Attribution |
| **Portfolio Allocation Lab** <br> (组合配置实验室) | `markowitz.html` | MPT + Robust Inputs <br> Risk Parity / Black-Litterman / Min CVaR | Efficient Frontier, Risk Contribution, <br> VaR/CVaR, Stress Test, BL Comparison, OOS |
| **Financial Statement Analyzer** <br> (三表分析与估值建模平台) | `statement-analyzer.html` | Accounting Mapping + Valuation <br> Ratio Analysis / DCF / Comps / LBO | Financial Health Score, NOPAT, NOA, <br> DCF, Football Field, AI Mock Report |

---

## 🛠️ 2. Core Modules Deep-Dive (核心模块详解)

### 2.1 Live Quant Engine (实盘蒙特卡洛预测引擎)
* **Functionality (功能):** Generates thousands of randomized asset price trajectories to simulate future stock distributions.
* **Key Features (核心特性):**
    * **Live Data Fetching (实盘数据拉取):** Dynamically requests real-time market data from Yahoo Finance API via a high-availability proxy.
    * **Fallback Architecture (容灾机制):** Gracefully falls back to a locally-hosted GitHub database or pre-cached asset snapshots if public API limits are breached.
    * **Probability Heatmap (概率密度热力图):** Renders a daily-normalized grid overlay showing the empirical distribution of price densities across time.

### 2.2 A-Share Quantitative Backtesting System (A股量化策略回测系统)
* **Functionality (功能):** A sandbox environment allowing historical analysis of simple alpha and timing strategies against macro benchmarks.
* **Key Features (核心特性):**
    * **Algorithmic Timing (智能择时策略):** Built-in support for **Dual Moving Average** (双均线交叉, e.g., 5-day / 20-day) and **Bollinger Bands** (布林带突破) with parametric input adjustments.
    * **Multi-Asset Basket (多资产分配):** Allows custom cross-sectional weighting among core index assets (e.g., CSI 300, ChiNext), with manifest-aware symbol suggestions that support touch, keyboard navigation, and visual-viewport-aware placement on narrow mobile screens.
    * **Performance Attribution (绩效评估):** Auto-calculates annualized volatility, excess return, Calmar ratio, Alpha, Beta, information ratio, tracking error, correlation, and R-squared against the selected benchmark.
    * **Risk Tear Sheet (风险报告):** Reports strategy-realized *Daily VaR/CVaR*, *Worst/Best Day*, *Skewness*, *Kurtosis*, and recent rolling VaR from actual strategy daily returns; monthly returns follow the selected backtest dates and paginate in 12-month pages.
    * **Trade Transparency (交易透明度):** Shows paginated buy/sell details by asset and exports the full trade history as an image.

### 2.3 Portfolio Allocation Lab (Markowitz / Risk Parity / Black-Litterman)
* **Functionality (功能):** Extends the original Markowitz optimizer into a multi-method allocation lab for comparing allocation assumptions, tail risk, and risk contribution.
* **Key Features (核心特性):**
    * **Optimization Matrix (优化方法矩阵):** Supports Equal Weight, Max Sharpe, Min Volatility, Risk Parity, and Monte Carlo search.
    * **Black-Litterman Inputs (观点修正):** Uses a standard single relative-view posterior with market-equilibrium excess returns, confidence-derived view uncertainty, posterior predictive covariance, and same-period replay comparison; the posterior also feeds the Min CVaR return/covariance tilt while its empirical tail objective remains historical.
    * **Asset Pool Workflow (资产池输入):** Uses manifest-aware bilingual suggestions with touch, keyboard, ARIA support, and automatic upward/downward opening based on the available visual viewport instead of relying on browser-native datalist behavior.
    * **Tail Risk Metrics (尾部风险):** Adds historical 95%/99% VaR and CVaR to explain the optimal portfolio's extreme-loss profile.
    * **Rolling Window Rebalancing (滚动窗口重平衡):** Dynamically steps through historical dates to calculate rolling estimates of expected return and covariance ($\Sigma$).
    * **Stress Testing (压力测试场景):** Applies bounded, date-validated tail-risk scenarios (e.g., *Market Crash 市场暴跌*, *Rate Hike 利率骤升*, *Volatility Shock 波动率冲击*) after portfolio formation, keeping stress replay out of Black-Litterman estimation to avoid look-ahead bias.

### 2.4 Financial Statement Analyzer (三表分析与估值建模平台)
* **Functionality (功能):** Uploads or loads standardized financial statements, cleans line items, calculates core ratios, and generates a research-style report.
* **Key Features (核心特性):**
    * **Statement Standardization (三表标准化):** Parses income statement, balance sheet, and cash flow statement inputs, then maps varied account names to standardized fields.
    * **Quality Diagnostics (财务质量诊断):** Calculates profitability, growth, leverage, liquidity, cash-flow quality, NOPAT margin, NOA / sales, and business-risk indicators.
    * **Valuation Models (估值模型):** Includes DCF, trading comps, football field visualization, M&A accretion/dilution, and LBO modules for investment-banking style modeling.
    * **Responsive Visuals (响应式图表):** Rebuilds chart titles, scrollable legends, labels, and plotting grids for narrow screens and device rotation without changing model outputs.
    * **Report Copilot (报告生成):** Produces an AI mock investment narrative and full-page exportable web report while keeping the current version deployable as a static GitHub Pages site.

---

## 🏗️ 3. Architecture & Tech Stack (项目搭建与技术栈)

The philosophy of this repository is **Zero-Infrastructure**. No Docker, no server instances, and no databases are needed.

* **Frontend Core (前端基础):** Native Semantic HTML5, Vanilla CSS3, and modern ECMAScript (Vanilla JS). Completely independent of heavy frameworks (React/Vue), yielding lightning-fast runtime performance.
* **Responsive Workbench (响应式工作台):** Backtest, Markowitz, and Statement Analyzer share a compact research-workbench hierarchy, safe-area-aware mobile spacing, touch-sized controls, frame-throttled active-section navigation, and direction-aware scroll cues for dense tables on 360px-class screens.
* **Data Visualization (数据可视化):** Powered by **Apache ECharts 5**, delivering responsive multi-coordinate charts, asset weight pie matrixes, and dense matrix heatmaps.
* **Local Runtime Assets (本地运行依赖):** ECharts, html2canvas, SheetJS, and Font Awesome are served from repository-local files so charts, icons, image reports, and XLSX import/export do not depend on a public CDN. Third-party licenses are retained under `vendor-licenses/`; the homepage uses a system monospace stack instead of a remote webfont.
* **Report Generation (报告导出):** Uses the local `html2canvas` runtime and a canonical 1360px export layout to capture the complete Backtest/Markowitz workspace, charts, settings, and full-width scrollable tables consistently from both mobile and desktop viewports.
* **Data Pipeline (数据链路):**
    * *Static Store:* Pre-formatted local historical JSON objects under `data/*.json`, deployed directly onto GitHub Pages content storage.
    * *Asset Manifest:* `data/asset_manifest.json` controls available assets, display names, date ranges, and latest update time.
    * *Quality Report:* `data/quality_report.json` records fetch success/failure, stale cache usage, and missing-data conditions.
    * *Browser Cache:* Frontend pages use bounded three-second request timeouts and browser caches before falling back to embedded demo data, reducing accidental 2025-only fallback on slower mobile networks.

---

## 💻 4. Setup & Deployment (运行与部署指南)

### Local Execution (本地运行)

1. **Clone the Repository (克隆仓库):**
   ```bash
   git clone https://github.com/Hanson-SW/your-repo-name.git
   cd your-repo-name
   ```

2. **Launch a Local Server (启动本地服务器):**
   Because modern browsers restrict file protocol requests (`file://`) due to CORS security policies, it is highly recommended to run the project using a simple local environment:
   ```bash
   # Using Python 3.x
   python -m http.server 8000
   ```

3. **Access the Tools (浏览器访问):**
   Open your browser and navigate to:
   * Main Page / Quant Engine: `http://localhost:8000/index.html` (or your mapped index)
   * Backtesting Engine: `http://localhost:8000/backtest.html`
   * Markowitz Sandbox: `http://localhost:8000/markowitz.html`
   * Statement Analyzer: `http://localhost:8000/statement-analyzer.html`

### Cloud Deployment (云端部署)

Since the pipeline consists entirely of static assets, it can be deployed immediately to **GitHub Pages**, Vercel, or Netlify by simply pushing the main directory to a production branch.

---

## 🔮 5. Future Enhancements (未来拓展规划)

* **Visual System Refinement:** Continue unifying the index, Backtest, Markowitz, and Statement Analyzer pages around a denser professional dashboard style.
* **Strict Optimization Engine:** Replace front-end friendly approximations with a more rigorous QP/CVaR optimizer when a lightweight browser-safe solver is selected.
* **Deeper Attribution:** Extend Backtest trade analytics with win rate, turnover, and average holding period while keeping benchmark-relative metrics auditable.
* **Data Pipeline Maintenance:** Keep `data/*.json`, `asset_manifest.json`, and `quality_report.json` updated through scheduled GitHub Actions and local cache fallback checks.
