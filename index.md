---
layout: default
title: 金融工程 · 个人主页
---

<button onclick="toggleLang()" style="position: absolute; top: 1.5rem; right: 1.5rem; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 20px; padding: 0.4rem 1rem; font-size: 0.85rem; font-weight: 600; color: #334155; cursor: pointer; z-index: 1000; box-shadow: 0 2px 5px rgba(0,0,0,0.05); transition: all 0.2s;">
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
            <span class="card-tag" data-i18n="proj1_tag">· Python 回测 &amp; 归因</span>
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
            <span class="card-text" data-i18n="proj2_name">A股择时策略</span>
            <span class="card-tag" data-i18n="proj2_tag">· 宏观 + 情绪指标</span>
        </div>
        <div class="card-buttons">
            <button onclick="window.open('https://github.com/hanson-sw/astock-strategy', '_blank')" class="btn btn-outline">
                <i class="fab fa-github"></i> Repository
            </button>
        </div>
    </div>

    <h2 class="section-title" style="margin-top: 3.5rem;">
        <i class="fas fa-chart-area" style="color: #2563eb;"></i> <span data-i18n="mc_title">实盘量化引擎：蒙特卡洛股价路径预测</span>
    </h2>
    <p style="color: #64748b; font-size: 0.95rem; margin-bottom: 1.5rem;" data-i18n="mc_desc">
        支持A股(后缀.SS/.SZ)与美股。系统将自动拉取真实历史数据测算参数，并在后台进行 <b>5000次</b> Itô 随机漫步，生成未来走势的双色概率密度热力图。
    </p>

    <div class="model-panel" style="background: #ffffff; border-radius: 16px; padding: 1.5rem; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0,0,0,0.03); margin-bottom: 1.5rem;">
        <div style="display: flex; flex-wrap: wrap; gap: 1rem; align-items: flex-end;">
            
            <div style="flex: 2; min-width: 220px; position: relative;">
                <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;" data-i18n="mc_ticker">股票代码 (Ticker)</label>
                <div style="display: flex; gap: 0.5rem;">
                    <input type="text" id="stockTicker" value="AAPL" oninput="handleTickerSearch()" autocomplete="off" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none; text-transform: uppercase;" placeholder="尝试输入 A 或 600..." />
                    <button onclick="fetchStockData()" id="fetchBtn" class="btn btn-outline" style="padding: 0 1rem; white-space: nowrap; flex-shrink: 0;">
                        <i class="fas fa-cloud-download-alt"></i> <span data-i18n="mc_pull">拉取</span>
                    </button>
                </div>
                <div id="autocompleteList" style="display:none; position:absolute; top: 100%; left: 0; right: 0; background: #fff; border: 1px solid #cbd5e1; border-radius: 8px; margin-top: 4px; max-height: 200px; overflow-y: auto; z-index: 999; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></div>
            </div>

            <div style="flex: 1; min-width: 90px;">
                <label id="priceLabel" style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;">当前股价 ($)</label>
                <input type="number" id="currentPrice" value="170.00" step="0.01" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none; background: #f8fafc;" />
            </div>

            <div style="flex: 1; min-width: 90px;">
                <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;" data-i18n="mc_vol">波动率 (σ)</label>
                <input type="number" id="impliedVol" value="0.25" step="0.001" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none; background: #f8fafc;" />
            </div>

            <div style="flex: 1; min-width: 90px;">
                <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;" data-i18n="mc_mu">期望收益 (μ)</label>
                <input type="number" id="expReturn" value="0.08" step="0.001" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none; background: #f8fafc;" />
            </div>

            <div style="flex: 1; min-width: 90px;">
                <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;" data-i18n="mc_days">预测天数</label>
                <input type="number" id="timeHorizon" value="252" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none;" />
            </div>

            <button onclick="runSimulation()" id="simBtn" class="btn btn-primary" style="height: 42px; padding: 0 1.5rem; white-space: nowrap; flex-shrink: 0;">
                <i class="fas fa-play"></i> <span data-i18n="mc_run">运行</span>
            </button>
        </div>
        <div id="dataStatus" style="font-size: 0.8rem; color: #2563eb; margin-top: 0.8rem; font-weight: 500; min-height: 1.2rem;"></div>
    </div>

    <div id="chartContainer" style="position: relative; background: #0f172a; border-radius: 16px; padding: 1rem; border: 1px solid #1e293b; box-shadow: 0 10px 25px rgba(0,0,0,0.15); transition: all 0.3s ease;">
        <button onclick="toggleFullscreen()" style="position: absolute; top: 15px; right: 15px; z-index: 100; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); border-radius: 8px; padding: 0.5rem 0.8rem; cursor: pointer; color: #f8fafc; transition: all 0.2s;">
            <i id="fullscreenIcon" class="fas fa-expand"></i>
        </button>
        <div id="itoChart" style="width: 100%; height: 480px;"></div>
    </div>

    <h2 class="section-title">
        <i class="fas fa-paper-plane"></i> <span data-i18n="contact_title">联系我</span>
    </h2>
    <div class="contact-wrapper">
        <a href="mailto:sw6245@nyu.edu" class="contact-tag">
            <i class="fas fa-envelope"></i> sw6245@nyu.edu
        </a>
        <a href="tel:+8615908963789" class="contact-tag">
            <i class="fas fa-phone"></i> +86 159 0896 3789
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

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" />
<script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>

