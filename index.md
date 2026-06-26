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

    <h2 class="section-title" style="margin-top: 3.5rem;">
        <i class="fas fa-chart-area" style="color: #2563eb;"></i> 实盘量化引擎：蒙特卡洛股价路径预测
    </h2>
    <p style="color: #64748b; font-size: 0.95rem; margin-bottom: 1.5rem;">
        输入美股代码，系统自动通过 Yahoo Finance 拉取过去一年真实数据，测算历史波动率(σ)与期望收益(μ)，并在后台进行 500 次 Itô 随机漫步，生成未来走势的概率密度热力图。
    </p>

    <div class="model-panel" style="background: #ffffff; border-radius: 16px; padding: 1.5rem; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0,0,0,0.03); margin-bottom: 1.5rem;">
        <div style="display: flex; flex-wrap: wrap; gap: 1rem; align-items: flex-end;">
            
            <div style="flex: 2; min-width: 220px;">
                <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;">美股代码 (Ticker)</label>
                <div style="display: flex; gap: 0.5rem;">
                    <input type="text" id="stockTicker" value="AAPL" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none; text-transform: uppercase;" placeholder="如: AAPL" />
                    <button onclick="fetchStockData()" id="fetchBtn" class="btn btn-outline" style="padding: 0 1rem; white-space: nowrap; flex-shrink: 0;">
                        <i class="fas fa-cloud-download-alt"></i> 拉取
                    </button>
                </div>
            </div>

            <div style="flex: 1; min-width: 90px;">
                <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;">当前股价 ($)</label>
                <input type="number" id="currentPrice" value="170.00" step="0.01" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none; background: #f8fafc;" />
            </div>

            <div style="flex: 1; min-width: 90px;">
                <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;">波动率 (σ)</label>
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

            <button onclick="runSimulation()" id="simBtn" class="btn btn-primary" style="height: 42px; padding: 0 1.5rem; white-space: nowrap; flex-shrink: 0;">
                <i class="fas fa-play"></i> 运行
            </button>
        </div>
        <div id="dataStatus" style="font-size: 0.8rem; color: #2563eb; margin-top: 0.8rem; font-weight: 500; min-height: 1.2rem;"></div>
    </div>

    <div id="chartContainer" style="position: relative; background: #ffffff; border-radius: 16px; padding: 1rem; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0,0,0,0.03); transition: all 0.3s ease;">
        <button onclick="toggleFullscreen()" style="position: absolute; top: 15px; right: 15px; z-index: 100; background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 8px; padding: 0.5rem 0.8rem; cursor: pointer; color: #475569; transition: all 0.2s;">
            <i id="fullscreenIcon" class="fas fa-expand"></i>
        </button>
        <div id="itoChart" style="width: 100%; height: 450px;"></div>
    </div>

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
        <i class="fas fa-robot"></i> AI 智能搜索 (LLM 接入)
    </h2>
    <div class="search-wrapper">
        <input type="text" id="aiSearchInput" placeholder="输入你想问的金融问题…" />
        <button onclick="handleAISearch()" class="btn btn-primary search-btn">
            <i class="fas fa-paper-plane"></i> 提问
        </button>
    </div>
    <div id="aiSearchResult"></div>
    <p class="search-tip">
        <i class="fas fa-info-circle"></i> 代码已预留真实 API 接入逻辑，填入 Key 即可激活大模型，否则将展示模拟演示。
    </p>
</div>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" />
<script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>

<style>
    /* CSS 样式表完全恢复 */
    .cv-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 2rem 1.5rem;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        color: #0f172a;
    }
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
        background: linear-gradient(135deg, #1e40af, #3b82f6);
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
        transition: all 0.25s ease;
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
    .chart-fullscreen {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        z-index: 9999 !important;
        border-radius: 0 !important;
        margin: 0 !important;
        padding: 2rem !important;
        box-sizing: border-box;
        background: #ffffff !important;
    }
    .chart-fullscreen #itoChart {
        height: 100% !important;
    }
    @media (max-width: 600px) {
        .cv-container { padding: 1.5rem 1rem; }
        .header-section { flex-direction: column; align-items: flex-start; gap: 1rem; }
        .info-card { flex-direction: column; align-items: flex-start; padding: 1.25rem; }
        .card-buttons, .btn { width: 100%; justify-content: center; }
        .search-wrapper { flex-direction: column; }
        #aiSearchInput, .search-btn { width: 100% !important; box-sizing: border-box; }
    }
