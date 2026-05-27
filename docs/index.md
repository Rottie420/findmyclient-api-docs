---
hide:
  - navigation
  - toc
  - path
---

<style>
  /* 1. Reset Global Container Layout (Forces true edge-to-edge space) */
  .md-typeset h1 {
    display: none !important; /* Hides default page title */
  }
  .md-content {
    max-width: none !important;
  }
  .md-content__inner {
    max-width: 100% !important;
    padding: 0 !important; /* Leave at 0 so hero section touches the screen edges */
  }

  /* 2. Hero Component Design Wrapper */
  .custom-hero-wrapper {
    background-color: var(--md-primary-color);
    color: var(--md-primary-bg-color);
    padding: 3.5rem 1.5rem 5.5rem;
    text-align: center;
    margin-top: -38px;
  }

  .custom-hero-wrapper {
  width: 100vw;
  margin-left: calc(50% - 50vw);

  background-image:
    linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0)),
    url('assets/images/fd72705f-5914-462a-8ece-85fe0d5ae2b6.jpg');

  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

  .custom-hero-wrapper h1 {
    color: #ffffff !important;
    font-size: 2.2rem !important;
    line-height: 1.25 !important;
    font-weight: 700 !important;
    max-width: 45rem;
    margin: 1.5rem auto 1rem !important;
    display: block !important;
  }
  .custom-hero-wrapper p {
    font-size: 1rem !important;
    line-height: 1.6 !important;
    max-width: 38rem;
    margin: 0 auto 2.5rem;
    opacity: 0.85;
  }

  /* 3. Official Documentation Button Layouts */
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

/* Custom White Button */
.md-button--white {
  background-color: transparent !important;
  color: #ffffff !important;          /* Black text for contrast */
  border-color: #ffffff !important;
}

/* Hover effect */
.md-button--white:hover {
  background-color: #ffffff71 !important;
  color: #ffffff !important;          /* Black text for contrast */
  border-color: #ffffff !important;;
}
  /* 4. Grid Grid Container Rules (Scoped to protect hero banner) */
  .grid-content-container {
    padding: 1.5rem; /* Moves padding out of global and into the grid section */
  }
  .md-typeset .grid > ul > li, 
  .md-typeset .grid > li {
    padding: 1.5rem !important; 
  }

  /* 5. Desktop Viewports (Screens wider than tablet breakpoint) */
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
</style>

<!-- Hero Banner Layout Area -->
<div class="custom-hero-wrapper" markdown>

# API For Finding Emails<br>From Web Data

The API powering AI agents, workflow automation, CRM enrichment, and lead generation systems.

<div class="hero-btn-container" markdown>
[Get Started](/introduction/){ .md-button .md-button--primary }
[&nbsp;&nbsp;Sign In&nbsp;&nbsp;](https://findmyclient.org/login){ .md-button .md-button--white }
</div>

</div>


<!-- 2x2 Responsive Grid Content Area -->
<div class="grid-content-container" markdown>

<!-- Hero Banner Layout Area -->
<div style="text-align:center;" markdown>

<h2> Designed For Modern Lead Generation </h2>

A B2B tool for finding public contact data, enriching prospects, and streamlining outbound research workflows.

</div>
<br><br>
<div class="grid cards" markdown>

-   :material-magnify:{ .lg .middle } __Business Discovery__

    ---

    [`Search`](#) businesses using keyword, location, and industry-based discovery powered by public business data.

    ```JSON
    {
      "query": "singapore cafe"
    }
    ```


-   :material-lightning-bolt:{ .lg .middle } __Automation Ready__

    ---

    Integrate directly into internal tools, [`AI workflows`](#), CRMs, and outreach automation systems.

    ```JSON
    {
      "method": "GET",
      "url": "https://findmyclient.org/api/search",
      "webhook": "n8n webhook URL"
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


<br><br><br><br><br><br><br><br><br><br>