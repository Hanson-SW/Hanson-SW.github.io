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
    <i class="fas fa-chart-line" style="color: #2563eb;"></i> 量化模型在线演示：股价路径模拟 (Itô Process)
</h2>
<p style="color: #64748b; font-size: 0.95rem; margin-bottom: 1.5rem;">
    基于几何布朗运动 (Geometric Brownian Motion)，设定参数后点击“运行模拟”，即可生成未来股价的随机漫步路径。
</p>

<div class="model-panel" style="background: #ffffff; border-radius: 16px; padding: 1.5rem; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0,0,0,0.03); margin-bottom: 1.5rem;">
    <div style="display: flex; flex-wrap: wrap; gap: 1rem; align-items: flex-end;">
        
        <div style="flex: 1; min-width: 120px;">
            <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;">选择股票 (数据源)</label>
            <select id="stockTicker" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none; background: #f8fafc;">
                <option value="AAPL|170.0">Apple (AAPL) - $170.0</option>
                <option value="TSLA|175.0">Tesla (TSLA) - $175.0</option>
                <option value="SPY|510.0">S&P 500 (SPY) - $510.0</option>
                <option value="CUSTOM">自定义当前股价...</option>
            </select>
        </div>

        <div style="flex: 1; min-width: 100px;">
            <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;">当前股价 ($)</label>
            <input type="number" id="currentPrice" value="170" step="0.1" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none;" />
        </div>

        <div style="flex: 1; min-width: 100px;">
            <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;">隐含波动率 (σ)</label>
            <input type="number" id="impliedVol" value="0.20" step="0.01" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none;" />
        </div>

        <div style="flex: 1; min-width: 100px;">
            <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;">预期年化收益 (μ)</label>
            <input type="number" id="expReturn" value="0.08" step="0.01" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none;" />
        </div>

        <div style="flex: 1; min-width: 100px;">
            <label style="display: block; font-size: 0.85rem; color: #475569; margin-bottom: 0.4rem; font-weight: 600;">预测天数</label>
            <input type="number" id="timeHorizon" value="252" style="width: 100%; padding: 0.6rem; border-radius: 8px; border: 1px solid #cbd5e1; outline: none;" />
        </div>

        <button onclick="runSimulation()" class="btn btn-primary" style="height: 42px; padding: 0 1.5rem; white-space: nowrap;">
            <i class="fas fa-play"></i> 运行模拟
        </button>
    </div>
</div>

<div style="background: #ffffff; border-radius: 16px; padding: 1rem; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
    <div id="itoChart" style="width: 100%; height: 400px;"></div>
</div>

<script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>

<script>
    // 监听股票选择下拉框，自动填充当前股价
    document.getElementById('stockTicker').addEventListener('change', function(e) {
        if(this.value !== 'CUSTOM') {
            const price = this.value.split('|')[1];
            document.getElementById('currentPrice').value = price;
        }
    });

    // Box-Muller 算法生成标准正态分布随机数 (模拟 Excel 里的随机抽取)
    function randomNormal() {
        let u = 0, v = 0;
        while(u === 0) u = Math.random();
        while(v === 0) v = Math.random();
        return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
    }

    // Itô Process (几何布朗运动) 核心算法
    function generateItoPath(S0, mu, sigma, days) {
        let dt = 1 / 252; // 假设一年252个交易日 (对应你Excel中的 0.003968)
        let simPath = [S0];
        let idealPath = [S0];

        for(let i = 1; i <= days; i++) {
            let Z = randomNormal();
            // 随机漫步公式：St = S_{t-1} * exp((mu - 0.5*sigma^2)*dt + sigma*sqrt(dt)*Z)
            let drift = (mu - 0.5 * sigma * sigma) * dt;
            let shock = sigma * Math.sqrt(dt) * Z;
            let nextPrice = simPath[i-1] * Math.exp(drift + shock);
            simPath.push(nextPrice);

            // 无波动的理想走势 (Excel里的橙线)
            let idealNext = idealPath[i-1] * Math.exp(mu * dt);
            idealPath.push(idealNext);
        }
        return { simPath, idealPath };
    }

    // 初始化 ECharts 实例
    let chartInstance = null;

    function runSimulation() {
        const S0 = parseFloat(document.getElementById('currentPrice').value);
        const sigma = parseFloat(document.getElementById('impliedVol').value);
        const mu = parseFloat(document.getElementById('expReturn').value);
        const days = parseInt(document.getElementById('timeHorizon').value);

        // 生成 x 轴 (天数)
        let xAxisData = [];
        for(let i = 0; i <= days; i++) xAxisData.push('Day ' + i);

        // 运行模型生成数据
        const data = generateItoPath(S0, mu, sigma, days);

        // 渲染图表
        if (!chartInstance) {
            chartInstance = echarts.init(document.getElementById('itoChart'));
        }

        const option = {
            title: { text: 'Itô Process 股价模拟', left: 'center', textStyle: { color: '#334155', fontSize: 16 } },
            tooltip: { trigger: 'axis' },
            legend: { data: ['模拟股价走势 (Simulated)', '理想期望走势 (Ideal)'], bottom: 0 },
            grid: { left: '5%', right: '5%', top: '15%', bottom: '12%', containLabel: true },
            xAxis: { type: 'category', boundaryGap: false, data: xAxisData },
            yAxis: { type: 'value', min: 'dataMin', axisLabel: { formatter: '${value}' } },
            series: [
                {
                    name: '模拟股价走势 (Simulated)',
                    type: 'line',
                    data: data.simPath,
                    showSymbol: false,
                    lineStyle: { width: 2, color: '#2563eb' },
                    itemStyle: { color: '#2563eb' }
                },
                {
                    name: '理想期望走势 (Ideal)',
                    type: 'line',
                    data: data.idealPath,
                    showSymbol: false,
                    lineStyle: { width: 2, type: 'dashed', color: '#f59e0b' },
                    itemStyle: { color: '#f59e0b' }
                }
            ]
        };

        chartInstance.setOption(option);
    }

    // 页面加载完成后自动跑一次默认数据
    window.onload = function() {
        runSimulation();
    };
    
    // 适配窗口缩放
    window.addEventListener('resize', function() {
        if(chartInstance) chartInstance.resize();
    });
</script>
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
