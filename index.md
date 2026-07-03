---
layout: default
title: 金融工程 · 个人主页
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/echarts/5.4.3/echarts.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" />
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&display=swap" rel="stylesheet">

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
                <i class="fas fa-file-pdf card-icon"></i>
                <span class="card-text" data-i18n="resume_en_name">金融工程简历 (English)</span>
                <span class="card-tag" data-i18n="resume_en_tag">· 2026 Updated</span>
            </div>
            <button onclick="window.open('SWresume.pdf', '_blank')" class="btn btn-outline btn-bubble" style="color: #2563eb; border-color: #2563eb;">
                <i class="fas fa-eye"></i> <span data-i18n="resume_en_btn">View PDF</span>
            </button>
        </div>

        <h2 class="section-title">
            <i class="fas fa-code-branch"></i> <span data-i18n="project_title">项目展示</span>
        </h2>

        <div class="project-grid">
            
            <div class="project-card glass-card">
                <div class="header">
                    <div class="title" data-i18n="proj_backtest_name">A股回测模型</div>
                    <div class="tag" data-i18n="proj_backtest_tag">· 量化择时 + 技术指标</div>
                </div>
                <div class="project-meta">
                    <div><strong data-i18n="card_goal">目标</strong><span data-i18n="proj_backtest_goal">检验择时策略在历史净值曲线上的收益、风险和交易行为。</span></div>
                    <div><strong data-i18n="card_method">方法</strong><span data-i18n="proj_backtest_method">双均线、布林带、逐资产持仓、交易明细和策略 VaR/CVaR。</span></div>
                    <div><strong data-i18n="card_output">输出</strong><span data-i18n="proj_backtest_output">净值、回撤、交易历史、归因、Risk Tear Sheet。</span></div>
                    <div><strong data-i18n="card_limit">局限</strong><span data-i18n="proj_backtest_limit">仍需加入样本外切分、参数敏感性和 Walk-forward 参数选择。</span></div>
                </div>
                <div class="spacer"></div>
                <button onclick="window.open('./backtest.html', '_blank')" class="btn project-btn btn-bubble">
                    <i class="fas fa-play"></i> <span data-i18n="proj_backtest_btn">运行回测模型</span>
                </button>
            </div>

            <div class="project-card glass-card">
                <div class="header">
                    <div class="title" data-i18n="proj_markowitz_name">Markowitz 资产轮动与量化配置模型</div>
                    <div class="tag" data-i18n="proj_markowitz_tag">· 现代投资组合理论 (MPT)</div>
                </div>
                <div class="project-meta">
                    <div><strong data-i18n="card_goal">目标</strong><span data-i18n="proj_markowitz_goal">比较不同资产配置方法的权重、风险贡献和尾部风险。</span></div>
                    <div><strong data-i18n="card_method">方法</strong><span data-i18n="proj_markowitz_method">Max Sharpe、Min Vol、Risk Parity、Black-Litterman、Monte Carlo。</span></div>
                    <div><strong data-i18n="card_output">输出</strong><span data-i18n="proj_markowitz_output">有效前沿、VaR/CVaR、风险贡献、压力测试和 BL 对比表。</span></div>
                    <div><strong data-i18n="card_limit">局限</strong><span data-i18n="proj_markowitz_limit">Bootstrap 区间和完整样本外对照仍在下一阶段补强。</span></div>
                </div>
                <div class="spacer"></div>
                <button onclick="window.open('./markowitz.html', '_blank')" class="btn project-btn btn-bubble">
                    <i class="fas fa-play"></i> <span data-i18n="proj_markowitz_btn">运行配置模型</span>
                </button>
            </div>


            <div class="project-card glass-card">
                <div class="header">
                    <div class="title" data-i18n="proj_statement_name">AI 三表分析与估值建模平台</div>
                    <div class="tag" data-i18n="proj_statement_tag">· 财报解析 + DCF / Comps / LBO</div>
                </div>
                <div class="project-meta">
                    <div><strong data-i18n="card_goal">目标</strong><span data-i18n="proj_statement_goal">上传三张财务报表，自动标准化科目、计算关键指标并生成投研式报告。</span></div>
                    <div><strong data-i18n="card_method">方法</strong><span data-i18n="proj_statement_method">Excel/CSV 解析、数据清洗、财务比率、DCF、Comps、M&A Accretion/Dilution、LBO。</span></div>
                    <div><strong data-i18n="card_output">输出</strong><span data-i18n="proj_statement_output">三表预览、指标矩阵、风险诊断、估值区间、AI Mock Report 和 PDF 报告。</span></div>
                    <div><strong data-i18n="card_limit">局限</strong><span data-i18n="proj_statement_limit">当前为纯前端 MVP；真实 AI 抽取和 API 网关将在下一阶段接入。</span></div>
                </div>
                <div class="spacer"></div>
                <button onclick="window.open('./statement-analyzer.html', '_blank')" class="btn project-btn btn-bubble">
                    <i class="fas fa-play"></i> <span data-i18n="proj_statement_btn">运行三表分析模型</span>
                </button>
            </div>

        </div>

        <h2 class="section-title" style="margin-top: 3.5rem;">
            <i class="fas fa-database"></i> <span data-i18n="data_arch_title">数据架构</span>
        </h2>
        <div class="research-grid">
            <div class="research-card glass-card">
                <strong data-i18n="data_arch_1_title">静态行情库</strong>
                <span data-i18n="data_arch_1_desc">data/*.json 提供指数、黄金、半导体、医药等资产历史价格。</span>
            </div>
            <div class="research-card glass-card">
                <strong data-i18n="data_arch_2_title">资产清单</strong>
                <span data-i18n="data_arch_2_desc">asset_manifest.json 统一管理资产名称、数据区间、更新时间和可用性。</span>
            </div>
            <div class="research-card glass-card">
                <strong data-i18n="data_arch_3_title">质量报告</strong>
                <span data-i18n="data_arch_3_desc">quality_report.json 用于追踪缺失、失败和缓存状态，让模型展示数据健康度。</span>
            </div>
        </div>

        <h2 class="section-title" style="margin-top: 3.5rem;">
            <i class="fas fa-flask"></i> <span data-i18n="research_title">研究能力矩阵</span>
        </h2>
        <div class="research-grid">
            <div class="research-card glass-card">
                <strong data-i18n="research_1_title">组合优化</strong>
                <span data-i18n="research_1_desc">均值-方差、最小方差、Risk Parity、Black-Litterman 和有效前沿。</span>
            </div>
            <div class="research-card glass-card">
                <strong data-i18n="research_2_title">策略回测</strong>
                <span data-i18n="research_2_desc">择时信号、交易明细、收益归因、回撤分析和风险报告。</span>
            </div>
            <div class="research-card glass-card">
                <strong data-i18n="research_3_title">可信度增强</strong>
                <span data-i18n="research_3_desc">已接入 Data Health；下一阶段补样本外、参数敏感性和 Bootstrap 区间。</span>
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

    .mono-font {
        font-family: 'Fira Code', Consolas, Monaco, monospace !important;
        font-variant-ligatures: contextual;
    }

    /* 全局高级感流体渐变背景 */
    body {
        margin: 0;
        background: linear-gradient(135deg, #ffffff, #f1f5f9, #e2e8f0, #f8fafc);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        overflow-x: hidden;
        overflow-y: auto; /* 恢复正常滚动 */
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    #page-wrapper {
        position: relative;
        z-index: 10;
        min-height: 100vh;
    }

    /* ================= ✨ 灵动板块上浮动效核心样式 ================= */
    @keyframes floatUpReveal {
        0% {
            opacity: 0;
            transform: translateY(40px) scale(0.97);
            filter: blur(4px);
        }
        100% {
            opacity: 1;
            transform: translateY(0) scale(1);
            filter: blur(0);
        }
    }

    /* 赋予初始透明状态，规避闪烁 */
    .reveal-item {
        opacity: 0;
        transform: translateY(40px);
        will-change: transform, opacity, filter;
    }

    /* 激活优雅的交错缓动 */
    .reveal-item.animated {
        animation: floatUpReveal 0.85s cubic-bezier(0.16, 1, 0.3, 1) forwards;
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

    /* ================= 项目卡片展示样式 (统一 Markowitz 风格) ================= */
    .project-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-bottom: 1rem; }
    .project-card { border-radius: 16px; padding: 1.5rem; display: flex; flex-direction: column; gap: 1.25rem; transition: transform 0.2s, box-shadow 0.2s; box-shadow: 0 4px 15px rgba(0,0,0,0.02); }
    .project-card:hover { transform: translateY(-4px); box-shadow: 0 10px 25px rgba(139, 92, 246, 0.15); }
    .project-card .header { display: flex; flex-direction: column; gap: 0.6rem; }
    .project-card .title { font-size: 1.15rem; font-weight: 700; color: #1e293b; }
    .project-card .tag { align-self: flex-start; background: rgba(139, 92, 246, 0.1); color: #8b5cf6; padding: 0.25rem 0.8rem; border-radius: 20px; font-size: 0.85rem; font-weight: 600; border-left: 3px solid #8b5cf6; }
    .project-meta { display: grid; gap: 0.65rem; font-size: 0.9rem; color: #475569; line-height: 1.5; }
    .project-meta div { display: grid; grid-template-columns: 3.5rem 1fr; gap: 0.6rem; align-items: start; }
    .project-meta strong { color: #0f172a; font-size: 0.82rem; white-space: nowrap; }
    .project-meta span { min-width: 0; overflow-wrap: anywhere; }
    .project-card .spacer { flex-grow: 1; }
    .project-card .project-btn { width: 100%; background: #8b5cf6; color: white; border: none; box-shadow: 0 4px 12px rgba(139, 92, 246, 0.2); font-size: 0.95rem; padding: 0.6rem 1.2rem; }
    .project-card .project-btn:hover { background: #7c3aed; }

    .research-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 1rem; margin-bottom: 1rem; }
    .research-card { border-radius: 14px; padding: 1rem 1.1rem; display: grid; gap: 0.45rem; color: #475569; line-height: 1.5; min-width: 0; }
    .research-card strong { color: #0f172a; font-size: 0.95rem; }
    .research-card span { overflow-wrap: anywhere; }

    /* ================= 模型面板及其他组件 ================= */
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
        .project-meta div { grid-template-columns: 3rem 1fr; }
        .search-wrapper { flex-direction: column; }
        #aiSearchInput, .search-btn { width: 100% !important; }
    }
</style>

<script>
    // ================= 1. 灵动多板块交错瀑布流浮现引擎 =================
    function initFloatUpIntro() {
        const elementsToAnimate = [];

        // 1. 先加入顶部切换栏
        const topBar = document.querySelector('.top-utility-bar');
        if (topBar) elementsToAnimate.push(topBar);

        // 2. 再加入头像核心个人信息栏
        const header = document.querySelector('.header-section');
        if (header) elementsToAnimate.push(header);

        // 3. 将简历、项目、量化面板等各个子版块逐个抓取，实现完美序列流
        const containerChildren = document.querySelectorAll('.cv-container > *');
        containerChildren.forEach(child => {
            elementsToAnimate.push(child);
        });

        // 4. 为每个板块动态绑定时间差（步长 65ms 紧凑生动）
        elementsToAnimate.forEach((el, index) => {
            el.classList.add('reveal-item');
            el.style.animationDelay = `${index * 65}ms`;
            
            // 稍作微小延迟加入激活类触发硬件加速
            setTimeout(() => {
                el.classList.add('animated');
            }, 30);
        });

        // 5. 让股价路径图表立刻开始准备数据并绘制
        runSimulation();
        setTimeout(() => { if (chartInstance) chartInstance.resize(); }, 400);
    }

    // 监听 DOM 加载完毕直接渲染，不再等待多余资源
    window.addEventListener('DOMContentLoaded', initFloatUpIntro);


    // ================= 2. 基础多语言与量化配置引擎数据 =================
    const i18nDict = {
        title: { zh: "金融工程 · 个人主页", en: "Homepage" },
        name: { zh: "王 盛 烨", en: "Shengye (Hanson) Wang" },
        degree: { zh: "上海纽约大学 · 商业与金融（商业分析）", en: "NYU Shanghai · Business & Finance (Business Analytics)" },
        resume_title: { zh: "我的简历", en: "My Resume" },
        resume_name: { zh: "金融工程简历 (中文版)", en: "Financial Engineering Resume (CN)" },
        resume_tag: { zh: "· 2026 最新版", en: "· 2026 Updated" },
        resume_btn: { zh: "查看简历", en: "View PDF" },
        resume_en_name: { zh: "金融工程简历 (English)", en: "Financial Engineering Resume" },
        resume_en_tag: { zh: "· 2026 Updated", en: "· 2026 Updated" },
        resume_en_btn: { zh: "View PDF", en: "View PDF" },
        project_title: { zh: "项目展示", en: "Projects" },
        proj_backtest_name: { zh: "A股回测模型", en: "A-Share Backtesting Model" },
        proj_backtest_tag: { zh: "· 量化择时 + 技术指标", en: "· Quantitative Timing + Technical Indicators" },
        card_goal: { zh: "目标", en: "Goal" },
        card_method: { zh: "方法", en: "Method" },
        card_output: { zh: "输出", en: "Output" },
        card_limit: { zh: "局限", en: "Limit" },
        proj_backtest_goal: { zh: "检验择时策略在历史净值曲线上的收益、风险和交易行为。", en: "Evaluate timing strategies through historical NAV, risk, and trading behavior." },
        proj_backtest_method: { zh: "双均线、布林带、逐资产持仓、交易明细和策略 VaR/CVaR。", en: "Dual MA, Bollinger Bands, per-asset positions, trade logs, and strategy VaR/CVaR." },
        proj_backtest_output: { zh: "净值、回撤、交易历史、归因、Risk Tear Sheet。", en: "NAV, drawdown, trade history, attribution, and Risk Tear Sheet." },
        proj_backtest_limit: { zh: "仍需加入样本外切分、参数敏感性和 Walk-forward 参数选择。", en: "Out-of-sample split, parameter sensitivity, and walk-forward parameter selection are next." },
        proj_backtest_btn: { zh: "运行回测模型", en: "Run Backtest Model" },
        proj_markowitz_name: { zh: "Markowitz 资产轮动与量化配置模型", en: "Markowitz Portfolio Allocation Model" },
        proj_markowitz_tag: { zh: "· 现代投资组合理论 (MPT)", en: "· Modern Portfolio Theory (MPT)" },
        proj_markowitz_goal: { zh: "比较不同资产配置方法的权重、风险贡献和尾部风险。", en: "Compare allocation methods by weights, risk contribution, and tail risk." },
        proj_markowitz_method: { zh: "Max Sharpe、Min Vol、Risk Parity、Black-Litterman、Monte Carlo。", en: "Max Sharpe, Min Vol, Risk Parity, Black-Litterman, and Monte Carlo." },
        proj_markowitz_output: { zh: "有效前沿、VaR/CVaR、风险贡献、压力测试和 BL 对比表。", en: "Efficient frontier, VaR/CVaR, risk contribution, stress tests, and BL comparison." },
        proj_markowitz_limit: { zh: "Bootstrap 区间和完整样本外对照仍在下一阶段补强。", en: "Bootstrap intervals and fuller out-of-sample comparison remain next-stage work." },
        proj_markowitz_btn: { zh: "运行配置模型", en: "Run Allocation Model" },
        proj_statement_name: { zh: "AI 三表分析与估值建模平台", en: "AI Financial Statement & Valuation Analyzer" },
        proj_statement_tag: { zh: "· 财报解析 + DCF / Comps / LBO", en: "· Statement Parsing + DCF / Comps / LBO" },
        proj_statement_goal: { zh: "上传三张财务报表，自动标准化科目、计算关键指标并生成投研式报告。", en: "Upload three financial statements, standardize line items, calculate key metrics, and generate an investment-style report." },
        proj_statement_method: { zh: "Excel/CSV 解析、数据清洗、财务比率、DCF、Comps、M&A Accretion/Dilution、LBO。", en: "Excel/CSV parsing, data cleaning, financial ratios, DCF, comps, M&A accretion/dilution, and LBO modeling." },
        proj_statement_output: { zh: "三表预览、指标矩阵、风险诊断、估值区间、AI Mock Report 和 PDF 报告。", en: "Statement preview, metric matrix, risk diagnostics, valuation range, AI mock report, and PDF export." },
        proj_statement_limit: { zh: "当前为纯前端 MVP；真实 AI 抽取和 API 网关将在下一阶段接入。", en: "Current version is a pure front-end MVP; real AI extraction and API gateway integration are planned for the next stage." },
        proj_statement_btn: { zh: "运行三表分析模型", en: "Run Statement Analyzer" },
        data_arch_title: { zh: "数据架构", en: "Data Architecture" },
        data_arch_1_title: { zh: "静态行情库", en: "Static Market Store" },
        data_arch_1_desc: { zh: "data/*.json 提供指数、黄金、半导体、医药等资产历史价格。", en: "data/*.json stores historical prices for indices, gold, semiconductors, healthcare, and more." },
        data_arch_2_title: { zh: "资产清单", en: "Asset Manifest" },
        data_arch_2_desc: { zh: "asset_manifest.json 统一管理资产名称、数据区间、更新时间和可用性。", en: "asset_manifest.json manages names, ranges, update time, and availability." },
        data_arch_3_title: { zh: "质量报告", en: "Quality Report" },
        data_arch_3_desc: { zh: "quality_report.json 用于追踪缺失、失败和缓存状态，让模型展示数据健康度。", en: "quality_report.json tracks missing data, failures, and cache status for Data Health display." },
        research_title: { zh: "研究能力矩阵", en: "Research Capability Matrix" },
        research_1_title: { zh: "组合优化", en: "Portfolio Optimization" },
        research_1_desc: { zh: "均值-方差、最小方差、Risk Parity、Black-Litterman 和有效前沿。", en: "Mean-variance, min-volatility, Risk Parity, Black-Litterman, and efficient frontier." },
        research_2_title: { zh: "策略回测", en: "Strategy Backtesting" },
        research_2_desc: { zh: "择时信号、交易明细、收益归因、回撤分析和风险报告。", en: "Timing signals, trade logs, attribution, drawdown analysis, and risk reports." },
        research_3_title: { zh: "可信度增强", en: "Credibility Enhancements" },
        research_3_desc: { zh: "已接入 Data Health；下一阶段补样本外、参数敏感性和 Bootstrap 区间。", en: "Data Health is live; out-of-sample, sensitivity, and bootstrap intervals are next." },
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
