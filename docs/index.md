---
hide:
  - navigation
  - toc
  - path
---

<style>
.md-typeset h1 {
  display: none !important;
}

.md-content {
  max-width: none !important;
}

.md-content__inner {
  max-width: 100% !important;
  padding: 0 !important;
}

.custom-hero-wrapper {
  width: 100vw;
  margin-top: -1.9rem;
  margin-left: calc(50% - 50vw);
  padding: 2.5rem 1.5rem 5.5rem;
  background-color: var(--md-primary-color);
  color: var(--md-primary-bg-color);
  background-image: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0)),
    url("assets/images/findmyclient_hero_bg.webp");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  text-align: center;
}

.custom-hero-wrapper h1 {
  display: block !important;
  max-width: 45rem;
  margin: 1.5rem auto 1rem !important;
  color: #ffffff !important;
  font-size: 2.2rem !important;
  font-weight: 700 !important;
  line-height: 1.25 !important;
}

.custom-hero-wrapper p {
  max-width: 38rem;
  margin: 0 auto 2.5rem;
  opacity: 0.85;
  font-size: 1rem !important;
  line-height: 1.6 !important;
}

.how-it-works {
  width: 100vw;
  height: 500px;
  margin-left: calc(50% - 50vw);
  background-image: url("assets/images/how_it_works.png");
  background-size: contain;
  background-position: center;
  background-repeat: no-repeat;
}

.hero-btn-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.5rem;
}

.hero-btn-container .md-button {
  margin: 0 !important;
  padding: 0.625rem 1.25rem !important;
  font-size: 0.8rem !important;
  font-weight: 600 !important;
  border-radius: 0.1rem !important;
  transition: color 125ms, background-color 125ms, border-color 125ms !important;
}

.md-button--white {
  background-color: transparent !important;
  color: #ffffff !important; 
  border-color: #ffffff !important;
}

.md-button--white:hover {
  background-color: #ffffff71 !important;
  color: #ffffff !important; 
  border-color: #ffffff !important;;
}
.grid-content-container {
  padding: 1.5rem;
}

.md-typeset .grid > ul > li,
.md-typeset .grid > li {
  padding: 1.5rem !important;
}

.md-typeset .admonition,
.md-typeset details {
  max-width: 800px;
  margin: 0 auto 8px !important;
}