<style>
    .cv-container { max-width: 800px; margin: 0 auto; padding: 2rem 1.5rem; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; color: #0f172a; position: relative;}
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
    .btn { display: inline-flex; align-items: center; gap: 0.4rem; padding: 0.5rem 1.2rem; border-radius: 40px; font-size: 0.85rem; font-weight: 500; cursor: pointer; transition: background 0.2s; border: none; }
    .btn-primary { background: #2563eb; color: white; box-shadow: 0 4px 12px rgba(37, 99, 235, 0.15); }
    .btn-primary:hover { background: #1d4ed8; }
    .btn-outline { background: transparent; color: #334155; border: 1px solid #cbd5e1; }
    .btn-outline:hover { background: #f8fafc; border-color: #94a3b8; }
    .contact-wrapper { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 0.5rem; }
    .contact-tag { display: inline-flex; align-items: center; gap: 0.5rem; color: #334155; text-decoration: none; font-size: 0.9rem; font-weight: 500; background: #f1f5f9; padding: 0.5rem 1.1rem; border-radius: 30px; transition: all 0.2s; }
    .contact-tag:hover { background: #e2e8f0; color: #0f172a; }
    .ai-top-border { padding-top: 2rem; border-top: 1px solid #eef2f6; }
    .search-wrapper { display: flex; gap: 0.6rem; flex-wrap: wrap; }
    #aiSearchInput { flex: 1; min-width: 260px; padding: 0.75rem 1.2rem; border-radius: 40px; border: 1px solid #cbd5e1; font-size: 0.95rem; background: #f8fafc; outline: none; transition: all 0.2s; }
    #aiSearchInput:focus { border-color: #2563eb; background: #ffffff; box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1); }
    #aiSearchResult { margin-top: 1.2rem; font-size: 0.95rem; color: #334155; padding: 0 0.5rem; line-height: 1.5; }
    .search-tip { font-size: 0.8rem; color: #94a3b8; margin-top: 0.6rem; }
    .chart-fullscreen { position: fixed !important; top: 0 !important; left: 0 !important; width: 100vw !important; height: 100vh !important; z-index: 9999 !important; border-radius: 0 !important; margin: 0 !important; padding: 2rem !important; box-sizing: border-box; background: #0f172a !important; }
    .chart-fullscreen #itoChart { height: 100% !important; }
    
    .autocomplete-item { padding: 10px 12px; cursor: pointer; border-bottom: 1px solid #f1f5f9; font-size: 0.85rem; color: #334155; transition: background 0.1s; }
    .autocomplete-item:hover { background: #eff6ff; color: #2563eb; }
    .autocomplete-item strong { color: #0f172a; }

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
    // ================= 1. 多语言 (i18n) 系统 =================
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
        proj2_name: { zh: "A股择时策略", en: "A-Share Timing Strategy" },
        proj2_tag: { zh: "· 宏观 + 情绪指标", en: "· Macro + Sentiment Indicators" },
        mc_title: { zh: "实盘量化引擎：蒙特卡洛股价路径预测", en: "Live Quant Engine: Monte Carlo Path Prediction" },
        mc_desc: { zh: "支持A股(后缀.SS/.SZ)与美股。系统将自动拉取真实历史数据测算参数，并在后台进行 <b>5000次</b> Itô 随机漫步，生成未来走势的双色概率密度热力图。", en: "Supports US & China A-shares (.SS/.SZ). Auto-fetches live data to estimate parameters, runs <b>5000</b> Itô random walks, and generates a dual-color probability density heatmap." },
        mc_ticker: { zh: "股票代码 (Ticker)", en: "Stock Ticker" },
        mc_pull: { zh: "拉取", en: "Fetch" },
        mc_vol: { zh: "波动率 (σ)", en: "Volatility (σ)" },
        mc_mu: { zh: "期望收益 (μ)", en: "Expected Ret (μ)" },
        mc_days: { zh: "预测天数", en: "Horizon (Days)" },
        mc_run: { zh: "运行", en: "Run" },
        contact_title: { zh: "联系我", en: "Contact Me" },
        contact_gh: { zh: "GitHub 主页", en: "GitHub Profile" },
        ai_title: { zh: "AI 智能搜索 (LLM 接入)", en: "AI Financial Assistant (LLM)" },
        ai_btn: { zh: "提问", en: "Ask AI" },
        ai_tip: { zh: "代码已预留真实 API 接入逻辑，填入 Key 即可激活大模型，否则将展示模拟演示。", en: "Real API integration reserved in code. Provide Key to activate, otherwise shows mock demo." }
    };

    let currentLang = 'zh';
    function toggleLang() {
        currentLang = currentLang === 'zh' ? 'en' : 'zh';
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if(i18nDict[key]) el.innerHTML = i18nDict[key][currentLang];
        });
        document.getElementById('stockTicker').placeholder = currentLang === 'zh' ? "尝试输入 A 或 600..." : "Try typing AAPL or TSLA...";
        document.getElementById('aiSearchInput').placeholder = currentLang === 'zh' ? "输入你想问的金融问题…" : "Ask a financial question...";
        
        // 更新货币符号相关的 Label
        document.getElementById('priceLabel').innerText = currentLang === 'zh' ? `当前股价 (${currentCurrency})` : `Current Price (${currentCurrency})`;
        
        if(chartInstance) runSimulation(); 
    }

    // ================= 2. 股票智能联想 (Yahoo Finance API) =================
    let searchTimer = null;
    async function handleTickerSearch() {
        clearTimeout(searchTimer);
        const q = document.getElementById('stockTicker').value.trim();
        const listDiv = document.getElementById('autocompleteList');
        
        if(q.length < 1) { listDiv.style.display = 'none'; return; }
        
        searchTimer = setTimeout(async () => {
            try {
                const proxyUrl = `https://api.allorigins.win/get?url=`;
                const targetUrl = encodeURIComponent(`https://query2.finance.yahoo.com/v1/finance/search?q=${q}&quotesCount=6&newsCount=0`);
                const res = await fetch(proxyUrl + targetUrl);
                const raw = await res.json();
                const data = JSON.parse(raw.contents);
                
                if(data.quotes && data.quotes.length > 0) {
                    let html = '';
                    data.quotes.forEach(item => {
                        if(item.quoteType === 'EQUITY' || item.quoteType === 'ETF') {
                            const name = item.shortname || item.longname || '';
                            html += `<div class="autocomplete-item" onclick="selectTicker('${item.symbol}')">
                                        <strong>${item.symbol}</strong> - ${name} <span style="color:#94a3b8;font-size:0.8em">(${item.exchDisp})</span>
                                     </div>`;
                        }
                    });
                    if(html) {
                        listDiv.innerHTML = html;
                        listDiv.style.display = 'block';
                    } else {
                        listDiv.style.display = 'none';
                    }
                }
            } catch(e) { console.error(e); }
        }, 400);
    }

    function selectTicker(symbol) {
        document.getElementById('stockTicker').value = symbol;
        document.getElementById('autocompleteList').style.display = 'none';
        fetchStockData();
    }

    document.addEventListener('click', function(e) {
        if(!document.getElementById('autocompleteList').contains(e.target) && e.target.id !== 'stockTicker') {
            document.getElementById('autocompleteList').style.display = 'none';
        }
    });

    // ================= 3. 量化图表与数据拉取 =================
    let chartInstance = null;
    let currentCurrency = '$'; // 全局记录当前货币符号

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
        
        // 动态判定货币符号 (A股为 ¥，其它默认 $)
        currentCurrency = (ticker.endsWith('.SS') || ticker.endsWith('.SZ')) ? '¥' : '$';
        document.getElementById('priceLabel').innerText = currentLang === 'zh' ? `当前股价 (${currentCurrency})` : `Current Price (${currentCurrency})`;

        const statusDiv = document.getElementById('dataStatus');
        const fetchBtn = document.getElementById('fetchBtn');
        statusDiv.innerHTML = `<i class="fas fa-spinner fa-spin"></i> ${currentLang==='zh'?'拉取数据中...':'Fetching data...'}`;
        fetchBtn.disabled = true;

        try {
            // 加入 disableCache=true 防止代理服务器返回过期的 A股缓存
            const yahooUrl = `https://query1.finance.yahoo.com/v8/finance/chart/${ticker}?range=1y&interval=1d`;
            const proxyUrl = `https://api.allorigins.win/get?disableCache=true&url=${encodeURIComponent(yahooUrl)}`;
            const response = await fetch(proxyUrl);
            const rawData = await response.json();
            const data = JSON.parse(rawData.contents);

            if (!data.chart || !data.chart.result) throw new Error("Ticker not found in Yahoo Finance");

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
            
            let msg = currentLang === 'zh' ? 
                `成功！历史年化波动率 ${(annVol*100).toFixed(1)}%, 期望收益 ${(annMu*100).toFixed(1)}%。` :
                `Success! Hist. Vol ${(annVol*100).toFixed(1)}%, Exp. Ret ${(annMu*100).toFixed(1)}%.`;
            statusDiv.innerHTML = `<i class="fas fa-check-circle" style="color: #10b981;"></i> ${msg}`;
            
            runSimulation();
        } catch (error) {
            console.error(error);
            statusDiv.innerHTML = `<i class="fas fa-exclamation-triangle" style="color: #ef4444;"></i> ${currentLang==='zh'?'拉取失败，请检查代码(A股务必添加后缀 .SS 或 .SZ)':'Fetch failed. Check ticker (China stocks need .SS or .SZ)'}`;
        } finally {
            fetchBtn.disabled = false;
        }
    }

    function generateMonteCarloData(S0, mu, sigma, days, numPaths = 5000, numBins = 70) {
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

        // 保留所有发生频数 >= 1 的网格数据
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

        document.getElementById('simBtn').innerHTML = `<i class="fas fa-spinner fa-spin"></i> ${currentLang==='zh'?'计算中':'Computing'}`;

        setTimeout(() => {
            const data = generateMonteCarloData(S0, mu, sigma, days, 5000, 70);
            let xAxisData = [];
            for(let i = 0; i <= days; i++) xAxisData.push(i);

            if (!chartInstance) chartInstance = echarts.init(document.getElementById('itoChart'));

            const titleText = currentLang === 'zh' ? '5000次 蒙特卡洛概率密度预测 vs 单次闪光模拟' : '5000-Path Monte Carlo Heatmap vs Single Glowing Path';

            const option = {
                title: { text: titleText, left: 'center', textStyle: { color: '#f8fafc', fontSize: 16, fontWeight: 600 } },
                tooltip: {
                    position: 'top', backgroundColor: 'rgba(15, 23, 42, 0.95)', borderColor: '#334155', textStyle: { color: '#f8fafc' },
                    formatter: function (params) {
                        if(params.seriesType === 'heatmap') {
                            let day = params.value[0], binIdx = params.value[1], count = params.value[2];
                            let lower = parseFloat(data.yAxisLabels[binIdx]);
                            let upper = lower + data.binSize;
                            let prob = ((count / data.numPaths) * 100).toFixed(2);
                            return `<div style="font-weight:bold; margin-bottom:4px; color:#38bdf8;">${currentLang==='zh'?'第 '+day+' 天预测':'Day '+day+' Forecast'}</div>
                                    ${currentLang==='zh'?'价格区间':'Price Range'}: <b>[ ${currentCurrency}${lower.toFixed(2)} , ${currentCurrency}${upper.toFixed(2)} ]</b><br/>
                                    ${currentLang==='zh'?'落入概率':'Probability'}: <b style="color:#f472b6;">${prob}%</b> <span style="color:#94a3b8; font-size:0.85em;">(N=${count})</span>`;
                        } else {
                            return `<div style="font-weight:bold; margin-bottom:4px; color:#38bdf8;">${params.seriesName}</div>
                                    Day ${params.dataIndex} <br/>${currentLang==='zh'?'预期股价':'Expected Price'}: <b>${currentCurrency}${params.value.toFixed(2)}</b>`;
                        }
                    }
                },
                visualMap: {
                    // 从真实的最小频数(1次) 到真实的最大频数，确保渐变从头到尾无截断
                    min: 1, 
                    max: data.maxFreq, 
                    calculable: true, orient: 'vertical', right: '2%', top: 'center',
                    inRange: { 
                        // 深邃蓝(极小概率) -> 亮紫 -> 粉红 -> 荧光红(最大概率)，过渡平滑无断层
                        color: ['#1e3a8a', '#8b5cf6', '#d946ef', '#f43f5e'] 
                    },
                    textStyle: { color: '#94a3b8', fontSize: 10 },
                    formatter: function (value) { return value.toFixed(0) + (currentLang==='zh'?' 次':' Hits'); }
                },
                grid: { left: '6%', right: '12%', top: '15%', bottom: '15%', containLabel: true },
                xAxis: { type: 'category', data: xAxisData, name: currentLang==='zh'?'交易日 (Days)':'Trading Days', nameLocation: 'middle', nameGap: 25, axisLabel: {color: '#94a3b8'}, nameTextStyle: {color: '#cbd5e1'} },
                yAxis: [
                    { type: 'category', data: data.yAxisLabels, show: false }, 
                    { type: 'value', min: data.globalMin, max: data.globalMax, axisLabel: { color: '#94a3b8', formatter: function(val) { return currentCurrency + val.toFixed(0); } }, splitLine: { lineStyle: {color: '#1e293b', type: 'dashed'} } }
                ],
                series: [
                    { 
                        name: 'Probability Heatmap', type: 'heatmap', data: data.heatmapData, yAxisIndex: 0, 
                        itemStyle: { opacity: 0.8 }, emphasis: { itemStyle: { borderColor: '#fff', borderWidth: 1 } } 
                    },
                    { 
                        name: currentLang==='zh'?'单次发光模拟 (Simulated)':'Single Neon Path', type: 'line', data: data.singleSimPath, yAxisIndex: 1, 
                        showSymbol: false, 
                        lineStyle: { width: 3, color: '#22d3ee', shadowColor: '#22d3ee', shadowBlur: 15 }, 
                        itemStyle: { color: '#22d3ee' }, z: 10 
                    },
                    { 
                        name: currentLang==='zh'?'理论期望 (Deterministic)':'Expected Path', type: 'line', data: data.idealPath, yAxisIndex: 1, 
                        showSymbol: false, lineStyle: { width: 2, type: 'dashed', color: '#10b981' }, itemStyle: { color: '#10b981' }, z: 10 
                    }
                ]
            };

            chartInstance.setOption(option);
            document.getElementById('simBtn').innerHTML = `<i class="fas fa-play"></i> <span data-i18n="mc_run">${currentLang==='zh'?'运行':'Run'}</span>`;
        }, 50);
    }

    window.onload = function() { runSimulation(); };
    window.addEventListener('resize', function() { if(chartInstance) chartInstance.resize(); });

    // ================= 4. AI 引擎 =================
    async function handleAISearch() {
        const input = document.getElementById('aiSearchInput');
        const resultDiv = document.getElementById('aiSearchResult');
        const query = input.value.trim();
        if (!query) return;

        resultDiv.innerHTML = '🤔 ' + (currentLang==='zh'?'正在思考…':'Thinking...');

        try {
            const API_KEY = 'YOUR_API_KEY_HERE'; 
            const API_URL = 'https://api.deepseek.com/chat/completions';

            if (API_KEY !== 'YOUR_API_KEY_HERE') {
                const response = await fetch(API_URL, {
                    method: 'POST', headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${API_KEY}` },
                    body: JSON.stringify({
                        model: 'deepseek-chat',
                        messages: [
                            {"role": "system", "content": `你是一个金融分析师。请用${currentLang==='zh'?'中文':'English'}简明回答。`},
                            {"role": "user", "content": query}
                        ]
                    })
                });
                const data = await response.json();
                resultDiv.innerHTML = '💡 ' + data.choices[0].message.content.replace(/\n/g, '<br/>');
            } else {
                await new Promise(resolve => setTimeout(resolve, 800));
                const mockZh = ['模型当前处于展示模式，填入 Key 即可解锁完整 AI。建议关注 A 股大消费板块估值修复。'];
                const mockEn = ['Model is in Demo mode. Please provide an API Key to unlock the LLM. Recommend monitoring consumer sector valuation recovery.'];
                resultDiv.innerHTML = '💡 ' + (currentLang === 'zh' ? mockZh[0] : mockEn[0]);
            }
        } catch (error) {
            resultDiv.innerHTML = '❌ Request Failed.';
        }
    }

    document.getElementById('aiSearchInput').addEventListener('keydown', function(e) {
        if (e.key === 'Enter') handleAISearch();
    });
</script>
