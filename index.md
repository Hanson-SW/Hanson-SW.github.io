---
layout: default
title: 金融工程 · 个人主页
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/echarts/5.4.3/echarts.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" />

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
            <span class="card-text" data-i18n="proj2_name">A股回测模型</span>
<span class="card-tag" data-i18n="proj2_tag">· 宏观 + 情绪指标</span>

<div class="card-buttons">
    <button onclick="window.open('https://github.com/hanson-sw/astock-strategy', '_blank')" class="btn btn-outline">
        <i class="fab fa-github"></i> Repository
    </button>
    
    <button onclick="window.open('./backtest.html', '_blank')" class="btn btn-primary" style="margin-left: 10px;">
        <i class="fas fa-chart-line"></i> 运行回测模型
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
        支持A股与美股。自动拉取历史数据测算参数进行 Itô 随机漫步。概率热力图已逐日归一化(Per-Day Normalized)，确保主趋势线时刻高亮。
    </p>

    <div class="model-panel" style="background: #ffffff; border-radius: 16px; padding: 1.5rem; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0,0,0,0.03); margin-bottom: 1.5rem;">
        <div style="display: flex; flex-wrap: wrap; gap: 1rem; align-items: flex-end;">
            
            <div style="flex: 2; min-width: 200px; position: relative;">
                <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;" data-i18n="mc_ticker">股票代码 (Ticker)</label>
                <div style="display: flex; gap: 0.5rem;">
                    <input type="text" id="stockTicker" value="AAPL" oninput="handleLocalSearch()" autocomplete="off" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none; text-transform: uppercase;" placeholder="输入 AAPL, 600519.SS..." />
                    <button onclick="fetchStockData()" id="fetchBtn" class="btn btn-outline" style="padding: 0 1rem; white-space: nowrap; flex-shrink: 0;">
                        <i class="fas fa-cloud-download-alt"></i> <span data-i18n="mc_pull">拉取</span>
                    </button>
                </div>
                <div id="autocompleteList" style="display:none; position:absolute; top: 100%; left: 0; right: 0; background: #fff; border: 1px solid #cbd5e1; border-radius: 8px; margin-top: 4px; max-height: 200px; overflow-y: auto; z-index: 999; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></div>
            </div>

            <div style="flex: 1; min-width: 85px;">
                <label id="priceLabel" style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;">当前股价 ($)</label>
                <input type="number" id="currentPrice" value="175.00" step="0.01" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none; background: #f8fafc;" />
            </div>

            <div style="flex: 1; min-width: 85px;">
                <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;" data-i18n="mc_vol">波动率 (σ)</label>
                <input type="number" id="impliedVol" value="0.22" step="0.001" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none; background: #f8fafc;" />
            </div>

            <div style="flex: 1; min-width: 85px;">
                <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;" data-i18n="mc_mu">期望收益 (μ)</label>
                <input type="number" id="expReturn" value="0.08" step="0.001" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none; background: #f8fafc;" />
            </div>
            
            <div style="flex: 1; min-width: 85px;">
                <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;" data-i18n="mc_paths">模拟次数</label>
                <input type="number" id="numPaths" value="5000" step="500" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none;" />
            </div>

            <div style="flex: 1; min-width: 85px;">
                <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;" data-i18n="mc_days">预测天数</label>
                <input type="number" id="timeHorizon" value="252" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none;" />
            </div>

            <button onclick="runSimulation()" id="simBtn" class="btn btn-primary" style="height: 42px; padding: 0 1.5rem; white-space: nowrap; flex-shrink: 0;">
                <i class="fas fa-play"></i> <span data-i18n="mc_run">运行</span>
            </button>
        </div>
        <div id="dataStatus" style="font-size: 0.8rem; color: #2563eb; margin-top: 0.8rem; font-weight: 500; min-height: 1.2rem;"></div>
    </div>

    <div id="pdfExportWrapper" style="background: #ffffff; border-radius: 16px; padding: 1.5rem; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0,0,0,0.03); position: relative;">
        
        <div style="position: absolute; top: 1.5rem; right: 1.5rem; z-index: 100; display: flex; gap: 0.5rem;">
            <button onclick="downloadPDF()" style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 8px; padding: 0.5rem 0.8rem; cursor: pointer; color: #475569; transition: all 0.2s;" title="导出报告为 PDF">
                <i class="fas fa-file-pdf"></i>
            </button>
            <button onclick="toggleFullscreen()" style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 8px; padding: 0.5rem 0.8rem; cursor: pointer; color: #475569; transition: all 0.2s;" title="全屏放大">
                <i id="fullscreenIcon" class="fas fa-expand"></i>
            </button>
        </div>

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
    
    .chart-fullscreen { position: fixed !important; top: 0 !important; left: 0 !important; width: 100vw !important; height: 100vh !important; z-index: 9999 !important; border-radius: 0 !important; margin: 0 !important; padding: 2rem !important; box-sizing: border-box; background: #ffffff !important; overflow-y: auto;}
    .chart-fullscreen #itoChart { height: 90% !important; }
    
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
        mc_desc: { zh: "支持A股与美股。自动拉取历史数据测算参数进行 Itô 随机漫步。概率热力图已逐日归一化(Per-Day Normalized)，确保主趋势线时刻高亮。", en: "Supports US & A-shares. Auto-fetches live data for Itô random walks. Heatmap is Per-Day Normalized to ensure the main trend is always highlighted." },
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
        ai_tip: { zh: "代码已预留真实 API 接入逻辑，填入 Key 即可激活大模型，否则将展示模拟演示。", en: "Real API integration reserved in code. Provide Key to activate, otherwise shows mock demo." }
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

    // ================= 2. 本地容灾股票库 =================
    const localTickerDB = [
        { symbol: 'AAPL', name: '苹果公司 (Apple)' },
        { symbol: 'MSFT', name: '微软 (Microsoft)' },
        { symbol: 'NVDA', name: '英伟达 (NVIDIA)' },
        { symbol: 'TSLA', name: '特斯拉 (Tesla)' },
        { symbol: 'GOOGL', name: '谷歌 (Alphabet)' },
        { symbol: 'AMZN', name: '亚马逊 (Amazon)' },
        { symbol: 'META', name: 'Meta Platforms' },
        { symbol: 'SPY', name: '标普500指数 ETF' },
        { symbol: 'QQQ', name: '纳斯达克100 ETF' },
        { symbol: '600519.SS', name: '贵州茅台 (Kweichow Moutai)' },
        { symbol: '000858.SZ', name: '五粮液 (Wuliangye)' },
        { symbol: '600036.SS', name: '招商银行 (China Merchants Bank)' },
        { symbol: '601318.SS', name: '中国平安 (Ping An Insurance)' },
        { symbol: '002594.SZ', name: '比亚迪 (BYD)' },
        { symbol: '300750.SZ', name: '宁德时代 (CATL)' },
        { symbol: '000300.SS', name: '沪深300指数 (CSI 300)' },
        { symbol: 'BABA', name: '阿里巴巴 (Alibaba)' }
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
        if(list && !list.contains(e.target) && e.target.id !== 'stockTicker') {
            list.style.display = 'none';
        }
    });

    // ================= 3. 量化核心与防止PDF空白方案 =================
    let chartInstance = null;
    let currentCurrency = '$'; 

    function toggleFullscreen() {
        const container = document.getElementById('pdfExportWrapper');
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

    // 【核心修复】防止 PDF 空白的终极杀招
    function downloadPDF() {
        if(typeof html2pdf === 'undefined') {
            alert('PDF 导出组件尚未加载完毕，请稍后再试。');
            return;
        }

        const element = document.getElementById('pdfExportWrapper');
        const chartDiv = document.getElementById('itoChart');
        const ticker = document.getElementById('stockTicker').value || 'Model';
        
        // 1. 将交互式 ECharts Canvas 转换为静态高质量图片
        const imgData = chartInstance.getDataURL({
            type: 'png',
            pixelRatio: 2,
            backgroundColor: '#ffffff'
        });
        
        const imgEl = document.createElement('img');
        imgEl.src = imgData;
        imgEl.style.width = '100%';
        imgEl.id = 'tempPdfImg'; // 打个标记
        
        // 2. 隐藏动态图表，插入静态图，并隐藏不需要打印的按钮
        chartDiv.style.display = 'none';
        element.appendChild(imgEl);
        
        const buttons = element.querySelectorAll('button');
        buttons.forEach(b => b.style.display = 'none');
        
        const opt = {
            margin:       0.2,
            filename:     `Quant_Simulation_${ticker}.pdf`,
            image:        { type: 'jpeg', quality: 0.98 },
            html2canvas:  { scale: 2, useCORS: true, logging: false },
            jsPDF:        { unit: 'in', format: 'letter', orientation: 'landscape' }
        };
        
        // 3. 执行导出
        html2pdf().set(opt).from(element).save().then(() => {
            // 4. 导出完毕，把图片删掉，恢复原状
            buttons.forEach(b => b.style.display = 'inline-flex');
            element.removeChild(imgEl);
            chartDiv.style.display = 'block';
        });
    }

    function randomNormal() {
        let u = 0, v = 0;
        while(u === 0) u = Math.random();
        while(v === 0) v = Math.random();
        return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
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
            const yahooUrl = `https://query1.finance.yahoo.com/v8/finance/chart/${ticker}?range=1y&interval=1d`;
            const proxyUrl = `https://api.allorigins.win/raw?url=${encodeURIComponent(yahooUrl)}`;
            
            const controller = new AbortController();
            const timeoutId = setTimeout(() => controller.abort(), 5000);
            const response = await fetch(proxyUrl, { signal: controller.signal });
            clearTimeout(timeoutId);
            
            if (!response.ok) throw new Error("Proxy connection failed");
            const data = await response.json();

            if (!data.chart || !data.chart.result) throw new Error("Ticker not found");

            const closePrices = data.chart.result[0].indicators.quote[0].close.filter(p => p !== null && p !== undefined);
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
            console.warn("API Fetch failed, using fallback mechanism.", error);
            document.getElementById('currentPrice').value = ticker.includes('600519') ? "1500.00" : "175.00";
            document.getElementById('impliedVol').value = "0.220";
            document.getElementById('expReturn').value = "0.080";
            
            statusDiv.innerHTML = `<i class="fas fa-exclamation-triangle" style="color: #f59e0b;"></i> ${currentLang==='zh'?'网络受限，已自动启用备用参数出图。':'Network limited. Using fallback parameters.'}`;
            runSimulation();
        } finally {
            fetchBtn.disabled = false;
        }
    }

    function generateMonteCarloData(S0, mu, sigma, days, numPaths, numBins) {
        let dt = 1 / 252;
        let globalMin = S0, globalMax = S0;
        
        let drift = (mu - 0.5 * sigma * sigma) * dt;
        let vol = sigma * Math.sqrt(dt);
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
                let Z = Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
                
                currentPrice = currentPrice * Math.exp(drift + vol * Z);
                allPrices[p * (days + 1) + i] = currentPrice;
                
                if(p === 0) singleSimPath[i] = currentPrice;
                if(currentPrice < globalMin) globalMin = currentPrice;
                if(currentPrice > globalMax) globalMax = currentPrice;
            }
        }

        globalMin *= 0.95; globalMax *= 1.05;
        let binSize = (globalMax - globalMin) / numBins;
        
        let matrix = [];
        for(let d=0; d<=days; d++) {
            matrix.push(new Int32Array(numBins));
        }
        let maxFreqPerDay = new Int32Array(days + 1);

        for(let p = 0; p < numPaths; p++) {
            for(let d = 0; d <= days; d++) {
                let price = allPrices[p * (days + 1) + d];
                let binIdx = Math.floor((price - globalMin) / binSize);
                if(binIdx >= numBins) binIdx = numBins - 1;
                if(binIdx < 0) binIdx = 0;
                
                matrix[d][binIdx]++;
                if(matrix[d][binIdx] > maxFreqPerDay[d]) {
                    maxFreqPerDay[d] = matrix[d][binIdx];
                }
            }
        }

        let heatmapData = [];
        for(let d = 0; d <= days; d++) {
            for(let b = 0; b < numBins; b++) {
                if(matrix[d][b] > 0) {
                    let norm = maxFreqPerDay[d] > 0 ? (matrix[d][b] / maxFreqPerDay[d]) : 0;
                    heatmapData.push([d, b, matrix[d][b], norm]);
                }
            }
        }

        let yAxisLabels = [];
        for(let b = 0; b < numBins; b++) {
            yAxisLabels.push((globalMin + b * binSize).toFixed(2));
        }

        let idealPath = [];
        for(let i = 0; i <= days; i++) {
            idealPath.push(S0 * Math.exp(mu * dt * i));
        }

        return { heatmapData, yAxisLabels, globalMin, globalMax, singleSimPath: Array.from(singleSimPath), idealPath, binSize, numPaths };
    }

    function runSimulation() {
        if(typeof echarts === 'undefined') {
            document.getElementById('simBtn').innerHTML = `<i class="fas fa-exclamation-triangle"></i>`;
            alert('图表库加载中，请稍后再试。');
            return;
        }

        const ticker = document.getElementById('stockTicker').value || 'Model';
        const S0 = parseFloat(document.getElementById('currentPrice').value);
        const sigma = parseFloat(document.getElementById('impliedVol').value);
        const mu = parseFloat(document.getElementById('expReturn').value);
        const days = parseInt(document.getElementById('timeHorizon').value);
        const pathsCount = parseInt(document.getElementById('numPaths').value) || 5000;

        document.getElementById('simBtn').innerHTML = `<i class="fas fa-spinner fa-spin"></i> ${currentLang==='zh'?'极速计算中':'Computing'}`;

        setTimeout(() => {
            const data = generateMonteCarloData(S0, mu, sigma, days, pathsCount, 80);
            let xAxisData = [];
            for(let i = 0; i <= days; i++) xAxisData.push(i);

            const today = new Date();
            const dateStr = today.getFullYear() + '/' + String(today.getMonth() + 1).padStart(2, '0') + '/' + String(today.getDate()).padStart(2, '0');
            const watermarkText = currentLang === 'zh' 
                ? `模拟日期: ${dateStr}\n分析标的: ${ticker}\n当前价格: ${currentCurrency}${S0}\n设定波动率(σ): ${sigma}\n期望收益率(μ): ${mu}\n模拟路径数: ${pathsCount}`
                : `Date: ${dateStr}\nTicker: ${ticker}\nPrice: ${currentCurrency}${S0}\nVol (σ): ${sigma}\nExp. Ret (μ): ${mu}\nSim Paths: ${pathsCount}`;

            if (!chartInstance) chartInstance = echarts.init(document.getElementById('itoChart'));

            const titleText = currentLang === 'zh' ? `${pathsCount}次 蒙特卡洛路径模拟 (逐日归一化)` : `${pathsCount}-Path Monte Carlo (Per-Day Normalized)`;

            const option = {
                backgroundColor: '#ffffff',
                title: { text: titleText, left: 'center', top: 10, textStyle: { color: '#334155', fontSize: 16 } },
                graphic: [
                    {
                        type: 'text', left: '8%', top: '12%',
                        style: { text: watermarkText, fontSize: 10, fill: '#64748b', fontFamily: 'sans-serif', lineHeight: 16 },
                        z: 100
                    }
                ],
                tooltip: {
                    position: 'top', backgroundColor: 'rgba(255, 255, 255, 0.95)', borderColor: '#cbd5e1', textStyle: { color: '#334155' },
                    formatter: function (params) {
                        if(params.seriesType === 'heatmap') {
                            let day = params.value[0], binIdx = params.value[1], count = params.value[2];
                            let lower = parseFloat(data.yAxisLabels[binIdx]);
                            let upper = lower + data.binSize;
                            let prob = ((count / data.numPaths) * 100).toFixed(2);
                            return `<div style="font-weight:bold; margin-bottom:4px; color:#2563eb;">${currentLang==='zh'?'第 '+day+' 天预测':'Day '+day+' Forecast'}</div>
                                    ${currentLang==='zh'?'价格区间':'Price Range'}: <b>[ ${currentCurrency}${lower.toFixed(2)} , ${currentCurrency}${upper.toFixed(2)} ]</b><br/>
                                    ${currentLang==='zh'?'绝对落入概率':'Abs Probability'}: <b style="color:#ef4444;">${prob}%</b> <span style="color:#94a3b8; font-size:0.85em;">(N=${count})</span>`;
                        } else {
                            return `<div style="font-weight:bold; margin-bottom:4px; color:#2563eb;">${params.seriesName}</div>
                                    Day ${params.dataIndex} <br/>${currentLang==='zh'?'预期股价':'Expected Price'}: <b>${currentCurrency}${params.value.toFixed(2)}</b>`;
                        }
                    }
                },
                visualMap: {
                    dimension: 3, min: 0, max: 1, show: false,
                    inRange: { color: ['#ffffff', '#bfdbfe', '#3b82f6', '#ef4444'] }
                },
                grid: { left: '7%', right: '5%', top: '22%', bottom: '12%', containLabel: true },
                xAxis: { type: 'category', data: xAxisData, name: currentLang==='zh'?'交易日 (Days)':'Trading Days', nameLocation: 'middle', nameGap: 25, axisLabel: {color: '#64748b'}, nameTextStyle: {color: '#64748b'} },
                yAxis: [
                    { type: 'category', data: data.yAxisLabels, show: false }, 
                    { type: 'value', min: data.globalMin, max: data.globalMax, axisLabel: { color: '#64748b', formatter: function(val) { return currentCurrency + val.toFixed(0); } }, splitLine: { lineStyle: {color: '#e2e8f0', type: 'dashed'} } }
                ],
                series: [
                    { name: 'Probability Heatmap', type: 'heatmap', data: data.heatmapData, yAxisIndex: 0, itemStyle: { opacity: 0.9 } },
                    { name: currentLang==='zh'?'单次模拟抽样':'Single Walk Sample', type: 'line', data: data.singleSimPath, yAxisIndex: 1, showSymbol: false, lineStyle: { width: 2, color: '#1e3a8a' }, itemStyle: { color: '#1e3a8a' }, z: 10 },
                    { name: currentLang==='zh'?'无波动理论期望':'Expected Path', type: 'line', data: data.idealPath, yAxisIndex: 1, showSymbol: false, lineStyle: { width: 2, type: 'dashed', color: '#10b981' }, itemStyle: { color: '#10b981' }, z: 10 }
                ]
            };

            chartInstance.setOption(option);
            document.getElementById('simBtn').innerHTML = `<i class="fas fa-play"></i> <span data-i18n="mc_run">${currentLang==='zh'?'运行':'Run'}</span>`;
        }, 150);
    }

    document.addEventListener('DOMContentLoaded', () => { runSimulation(); });
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
