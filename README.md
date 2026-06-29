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

This repository contains a suite of web-based financial engineering tools and quantitative models (**量化模型**). Engineered entirely as a **Serverless Front-end (无后端/全客户端)** application, it empowers users to execute high-performance financial simulations, strategy backtesting, and portfolio optimization directly within any modern web browser.

### 📦 Key Modules Matrix (核心模块矩阵)

| Module Name (模块名称) | Core File (核心文件) | Mathematical Base (数学/金融基础) | Key Metrics (核心指标) |
| :--- | :--- | :--- | :--- |
| **Live Quant Engine** <br> (实盘蒙特卡洛预测引擎) | `index.md` | Geometric Brownian Motion (GBM) <br> 几何布朗运动 / 随机微分方程 | Implied Volatility ($\sigma$), <br> Expected Return ($\mu$) |
| **A-Share Backtesting System** <br> (A股量化策略回测系统) | `backtest.html` | Momentum & Mean Reversion <br> 双均线择时 / 布林带通道 | Sharpe Ratio, Calmar Ratio, <br> Max Drawdown (最大回撤) |
| **Markowitz Optimization** <br> (现代资产配置模型) | `markowitz.html` | Modern Portfolio Theory (MPT) <br> 均值-方差模型 / 二次规划 (QP) | Efficient Frontier (有效前沿), <br> Optimal Weights (最优权重) |

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
    * **Multi-Asset Basket (多资产分配):** Allows custom cross-sectional weighting among core index assets (e.g., CSI 300, ChiNext).
    * **Performance Attribution (绩效评估):** Auto-calculates institutional-grade risk/return parameters including *Annualized Volatility (年化波动)*, *Excess Return (超额收益)*, and *Calmar Ratio (卡玛比率)*.

### 2.3 Markowitz Asset Allocation Model (Markowitz 资产轮动模型)
* **Functionality (功能):** Implements Harry Markowitz's MPT framework to derive mathematically optimized risk-adjusted portfolio boundaries.
* **Key Features (核心特性):**
    * **Optimization Solvers (优化算法):** Executes both Monte Carlo multi-asset randomized sampling and strict **Quadratic Programming (QP - 二次规划)** matrix operations to lock in the Max Sharpe portfolio.
    * **Rolling Window Rebalancing (滚动窗口重平衡):** Dynamically steps through historical dates to calculate historical rolling covariance ($\Sigma$).
    * **Stress Testing (压力测试场景):** Allows manual injection of tail-risk scenarios (e.g., *Market Crash 市场暴跌*, *Rate Hike 利率骤升*, *Volatility Shock 波动率冲击*) to evaluate portfolio drawdowns during crises.

---

## 🏗️ 3. Architecture & Tech Stack (项目搭建与技术栈)

The philosophy of this repository is **Zero-Infrastructure**. No Docker, no server instances, and no databases are needed.

* **Frontend Core (前端基础):** Native Semantic HTML5, Vanilla CSS3, and modern ECMAScript (Vanilla JS). Completely independent of heavy frameworks (React/Vue), yielding lightning-fast runtime performance.
* **Data Visualization (数据可视化):** Powered by **Apache ECharts 5**, delivering responsive multi-coordinate charts, asset weight pie matrixes, and dense matrix heatmaps.
* **Report Generation (报告导出):** Combines `html2canvas` and `html2pdf.js` to parse local DOM nodes directly into crisp vector PDFs with a single click.
* **Data Pipeline (数据链路):**
    * *Dynamic API:* `query1.finance.yahoo.com` mapped through `allorigins.win` CORS bypass proxy.
    * *Static Store:* Pre-formatted local historical JSON objects deployed directly onto GitHub Pages content storage.

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

### Cloud Deployment (云端部署)

Since the pipeline consists entirely of static assets, it can be deployed immediately to **GitHub Pages**, Vercel, or Netlify by simply pushing the main directory to a production branch.

---

## 🔮 5. Future Enhancements (未来拓展规划)

* **Secure API Gateways:** Offload proxy requests to Cloudflare Workers to eliminate dependency on public CORS proxies.
* **LLM Copilot Integration (大模型金融助手):** Activate the pre-formatted UI chat interface by hooking up a serverless edge function linked to OpenAI's API (`gpt-4o-mini`) to provide automated performance analysis summaries on backtest metrics.
