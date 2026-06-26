---
layout: default
title: 金融工程 · 个人主页
---

<div class="cv-container">
    <div class="header-section">
        <div class="avatar-gradient">王</div>
        <div>
            <h1 class="main-title">王 盛 烨</h1>
            <p class="sub-title">
                <i class="fas fa-chart-line"></i> 上海纽约大学 · 商业与金融（商业分析）
            </p>
        </div>
    </div>

    <h2 class="section-title">
        <i class="fas fa-file-pdf"></i> 我的简历
    </h2>
    <div class="info-card">
        <div class="card-left">
            <i class="fas fa-file-pdf card-icon"></i>
            <span class="card-text">金融工程简历</span>
            <span class="card-tag">· 2026 最新版</span>
        </div>
        <button onclick="window.open('王盛烨简历.pdf', '_blank')" class="btn btn-primary">
            <i class="fas fa-eye"></i> 查看简历
        </button>
    </div>

    <h2 class="section-title">
        <i class="fas fa-code-branch"></i> 项目展示
    </h2>

    <div class="info-card">
        <div class="card-left">
            <i class="fas fa-chart-pie card-icon"></i>
            <span class="card-text">基金组合分析工具</span>
            <span class="card-tag">· Python 回测 &amp; 归因</span>
        </div>
        <div class="card-buttons">
            <button onclick="window.open('https://github.com/hanson-sw/fund-analysis', '_blank')" class="btn btn-outline">
                <i class="fab fa-github"></i> Repository
            </button>
        </div>
    </div>

    <div class="info-card">
        <div class="card-left">
            <i class="fas fa-bolt card-icon"></i>
            <span class="card-text">A股择时策略</span>
            <span class="card-tag">· 宏观 + 情绪指标</span>
        </div>
        <div class="card-buttons">
            <button onclick="window.open('https://github.com/hanson-sw/astock-strategy', '_blank')" class="btn btn-outline">
                <i class="fab fa-github"></i> Repository
            </button>
        </div>
    </div>
    //量化ito开始
<h2 class="section-title" style="margin-top: 3.5rem;">
    <i class="fas fa-chart-area" style="color: #2563eb;"></i> 实盘量化引擎：蒙特卡洛股价路径预测
</h2>
<p style="color: #64748b; font-size: 0.95rem; margin-bottom: 1.5rem;">
    输入美股代码，系统将自动通过 Yahoo Finance 拉取过去一年真实历史数据，测算历史波动率(σ)与期望收益(μ)，并在后台进行 500 次 Itô Process 模拟，生成未来走势概率密度的热力图。
</p>

<div class="model-panel" style="background: #ffffff; border-radius: 16px; padding: 1.5rem; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0,0,0,0.03); margin-bottom: 1.5rem;">
    <div style="display: flex; flex-wrap: wrap; gap: 1rem; align-items: flex-end;">
        
        <div style="flex: 1; min-width: 120px;">
            <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;">美股代码 (Ticker)</label>
            <div style="display: flex; gap: 0.5rem;">
                <input type="text" id="stockTicker" value="AAPL" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none; text-transform: uppercase;" placeholder="例如: AAPL, TSLA" />
                <button onclick="fetchStockData()" id="fetchBtn" class="btn btn-outline" style="padding: 0 1rem; white-space: nowrap;">
                    <i class="fas fa-cloud-download-alt"></i> 拉取
                </button>
            </div>
        </div>

        <div style="flex: 1; min-width: 90px;">
            <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;">当前股价 ($)</label>
            <input type="number" id="currentPrice" value="170.00" step="0.01" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none; background: #f8fafc;" />
        </div>

        <div style="flex: 1; min-width: 90px;">
            <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;">年化波动率 (σ)</label>
            <input type="number" id="impliedVol" value="0.25" step="0.001" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none; background: #f8fafc;" />
        </div>

        <div style="flex: 1; min-width: 90px;">
            <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;">期望收益 (μ)</label>
            <input type="number" id="expReturn" value="0.08" step="0.001" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none; background: #f8fafc;" />
        </div>

        <div style="flex: 1; min-width: 90px;">
            <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;">预测天数</label>
            <input type="number" id="timeHorizon" value="252" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none;" />
        </div>

        <button onclick="runSimulation()" id="simBtn" class="btn btn-primary" style="height: 42px; padding: 0 1.5rem; white-space: nowrap;">
            <i class="fas fa-play"></i> 运行蒙特卡洛
        </button>
    </div>
    <div id="dataStatus" style="font-size: 0.8rem; color: #2563eb; margin-top: 0.8rem; font-weight: 500; min-height: 1.2rem;"></div>
