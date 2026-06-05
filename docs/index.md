---
hide:
  - navigation
  - toc
  - path
class: md-home
---


<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

  * { box-sizing: border-box; margin: 0; padding: 0; }

  .n8n-wrap {
    font-family: 'DM Sans', sans-serif;
    background: transparent;
    color: #e8e8e8;
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* NAV */
  .n8n-nav {
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 28px; height: 52px;
    border-bottom: 1px solid #1e1e1e;
    background: #0f0f0f;
    position: sticky; top: 0; z-index: 100;
  }
  .n8n-logo {
    display: flex; align-items: center; gap: 8px;
    font-weight: 700; font-size: 15px; color: #fff; letter-spacing: -0.02em;
  }
  .n8n-logo-mark {
    width: 26px; height: 26px; border-radius: 6px;
    background: #f04e2c;
    display: flex; align-items: center; justify-content: center;
    font-size: 11px; font-weight: 800; color: #fff; letter-spacing: -0.05em;
  }
  .n8n-nav-links { display: flex; gap: 4px; align-items: center; }
  .n8n-nav-links a {
    font-size: 13px; color: #aaa; padding: 5px 10px;
    border-radius: 5px; cursor: pointer; text-decoration: none;
    transition: color 0.15s, background 0.15s;
  }
  .n8n-nav-links a:hover { color: #fff; background: #1e1e1e; }
  .n8n-nav-cta {
    display: flex; gap: 8px; align-items: center;
  }
  .btn-ghost {
    font-family: 'DM Sans', sans-serif; font-size: 13px;
    background: transparent; border: 1px solid #2e2e2e;
    color: #ccc; padding: 6px 14px; border-radius: 6px; cursor: pointer;
    transition: border-color 0.15s, color 0.15s;
  }
  .btn-ghost:hover { border-color: #555; color: #fff; }
  .btn-primary {
    font-family: 'DM Sans', sans-serif; font-size: 13px; font-weight: 600;
    background: #f04e2c; border: none;
    color: #fff; padding: 7px 16px; border-radius: 6px; cursor: pointer;
    transition: background 0.15s;
  }
  .btn-primary:hover { background: #d44424; }

  /* HERO */
  .n8n-hero {
    text-align: center;
    padding: 80px 24px 60px;
    position: relative; overflow: hidden;
  }
  .n8n-hero::before {
    content: '';
    position: absolute; top: -120px; left: 50%; transform: translateX(-50%);
    width: 700px; height: 500px;
    background: radial-gradient(ellipse at center, rgba(240,78,44,0.12) 0%, transparent 65%);
    pointer-events: none;
  }
  .badge-row {
    display: inline-flex; align-items: center; gap: 6px;
    background: #1a1a1a; border: 1px solid #2a2a2a;
    border-radius: 999px; padding: 4px 12px 4px 6px;
    font-size: 12px; color: #aaa; margin-bottom: 28px;
  }
  .badge-dot {
    display: flex; gap: 3px;
  }
  .bdot {
    width: 18px; height: 18px; border-radius: 999px;
    font-size: 8px; font-weight: 800; color: #fff;
    display: flex; align-items: center; justify-content: center;
    letter-spacing: -0.04em;
  }
  .n8n-hero h1 {
    font-size: clamp(32px, 5vw, 52px); font-weight: 700; line-height: 1.1;
    letter-spacing: -0.03em; color: var(--md-default-fg-color); margin-bottom: 18px;
    max-width: 640px; margin-left: auto; margin-right: auto;
  }
  .n8n-hero h1 span { color: #f04e2c; }
  .n8n-hero p {
    font-size: 16px; color: #888; line-height: 1.65;
    max-width: 480px; margin: 0 auto 36px;
  }
  .hero-btns { display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; }
  .btn-lg {
    font-family: 'DM Sans', sans-serif; font-size: 14px; font-weight: 600;
    padding: 10px 22px; border-radius: 7px; cursor: pointer; transition: 0.15s;
  }
  .btn-lg.primary { background: #f04e2c; border: none; color: #fff; }
  .btn-lg.primary:hover { background: #d44424; }
  .btn-lg.outline { background: transparent; border: 1px solid #2e2e2e; color: #ccc; }
  .btn-lg.outline:hover { border-color: #555; color: #fff; }

  /* INTEGRATION PILLS */
  .integration-row {
    display: flex; justify-content: center; gap: 8px; flex-wrap: wrap;
    margin: 40px auto 0; padding: 0 24px;
  }
  .int-pill {
    display: flex; align-items: center; gap: 6px;
    background: #171717; border: 1px solid #252525;
    border-radius: 999px; padding: 5px 12px;
    font-size: 12px; font-weight: 500; color: #999;
  }
  .int-dot { width: 8px; height: 8px; border-radius: 50%; }
  .section {
    padding: 72px 24px;
    max-width: 900px; margin: 0 auto;
  }
  .section-label {
    font-size: 11px; font-weight: 600; text-transform: uppercase;
    letter-spacing: 0.1em; color: #f04e2c; margin-bottom: 12px;
  }
  .section-title {
    font-size: clamp(22px, 3vw, 32px); font-weight: 700;
    letter-spacing: -0.025em; color: var(--md-default-fg-color); margin-bottom: 12px;
    line-height: 1.2;
  }
  
  .section-sub {
    font-size: 15px; color: #777; line-height: 1.6; max-width: 480px;
  }
  .section-header { margin-bottom: 40px; }

  /* WORKFLOW DIAGRAM */
  .workflow-wrap {
    background: #111; border: 1px solid #1e1e1e;
    border-radius: 12px; padding: 28px 20px; overflow: hidden;
  }
  .workflow-nodes {
    display: flex; align-items: center;
    gap: 0; overflow-x: auto;
  }
  .wf-node {
    flex-shrink: 0;
    background: #1a1a1a; border: 1px solid #2a2a2a;
    border-radius: 8px; padding: 10px 14px;
    display: flex; align-items: center; gap: 8px;
    font-size: 12px; font-weight: 500; color: #ccc;
    min-width: 120px;
  }
  .wf-node-icon {
    width: 24px; height: 24px; border-radius: 5px;
    display: flex; align-items: center; justify-content: center;
    font-size: 11px; font-weight: 800; flex-shrink: 0;
  }
  .wf-arrow {
    flex-shrink: 0; color: #333; padding: 0 8px;
    font-size: 16px; display: flex; align-items: center;
  }
  .wf-result {
    margin-top: 20px; background: #0d0d0d; border: 1px solid #1e1e1e;
    border-radius: 8px; padding: 16px;
  }
  .wf-result-label { font-size: 11px; color: #555; margin-bottom: 8px; font-family: 'IBM Plex Mono', monospace; }
  .json-line { font-family: 'IBM Plex Mono', monospace; font-size: 11px; line-height: 1.7; }
  .jk { color: #888; }
  .jv-str { color: #98c379; }
  .jv-key { color: #61afef; }
  .jv-num { color: #e5c07b; }
  .jv-orange { color: #f04e2c; }

  /* FEATURE CARDS (mobile first) */
.feat-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 12px;
}

/* tablets and up */
@media (min-width: 640px) {
  .feat-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

.feat-card {
  background: #111;
  border: 1px solid #1e1e1e;
  border-radius: 10px;
  padding: 16px; /* smaller for mobile */
  transition: border-color 0.2s;
}

/* slightly more padding on larger screens */
@media (min-width: 640px) {
  .feat-card {
    padding: 22px;
  }
}

.feat-card:hover {
  border-color: #333;
}

.feat-card-icon {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: #1e1e1e;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 12px;
  font-size: 15px;
  color: #f04e2c;
}

@media (min-width: 640px) {
  .feat-card-icon {
    width: 36px;
    height: 36px;
    margin-bottom: 14px;
    font-size: 16px;
  }
}

.feat-card h3 {
  font-size: 14px;
  font-weight: 600;
  color: #e8e8e8;
  margin-bottom: 6px;
}

.feat-card p {
  font-size: 13px;
  color: #666;
  line-height: 1.6;
}

.feat-card pre {
  margin-top: 14px;
  background: #0d0d0d;
  border: 1px solid #1e1e1e;
  border-radius: 6px;
  padding: 12px;
  overflow-x: auto;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 10.5px;
  line-height: 1.7;
  color: #666;
}

  /* FAQ */
  .faq-wrap { max-width: 700px; margin: 0 auto; }
  .faq-item {
    border: 1px solid #1e1e1e; border-radius: 8px;
    margin-bottom: 8px; overflow: hidden;
    transition: border-color 0.2s;
  }
  .faq-item:hover { border-color: #2a2a2a; }
  .faq-q {
    width: 100%; background: #111; border: none; color: #d0d0d0;
    font-family: 'DM Sans', sans-serif; font-size: 14px; font-weight: 500;
    text-align: left; padding: 16px 18px;
    display: flex; justify-content: space-between; align-items: center;
    cursor: pointer; transition: background 0.15s;
  }
  .faq-q:hover { background: #141414; }
  .faq-chevron { transition: transform 0.25s; color: #555; font-size: 16px; }
  .faq-a {
    font-size: 13px; color: #666; line-height: 1.7;
    padding: 0 18px; max-height: 0; overflow: hidden;
    transition: max-height 0.3s ease, padding 0.3s ease;
  }
  .faq-item.open .faq-chevron { transform: rotate(180deg); }
  .faq-item.open .faq-a { max-height: 200px; padding: 0 18px 16px; }

  /* CTA STRIP */
  .cta-strip {
    background: #111; border: 1px solid #1e1e1e;
    border-radius: 12px; padding: 40px 32px;
    text-align: center; max-width: 640px; margin: 0 auto 80px;
  }
  .cta-strip h2 {
    font-size: 24px; font-weight: 700; color: #f0f0f0;
    letter-spacing: -0.025em; margin-bottom: 10px;
  }
  .cta-strip p { font-size: 14px; color: #666; margin-bottom: 24px; }

  /* DIVIDER */
  .divider-line {
    border: none; border-top: 1px solid #1a1a1a;
    margin: 0 24px;
  }
</style>

<div class="n8n-wrap">
  <h2 class="sr-only" style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0)">FindMyClient — Email discovery API for workflow automation</h2>


  <!-- HERO -->
  <section class="n8n-hero">
    <div class="badge-row">
      <div class="badge-dot">
        <span class="bdot" style="background:#EA4B71">n8n</span>
        <span class="bdot" style="background:#FF4A00">Z</span>
        <span class="bdot" style="background:#6D00CC">M</span>
      </div>
      Ready to integrate
    </div>
    <h1>The first <span>email discovery API</span> built for workflow automation</h1>
    <p>Send a search query and the system runs an async web crawl across multiple sources — returning structured leads straight into your pipelines.</p>
    <div class="hero-btns">
      <button class="btn-lg primary" onclick="window.location.href='/introduction'">Get started →</button>
      <button class="btn-lg outline" onclick="window.location.href='https://findmyclient.org/login'">Sign in</button>
    </div>

    <div class="integration-row">
      <div class="int-pill"><span class="int-dot" style="background:#EA4B71"></span>n8n</div>
      <div class="int-pill"><span class="int-dot" style="background:#FF4A00"></span>Zapier</div>
      <div class="int-pill"><span class="int-dot" style="background:#6D00CC"></span>Make</div>
      <div class="int-pill"><span class="int-dot" style="background:#3b82f6"></span>REST API</div>
      <div class="int-pill"><span class="int-dot" style="background:#f59e0b"></span>Self-hosted</div>
    </div>
  </section>

  <hr class="divider-line">

  <!-- HOW IT WORKS -->
  <div class="section">
    <div class="section-header">
      <div class="section-label">How it works</div>
      <div class="section-title">From search query to enriched leads</div>
      <div class="section-sub">Drop an HTTP Request node into any workflow. Query fires, async crawl runs, structured JSON comes back.</div>
    </div>

    <div class="workflow-wrap">
      <div class="workflow-nodes">
        <div class="wf-node">
          <div class="wf-node-icon" style="background:#1e1e1e; color:#f04e2c;">⚡</div>
          <div>
            <div style="font-size:10px;color:#555;margin-bottom:2px;">Trigger</div>
            Schedule
          </div>
        </div>
        <div class="wf-arrow">→</div>
        <div class="wf-node">
          <div class="wf-node-icon" style="background:#162236; color:#61afef;">{ }</div>
          <div>
            <div style="font-size:10px;color:#555;margin-bottom:2px;">HTTP Request</div>
            /api/search
          </div>
        </div>
        <div class="wf-arrow">→</div>
        <div class="wf-node">
          <div class="wf-node-icon" style="background:#1e1e1e; color:#e5c07b;">↻</div>
          <div>
            <div style="font-size:10px;color:#555;margin-bottom:2px;">Async Crawl</div>
            Poll
          </div>
        </div>
        <div class="wf-arrow">→</div>
        <div class="wf-node" style="border-color:#2a3a2a;">
          <div class="wf-node-icon" style="background:#162616; color:#98c379;">✓</div>
          <div>
            <div style="font-size:10px;color:#555;margin-bottom:2px;">Result</div>
            Emails
          </div>
        </div>
        <div class="wf-arrow">→</div>
        <div class="wf-node">
          <div class="wf-node-icon" style="background:#1e1e1e; color:#888;">⊞</div>
          <div>
            <div style="font-size:10px;color:#555;margin-bottom:2px;">Send to</div>
            CRM / Outreach
          </div>
        </div>
      </div>

      <div class="wf-result">
        <div class="wf-result-label">// Response payload</div>
        <div class="json-line"><span class="jk">{</span></div>
        <div class="json-line" style="padding-left:16px"><span class="jk">"query":</span> <span class="jv-str">"singapore cafe"</span><span class="jk">,</span></div>
        <div class="json-line" style="padding-left:16px"><span class="jk">"status":</span> <span class="jv-orange">"completed"</span><span class="jk">,</span></div>
        <div class="json-line" style="padding-left:16px"><span class="jk">"result":</span> <span class="jk">{</span></div>
        <div class="json-line" style="padding-left:32px"><span class="jk">"emails":</span> <span class="jk">[</span><span class="jv-str">"hello@sgcoffee.com"</span><span class="jk">, </span><span class="jv-str">"cafe@beanstory.sg"</span><span class="jk">],</span></div>
        <div class="json-line" style="padding-left:32px"><span class="jk">"total_emails_found":</span> <span class="jv-num">2</span></div>
        <div class="json-line" style="padding-left:16px"><span class="jk">}</span></div>
        <div class="json-line"><span class="jk">}</span></div>
      </div>
    </div>
  </div>

  <hr class="divider-line">

  <!-- FEATURES -->
  <div class="section">
    <div class="section-header">
      <div class="section-label">Features</div>
      <div class="section-title">Everything your pipeline needs</div>
      <div class="section-sub">Built for teams who move fast and want leads without the manual lookup.</div>
    </div>

    <div class="feat-grid">
      <div class="feat-card">
        <div class="feat-card-icon">🔍</div>
        <h3>Business Discovery</h3>
        <p>Search by keyword, location, and industry using public business data sources and mapping APIs.</p>
        <pre><span class="jk">GET</span> <span class="jv-orange">/api/search</span>
<span class="jv-key">?query=</span><span class="jv-str">singapore+cafe</span>
<span class="jv-key">&token=</span><span class="jv-str">YOUR-API-TOKEN</span></pre>
      </div>

      <div class="feat-card">
        <div class="feat-card-icon">⚡</div>
        <h3>Automation Ready</h3>
        <p>Drop into n8n, Zapier, or Make in minutes. Designed to slot into existing outreach stacks.</p>
        <pre><span class="jk">"type":</span> <span class="jv-str">"httpRequest"</span>
<span class="jk">"url":</span> <span class="jv-orange">"findmyclient.org/api"</span>
<span class="jk">"method":</span> <span class="jv-str">"GET"</span></pre>
      </div>

      <div class="feat-card">
        <div class="feat-card-icon">{ }</div>
        <h3>Developer Friendly</h3>
        <p>Simple REST API with async processing, webhook callbacks, and full self-hosted deployment support.</p>
        <pre><span class="jk">"endpoint":</span> <span class="jv-orange">"/api/search"</span>
<span class="jk">"token":</span> <span class="jv-num">YOUR-API-TOKEN</span>
<span class="jk">"query": </span> <span class="jv-str">"singapore cafe"</span></pre>
      </div>

      <div class="feat-card">
        <div class="feat-card-icon">📈</div>
        <h3>Built for Growth</h3>
        <p>Scales from solo prospecting to agency-level lead generation pipelines without changing your workflow.</p>
        <pre><span class="jk">"scale":</span> <span class="jv-str">"startup_to_enterprise"</span>
<span class="jk">"goal":</span> <span class="jv-orange">"lead_generation"</span></pre>
      </div>
    </div>
  </div>

  <hr class="divider-line">

  <!-- FAQ -->
  <div class="section">
    <div class="section-header" style="text-align:center;">
      <div class="section-label" style="text-align:center;">FAQ</div>
      <div class="section-title" style="text-align:center;">Common questions</div>
    </div>
    <div class="faq-wrap" id="faq"></div>
  </div>

  <!-- CTA -->
  <div style="padding: 0 24px 80px;">
    <div class="cta-strip">
      <h2>Start discovering leads today</h2>
      <p>No scraping needed. No manual lookup. Just a query and a workflow.</p>
      <div style="display:flex; gap:10px; justify-content:center;">
        <button class="btn-lg primary" onclick="window.location.href='/introduction'">Get started →</button>
      <button class="btn-lg outline" onclick="window.location.href='https://findmyclient.org/login'">Sign in</button>
      </div>
    </div>
  </div>
</div>

<script>
const faqs = [
  {
    q: "How does the FindMyClient API work?",
    a: "The API uses location-based business search powered by public web data and mapping sources to discover businesses matching your queries. It then crawls publicly available company websites and business pages to extract emails for sales, outreach, CRM, and AI workflow automation."
  },
  {
    q: "What kind of data can FindMyClient discover?",
    a: "FindMyClient discovers publicly available business emails, websites, and location-based business data from web sources and mapping platforms. The API returns structured JSON schemas optimized for AI agents, automation workflows, and developer integrations."
  },
  {
    q: "Can I integrate this into AI agents or workflow automation?",
    a: "Yes. The API is designed for AI agents, workflow automation, CRM enrichment, and internal lead generation. It returns structured JSON schemas optimized for LLMs, autonomous agents, and no-code workflows such as n8n, Zapier, and Make."
  },
  {
    q: "Does FindMyClient support self-hosting?",
    a: "Yes. FindMyClient supports self-hosting through its web UI, allowing developers and teams to run the platform locally or on private infrastructure for greater control, custom workflows, and internal business data operations."
  }
];

const faqEl = document.getElementById('faq');
faqs.forEach((f, i) => {
  const item = document.createElement('div');
  item.className = 'faq-item';
  item.innerHTML = `
    <button class="faq-q" aria-expanded="false">
      ${f.q}
      <i class="ti ti-chevron-down faq-chevron" aria-hidden="true"></i>
    </button>
    <div class="faq-a">${f.a}</div>
  `;
  item.querySelector('.faq-q').addEventListener('click', () => {
    const open = item.classList.toggle('open');
    item.querySelector('.faq-q').setAttribute('aria-expanded', open);
  });
  faqEl.appendChild(item);
});
</script>