.badge {
  display: inline-block;
  padding: 8px 14px;
  border-radius: 999px;
  background: white;
  box-shadow: 0 10px 30px rgba(0,0,0,0.06);
  color: #6d5efc;
  font-weight: 600;
  font-size: 14px;
  margin-bottom: 16px;
}
.logos { display: inline-flex; gap: 3px; }
.logo {
  font-size: 10px; font-weight: 600;
  padding: 3px 8px; border-radius: 999px;
  letter-spacing: 0.03em; color: #fff;
}
.logo.n8n    { background: #EA4B71; }
.logo.zapier { background: #FF4A00; }
.logo.make   { background: #6D00CC; }
.divider { width: 1px; height: 16px; background: rgba(0,0,0,0.15); }
.tagline { font-size: 12.5px; font-weight: 600; color: #6d5efc; white-space: nowrap; }

h1 {
  margin: 0;
  color: #0b1220;
  font-size: 42px;
  font-weight: 800;
  line-height: 1.1;
}

h1 span {
  background: linear-gradient(90deg, #6d5efc, #9b7bff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

@media screen and (min-width: 60em) {
  .custom-hero-wrapper {
    padding: 6rem 2rem 8rem;
  }

  .custom-hero-wrapper h1 {
    font-size: 3.4rem !important;
  }

  .custom-hero-wrapper p {
    font-size: 1rem !important;
  }

  .grid-content-container {
    padding: 3.5rem; /* Adds wide spacing for grids on desktops */
  }

  .md-typeset .grid {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important; /* Locks 2x2 grid */
    gap: 2rem !important;
  }

  .md-typeset .grid > ul > li,
  .md-typeset .grid > li {
    padding: 3rem !important;
  }
}

@media (min-width: 768px) {
  .badge {
    padding: 10px 16px;
    font-size: 15px;
  }

  h1 {
    font-size: 56px;
  }
}

@media (min-width: 1024px) {
  h1 {
    font-size: 64px;
  }
}

</style>

<!-- Hero Banner Layout Area -->
<div class="custom-hero-wrapper" markdown>


<span class="badge">
  <span class="logos">
    <span class="logo n8n">n8n</span>
    <span class="logo zapier">Zapier</span>
    <span class="logo make">Make</span>
  </span>
  <span class="divider"></span>
  <span class="tagline">Ready to integrate.</span>
</span>

<h1>
The first <span>email discovery API</span><br>
built natively for<br>
workflow automation
</h1>

<div class="hero-btn-container" markdown>
[Get Started](/introduction/){ .md-button .md-button--primary }
[&nbsp;&nbsp;Sign In&nbsp;&nbsp;](https://findmyclient.org/login){ .md-button .md-button--white }</div>

</div>


<!-- 2x2 Responsive Grid Content Area -->
<div class="grid-content-container" markdown>

<!-- Hero Banner Layout Area -->
<div style="text-align:center;" markdown>

<h2> Send a search query and the system runs an async web <br>crawl across multiple sources. </h2>


</div>


<div class="how-it-works"></div>

<div style="text-align:center; margin-top:" markdown>
<h2> Turn any search into business emails and power automated <br>lead generation inside workflow systems. </h2>

</div>

<br>

<div class="grid cards" markdown>

-   :material-magnify:{ .lg .middle } __Business Discovery__

    ---

    [`Search`](#) businesses using keyword, location, and industry-based discovery powered by public business data.

    ```JSON
    {
      "query": "singapore cafe",
      "status": "completed",
      "result": {
        "emails": [sgcoffee@email.com]
      }
    }
    ```


-   :material-lightning-bolt:{ .lg .middle } __Automation Ready__

    ---

    Integrate directly into internal tools, [`AI workflows`](#), CRMs, and outreach automation systems.

    ```JSON
    "nodes": [
        {
          "name": "HTTP Request",
          "type": "n8n-nodes-base.httpRequest",
          "parameters": {
            "method": "GET",
            "url": "https://findmyclient.org/api/search"
          }
        }
    ```

    
-   :material-api:{ .lg .middle } __Developer Friendly__

    ---

    Simple [`REST API`](#), asynchronous processing, webhook support, and self-hosted deployment options.

    ```JSON
    {
      "endpoint": "/api/search",
      "method": "GET",
      "params": {
        "query": "singapore cafe"
      }
    }
    ```


-   :material-chart-line:{ .lg .middle } __Built for Growth__

    ---

    Designed for startups, agencies, and teams scaling [`lead generation`](#) efforts.

    ```JSON
    {
      "use_case": "lead_generation",
      "scale": "startup_to_enterprise",
      "goal": "find_and_enrich_business_leads",
      "query_example": "singapore cafe"
    }
    ```

</div>

</div>



<div style="text-align:center;" markdown>

<h2> Frequently Asked Questions </h2>
Common questions about the API and platform
</div>

<br>


??? note "How does the FindMyClient API work?"

    The FindMyClient API uses location-based business search powered by public web data and mapping sources to discover businesses matching your queries. It then crawls publicly available company websites and business pages to extract emails  for sales, outreach, CRM, and AI workflow automation.

??? note "What kind of data can FindMyClient discover?"

    FindMyClient can discover publicly available business emails, websites, and location-based business data from web sources and mapping platforms. The open-source version includes a self-hosted UI that can run locally, while the API version returns structured JSON schemas optimized for AI agents, automation workflows, and developer integrations.


??? note "Can I integrate this into AI agents or workflow?"

    Yes. The FindMyClient API is designed for AI agents, workflow automation, CRM enrichment, and internal lead generation systems. It returns structured JSON schemas optimized for LLMs, autonomous agents, APIs, and no-code workflows such as n8n and automation pipelines.

??? note "Does FindMyClient support self-hosting?"

    Yes. FindMyClient supports self-hosting through its web UI, allowing developers and teams to run the platform locally or on private infrastructure for greater control, custom workflows, and internal business data operations


<br><br><br><br><br><br><br><br><br><br>