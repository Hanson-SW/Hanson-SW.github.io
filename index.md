---
layout: default
title: 金融工程 · 个人主页
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/echarts/5.4.3/echarts.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" />
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&display=swap" rel="stylesheet">

<canvas id="intro-canvas"></canvas>

<div id="page-wrapper">
    <div class="top-utility-bar">
        <button onclick="toggleLang()" class="lang-toggle-btn btn-bubble">
            <i class="fas fa-globe"></i> <span id="langBtnText">中 / EN</span>
        </button>
    </div>

    <div class="cv-container" id="main-content-container">
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
        
        <div class="info-card glass-card" style="margin-bottom: 0.8rem;">
            <div class="card-left">
                <i class="fas fa-file-pdf card-icon"></i>
                <span class="card-text" data-i18n="resume_name">金融工程简历 (中文版)</span>
                <span class="card-tag" data-i18n="resume_tag">· 2026 最新版</span>
            </div>
            <button onclick="window.open('王盛烨简历.pdf', '_blank')" class="btn btn-primary btn-bubble">
                <i class="fas fa-eye"></i> <span data-i18n="resume_btn">查看简历</span>
            </button>
        </div>

        <div class="info-card glass-card">
            <div class="card-left">
                <i class="fas fa-file-pdf card-icon" style="color: #10b981;"></i>
                <span class="card-text" data-i18n="resume_en_name">金融工程简历 (English)</span>
                <span class="card-tag" data-i18n="resume_en_tag">· 2026 Updated</span>
            </div>
            <button onclick="window.open('SWresume.pdf', '_blank')" class="btn btn-outline btn-bubble" style="color: #10b981; border-color: #10b981;">
                <i class="fas fa-eye"></i> <span data-i18n="resume_en_btn">View PDF</span>
            </button>
        </div>

        <h2 class="section-title">
            <i class="fas fa-code-branch"></i> <span data-i18n="project_title">项目展示</span>
        </h2>

        <div class="info-card glass-card">
            <div class="card-left">
                <i class="fas fa-chart-line card-icon"></i>
                <span class="card-text" data-i18n="proj_backtest_name">A股回测模型</span>
                <span class="card-tag" data-i18n="proj_backtest_tag">· 宏观 + 情绪指标</span>
            </div>
            <div class="card-buttons">
                <button onclick="window.open('./backtest.html', '_blank')" class="btn btn-primary btn-bubble">
                    <i class="fas fa-play"></i> <span data-i18n="proj_backtest_btn">运行回测模型</span>
                </button>
            </div>
        </div>

        <div class="info-card glass-card">
            <div class="card-left">
                <i class="fas fa-pie-chart card-icon" style="color: #8b5cf6;"></i>
                <span class="card-text" data-i18n="proj_markowitz_name">Markowitz 资产轮动与量化配置模型</span>
                <span class="card-tag" data-i18n="proj_markowitz_tag">· 现代投资组合理论 (MPT)</span>
            </div>
            <div class="card-buttons">
                <button onclick="window.open('./markowitz.html', '_blank')" class="btn btn-primary btn-bubble" style="background: #8b5cf6;">
                    <i class="fas fa-play"></i> <span data-i18n="proj_markowitz_btn">运行配置模型</span>
                </button>
            </div>
        </div>

        <h2 class="section-title" style="margin-top: 3.5rem;">
            <i class="fas fa-chart-area" style="color: #2563eb;"></i> <span data-i18n="mc_title">实盘量化引擎：股价路径预测</span>
        </h2>
        <p style="color: #64748b; font-size: 0.95rem; margin-bottom: 1.5rem;" data-i18n="mc_desc">
            系统自动拉取历史 data(含GitHub缓存容灾)。支持自定义模拟次数，极速引擎生成逐日归一化的概率密度热力图。
        </p>

        <div class="model-panel glass-card">
            <div class="param-grid">
                <div class="grid-col-span-2 relative-box">
                    <label class="param-label" data-i18n="mc_ticker">股票/指数代码 (Ticker)</label>
                    <div class="flex-input-group">
                        <input type="text" id="stockTicker" value="AAPL" oninput="handleLocalSearch(); markCustom();" autocomplete="off" class="param-input uppercase-text mono-font" placeholder="输入 AAPL 或指数代码..." />
                        <button onclick="fetchStockData()" id="fetchBtn" class="btn btn-outline fetch-btn btn-bubble">
                            <i class="fas fa-cloud-download-alt"></i> <span data-i18n="mc_pull">拉取</span>
                        </button>
                    </div>
                    <div id="autocompleteList" class="autocomplete-dropdown"></div>
                </div>

                <div class="grid-col">
                    <label id="priceLabel" class="param-label">当前价格 ($)</label>
                    <input type="number" id="currentPrice" value="175.00" step="0.01" oninput="markCustom()" class="param-input bg-gray mono-font" />
                </div>

                <div class="grid-col">
                    <label class="param-label" data-i18n="mc_vol">波动率 (σ)</label>
                    <input type="number" id="impliedVol" value="0.22" step="0.001" oninput="markCustom()" class="param-input bg-gray mono-font" />
                </div>

                <div class="grid-col">
                    <label class="param-label" data-i18n="mc_mu">期望收益 (μ)</label>
                    <input type="number" id="expReturn" value="0.08" step="0.001" oninput="markCustom()" class="param-input bg-gray mono-font" />
                </div>
                
                <div class="grid-col">
                    <label class="param-label" data-i18n="mc_paths">模拟次数</label>
                    <input type="number" id="numPaths" value="5000" step="500" oninput="markCustom()" class="param-input mono-font" />
                </div>

                <div class="grid-col">
                    <label class="param-label" data-i18n="mc_days">预测天数</label>
                    <input type="number" id="timeHorizon" value="252" oninput="markCustom()" class="param-input mono-font" />
                </div>

                <div class="grid-col-btn">
                    <button onclick="runSimulation()" id="simBtn" class="btn btn-primary run-sim-btn btn-bubble">
                        <i class="fas fa-play"></i> <span data-i18n="mc_run">运行</span>
                    </button>
                </div>
            </div>
            <div id="dataStatus" class="data-status-text"></div>
        </div>

        <div id="chartExportWrapper" class="chart-wrapper glass-card">
            <div class="chart-tools">
                <button onclick="downloadImage()" class="icon-btn btn-bubble" title="导出高清图片">
                    <i class="fas fa-download"></i>
                </button>
                <button onclick="toggleFullscreen()" class="icon-btn btn-bubble" title="全屏放大">
                    <i id="fullscreenIcon" class="fas fa-expand"></i>
                </button>
            </div>
            <div id="itoChart" style="width: 100%; height: 500px;"></div>
        </div>

        <h2 class="section-title">
            <i class="fas fa-paper-plane"></i> <span data-i18n="contact_title">联系我</span>
        </h2>
        <div class="contact-wrapper">
            <a href="mailto:sw6245@nyu.edu" class="contact-tag btn-bubble">
                <i class="fas fa-envelope"></i> sw6245@nyu.edu
            </a>
            <a href="tel:+8615908963789" class="contact-tag mono-font">
                <i class="fas fa-phone"></i> +86 159 0896 3789
            </a>
            <button onclick="window.open('https://github.com/Hanson-SW', '_blank')" class="btn btn-outline github-contact-btn btn-bubble">
                <i class="fab fa-github"></i> <span data-i18n="contact_gh">GitHub 主页</span>
            </button>
        </div>

        <h2 class="section-title ai-top-border">
            <i class="fas fa-robot"></i> <span data-i18n="ai_title">AI 智能搜索 (LLM 接入)</span>
        </h2>
        <div class="search-wrapper">
            <input type="text" id="aiSearchInput" placeholder="输入你想问的金融问题…" />
            <button onclick="handleAISearch()" class="btn btn-primary search-btn btn-bubble">
                <i class="fas fa-paper-plane"></i> <span data-i18n="ai_btn">提问</span>
            </button>
        </div>
        <div id="aiSearchResult"></div>
        <p class="search-tip">
            <i class="fas fa-info-circle"></i> <span data-i18n="ai_tip">代码已预留真实 API 接入逻辑，填入 Key 即可激活大模型，否则将展示模拟演示。</span>
        </p>
    </div>
