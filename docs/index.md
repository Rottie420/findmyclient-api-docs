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
  }

  .custom-hero-wrapper {
  background-image:
    linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0)),
    url('/assets/images/fd72705f-5914-462a-8ece-85fe0d5ae2b6.jpg');

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
[Search Now](https://findmyclient.org){ .md-button .md-button--primary }
[Contact Us](#){ .md-button }
</div>

</div>


<!-- 2x2 Responsive Grid Content Area -->
<div class="grid-content-container" markdown>

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Set up in 5 minutes__

    ---

    Install [`mkdocs-material`](#) with [`pip`](#) and get up
    and running in minutes

    [:octicons-arrow-right-24: Getting started](#)

-   :fontawesome-brands-markdown:{ .lg .middle } __It's just Markdown__

    ---

    Focus on your content and generate a responsive and searchable static site

    [:octicons-arrow-right-24: Reference](#)

-   :material-format-font:{ .lg .middle } __Made to measure__

    ---

    Change the colors, fonts, language, icons, logo and more with a few lines

    [:octicons-arrow-right-24: Customization](#)

-   :material-scale-balance:{ .lg .middle } __Open Source, MIT__

    ---

    Material for MkDocs is licensed under MIT and available on [GitHub]

    [:octicons-arrow-right-24: License](#)

</div>

</div>


<br><br><br><br><br><br><br><br><br><br>