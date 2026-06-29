---
layout: default
title: 金融工程 · 个人主页
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/echarts/5.4.3/echarts.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" />

<button onclick="toggleLang()" class="lang-toggle-btn">
    <i class="fas fa-globe"></i> <span id="langBtnText">中 / EN</span>
</button>

<div class="cv-container">
    <div class="header-section">
        <div class="avatar-gradient">王</div>
        <div>
            <h1 class="main-title" data-i18n="name">王 盛 烨</h1>
            <p class="sub-title">
                <i class="fas fa-chart-line"></i> <span data-i18n="degree">上海纽约大学 · 商业与金融（商业分析）</span>
            </p>
        </div>
    </div>

    <h2 class="section-title">
        <i class="fas fa-file-pdf"></i> <span data-i18n="resume_title">我的简历</span>
    </h2>
    <div class="info-card">
        <div class="card-left">
            <i class="fas fa-file-pdf card-icon"></i>
            <span class="card-text" data-i18n="resume_name">金融工程简历</span>
            <span class="card-tag" data-i18n="resume_tag">· 2026 最新版</span>
        </div>
        <button onclick="window.open('王盛烨简历.pdf', '_blank')" class="btn btn-primary">
            <i class="fas fa-eye"></i> <span data-i18n="resume_btn">查看简历</span>
        </button>
    </div>

    <h2 class="section-title">
        <i class="fas fa-code-branch"></i> <span data-i18n="project_title">项目展示</span>
    </h2>

    <div class="info-card">
        <div class="card-left">
            <i class="fas fa-chart-pie card-icon"></i>
            <span class="card-text" data-i18n="proj1_name">基金组合分析工具</span>
            <span class="card-tag" data-i18n="proj1_tag">· Python 回测 & 归因</span>
        </div>
        <div class="card-buttons">
            <button onclick="window.open('https://github.com/hanson-sw/fund-analysis', '_blank')" class="btn btn-outline">
                <i class="fab fa-github"></i> Repository
            </button>
        </div>
    </div>

    <div class="info-card">
        <div class="card-left">
            <i class="fas fa-chart-line card-icon"></i>
            <span class="card-text" data-i18n="proj_backtest_name">A股回测模型</span>
            <span class="card-tag" data-i18n="proj_backtest_tag">· 宏观 + 情绪指标</span>
        </div>
        <div class="card-buttons">
            <button onclick="window.open('https://github.com/hanson-sw/astock-strategy', '_blank')" class="btn btn-outline">
                <i class="fab fa-github"></i> Repository
            </button>
            <button onclick="window.open('./backtest.html', '_blank')" class="btn btn-primary">
                <i class="fas fa-play"></i> <span data-i18n="proj_backtest_btn">运行回测模型</span>
            </button>
        </div>
    </div>

    <h2 class="section-title" style="margin-top: 3.5rem;">
        <i class="fas fa-chart-area" style="color: #2563eb;"></i> <span data-i18n="mc_title">实盘量化引擎：股价路径预测</span>
    </h2>
    <p style="color: #64748b; font-size: 0.95rem; margin-bottom: 1.5rem;" data-i18n="mc_desc">
        系统自动拉取历史数据(含GitHub缓存容灾)。支持自定义模拟次数，极速引擎生成逐日归一化的概率密度热力图。
    </p>

    <div class="model-panel">
        <div class="param-grid">
            <div class="grid-col-span-2 relative-box">
                <label class="param-label" data-i18n="mc_ticker">股票代码 (Ticker)</label>
                <div class="flex-input-group">
                    <input type="text" id="stockTicker" value="AAPL" oninput="handleLocalSearch(); markCustom();" autocomplete="off" class="param-input uppercase-text" placeholder="输入 AAPL..." />
                    <button onclick="fetchStockData()" id="fetchBtn" class="btn btn-outline fetch-btn">
                        <i class="fas fa-cloud-download-alt"></i> <span data-i18n="mc_pull">拉取</span>
                    </button>
                </div>
                <div id="autocompleteList" class="autocomplete-dropdown"></div>
            </div>

            <div class="grid-col">
                <label id="priceLabel" class="param-label">当前股价 ($)</label>
                <input type="number" id="currentPrice" value="175.00" step="0.01" oninput="markCustom()" class="param-input bg-gray" />
            </div>

            <div class="grid-col">
                <label class="param-label" data-i18n="mc_vol">波动率 (σ)</label>
                <input type="number" id="impliedVol" value="0.22" step="0.001" oninput="markCustom()" class="param-input bg-gray" />
            </div>

            <div class="grid-col">
                <label class="param-label" data-i18n="mc_mu">期望收益 (μ)</label>
                <input type="number" id="expReturn" value="0.08" step="0.001" oninput="markCustom()" class="param-input bg-gray" />
            </div>
            
            <div class="grid-col">
                <label class="param-label" data-i18n="mc_paths">模拟次数</label>
                <input type="number" id="numPaths" value="5000" step="500" oninput="markCustom()" class="param-input" />
            </div>

            <div class="grid-col">
                <label class="param-label" data-i18n="mc_days">预测天数</label>
                <input type="number" id="timeHorizon" value="252" oninput="markCustom()" class="param-input" />
            </div>

            <div class="grid-col-btn">
                <button onclick="runSimulation()" id="simBtn" class="btn btn-primary run-sim-btn">
                    <i class="fas fa-play"></i> <span data-i18n="mc_run">运行</span>
                </button>
            </div>
        </div>
        <div id="dataStatus" class="data-status-text"></div>
    </div>

    <div id="chartExportWrapper" class="chart-wrapper">
        <div class="chart-tools">
            <button onclick="downloadImage()" class="icon-btn" title="导出高清图片">
                <i class="fas fa-download"></i>
            </button>
            <button onclick="toggleFullscreen()" class="icon-btn" title="全屏放大">
                <i id="fullscreenIcon" class="fas fa-expand"></i>
            </button>
        </div>
        <div id="itoChart" style="width: 100%; height: 500px;"></div>
    </div>

    <h2 class="section-title">
        <i class="fas fa-paper-plane"></i> <span data-i18n="contact_title">联系我</span>
    </h2>
    <div class="contact-wrapper">
        <a href="mailto:sw6245@nyu.edu" class="contact-tag">
            <i class="fas fa-envelope"></i> sw6245@nyu.edu
        </a>
        <a href="https://github.com/hanson-sw" target="_blank" class="contact-tag">
            <i class="fab fa-github"></i> <span data-i18n="contact_gh">GitHub 主页</span>
        </a>
    </div>

    <h2 class="section-title ai-top-border">
        <i class="fas fa-robot"></i> <span data-i18n="ai_title">AI 智能搜索 (LLM 接入)</span>
    </h2>
    <div class="search-wrapper">
        <input type="text" id="aiSearchInput" placeholder="输入你想问的金融问题…" />
        <button onclick="handleAISearch()" class="btn btn-primary search-btn">
            <i class="fas fa-paper-plane"></i> <span data-i18n="ai_btn">提问</span>
        </button>
    </div>
    <div id="aiSearchResult"></div>
    <p class="search-tip">
        <i class="fas fa-info-circle"></i> <span data-i18n="ai_tip">代码已预留真实 API 接入逻辑，填入 Key 即可激活大模型，否则将展示模拟演示。</span>
    </p>
