# 📈 Quant Finance Portfolio & Analytics Suite
**金融工程量化分析与个人作品集系统**

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![ECharts](https://img.shields.io/badge/Apache_ECharts-E43961?style=for-the-badge&logo=apache-echarts&logoColor=white)

本项目是一个纯前端（Zero-Backend）实现的量化金融工具集与个人主页。系统集成了蒙特卡洛随机过程模拟、A股多因子择时回测、以及基于现代投资组合理论（MPT）的动态资产配置模型。所有的复杂金融数学运算（二次规划、矩阵运算、随机模拟）均在浏览器端高性能完成。

---

## 🌟 核心模块 (Core Modules)

### 1. 🎛️ 个人中枢控制台 (Portfolio Hub)
文件: `index.md` (或 `index.html`)
* **实盘量化预测引擎**：内置伊藤引理（Ito's Lemma）和几何布朗运动（GBM）逻辑。一键调用 Yahoo Finance API 拉取标的实时行情。
* **极速蒙特卡洛模拟**：支持最高 10,000 次未来 252 个交易日的路径推演，并通过底层算法将其归一化，生成高精度“概率密度热力图”。
* **现代 UI 架构**：采用毛玻璃拟物化设计（Glassmorphism）、交错式瀑布流加载动效，并预留了 LLM（大语言模型）的金融问答接口。

### 2. 📊 量化择时回测沙盒 (Backtesting Engine)
文件: `backtest.html`
* **技术指标与因子择时**：基于经典量价因子构建策略基座，支持自定义趋势追踪信号。
* **高拟真交易环境**：支持配置初始资金、交易滑点（Slippage）、印花税与佣金，真实还原摩擦成本。
* **专业归因分析**：实时计算夏普比率（Sharpe）、最大回撤（Max Drawdown）、卡玛比率（Calmar），并利用双 Y 轴动态绘制投资组合净值与超额收益柱状图。

### 3. 🛡️ 智能资产配置与压力测试 (Markowitz Portfolio)
文件: `markowitz.html`
* **MPT 有效边界寻优**：通过**二次规划 (Quadratic Programming)** 与随机模拟双引擎，求解给定资产池（支持做空/禁空约束）的最优权重配比。
* **滚动窗口分析 (Rolling Window)**：模拟真实的“样本外”换仓逻辑，避免前视偏差（Look-ahead bias）。
* **极端情景压测 (Stress Testing)**：首创交互式情景注入功能，允许用户在特定时间节点叠加“暴跌 -15%”、“利率飙升”等冲击，实时重算净值曲线与回撤指标。

---

## 🚀 快速启动 (How to Run)

本项目无需部署任何后端环境（Node.js/Python等均不需要），开箱即用：

1. 克隆或下载本仓库到本地。
2. 推荐使用 VS Code 的 `Live Server` 插件，或直接双击在浏览器（Chrome/Edge/Safari）中打开。
3. 确保网络通畅以加载外部依赖（如 `ECharts.js` 和字体图标）。

---

## 🛠️ 技术栈与数学模型 (Tech & Math Stack)

* **前端渲染**: HTML5 / CSS3 (CSS Variables, Flexbox/Grid) / Vanilla JS (ES6+)
* **可视化引擎**: Apache ECharts 5.5 (处理数万量级数据点的高渲染性能)
* **量化与数学核心**:
  * 现代投资组合理论 (Modern Portfolio Theory)
  * 二次规划最优化求解 (QP Solver for Convex Optimization)
  * 几何布朗运动随机过程 (Geometric Brownian Motion)
  * 时间序列收益率/协方差矩阵对角化

---

## 📬 联系作者

* **作者**: 王盛烨 (Shengye Hanson Wang)
* **专业**: 商业与金融 (Data Analytics) - 上海纽约大学 (NYU Shanghai)
* **Email**: [sw6245@nyu.edu](mailto:sw6245@nyu.edu)
* **GitHub**: [Hanson-SW](https://github.com/Hanson-SW)