</div>

<div style="background: #ffffff; border-radius: 16px; padding: 1rem; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
    <div id="itoChart" style="width: 100%; height: 450px;"></div>
</div>

<script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>

<script>
    let chartInstance = null;

    // Box-Muller 算法生成标准正态分布随机数
    function randomNormal() {
        let u = 0, v = 0;
        while(u === 0) u = Math.random();
        while(v === 0) v = Math.random();
        return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
    }

    // 从 Yahoo Finance 获取真实股票历史数据，并自动测算金融参数
    async function fetchStockData() {
        const ticker = document.getElementById('stockTicker').value.trim().toUpperCase();
        if(!ticker) return;

        const statusDiv = document.getElementById('dataStatus');
        const fetchBtn = document.getElementById('fetchBtn');
        statusDiv.innerHTML = `<i class="fas fa-spinner fa-spin"></i> 正在从 Yahoo Finance 拉取 ${ticker} 过去 1 年的历史数据...`;
        fetchBtn.disabled = true;

        try {
            // 使用 allorigins 代理绕过 CORS 限制，直连 Yahoo Finance
            const yahooUrl = `https://query1.finance.yahoo.com/v8/finance/chart/${ticker}?range=1y&interval=1d`;
            const proxyUrl = `https://api.allorigins.win/get?url=${encodeURIComponent(yahooUrl)}`;
            
            const response = await fetch(proxyUrl);
            const rawData = await response.json();
            const data = JSON.parse(rawData.contents);

            if (!data.chart || !data.chart.result) throw new Error("Ticker not found");

            const closePrices = data.chart.result[0].indicators.quote[0].close.filter(p => p !== null);
            const currentPrice = closePrices[closePrices.length - 1];

            // 计算对数收益率
            let logReturns = [];
            for (let i = 1; i < closePrices.length; i++) {
                logReturns.push(Math.log(closePrices[i] / closePrices[i - 1]));
            }

            // 计算均值和方差
            const meanReturn = logReturns.reduce((a, b) => a + b, 0) / logReturns.length;
            const variance = logReturns.reduce((a, b) => a + Math.pow(b - meanReturn, 2), 0) / (logReturns.length - 1);
            
            // 年化处理 (假设一年 252 个交易日)
            const annVol = Math.sqrt(variance) * Math.sqrt(252);
            const annMu = meanReturn * 252 + (annVol * annVol) / 2; // 伊托引理调整

            // 自动填入表单
            document.getElementById('currentPrice').value = currentPrice.toFixed(2);
            document.getElementById('impliedVol').value = annVol.toFixed(3);
            document.getElementById('expReturn').value = annMu.toFixed(3);

            statusDiv.innerHTML = `<i class="fas fa-check-circle" style="color: #10b981;"></i> 成功加载 ${ticker} 数据！基于历史表现推算：年化波动率 ${(annVol*100).toFixed(1)}%, 期望收益 ${(annMu*100).toFixed(1)}%。`;
            
            // 自动运行模拟
            runSimulation();

        } catch (error) {
            console.error(error);
            statusDiv.innerHTML = `<i class="fas fa-exclamation-triangle" style="color: #ef4444;"></i> 拉取失败，请检查股票代码是否正确 (如 AAPL)。`;
        } finally {
            fetchBtn.disabled = false;
        }
    }

    // 核心引擎：运行蒙特卡洛并生成热力图数据
    function generateMonteCarloData(S0, mu, sigma, days, numPaths = 500, numBins = 60) {
        let paths = [];
        let dt = 1 / 252;
        let globalMin = S0, globalMax = S0;

        // 1. 跑 500 次模拟路径
        for(let p = 0; p < numPaths; p++) {
            let simPath = [S0];
            for(let i = 1; i <= days; i++) {
                let Z = randomNormal();
                let drift = (mu - 0.5 * sigma * sigma) * dt;
                let shock = sigma * Math.sqrt(dt) * Z;
                let nextPrice = simPath[i-1] * Math.exp(drift + shock);
                simPath.push(nextPrice);
                
                if(nextPrice < globalMin) globalMin = nextPrice;
                if(nextPrice > globalMax) globalMax = nextPrice;
            }
            paths.push(simPath);
        }

        // 上下留出一点视觉缓冲空间
        globalMin *= 0.95; 
        globalMax *= 1.05;
        let binSize = (globalMax - globalMin) / numBins;

        // 2. 将数据装入热力图矩阵 (Day vs Price Bin)
        let heatmapData = [];
        let matrix = Array(days + 1).fill(0).map(() => Array(numBins).fill(0));
        let maxFreq = 0;

        for(let p = 0; p < numPaths; p++) {
            for(let d = 0; d <= days; d++) {
                let price = paths[p][d];
                let binIdx = Math.floor((price - globalMin) / binSize);
                if(binIdx >= numBins) binIdx = numBins - 1;
                if(binIdx < 0) binIdx = 0;
                matrix[d][binIdx]++;
                if(matrix[d][binIdx] > maxFreq) maxFreq = matrix[d][binIdx];
            }
        }

        // 整理给 ECharts 的数据格式 [x, y, value]
        for(let d = 0; d <= days; d++) {
            for(let b = 0; b < numBins; b++) {
                if(matrix[d][b] > 0) {
                    heatmapData.push([d, b, matrix[d][b]]);
                }
            }
        }

        // 生成 Y 轴的分类标签（价格区间）
        let yAxisLabels = [];
        for(let b = 0; b < numBins; b++) {
            yAxisLabels.push((globalMin + b * binSize).toFixed(1));
        }

        // 3. 生成理想走势线 (Deterministic path)
        let idealPath = [S0];
        for(let i = 1; i <= days; i++) {
            idealPath.push(idealPath[i-1] * Math.exp(mu * dt));
        }

        return { heatmapData, yAxisLabels, globalMin, globalMax, maxFreq, singleSimPath: paths[0], idealPath };
    }

    // 渲染图表
    function runSimulation() {
        const S0 = parseFloat(document.getElementById('currentPrice').value);
        const sigma = parseFloat(document.getElementById('impliedVol').value);
        const mu = parseFloat(document.getElementById('expReturn').value);
        const days = parseInt(document.getElementById('timeHorizon').value);

        document.getElementById('simBtn').innerHTML = `<i class="fas fa-spinner fa-spin"></i> 计算中...`;

        // 使用 setTimeout 防止阻塞 UI
        setTimeout(() => {
            const data = generateMonteCarloData(S0, mu, sigma, days, 500, 60);

            let xAxisData = [];
            for(let i = 0; i <= days; i++) xAxisData.push(i);

            if (!chartInstance) {
                chartInstance = echarts.init(document.getElementById('itoChart'));
            }

            const option = {
                title: { text: 'Monte Carlo 概率密度热力图 vs 单次模拟', left: 'center', textStyle: { color: '#334155', fontSize: 15 } },
                tooltip: {
                    position: 'top',
                    formatter: function (params) {
                        if(params.seriesType === 'heatmap') {
                            return `Day ${params.value[0]} <br/>股价边界: $${data.yAxisLabels[params.value[1]]} <br/>落入概率权重: ${params.value[2]}`;
                        } else {
                            return `Day ${params.dataIndex} <br/>股价: $${params.value.toFixed(2)}`;
                        }
                    }
                },
                // 配置热力图的视觉映射 (颜色渐变)
                visualMap: {
                    min: 0,
                    max: Math.min(data.maxFreq, 50), // 截断极端极值让颜色更饱满
                    calculable: true,
                    orient: 'horizontal',
                    left: 'center',
                    bottom: '0%',
                    inRange: {
                        color: ['#ffffff', '#bfdbfe', '#3b82f6', '#1e40af'] // 从白到浅蓝到深蓝
                    },
                    textStyle: { color: '#64748b', fontSize: 10 }
                },
                grid: { left: '8%', right: '5%', top: '12%', bottom: '20%', containLabel: true },
                xAxis: { type: 'category', data: xAxisData, name: 'Days', nameLocation: 'middle', nameGap: 25 },
                // 采用双 Y 轴黑科技：轴0用于热力图分类，轴1用于连线绝对数值，确保完美重叠
                yAxis: [
                    { type: 'category', data: data.yAxisLabels, show: false }, // 隐藏的 heatmap 分类轴
                    { type: 'value', min: data.globalMin, max: data.globalMax, axisLabel: { formatter: '${value}' }, splitLine: { show: false } }
                ],
                series: [
                    {
                        name: '概率密度热力图 (500次模拟)',
                        type: 'heatmap',
                        data: data.heatmapData,
                        yAxisIndex: 0,
                        itemStyle: { opacity: 0.4 }, // 设置透明度 40%
                        emphasis: { itemStyle: { borderColor: '#333', borderWidth: 1 } }
                    },
                    {
                        name: '单次随机模拟走势 (Simulated)',
                        type: 'line',
                        data: data.singleSimPath,
                        yAxisIndex: 1,
                        showSymbol: false,
                        lineStyle: { width: 2, color: '#f59e0b' }, // 橘黄色，在蓝色背景上极其显眼
                        itemStyle: { color: '#f59e0b' },
                        z: 10 // 确保显示在最上层
                    },
                    {
                        name: '理论期望走势 (Deterministic)',
                        type: 'line',
                        data: data.idealPath,
                        yAxisIndex: 1,
                        showSymbol: false,
                        lineStyle: { width: 2, type: 'dashed', color: '#10b981' }, // 绿色虚线
                        itemStyle: { color: '#10b981' },
                        z: 10
                    }
                ]
            };

            chartInstance.setOption(option);
            document.getElementById('simBtn').innerHTML = `<i class="fas fa-play"></i> 运行蒙特卡洛`;
        }, 100);
    }

    // 页面初始加载时自动运行一次默认模型
    window.onload = function() {
        runSimulation();
    };
    
    // 适配窗口响应式
    window.addEventListener('resize', function() {
        if(chartInstance) chartInstance.resize();
    });