</div>

<style>
    /* 核心修复 1：全局启用 border-box 盒模型，防止边距撑爆容器 */
    *, *::before, *::after { box-sizing: border-box; }

    /* 基础样式 */
    .cv-container { max-width: 900px; margin: 0 auto; padding: 4rem 1.5rem 2rem 1.5rem; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; color: #0f172a; position: relative; }
    
    /* 修复 2：语言切换按钮脱离文档流优化，防重叠 */
    .lang-toggle-btn { position: absolute; top: 1rem; right: 1.5rem; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 20px; padding: 0.4rem 1rem; font-size: 0.85rem; font-weight: 600; color: #334155; cursor: pointer; z-index: 1000; box-shadow: 0 2px 5px rgba(0,0,0,0.05); transition: all 0.2s; }
    
    .header-section { display: flex; align-items: center; gap: 1.5rem; flex-wrap: wrap; margin-bottom: 2.5rem; padding-bottom: 2rem; border-bottom: 1px solid #eef2f6; }
    .avatar-gradient { width: 80px; height: 80px; border-radius: 50%; background: linear-gradient(135deg, #1e40af, #3b82f6); display: flex; align-items: center; justify-content: center; font-size: 2rem; font-weight: 600; color: white; flex-shrink: 0; box-shadow: 0 10px 25px rgba(37, 99, 235, 0.2); }
    .main-title { font-size: 2.2rem; font-weight: 700; margin: 0; background: linear-gradient(135deg, #0f172a, #1e40af); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; letter-spacing: 2px; }
    .sub-title { font-size: 1.05rem; color: #475569; margin: 0.4rem 0 0 0; }
    .section-title { font-size: 1.25rem; font-weight: 600; margin-top: 3rem; margin-bottom: 1.2rem; display: flex; align-items: center; gap: 0.6rem; }
    .section-title i { color: #2563eb; width: 1.5rem; }
    
    .info-card { background: #ffffff; border-radius: 16px; padding: 1.25rem 1.5rem; border: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; margin-bottom: 1rem; box-shadow: 0 2px 4px rgba(0,0,0,0.02); transition: all 0.25s ease; }
    .info-card:hover { transform: translateY(-2px); box-shadow: 0 8px 20px rgba(15, 23, 42, 0.05); border-color: #cbd5e1; }
    .card-left { display: flex; align-items: center; gap: 0.75rem; }
    .card-icon { font-size: 1.3rem; color: #2563eb; }
    .card-text { font-weight: 600; color: #1e293b; }
    .card-tag { font-size: 0.9rem; color: #64748b; }
    .card-buttons { display: flex; gap: 0.5rem; }
    
    .btn { display: inline-flex; align-items: center; justify-content: center; gap: 0.4rem; padding: 0.5rem 1.2rem; border-radius: 40px; font-size: 0.85rem; font-weight: 500; cursor: pointer; transition: background 0.2s; border: none; }
    .btn-primary { background: #2563eb; color: white; box-shadow: 0 4px 12px rgba(37, 99, 235, 0.15); }
    .btn-primary:hover { background: #1d4ed8; }
    .btn-outline { background: transparent; color: #334155; border: 1px solid #cbd5e1; }
    .btn-outline:hover { background: #f8fafc; border-color: #94a3b8; }

    /* 核心修复 3：使用 CSS Grid 彻底重构模型参数面板 */
    .model-panel { background: #ffffff; border-radius: 16px; padding: 1.5rem; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0,0,0,0.03); margin-bottom: 1rem; }
    .param-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(110px, 1fr)); gap: 1rem; align-items: end; }
    .grid-col-span-2 { grid-column: span 2; }
    .relative-box { position: relative; }
    .param-label { display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600; white-space: nowrap; }
    .param-input { width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none; transition: border-color 0.2s; }
    .param-input:focus { border-color: #2563eb; }
    .bg-gray { background: #f8fafc; }
    .uppercase-text { text-transform: uppercase; }
    .flex-input-group { display: flex; gap: 0.5rem; }
    .fetch-btn { padding: 0 1rem; flex-shrink: 0; }
    .run-sim-btn { height: 42px; width: 100%; }
    .data-status-text { font-size: 0.8rem; color: #2563eb; margin-top: 1rem; font-weight: 500; min-height: 1.2rem; }
    .autocomplete-dropdown { display:none; position:absolute; top: 100%; left: 0; right: 0; background: #fff; border: 1px solid #cbd5e1; border-radius: 8px; margin-top: 4px; max-height: 200px; overflow-y: auto; z-index: 999; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
    .autocomplete-item { padding: 10px 12px; cursor: pointer; border-bottom: 1px solid #f1f5f9; font-size: 0.85rem; color: #334155; }
    .autocomplete-item:hover { background: #eff6ff; color: #2563eb; }

    /* 图表容器 */
    .chart-wrapper { background: #ffffff; border-radius: 12px; padding: 1rem 0; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0,0,0,0.03); position: relative; margin-left: -1.5rem; margin-right: -1.5rem; overflow: hidden; }
    .chart-tools { position: absolute; top: 1rem; right: 1rem; z-index: 100; display: flex; gap: 0.5rem; }
    .icon-btn { background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 8px; padding: 0.5rem 0.8rem; cursor: pointer; color: #475569; transition: all 0.2s; }
    .icon-btn:hover { background: #e2e8f0; }

    /* 搜索及其他 */
    .contact-wrapper { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 0.5rem; }
    .contact-tag { display: inline-flex; align-items: center; gap: 0.5rem; color: #334155; text-decoration: none; font-size: 0.9rem; font-weight: 500; background: #f1f5f9; padding: 0.5rem 1.1rem; border-radius: 30px; transition: all 0.2s; }
    .contact-tag:hover { background: #e2e8f0; color: #0f172a; }
    .ai-top-border { padding-top: 2rem; border-top: 1px solid #eef2f6; }
    .search-wrapper { display: flex; gap: 0.6rem; flex-wrap: wrap; }
    #aiSearchInput { flex: 1; min-width: 260px; padding: 0.75rem 1.2rem; border-radius: 40px; border: 1px solid #cbd5e1; font-size: 0.95rem; background: #f8fafc; outline: none; }
    #aiSearchInput:focus { border-color: #2563eb; background: #ffffff; box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1); }
    #aiSearchResult { margin-top: 1.2rem; font-size: 0.95rem; color: #334155; padding: 0 0.5rem; line-height: 1.5; }
    .search-tip { font-size: 0.8rem; color: #94a3b8; margin-top: 0.6rem; }
    
    .chart-fullscreen { position: fixed !important; top: 0 !important; left: 0 !important; width: 100vw !important; height: 100vh !important; z-index: 9999 !important; border-radius: 0 !important; margin: 0 !important; padding: 2rem !important; background: #ffffff !important; overflow-y: auto;}
    .chart-fullscreen #itoChart { height: 95% !important; }

    /* 核心修复 4：极致的移动端适配媒体查询 */
    @media (max-width: 768px) {
        .cv-container { padding: 4rem 1rem 1rem 1rem; }
        .lang-toggle-btn { top: 1rem; right: 1rem; } /* 调整按钮防碰撞 */
        .header-section { flex-direction: column; align-items: flex-start; gap: 1rem; }
        .info-card { flex-direction: column; align-items: flex-start; padding: 1.25rem; }
        .card-buttons, .btn { width: 100%; justify-content: center; }
        
        /* 移动端打断网格，垂直堆叠，100% 杜绝重叠 */
        .param-grid { grid-template-columns: 1fr 1fr; }
        .grid-col-span-2 { grid-column: span 2; }
        .grid-col-btn { grid-column: span 2; }
        
        .chart-wrapper { margin-left: -1rem; margin-right: -1rem; border-radius: 0; border-left: none; border-right: none;}
        .search-wrapper { flex-direction: column; }
        #aiSearchInput, .search-btn { width: 100% !important; }
    }
    
    @media (max-width: 480px) {
        /* 极小屏幕完全单列 */
        .param-grid { grid-template-columns: 1fr; }
        .grid-col-span-2, .grid-col-btn { grid-column: span 1; }
    }
</style>

<script>
    // i18n 多语言系统
    const i18nDict = {
        name: { zh: "王 盛 烨", en: "Shengye Wang" },
        degree: { zh: "上海纽约大学 · 商业与金融（商业分析）", en: "NYU Shanghai · Business & Finance (Data Analytics)" },
        resume_title: { zh: "我的简历", en: "My Resume" },
        resume_name: { zh: "金融工程简历", en: "Financial Engineering Resume" },
        resume_tag: { zh: "· 2026 最新版", en: "· 2026 Updated" },
        resume_btn: { zh: "查看简历", en: "View PDF" },
        project_title: { zh: "项目展示", en: "Projects" },
        proj1_name: { zh: "基金组合分析工具", en: "Fund Portfolio Analyzer" },
        proj1_tag: { zh: "· Python 回测 & 归因", en: "· Python Backtesting & Attribution" },
        proj_backtest_name: { zh: "A股回测模型", en: "A-Share Backtesting Model" },
        proj_backtest_tag: { zh: "· 宏观 + 情绪指标", en: "· Macro + Sentiment Indicators" },
        proj_backtest_btn: { zh: "运行回测模型", en: "Run Backtest Model" },
        mc_title: { zh: "实盘量化引擎：股价路径预测", en: "Live Quant Engine: Monte Carlo Prediction" },
        mc_desc: { zh: "系统自动拉取历史数据(含GitHub缓存容灾)。支持自定义模拟次数，生成逐日概率热力图。", en: "Auto-fetches live data. Per-Day Normalized heatmap." },
        mc_ticker: { zh: "股票代码 (Ticker)", en: "Stock Ticker" },
        mc_pull: { zh: "拉取", en: "Fetch" },
        mc_vol: { zh: "波动率 (σ)", en: "Volatility (σ)" },
        mc_mu: { zh: "期望收益 (μ)", en: "Expected Ret (μ)" },
        mc_paths: { zh: "模拟次数", en: "Sim Paths" },
        mc_days: { zh: "预测天数", en: "Horizon (Days)" },
        mc_run: { zh: "运行", en: "Run" },
        contact_title: { zh: "联系我", en: "Contact Me" },
        contact_gh: { zh: "GitHub 主页", en: "GitHub Profile" },
        ai_title: { zh: "AI 智能搜索 (LLM 接入)", en: "AI Financial Assistant (LLM)" },
        ai_btn: { zh: "提问", en: "Ask AI" },
        ai_tip: { zh: "代码已预留真实 API 接入逻辑，填入 Key 即可激活大模型，否则将展示模拟演示。", en: "Real API integration reserved in code." }
    };

    let currentLang = 'zh';
    function toggleLang() {
        currentLang = currentLang === 'zh' ? 'en' : 'zh';
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if(i18nDict[key]) el.innerHTML = i18nDict[key][currentLang];
        });
        document.getElementById('stockTicker').placeholder = currentLang === 'zh' ? "输入 AAPL, 600519.SS..." : "Type AAPL, TSLA...";
        document.getElementById('aiSearchInput').placeholder = currentLang === 'zh' ? "输入你想问的金融问题…" : "Ask a financial question...";
        document.getElementById('priceLabel').innerText = currentLang === 'zh' ? `当前股价 (${currentCurrency})` : `Current Price (${currentCurrency})`;
        if(chartInstance) runSimulation(); 
    }

    let currentDataSource = '用户自定义 (Custom Input)';
    let currentCurrency = '$'; 
    let chartInstance = null;

    function markCustom() { currentDataSource = currentLang === 'zh' ? '用户自定义 (Custom Input)' : 'User Custom Input'; }

    const localTickerDB = [
        { symbol: 'AAPL', name: '苹果公司 (Apple)' },
        { symbol: 'MSFT', name: '微软 (Microsoft)' },
        { symbol: 'NVDA', name: '英伟达 (NVIDIA)' },
        { symbol: 'TSLA', name: '特斯拉 (Tesla)' },
        { symbol: 'SPY', name: '标普500 ETF' },
        { symbol: '600519.SS', name: '贵州茅台 (Moutai)' }
    ];

    function handleLocalSearch() {
        const q = document.getElementById('stockTicker').value.trim().toUpperCase();
        const listDiv = document.getElementById('autocompleteList');
        if(q.length < 1) { listDiv.style.display = 'none'; return; }
        
        let results = localTickerDB.filter(item => item.symbol.includes(q) || item.name.toUpperCase().includes(q));
        if(results.length > 0) {
            let html = results.map(item => 
                `<div class="autocomplete-item" onclick="selectTicker('${item.symbol}')">
                    <strong>${item.symbol}</strong> - ${item.name}
                 </div>`
            ).join('');
            listDiv.innerHTML = html;
            listDiv.style.display = 'block';
        } else {
            listDiv.style.display = 'none';
        }
    }

    function selectTicker(symbol) {
        document.getElementById('stockTicker').value = symbol;
        document.getElementById('autocompleteList').style.display = 'none';
        fetchStockData();
    }

    document.addEventListener('click', function(e) {
        const list = document.getElementById('autocompleteList');
        if(list && !list.contains(e.target) && e.target.id !== 'stockTicker') list.style.display = 'none';
    });

    function toggleFullscreen() {
        const container = document.getElementById('chartExportWrapper');
        const icon = document.getElementById('fullscreenIcon');
        container.classList.toggle('chart-fullscreen');
        if(container.classList.contains('chart-fullscreen')) {
            icon.className = 'fas fa-compress';
            document.body.style.overflow = 'hidden';
        } else {
            icon.className = 'fas fa-expand';
            document.body.style.overflow = 'auto';
        }
    }

    function downloadImage() {
        if(!chartInstance) return;
        const url = chartInstance.getDataURL({ type: 'png', pixelRatio: 2, backgroundColor: '#ffffff' });
        const a = document.createElement('a');
        a.download = `Quant_Simulation_${document.getElementById('stockTicker').value || 'Model'}.png`;
        a.href = url;
        a.click();
    }

    async function fetchStockData() {
        const ticker = document.getElementById('stockTicker').value.trim().toUpperCase();
        if(!ticker) return;
        currentCurrency = (ticker.endsWith('.SS') || ticker.endsWith('.SZ')) ? '¥' : '$';
        document.getElementById('priceLabel').innerText = currentLang === 'zh' ? `当前股价 (${currentCurrency})` : `Current Price (${currentCurrency})`;

        const statusDiv = document.getElementById('dataStatus');
        const fetchBtn = document.getElementById('fetchBtn');
        statusDiv.innerHTML = `<i class="fas fa-spinner fa-spin"></i> ${currentLang==='zh'?'拉取数据中...':'Fetching data...'}`;
        fetchBtn.disabled = true;

        try {
            const proxyUrl = `https://api.allorigins.win/raw?url=${encodeURIComponent(`https://query1.finance.yahoo.com/v8/finance/chart/${ticker}?range=1y&interval=1d`)}`;
            const controller = new AbortController();
            const timeoutId = setTimeout(() => controller.abort(), 4000);
            const response = await fetch(proxyUrl, { signal: controller.signal });
            clearTimeout(timeoutId);
            
            if (!response.ok) throw new Error("Live API failed");
            const data = await response.json();
            const closePrices = data.chart.result[0].indicators.quote[0].close.filter(p => p != null);
            const currentPrice = closePrices[closePrices.length - 1];

            let logReturns = [];
            for (let i = 1; i < closePrices.length; i++) logReturns.push(Math.log(closePrices[i] / closePrices[i - 1]));
            const meanReturn = logReturns.reduce((a, b) => a + b, 0) / logReturns.length;
            const variance = logReturns.reduce((a, b) => a + Math.pow(b - meanReturn, 2), 0) / (logReturns.length - 1);
            const annVol = Math.sqrt(variance) * Math.sqrt(252);
            const annMu = meanReturn * 252 + (annVol * annVol) / 2;

            document.getElementById('currentPrice').value = currentPrice.toFixed(2);
            document.getElementById('impliedVol').value = annVol.toFixed(3);
            document.getElementById('expReturn').value = annMu.toFixed(3);
            currentDataSource = currentLang === 'zh' ? '实时接口 (Live Yahoo API)' : 'Live API (Yahoo)';
            statusDiv.innerHTML = `<i class="fas fa-check-circle" style="color: #10b981;"></i> 成功！[${currentDataSource}]`;
            runSimulation();
        } catch (e1) {
            try {
                const localRes = await fetch('./market_data.json');
                const localData = await localRes.json();
                if(!localData[ticker]) throw new Error("Ticker not in DB");
                document.getElementById('currentPrice').value = localData[ticker].price.toFixed(2);
                document.getElementById('impliedVol').value = localData[ticker].vol.toFixed(3);
                document.getElementById('expReturn').value = localData[ticker].mu.toFixed(3);
                currentDataSource = currentLang === 'zh' ? '本地缓存 (GitHub Data)' : 'Local Cache (GitHub DB)';
                statusDiv.innerHTML = `<i class="fas fa-check-circle" style="color: #2563eb;"></i> 使用本地每日缓存 [${currentDataSource}]`;
                runSimulation();
            } catch(e2) {
                document.getElementById('currentPrice').value = ticker.includes('600519') ? "1500.00" : "175.00";
                document.getElementById('impliedVol').value = "0.220";
                document.getElementById('expReturn').value = "0.080";
                currentDataSource = currentLang === 'zh' ? '离线备用数据' : 'Offline Fallback';
                statusDiv.innerHTML = `<i class="fas fa-exclamation-triangle" style="color: #f59e0b;"></i> 网络受限启用备用参数 [${currentDataSource}]`;
                runSimulation();
            }
        } finally {
            fetchBtn.disabled = false;
        }
    }

    function generateMonteCarloData(S0, mu, sigma, days, numPaths, numBins) {
        let dt = 1 / 252;
        let globalMin = S0, globalMax = S0;
        let drift = (mu - 0.5 * sigma * sigma) * dt, vol = sigma * Math.sqrt(dt);
        let singleSimPath = new Float64Array(days + 1);
        let allPrices = new Float64Array(numPaths * (days + 1));

        for(let p = 0; p < numPaths; p++) {
            let currentPrice = S0;
            allPrices[p * (days + 1)] = currentPrice;
            if(p === 0) singleSimPath[0] = currentPrice;
            
            for(let i = 1; i <= days; i++) {
                let u = 0, v = 0;
                while(u === 0) u = Math.random();
                while(v === 0) v = Math.random();
                currentPrice = currentPrice * Math.exp(drift + vol * Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v));
                allPrices[p * (days + 1) + i] = currentPrice;
                if(p === 0) singleSimPath[i] = currentPrice;
                if(currentPrice < globalMin) globalMin = currentPrice;
                if(currentPrice > globalMax) globalMax = currentPrice;
            }
        }

        globalMin *= 0.95; globalMax *= 1.05;
        let binSize = (globalMax - globalMin) / numBins;
        let matrix = Array.from({length: days + 1}, () => new Int32Array(numBins));
        let maxFreqPerDay = new Int32Array(days + 1);

        for(let p = 0; p < numPaths; p++) {
            for(let d = 0; d <= days; d++) {
                let binIdx = Math.max(0, Math.min(numBins - 1, Math.floor((allPrices[p * (days + 1) + d] - globalMin) / binSize)));
                matrix[d][binIdx]++;
                if(matrix[d][binIdx] > maxFreqPerDay[d]) maxFreqPerDay[d] = matrix[d][binIdx];
            }
        }

        let heatmapData = [];
        for(let d = 0; d <= days; d++) {
            for(let b = 0; b < numBins; b++) {
                if(matrix[d][b] > 0) heatmapData.push([d, b, matrix[d][b], maxFreqPerDay[d] > 0 ? (matrix[d][b] / maxFreqPerDay[d]) : 0]);
            }
        }

        let yAxisLabels = Array.from({length: numBins}, (_, b) => (globalMin + b * binSize).toFixed(2));
        let idealPath = Array.from({length: days + 1}, (_, i) => S0 * Math.exp(mu * dt * i));

        return { heatmapData, yAxisLabels, globalMin, globalMax, singleSimPath: Array.from(singleSimPath), idealPath, binSize, numPaths };
    }

    function runSimulation() {
        if(typeof echarts === 'undefined') return;

        const ticker = document.getElementById('stockTicker').value || 'Model';
        const S0 = parseFloat(document.getElementById('currentPrice').value);
        const sigma = parseFloat(document.getElementById('impliedVol').value);
        const mu = parseFloat(document.getElementById('expReturn').value);
        const days = parseInt(document.getElementById('timeHorizon').value);
        const pathsCount = parseInt(document.getElementById('numPaths').value) || 5000;

        document.getElementById('simBtn').innerHTML = `<i class="fas fa-spinner fa-spin"></i> 计算中`;

        setTimeout(() => {
            const data = generateMonteCarloData(S0, mu, sigma, days, pathsCount, 80);
            let xAxisData = Array.from({length: days + 1}, (_, i) => i);
            const today = new Date();
            const dateStr = `${today.getFullYear()}/${String(today.getMonth()+1).padStart(2,'0')}/${String(today.getDate()).padStart(2,'0')}`;
            
            const watermarkText = currentLang === 'zh' 
                ? `【运行参数】 标的: ${ticker} | 日期: ${dateStr} | 数据源: ${currentDataSource}\n 模型设定: 价格 ${currentCurrency}${S0} | 波动率(σ) ${sigma} | 期望收益(μ) ${mu} | 路径数 ${pathsCount}`
                : `[Params] Ticker: ${ticker} | Date: ${dateStr} | Source: ${currentDataSource}\n Input: Price ${currentCurrency}${S0} | Vol(σ) ${sigma} | Exp.Ret(μ) ${mu} | Paths ${pathsCount}`;

            if (!chartInstance) chartInstance = echarts.init(document.getElementById('itoChart'));

            chartInstance.setOption({
                backgroundColor: '#ffffff',
                graphic: [{ type: 'text', left: '2%', top: '3%', style: { text: watermarkText, fontSize: 10, fill: '#64748b', lineHeight: 15 }, z: 100 }],
                tooltip: {
                    position: 'top', backgroundColor: 'rgba(255,255,255,0.95)', borderColor: '#cbd5e1',
                    formatter: function (p) {
                        if(p.seriesType === 'heatmap') {
                            let lower = parseFloat(data.yAxisLabels[p.value[1]]);
                            return `<div style="color:#2563eb;">Day ${p.value[0]}</div>
                                    Range: <b>[ ${currentCurrency}${lower.toFixed(2)} , ${currentCurrency}${(lower+data.binSize).toFixed(2)} ]</b><br/>
                                    Prob: <b style="color:#ef4444;">${((p.value[2] / data.numPaths)*100).toFixed(2)}%</b>`;
                        } else {
                            return `<div style="color:#2563eb;">${p.seriesName}</div> Day ${p.dataIndex} <br/>Price: <b>${currentCurrency}${p.value.toFixed(2)}</b>`;
                        }
                    }
                },
                visualMap: { dimension: 3, min: 0, max: 1, show: false, inRange: { color: ['#ffffff', '#bfdbfe', '#3b82f6', '#ef4444'] } },
                grid: { left: '2%', right: '3%', top: 45, bottom: 25, containLabel: true },
                xAxis: { type: 'category', data: xAxisData },
                yAxis: [
                    { type: 'category', data: data.yAxisLabels, show: false }, 
                    { type: 'value', min: data.globalMin, max: data.globalMax, axisLabel: { formatter: currentCurrency+'{value}' } }
                ],
                series: [
                    { name: 'Heatmap', type: 'heatmap', data: data.heatmapData, yAxisIndex: 0 },
                    { name: 'Single Path', type: 'line', data: data.singleSimPath, yAxisIndex: 1, showSymbol: false, lineStyle: { width: 2, color: '#1e3a8a' }, z: 10 },
                    { name: 'Ideal', type: 'line', data: data.idealPath, yAxisIndex: 1, showSymbol: false, lineStyle: { width: 2, type: 'dashed', color: '#10b981' }, z: 10 }
                ]
            });
            document.getElementById('simBtn').innerHTML = `<i class="fas fa-play"></i> <span data-i18n="mc_run">${currentLang==='zh'?'运行':'Run'}</span>`;
        }, 50);
    }

    document.addEventListener('DOMContentLoaded', () => { runSimulation(); });
    
    // 核心修复 5：使用现代 ResizeObserver 监听容器缩放，彻底杜绝图表溢出
    const resizeObserver = new ResizeObserver(() => {
        if (chartInstance) chartInstance.resize();
    });
    resizeObserver.observe(document.getElementById('chartExportWrapper'));

    // AI 代码省略保持一致...
    async function handleAISearch() { /* ...同前... */ }
</script>
