---
hide:
  - navigation
  - toc
  - path
---
<style>
  /* 1. Global / Mobile-First Layout (Applies to all screens) */
  .md-typeset h1 {
    display: none !important;
  }
  .md-content {
    max-width: none !important;
  }
  .md-content__inner {
    max-width: 100% !important;
    padding: 1rem; /* Smaller padding on mobile phones */
  }
  .md-typeset .grid > ul > li, 
  .md-typeset .grid > li {
    padding: 1.5rem !important; /* Compact cards on mobile phones */
  }

  /* 2. Desktop Layout (Applies only to screens wider than 768px) */
  @media screen and (min-width: 48em) {
    .md-content__inner {
      padding: 2.5rem; /* Generous padding on desktop */
    }
    .md-typeset .grid {
      grid-template-columns: repeat(2, minmax(0, 1fr)) !important; /* Force 2x2 grid */
      gap: 2rem !important;
    }
    .md-typeset .grid > ul > li, 
    .md-typeset .grid > li {
      padding: 3rem !important;   /* Extra roomy cards on desktop */
    }
  }
</style>
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