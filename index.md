# Financial Engineering & Quantitative Analysis Portfolio (金融工程与量化分析作品集)

**Author (作者):** Shengye (Hanson) Wang (王盛烨)  
**Education (教育背景):** NYU Shanghai · Business & Finance (Business Analytics) (上海纽约大学 · 商业与金融/商业分析)  
**Contact (联系方式):** - 📧 Email: sw6245@nyu.edu
- 📞 Phone: +86 159 0896 3789
- 💻 GitHub: [Hanson-SW](https://github.com/Hanson-SW)

---

## 1. Project Overview (项目概览)

This repository contains a suite of web-based financial engineering tools and quantitative models (量化模型v1.1). Built entirely as a serverless front-end application, it allows users to perform complex financial simulations, backtesting, and portfolio optimizations directly in the browser.

The portfolio consists of three main modules:
1. **Live Quant Engine: Monte Carlo Prediction** (实盘量化引擎：蒙特卡洛股价预测)
2. **A-Share Quantitative Backtesting System** (A股量化策略回测系统)
3. **Markowitz Asset Allocation Model** (Markowitz 资产配置模型)

---

## 2. Core Modules (核心模块)

### 2.1 Live Quant Engine (实盘蒙特卡洛预测引擎)
Located in `index.md` (rendered as the main homepage).
- **Functionality (功能):** Simulates future stock price paths using Geometric Brownian Motion (GBM) / Monte Carlo simulations.
- **Key Features (核心特性):**
  - **Live Data Fetching (实盘数据拉取):** Fetches real-time stock data (prices, calculating implied volatility $\sigma$ and expected return $\mu$) using Yahoo Finance API via a proxy.
  - **Fallback Mechanism (容灾机制):** Automatically switches to local GitHub database or hardcoded fallback data if the live API limits are reached.
  - **Probability Heatmap (概率密度热力图):** Generates a daily-normalized heatmap of possible future price distributions alongside individual simulated paths.

### 2.2 A-Share Quantitative Backtesting System (A股量化策略回测系统)
Located in `backtest.html`.
- **Functionality (功能):** A sandbox for testing multi-asset Long/Short strategies and performance attribution against a benchmark.
- **Key Features (核心特性):**
  - **Smart Timing Strategies (智能择时策略):** Implements Dual Moving Average (双均线择时, 5-day crossing 20-day) and Bollinger Bands (布林带择时, 20-day / 2 standard deviations) for independent asset timing.
  - **Custom Asset Allocation (自定义资产配置):** Users can define capital weights across different assets/indices (e.g., CSI 300, ChiNext).
  - **Performance Metrics (风险收益指标):** Calculates Total Return (累计收益), Annualized Return/Volatility (年化收益/波动), Maximum Drawdown (最大回撤), Sharpe Ratio (夏普比率), and Calmar Ratio (卡玛比率).

### 2.3 Markowitz Asset Allocation Model (Markowitz 资产轮动与配置模型)
Located in `markowitz.html`.
- **Functionality (功能):** Constructs optimal portfolios based on Modern Portfolio Theory (MPT - 现代投资组合理论).
- **Key Features (核心特性):**
  - **Optimization Solvers (优化算法):** Supports both Quadratic Programming (QP - 二次规划) and Monte Carlo simulation to find the optimal weights that maximize the Sharpe ratio.
  - **Rolling Window (滚动窗口):** Allows dynamic rebalancing based on historical rolling windows.
  - **Stress Testing (压力测试场景):** Injects user-defined shock scenarios (e.g., Market Crash 市场暴跌, Rate Hike 利率骤升, Volatility Shock 波动率冲击) at specific dates to observe portfolio resilience.

---

## 3. Architecture & Tech Stack (项目搭建与技术栈)

This project is designed as a **Zero-Backend (无后端)** lightweight application, ensuring maximum portability and easy deployment.

- **Frontend Framework (前端架构):** Pure HTML5, CSS3, and Vanilla JavaScript (原生JS). No heavy frameworks (like React or Vue) are required, making it extremely fast to load and render.
- **Data Visualization (数据可视化):** [Apache ECharts 5](https://echarts.apache.org/) is used extensively for rendering interactive time-series line charts, bar charts (excess returns), and complex heatmaps.
- **PDF Generation (报告导出):** Integrates `html2canvas` and `html2pdf.js` for one-click downloading of backtest and allocation reports.
- **Data Source (数据源):**
  - Live API: `query1.finance.yahoo.com` routed through `allorigins.win` CORS proxy.
  - Static JSON data hosted on GitHub Pages (`hanson-sw.github.io/data/`).

---

## 4. Setup & Deployment (运行与部署)

Because the project relies entirely on client-side execution, the setup process is frictionless.

### Local Execution (本地运行)
1. Clone the repository:
   ```bash
   git clone [https://github.com/Hanson-SW/your-repo-name.git](https://github.com/Hanson-SW/your-repo-name.git)
