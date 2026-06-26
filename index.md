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

        <div id="itoChart" style="width: 100%; height: 550px;"></div>
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
    .header-section { display: flex; align-items: center; gap: 1.5rem; flex-wrap: wrap; margin-bottom: 2