</script>
//量化ito结束

    <h2 class="section-title">
        <i class="fas fa-paper-plane"></i> 联系我
    </h2>
    <div class="contact-wrapper">
        <a href="mailto:sw6245@nyu.edu" class="contact-tag">
            <i class="fas fa-envelope"></i> sw6245@nyu.edu
        </a>
        <a href="tel:+8615908963789" class="contact-tag">
            <i class="fas fa-phone"></i> +86 159 0896 3789
        </a>
        <a href="https://github.com/hanson-sw" target="_blank" class="contact-tag">
            <i class="fab fa-github"></i> GitHub 主页
        </a>
    </div>

    <h2 class="section-title ai-top-border">
        <i class="fas fa-robot"></i> AI 智能搜索
    </h2>
    <div class="search-wrapper">
        <input type="text" id="aiSearchInput" placeholder="输入你想问的金融问题…" />
        <button onclick="handleAISearch()" class="btn btn-primary search-btn">
            <i class="fas fa-paper-plane"></i> 提问
        </button>
    </div>
    <div id="aiSearchResult"></div>
    <p class="search-tip">
        <i class="fas fa-info-circle"></i> 当前为模拟演示，真实接入需替换为后端 API
    </p>
</div>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" />

<style>
    /* 全局容器控制布局，防止全屏时排版过散 */
    .cv-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 2rem 1.5rem;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        color: #0f172a;
    }
    
    /* 头部区域 */
    .header-section {
        display: flex;
        align-items: center;
        gap: 1.5rem;
        flex-wrap: wrap;
        margin-bottom: 2.5rem;
        padding-bottom: 2rem;
        border-bottom: 1px solid #eef2f6;
    }
    .avatar-gradient {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        background: linear-gradient(135deg, #1e40af, #3b82f6); /* 调深了蓝色，更显专业 */
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        font-weight: 600;
        color: white;
        flex-shrink: 0;
        box-shadow: 0 10px 25px rgba(37, 99, 235, 0.2);
    }
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0;
        background: linear-gradient(135deg, #0f172a, #1e40af);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 2px;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #475569;
        margin: 0.4rem 0 0 0;
    }

    /* 板块标题 */
    .section-title {
        font-size: 1.25rem;
        font-weight: 600;
        margin-top: 3rem;
        margin-bottom: 1.2rem;
        display: flex;
        align-items: center;
        gap: 0.6rem;
    }
    .section-title i {
        color: #2563eb;
        width: 1.5rem;
    }

    /* 通用卡片设计 */
    .info-card {
        background: #ffffff;
        border-radius: 16px;
        padding: 1.25rem 1.5rem;
        border: 1px solid #e2e8f0;
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        transition: all 0.25s ease; /* 增加悬停平滑动画 */
    }
    .info-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(15, 23, 42, 0.05);
        border-color: #cbd5e1;
    }
    .card-left {
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    .card-icon {
        font-size: 1.3rem;
        color: #2563eb;
    }
    .card-text {
        font-weight: 600;
        color: #1e293b;
    }
    .card-tag {
        font-size: 0.9rem;
        color: #64748b;
    }
    .card-buttons {
        display: flex;
        gap: 0.5rem;
    }

    /* 按钮样式 */
    .btn {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        padding: 0.5rem 1.2rem;
        border-radius: 40px;
        font-size: 0.85rem;
        font-weight: 500;
        cursor: pointer;
        transition: background 0.2s;
        border: none;
    }
    .btn-primary {
        background: #2563eb;
        color: white;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.15);
    }
    .btn-primary:hover {
        background: #1d4ed8;
    }
    .btn-outline {
        background: transparent;
        color: #334155;
        border: 1px solid #cbd5e1;
    }
    .btn-outline:hover {
        background: #f8fafc;
        border-color: #94a3b8;
    }

    /* 联系方式 */
    .contact-wrapper {
        display: flex;
        flex-wrap: wrap;
        gap: 0.75rem;
        margin-top: 0.5rem;
    }
    .contact-tag {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        color: #334155;
        text-decoration: none;
        font-size: 0.9rem;
        font-weight: 500;
        background: #f1f5f9;
        padding: 0.5rem 1.1rem;
        border-radius: 30px;
        transition: all 0.2s;
    }
    .contact-tag:hover {
        background: #e2e8f0;
        color: #0f172a;
    }

    /* AI 搜索组件 */
    .ai-top-border {
        padding-top: 2rem;
        border-top: 1px solid #eef2f6;
    }
    .search-wrapper {
        display: flex;
        gap: 0.6rem;
        flex-wrap: wrap;
    }
    #aiSearchInput {
        flex: 1;
        min-width: 260px;
        padding: 0.75rem 1.2rem;
        border-radius: 40px;
        border: 1px solid #cbd5e1;
        font-size: 0.95rem;
        background: #f8fafc;
        outline: none;
        transition: all 0.2s;
    }
    #aiSearchInput:focus {
        border-color: #2563eb;
        background: #ffffff;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
    }
    #aiSearchResult {
        margin-top: 1.2rem;
        font-size: 0.95rem;
        color: #334155;
        padding: 0 0.5rem;
        line-height: 1.5;
    }
    .search-tip {
        font-size: 0.8rem;
        color: #94a3b8;
        margin-top: 0.6rem;
    }

    /* 移动端响应式极致优化 */
    @media (max-width: 600px) {
        .cv-container {
            padding: 1.5rem 1rem;
        }
        .header-section {
            flex-direction: column;
            align-items: flex-start;
            gap: 1rem;
        }
        .info-card {
            flex-direction: column;
            align-items: flex-start;
            padding: 1.25rem;
        }
        .card-buttons, .btn {
            width: 100%;
            justify-content: center;
        }
        .search-wrapper {
            flex-direction: column;
        }
        #aiSearchInput, .search-btn {
            width: 100% !important;
            box-sizing: border-box;
        }
    }
</style>

<script>
    async function handleAISearch() {
        const input = document.getElementById('aiSearchInput');
        const resultDiv = document.getElementById('aiSearchResult');
        const query = input.value.trim();

        if (!query) {
            resultDiv.innerHTML = '⚠️ 请输入一个问题。';
            return;
        }

        resultDiv.innerHTML = '🤔 正在思考…';

        try {
            await new Promise(resolve => setTimeout(resolve, 800));
            const mockAnswers = [
                '根据当前宏观数据，A股估值处于历史中位数水平，建议关注消费和科技板块。',
                '近期国债收益率曲线趋于平坦化，对权益资产定价有一定支撑。',
                '基金组合中，可以适当增加高股息策略的配置，降低波动风险。'
            ];
            resultDiv.innerHTML = '💡 ' + mockAnswers[Math.floor(Math.random() * mockAnswers.length)];
        } catch (error) {
            resultDiv.innerHTML = '❌ 搜索请求失败，请稍后重试。';
            console.error('AI Search Error:', error);
        }
    }

    document.getElementById('aiSearchInput').addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            handleAISearch();
        }
    });
</script>