</style>

<script>
    // ================= 量化图表与数据处理 JS =================
    let chartInstance = null;

    function toggleFullscreen() {
        const container = document.getElementById('chartContainer');
        const icon = document.getElementById('fullscreenIcon');
        container.classList.toggle('chart-fullscreen');
        if(container.classList.contains('chart-fullscreen')) {
            icon.className = 'fas fa-compress';
            document.body.style.overflow = 'hidden';
        } else {
            icon.className = 'fas fa-expand';
            document.body.style.overflow = 'auto';
        }
        if(chartInstance) setTimeout(() => chartInstance.resize(), 100);
    }

    document.addEventListener('keydown', function(e) {
        const container = document.getElementById('chartContainer');
        if (e.key === 'Escape' && container.classList.contains('chart-fullscreen')) toggleFullscreen();
    });

    function randomNormal() {
        let u = 0, v = 0;
        while(u === 0) u = Math.random();
        while(v === 0) v = Math.random();
        return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
    }

    async function fetchStockData() {
        const ticker = document.getElementById('stockTicker').value.trim().toUpperCase();
        if(!ticker) return;
        const statusDiv = document.getElementById('dataStatus');
        const fetchBtn = document.getElementById('fetchBtn');
        statusDiv.innerHTML = `<i class="fas fa-spinner fa-spin"></i> 拉取 ${ticker} 过去 1 年历史数据...`;
        fetchBtn.disabled = true;

        try {
            const yahooUrl = `https://query1.finance.yahoo.com/v8/finance/chart/${ticker}?range=1y&interval=1d`;
            const proxyUrl = `https://api.allorigins.win/get?url=${encodeURIComponent(yahooUrl)}`;
            const response = await fetch(proxyUrl);
            const rawData = await response.json();
            const data = JSON.parse(rawData.contents);

            if (!data.chart || !data.chart.result) throw new Error("Ticker not found");

            const closePrices = data.chart.result[0].indicators.quote[0].close.filter(p => p !== null);
            const currentPrice = closePrices[closePrices.length - 1];

            let logReturns = [];
            for (let i = 1; i < closePrices.length; i++) {
                logReturns.push(Math.log(closePrices[i] / closePrices[i - 1]));
            }
            const meanReturn = logReturns.reduce((a, b) => a + b, 0) / logReturns.length;
            const variance = logReturns.reduce((a, b) => a + Math.pow(b - meanReturn, 2), 0) / (logReturns.length - 1);
            const annVol = Math.sqrt(variance) * Math.sqrt(252);
            const annMu = meanReturn * 252 + (annVol * annVol) / 2;

            document.getElementById('currentPrice').value = currentPrice.toFixed(2);
            document.getElementById('impliedVol').value = annVol.toFixed(3);
            document.getElementById('expReturn').value = annMu.toFixed(3);
            statusDiv.innerHTML = `<i class="fas fa-check-circle" style="color: #10b981;"></i> 成功！历史年化波动率 ${(annVol*100).toFixed(1)}%, 期望收益 ${(annMu*100).toFixed(1)}%。`;
            
            runSimulation();
        } catch (error) {
            console.error(error);
            statusDiv.innerHTML = `<i class="fas fa-exclamation-triangle" style="color: #ef4444;"></i> 拉取失败，请检查代码 (如 AAPL)。`;
        } finally {
            fetchBtn.disabled = false;
        }
    }

    function generateMonteCarloData(S0, mu, sigma, days, numPaths = 500, numBins = 60) {
        let paths = [];
        let dt = 1 / 252;
        let globalMin = S0, globalMax = S0;

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

        globalMin *= 0.95; globalMax *= 1.05;
        let binSize = (globalMax - globalMin) / numBins;
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

        for(let d = 0; d <= days; d++) {
            for(let b = 0; b < numBins; b++) {
                if(matrix[d][b] > 0) heatmapData.push([d, b, matrix[d][b]]);
            }
        }

        let yAxisLabels = [];
        for(let b = 0; b < numBins; b++) {
            yAxisLabels.push((globalMin + b * binSize).toFixed(2));
        }

        let idealPath = [S0];
        for(let i = 1; i <= days; i++) {
            idealPath.push(idealPath[i-1] * Math.exp(mu * dt));
        }

        return { heatmapData, yAxisLabels, globalMin, globalMax, maxFreq, singleSimPath: paths[0], idealPath, binSize, numPaths };
    }

    function runSimulation() {
        const S0 = parseFloat(document.getElementById('currentPrice').value);
        const sigma = parseFloat(document.getElementById('impliedVol').value);
        const mu = parseFloat(document.getElementById('expReturn').value);
        const days = parseInt(document.getElementById('timeHorizon').value);

        document.getElementById('simBtn').innerHTML = `<i class="fas fa-spinner fa-spin"></i> 计算中`;

        setTimeout(() => {
            const data = generateMonteCarloData(S0, mu, sigma, days, 500, 60);
            let xAxisData = [];
            for(let i = 0; i <= days; i++) xAxisData.push(i);

            if (!chartInstance) chartInstance = echarts.init(document.getElementById('itoChart'));

            const option = {
                title: { text: 'Monte Carlo 概率密度热力图 vs 单次模拟', left: 'center', textStyle: { color: '#334155', fontSize: 15 } },
                tooltip: {
                    position: 'top', backgroundColor: 'rgba(255, 255, 255, 0.95)', borderColor: '#cbd5e1', textStyle: { color: '#334155' },
                    formatter: function (params) {
                        if(params.seriesType === 'heatmap') {
                            let day = params.value[0], binIdx = params.value[1], count = params.value[2];
                            let lower = parseFloat(data.yAxisLabels[binIdx]);
                            let upper = lower + data.binSize;
                            let prob = ((count / data.numPaths) * 100).toFixed(1);
                            return `<div style="font-weight:bold; margin-bottom:4px;">第 ${day} 天预测</div>
                                    价格区间: <b>[ $${lower.toFixed(2)} , $${upper.toFixed(2)} ]</b><br/>
                                    落入概率: <b>${prob}%</b> <span style="color:#64748b; font-size:0.85em;">(500次模拟有 ${count} 次落入此区间)</span>`;
                        } else {
                            return `<div style="font-weight:bold; margin-bottom:4px;">${params.seriesName}</div>
                                    第 ${params.dataIndex} 天 <br/>预期股价: <b>$${params.value.toFixed(2)}</b>`;
                        }
                    }
                },
                visualMap: {
                    min: 0, max: Math.min(data.maxFreq, 50), calculable: true, orient: 'horizontal', left: 'center', bottom: '0%',
                    inRange: { color: ['#ffffff', '#bfdbfe', '#3b82f6', '#1e40af'] },
                    textStyle: { color: '#64748b', fontSize: 11 },
                    formatter: function (value) { return value.toFixed(0) + ' 频数'; }
                },
                grid: { left: '8%', right: '5%', top: '15%', bottom: '20%', containLabel: true },
                xAxis: { type: 'category', data: xAxisData, name: '交易日 (Days)', nameLocation: 'middle', nameGap: 25 },
                // ⚠️ 之前代码截断的地方在这里得到了完整的修复：
                yAxis: [
                    { type: 'category', data: data.yAxisLabels, show: false }, 
                    { type: 'value', min: data.globalMin, max: data.globalMax, axisLabel: { formatter: function(val) { return '$' + val.toFixed(0); } }, splitLine: { show: false } }
                ],
                series: [
                    { name: '概率分布', type: 'heatmap', data: data.heatmapData, yAxisIndex: 0, itemStyle: { opacity: 0.45 }, emphasis: { itemStyle: { borderColor: '#333', borderWidth: 1 } } },
                    { name: '单次随机漫步 (Simulated)', type: 'line', data: data.singleSimPath, yAxisIndex: 1, showSymbol: false, lineStyle: { width: 2, color: '#f59e0b' }, itemStyle: { color: '#f59e0b' }, z: 10 },
                    { name: '理论期望 (Deterministic)', type: 'line', data: data.idealPath, yAxisIndex: 1, showSymbol: false, lineStyle: { width: 2, type: 'dashed', color: '#10b981' }, itemStyle: { color: '#10b981' }, z: 10 }
                ]
            };

            chartInstance.setOption(option);
            document.getElementById('simBtn').innerHTML = `<i class="fas fa-play"></i> 运行`;
        }, 50);
    }

    window.onload = function() { runSimulation(); };
    window.addEventListener('resize', function() { if(chartInstance) chartInstance.resize(); });

    // ================= AI 引擎真实接入与 Mock JS =================
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
            // 💡 这里是接入真实 AI 的接口位置
            // 只要你在这个变量里填入你的 API Key，它就会自动变成真实的 AI！
            // 目前主流兼容模型：DeepSeek (非常便宜/性价比极高), OpenAI (ChatGPT), 阿里通义千问 等等
            const API_KEY = 'YOUR_API_KEY_HERE'; 
            
            // 下方以 DeepSeek API 为例，你可以替换为对应厂商的 URL 和 Model
            const API_URL = 'https://api.deepseek.com/chat/completions';
            const MODEL_NAME = 'deepseek-chat';

            if (API_KEY !== 'YOUR_API_KEY_HERE') {
                // 如果填了 Key，触发真实的 API 请求
                const response = await fetch(API_URL, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${API_KEY}`
                    },
                    body: JSON.stringify({
                        model: MODEL_NAME,
                        messages: [
                            {"role": "system", "content": "你是一个专业的金融量化分析师助手。请用简明、严谨的中文回答用户的金融、投资和商业分析问题。"},
                            {"role": "user", "content": query}
                        ]
                    })
                });
                
                const data = await response.json();
                if(data.choices && data.choices.length > 0) {
                    // 把 Markdown 换行转换成网页换行标签显示
                    resultDiv.innerHTML = '💡 ' + data.choices[0].message.content.replace(/\n/g, '<br/>');
                } else {
                    resultDiv.innerHTML = '❌ 无法解析 AI 的回复，请检查 API 配置。';
                }
                
            } else {
                // 如果没填 Key，降级使用模拟回复（保护你不暴露 API Key）
                await new Promise(resolve => setTimeout(resolve, 800));
                const mockAnswers = [
                    '根据当前宏观数据，A股估值处于历史中位数水平，建议关注消费和科技板块。（提示：当前为模拟演示，填入 API Key 即可对话）',
                    '近期国债收益率曲线趋于平坦化，对权益资产定价有一定支撑。（提示：当前为模拟演示，填入 API Key 即可对话）',
                    '基金组合中，可以适当增加高股息策略的配置，降低波动风险。（提示：当前为模拟演示，填入 API Key 即可对话）'
                ];
                resultDiv.innerHTML = '💡 ' + mockAnswers[Math.floor(Math.random() * mockAnswers.length)];
            }
            
        } catch (error) {
            resultDiv.innerHTML = '❌ 网络请求失败。如果是跨域问题，请检查你的 API 服务商是否支持前端直连。';
            console.error('AI Search Error:', error);
        }
    }

    document.getElementById('aiSearchInput').addEventListener('keydown', function(e) {
        if (e.key === 'Enter') handleAISearch();
    });
</script>