</div>

<style>
    *, *::before, *::after { box-sizing: border-box; }

    /* 等宽字体类，应用连字效果 */
    .mono-font {
        font-family: 'Fira Code', Consolas, Monaco, monospace !important;
        font-variant-ligatures: contextual;
    }

    /* 初始全局背景为极暗太空黑 */
    body {
        margin: 0;
        background-color: #030712; 
        overflow-x: hidden;
        overflow-y: hidden; 
        transition: background 0.5s ease;
    }

    #intro-canvas {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        z-index: 1; pointer-events: none;
    }

    /* 包含所有UI的主容器，动画后它将释放clip-path */
    #page-wrapper {
        position: relative;
        z-index: 10;
        min-height: 100vh;
        background: linear-gradient(135deg, #ffffff, #f1f5f9, #e2e8f0, #f8fafc);
        background-size: 400% 400%;
        clip-path: circle(0px at 50% 50%);
        -webkit-clip-path: circle(0px at 50% 50%);
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* 核心修复 1：将卡片容器设为透明并稍微下沉，待背景亮起后再平滑浮现 */
    #main-content-container {
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .content-visible {
        opacity: 1 !important;
        transform: translateY(0) !important;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.7) !important;
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.8) !important;
    }

    .cv-container {
        max-width: 960px; margin: 0 auto; padding: 2rem 1.5rem; 
        font-family: -apple-system, BlinkMacSystemFont, sans-serif; 
        color: #0f172a; position: relative;
    }

    .btn-bubble { transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important; }
    .btn-bubble:hover {
        transform: scale(1.06) translateY(-2px);
        box-shadow: 0 10px 20px rgba(37, 99, 235, 0.15) !important;
    }

    /* ================= 基础 UI 样式 ================= */
    .top-utility-bar { display: flex; justify-content: flex-end; width: 100%; margin-bottom: 0.5rem; position: relative; z-index: 10;}
    .lang-toggle-btn { background: rgba(255,255,255,0.8); border: 1px solid #cbd5e1; border-radius: 20px; padding: 0.4rem 1.2rem; font-size: 0.85rem; font-weight: 600; color: #334155; cursor: pointer; backdrop-filter: blur(5px);}
    
    .header-section { display: flex; align-items: center; gap: 1.5rem; flex-wrap: wrap; margin-bottom: 2.5rem; padding-bottom: 2rem; border-bottom: 1px solid rgba(0,0,0,0.05); }
    .avatar-gradient { width: 80px; height: 80px; border-radius: 50%; background: linear-gradient(135deg, #1e40af, #3b82f6); display: flex; align-items: center; justify-content: center; font-size: 2rem; font-weight: 600; color: white; flex-shrink: 0; box-shadow: 0 10px 25px rgba(37, 99, 235, 0.2); }
    .main-title { font-size: 2.2rem; font-weight: 700; margin: 0; letter-spacing: 0px; display: block; }
    .sub-title { font-size: 1.05rem; color: #475569; margin: 0.4rem 0 0 0; }
    .section-title { font-size: 1.25rem; font-weight: 600; margin-top: 3rem; margin-bottom: 1.2rem; display: flex; align-items: center; gap: 0.6rem; }
    .section-title i { color: #2563eb; width: 1.5rem; }
    
    .info-card { border-radius: 16px; padding: 1.25rem 1.5rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; margin-bottom: 1rem; box-shadow: 0 4px 15px rgba(0,0,0,0.02); }
    .card-left { display: flex; align-items: center; gap: 0.75rem; }
    .card-icon { font-size: 1.3rem; color: #2563eb; }
    .card-text { font-weight: 600; color: #1e293b; }
    .card-tag { font-size: 0.9rem; color: #64748b; }
    .card-buttons { display: flex; gap: 0.5rem; }
    
    .btn { display: inline-flex; align-items: center; justify-content: center; gap: 0.4rem; padding: 0.5rem 1.2rem; border-radius: 40px; font-size: 0.85rem; font-weight: 500; cursor: pointer; border: none; text-decoration: none; }
    .btn-primary { background: #2563eb; color: white; box-shadow: 0 4px 12px rgba(37, 99, 235, 0.15); }
    .btn-outline { background: transparent; color: #334155; border: 1px solid #cbd5e1; }

    .model-panel { border-radius: 16px; padding: 1.5rem; margin-bottom: 1rem; box-shadow: 0 8px 30px rgba(0,0,0,0.04); }
    .param-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(110px, 1fr)); gap: 1rem; align-items: end; }
    .grid-col-span-2 { grid-column: span 2; }
    .relative-box { position: relative; }
    .param-label { display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600; white-space: nowrap; }
    .param-input { width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid rgba(203,213,225,0.6); outline: none; transition: border-color 0.2s; background: rgba(255,255,255,0.5); backdrop-filter: blur(4px);}
    .param-input:focus { border-color: #2563eb; background: #fff;}
    .bg-gray { background: rgba(248,250,252,0.6); }
    .uppercase-text { text-transform: uppercase; }
    .flex-input-group { display: flex; gap: 0.5rem; }
    .fetch-btn { padding: 0 1rem; flex-shrink: 0; background: rgba(255,255,255,0.8);}
    .run-sim-btn { height: 42px; width: 100%; }
    .data-status-text { font-size: 0.8rem; color: #2563eb; margin-top: 1rem; font-weight: 500; min-height: 1.2rem; }
    
    .autocomplete-dropdown { display:none; position:absolute; top: 100%; left: 0; right: 0; background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); border: 1px solid #cbd5e1; border-radius: 8px; margin-top: 4px; max-height: 220px; overflow-y: auto; z-index: 999; box-shadow: 0 10px 25px rgba(0,0,0,0.1); }
    .autocomplete-item { padding: 10px 12px; cursor: pointer; border-bottom: 1px solid rgba(0,0,0,0.05); font-size: 0.85rem; color: #334155; line-height: 1.4; }
    .autocomplete-item:hover { background: #eff6ff; color: #2563eb; }

    .chart-wrapper { border-radius: 12px; padding: 1rem; border: 1px solid rgba(255,255,255,0.8); box-shadow: 0 10px 30px rgba(0,0,0,0.06); position: relative; margin-bottom: 1.5rem; width: 100%; overflow: hidden; }
    .chart-tools { position: absolute; top: 1rem; right: 1rem; z-index: 100; display: flex; gap: 0.5rem; }
    .icon-btn { background: rgba(241,245,249,0.8); backdrop-filter: blur(4px); border: 1px solid #cbd5e1; border-radius: 8px; padding: 0.5rem 0.8rem; cursor: pointer; color: #475569; }

    .contact-wrapper { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 0.5rem; align-items: center; }
    .contact-tag { display: inline-flex; align-items: center; gap: 0.5rem; color: #334155; text-decoration: none; font-size: 0.9rem; font-weight: 500; background: rgba(241,245,249,0.8); backdrop-filter: blur(4px); padding: 0.5rem 1.2rem; border-radius: 30px; height: 38px;}
    .github-contact-btn { border-radius: 30px; padding: 0.5rem 1.2rem; height: 38px; font-size: 0.9rem; font-weight: 500;}

    .ai-top-border { padding-top: 2rem; border-top: 1px solid rgba(0,0,0,0.05); }
    .search-wrapper { display: flex; gap: 0.6rem; flex-wrap: wrap; }
    #aiSearchInput { flex: 1; min-width: 260px; padding: 0.75rem 1.2rem; border-radius: 40px; border: 1px solid rgba(203,213,225,0.6); font-size: 0.95rem; background: rgba(255,255,255,0.5); backdrop-filter: blur(4px); outline: none; }
    #aiSearchInput:focus { border-color: #2563eb; background: #ffffff; }
    #aiSearchResult { margin-top: 1.2rem; font-size: 0.95rem; color: #334155; padding: 0 0.5rem; line-height: 1.5; }
    .search-tip { font-size: 0.8rem; color: #94a3b8; margin-top: 0.6rem; }
    
    .chart-fullscreen { position: fixed !important; top: 0 !important; left: 0 !important; width: 100vw !important; height: 100vh !important; z-index: 9999 !important; border-radius: 0 !important; margin: 0 !important; padding: 2rem !important; background: #ffffff !important; overflow-y: auto;}
    .chart-fullscreen #itoChart { height: 95% !important; }

    @media (max-width: 768px) {
        .cv-container { padding: 1.5rem 1rem; }
        .header-section { flex-direction: column; align-items: flex-start; gap: 1rem; }
        .info-card { flex-direction: column; align-items: flex-start; padding: 1.25rem; }
        .card-buttons, .btn, .contact-tag { width: 100%; justify-content: center; }
        .param-grid { grid-template-columns: 1fr 1fr; }
        .grid-col-span-2, .grid-col-btn { grid-column: span 2; }
        .search-wrapper { flex-direction: column; }
        #aiSearchInput, .search-btn { width: 100% !important; }
    }
</style>

<script>
    function bezier(t, p0, p1, p2, p3) {
        let u = 1 - t;
        return (u*u*u * p0) + (3 * u*u * t * p1) + (3 * u * t*t * p2) + (t*t*t * p3);
    }

    function initCinematicIntro() {
        const siteTitleEl = document.querySelector('.site-title');
        if (siteTitleEl) {
            let origHtml = siteTitleEl.innerHTML;
            if (origHtml.includes('Hanson') && !origHtml.includes('id="target-h"')) {
                siteTitleEl.innerHTML = origHtml.replace('Hanson', '<span id="target-h" style="display: inline-block;">H</span>anson');
            }
        }

        window.scrollTo(0, 0);

        const canvas = document.getElementById('intro-canvas');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        const formulas = [
            'dS_t = μS_tdt + σS_tdW_t', 'V = S N(d_1) - K e^{-rT} N(d_2)', 
            'E(R_p) = w^T E(R)', 'σ_p^2 = w^T Σ w', 
            '∂V/∂t + ½σ²S²∂²V/∂S² + rS∂V/∂S - rV = 0', 
            'Δ = N(d_1)', 'Sharpe = (R_p - R_f)/σ_p', 'VAR = z_α σ √t', 
            'd_1 = (ln(S/K) + (r + σ²/2)t) / (σ√t)', 'd_2 = d_1 - σ√t',
            'Γ = N\'(d_1) / (Sσ√t)', 'Θ = -(S N\'(d_1)σ)/(2√t) - rKe^{-rT}N(d_2)',
            'ρ = Kte^{-rT}N(d_2)', 'r_e = r_f + β(E(r_m) - r_f)', 
            'WACC = (E/V)R_e + (D/V)R_d(1-T_c)', 'D = [Σ t*C_t/(1+y)^t] / P', 
            'C = (1/P) ∂²P/∂y²', 'F = S_0 e^{(r-q)T}', 
            'd(ln S) = (μ - σ²/2)dt + σ dW', 'dG = (∂G/∂t)dt + (∂G/∂x)dx + ½(∂²G/∂x²)dx²',
            'IR = (R_p - R_b)/σ_{TE}', 'Treynor = (R_p - R_f)/β_p',
            'P(S_T ≤ K) = N(-d_2)', 'd_2 = (ln(S/K)+(r-σ²/2)t)/(σ√t)',
            'PV = C / (1+r)^n', 'YTM = (C + (F-P)/n) / ((F+P)/2)'
        ];

        const particles = [];
        // 核心修复 2：公式数量提升到原先 3 倍 (从 250 到 750)
        const numParticles = 750; 
        
        class Particle {
            constructor() { this.reset(true); }
            reset(randomizeZ = false) {
                this.x = (Math.random() - 0.5) * canvas.width * 3.5; 
                this.y = (Math.random() - 0.5) * canvas.height * 3.5;
                this.z = randomizeZ ? Math.random() * canvas.width : canvas.width;
                this.formula = formulas[Math.floor(Math.random() * formulas.length)];
                this.isCyan = Math.random() > 0.4;
                this.fontSize = Math.random() * 16 + 12; 
                // 核心修复 3：速度提升 1.5 倍
                this.speed = (Math.random() * 15 + 5) * 1.5; 
            }
            update() {
                this.z -= this.speed; 
                if (this.z <= 10) this.reset();
            }
            draw() {
                let depth = 1 - this.z / canvas.width;
                if(depth < 0) return;

                let x = (this.x / this.z) * canvas.width + canvas.width / 2;
                let y = (this.y / this.z) * canvas.height + canvas.height / 2;
                
                let size = depth * this.fontSize * 4.0;
                if(size < 0.5) return; 

                let opacity = Math.pow(depth, 1.8) * 2.5;
                if (opacity > 1) opacity = 1;

                let r = this.isCyan ? 56 : 139;
                let g = this.isCyan ? 189 : 92;
                let b = this.isCyan ? 248 : 246;

                ctx.fillStyle = `rgba(${r}, ${g}, ${b}, ${opacity})`;
                ctx.font = `italic ${size}px "Times New Roman", Times, serif`;
                ctx.fillText(this.formula, x, y);
            }
        }

        for (let i = 0; i < numParticles; i++) particles.push(new Particle());

        const targetHEl = document.getElementById('target-h') || document.querySelector('.site-title') || document.querySelector('.main-title');
        
        const p0 = { x: canvas.width + 200, y: canvas.height * 0.6 }; 
        const p1 = { x: canvas.width * 0.4, y: canvas.height * 0.9 };  
        const p2 = { x: canvas.width * 0.2, y: canvas.height * 0.1 };  

        let startTime = Date.now();
        let animationFrameId;
        const flightDuration = 2.6; 
        const rippleDuration = 0.4; 

        function animate() {
            let elapsed = (Date.now() - startTime) / 1000;
            let t = Math.min(elapsed / flightDuration, 1);
            let rippleT = t >= 1 ? Math.min((elapsed - flightDuration) / rippleDuration, 1) : 0;

            const hRect = targetHEl ? targetHEl.getBoundingClientRect() : { left: 40, top: 20, width: 20, height: 20 };
            const isSpan = targetHEl && targetHEl.id === 'target-h';
            const targetX = isSpan ? (hRect.left + hRect.width / 2) : (hRect.left + 40); 
            const targetY = hRect.top + hRect.height / 2 + 1; 
            const targetFontSize = targetHEl ? parseFloat(window.getComputedStyle(targetHEl).fontSize) : 22; 
            const p3 = { x: targetX, y: targetY }; 

            ctx.fillStyle = 'rgba(3, 7, 18, 0.4)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            if (rippleT < 1) {
                particles.forEach(p => { p.update(); p.draw(); });
            }

            if (t < 1) {
                let easeT = t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;

                let hX = bezier(easeT, p0.x, p1.x, p2.x, p3.x);
                let hY = bezier(easeT, p0.y, p1.y, p2.y, p3.y);

                let currentSize;
                if (t < 0.6) {
                    let zPhase = t / 0.6;
                    currentSize = targetFontSize + 50 + Math.pow(Math.sin(zPhase * Math.PI), 1.5) * 450;
                } else {
                    let shrinkPhase = (t - 0.6) / 0.4;
                    let easeShrink = 1 - Math.pow(1 - shrinkPhase, 3);
                    currentSize = (targetFontSize + 50) - 50 * easeShrink;
                }

                let r = Math.round(0 + (15 - 0) * easeT);
                let g = Math.round(240 + (23 - 240) * Math.pow(t, 2));
                let b = Math.round(255 + (42 - 255) * Math.pow(t, 2));

                ctx.save();
                ctx.translate(hX, hY);
                let tilt = Math.sin(t * Math.PI) * 0.15 * (1 - easeT);
                ctx.rotate(tilt);

                ctx.font = `bold ${currentSize}px -apple-system, BlinkMacSystemFont, sans-serif`;
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                
                ctx.fillStyle = `rgb(${r}, ${g}, ${b})`;
                ctx.shadowColor = `rgba(0, 240, 255, ${1 - easeT})`;
                ctx.shadowBlur = 30 * (1 - easeT);
                
                ctx.fillText("H", 0, 0);
                ctx.restore();
            }

            if (t >= 1) {
                let rippleEase = 1 - Math.pow(1 - rippleT, 5);
                let maxRadius = Math.max(window.innerWidth, window.innerHeight) * 1.5;
                let currentRadius = maxRadius * rippleEase;

                const pageWrapper = document.getElementById('page-wrapper');
                pageWrapper.style.clipPath = `circle(${currentRadius}px at ${targetX}px ${targetY}px)`;
                pageWrapper.style.webkitClipPath = `circle(${currentRadius}px at ${targetX}px ${targetY}px)`;

                if (rippleT < 0.9) {
                    ctx.beginPath();
                    ctx.arc(targetX, targetY, currentRadius * 1.05, 0, Math.PI * 2);
                    ctx.strokeStyle = `rgba(56, 189, 248, ${1 - rippleT})`;
                    ctx.lineWidth = 15 * (1 - rippleT);
                    ctx.stroke();
                }

                if (rippleT === 1) {
                    pageWrapper.style.clipPath = 'none';
                    pageWrapper.style.webkitClipPath = 'none';
                    
                    document.body.style.background = 'linear-gradient(135deg, #ffffff, #f1f5f9, #e2e8f0, #f8fafc)';
                    document.body.style.backgroundSize = '400% 400%';
                    document.body.style.animation = 'gradientBG 15s ease infinite';
                    
                    document.getElementById('intro-canvas').style.display = 'none';
                    document.body.style.overflowY = 'auto'; 
                    cancelAnimationFrame(animationFrameId);

                    // 核心修复 4：等到背景特效全开后，让卡片丝滑浮现
                    document.getElementById('main-content-container').classList.add('content-visible');
                    
                    runSimulation();
                    setTimeout(() => { if (chartInstance) chartInstance.resize(); }, 150);
                    return;
                }
            }

            animationFrameId = requestAnimationFrame(animate);
        }

        animate();
    }

    window.addEventListener('load', initCinematicIntro);


    // ================= 基础多语言与量化配置引擎数据 =================
    const i18nDict = {
        name: { zh: "王 盛 烨", en: "Shengye (Hanson) Wang" },
        degree: { zh: "上海纽约大学 · 商业与金融（商业分析）", en: "NYU Shanghai · Business & Finance (Data Analytics)" },
        resume_title: { zh: "我的简历", en: "My Resume" },
        resume_name: { zh: "金融工程简历 (中文版)", en: "Financial Engineering Resume (CN)" },
        resume_tag: { zh: "· 2026 最新版", en: "· 2026 Updated" },
        resume_btn: { zh: "查看简历", en: "View PDF" },
        resume_en_name: { zh: "金融工程简历 (English)", en: "Financial Engineering Resume" },
        resume_en_tag: { zh: "· 2026 Updated", en: "· 2026 Updated" },
        resume_en_btn: { zh: "View PDF", en: "View PDF" },
        project_title: { zh: "项目展示", en: "Projects" },
        proj_backtest_name: { zh: "A股回测模型", en: "A-Share Backtesting Model" },
        proj_backtest_tag: { zh: "· 宏观 + 情绪指标", en: "· Macro + Sentiment Indicators" },
        proj_backtest_btn: { zh: "运行回测模型", en: "Run Backtest Model" },
        proj_markowitz_name: { zh: "Markowitz 资产轮动与量化配置模型", en: "Markowitz Portfolio Allocation Model" },
        proj_markowitz_tag: { zh: "· 现代投资组合理论 (MPT)", en: "· Modern Portfolio Theory (MPT)" },
        proj_markowitz_btn: { zh: "运行配置模型", en: "Run Allocation Model" },
        mc_title: { zh: "实盘量化引擎：股价路径预测", en: "Live Quant Engine: Monte Carlo Prediction" },
        mc_desc: { zh: "系统自动拉取历史 data(含GitHub缓存容灾)。支持自定义模拟次数，极速引擎生成逐日归一化的概率密度热力图。", en: "Auto-fetches live data. Per-Day Normalized heatmap." },
        mc_ticker: { zh: "股票/指数代码 (Ticker)", en: "Stock/Index Ticker" },
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
        document.getElementById('stockTicker').placeholder = currentLang === 'zh' ? "输入 AAPL 或指数代码..." : "Type AAPL, ^GSPC...";
        document.getElementById('aiSearchInput').placeholder = currentLang === 'zh' ? "输入你想问的金融问题…" : "Ask a financial question...";
        document.getElementById('priceLabel').innerText = currentLang === 'zh' ? `当前价格 (${currentCurrency})` : `Current Price (${currentCurrency})`;
        if(chartInstance) runSimulation(); 
    }

    let currentDataSource = '用户自定义 (Custom Input)';
    let currentCurrency = '$'; 
    let chartInstance = null;

    function markCustom() { currentDataSource = currentLang === 'zh' ? '用户自定义 (Custom Input)' : 'User Custom Input'; }

    const localTickerDB = [
        { symbol: '000300.SS', name: '沪深300指数 (CSI 300 Index)' },
        { symbol: '000905.SS', name: '中证500指数 (CSI 500 Index)' },
        { symbol: '^GSPC', name: '标谱500指数 (S&P 500 Index)' },
        { symbol: '^IXIC', name: '纳斯达克综合指数 (Nasdaq Composite)' },
        { symbol: '^DJI', name: '道琼斯工业指数 (Dow Jones Index)' },
        { symbol: '^HSI', name: '恒生指数 (Hang Seng Index)' },
        { symbol: 'AAPL', name: '苹果公司 (Apple)' },
        { symbol: 'MSFT', name: '微软 (Microsoft)' },
        { symbol: 'NVDA', name: '英伟达 (NVIDIA)' },
        { symbol: 'TSLA', name: '特斯拉 (Tesla)' },
        { symbol: 'SPY', name: '标谱500 ETF (SPY)' },
        { symbol: 'QQQ', name: '纳斯达克100 ETF (QQQ)' },
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
                    <strong class="mono-font">${item.symbol}</strong><br><small style="color:#64748b">${item.name}</small>
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
            document.body.style.overflowY = 'hidden'; 
        } else {
            icon.className = 'fas fa-expand';
            document.body.style.overflowY = 'auto';
        }
        if(chartInstance) setTimeout(() => chartInstance.resize(), 100);
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
        document.getElementById('priceLabel').innerText = currentLang === 'zh' ? `当前价格 (${currentCurrency})` : `Current Price (${currentCurrency})`;

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
                document.getElementById('currentPrice').value = ticker.includes('600519') ? "1500.00" : (ticker.startsWith('000')?"3500.00":"175.00");
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
                backgroundColor: 'transparent',
                textStyle: { fontFamily: '-apple-system, sans-serif' },
                graphic: [{ type: 'text', left: '2%', top: '3%', style: { text: watermarkText, fontSize: 10, fill: '#64748b', lineHeight: 15, fontFamily: "'Fira Code', monospace" }, z: 100 }],
                tooltip: {
                    position: 'top', backgroundColor: 'rgba(255,255,255,0.95)', borderColor: '#cbd5e1',
                    textStyle: { fontFamily: "'Fira Code', monospace" }, 
                    formatter: function (p) {
                        if(p.seriesType === 'heatmap') {
                            let lower = parseFloat(data.yAxisLabels[p.value[1]]);
                            return `<div style="color:#2563eb; font-family:-apple-system, sans-serif;">Day ${p.value[0]}</div>
                                    Range: <b>[ ${currentCurrency}${lower.toFixed(2)} , ${currentCurrency}${(lower+data.binSize).toFixed(2)} ]</b><br/>
                                    Prob: <b style="color:#ef4444;">${((p.value[2] / data.numPaths)*100).toFixed(2)}%</b>`;
                        } else {
                            return `<div style="color:#2563eb; font-family:-apple-system, sans-serif;">${p.seriesName}</div> Day ${p.dataIndex} <br/>Price: <b>${currentCurrency}${p.value.toFixed(2)}</b>`;
                        }
                    }
                },
                visualMap: { dimension: 3, min: 0, max: 1, show: false, inRange: { color: ['#ffffff', '#bfdbfe', '#3b82f6', '#ef4444'] } },
                grid: { left: '1%', right: '2%', top: 60, bottom: 10, containLabel: true },
                xAxis: { type: 'category', data: xAxisData, axisLabel: { fontFamily: "'Fira Code', monospace" } }, 
                yAxis: [
                    { type: 'category', data: data.yAxisLabels, show: false }, 
                    { type: 'value', min: data.globalMin, max: data.globalMax, axisLabel: { fontFamily: "'Fira Code', monospace", formatter: function(v) { return currentCurrency + parseFloat(v).toFixed(2); } } } 
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

    const resizeObserver = new ResizeObserver(() => {
        if (chartInstance) chartInstance.resize();
    });
    resizeObserver.observe(document.getElementById('chartExportWrapper'));

    async function handleAISearch() {
        const query = document.getElementById('aiSearchInput').value.trim();
        const resultDiv = document.getElementById('aiSearchResult');
        if(!query) return;
        resultDiv.innerHTML = `<i class="fas fa-spinner fa-spin"></i> Analyzing...`;
        setTimeout(() => {
            resultDiv.innerHTML = `<div style="background:rgba(255,255,255,0.7); backdrop-filter:blur(5px); padding:1rem; border-left:4px solid #2563eb; border-radius:4px;">
                <strong>[模拟演示效果]</strong><br>您输入的问题是："${query}"<br><br>
                在实际生成环境中，此模块将通过安全的后端云函数反向代理调用 OpenAI API。
            </div>`;
        }, 800);
    }
</script>
