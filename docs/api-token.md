# API Tokens

API tokens allow you to authenticate requests to the FindMyClient API.

Once signed in, users can generate and manage API tokens directly from the dashboard.

<br>

### :material-key-variant: Getting Your API Token
---

??? info "Dashboard Access"

    API tokens are only available to authenticated users through the FindMyClient dashboard.

1. [Sign in](https://findmyclient.org/login) to your FindMyClient account.
2. Open the Dashboard.
3. Navigate to the `API Tokens` section.
4. Generate or copy your API token.

<br>

### :material-shield-key: Authentication
=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.6</span>"

Include your API token in the request headers when making API calls.

```http
token: YOUR_API_TOKEN
```

<br>

### :material-api: Example Request
=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.6</span>"

```bash

    curl -X POST "https://findmyclient.org/api/search" \
    -H "token: YOUR_API_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
        "query": "singapore cafe"
    }'

```

<br>

### :material-lock-outline: Security Recommendations
---

!!! warning "Keep Your Token Secure"

    Your API token provides access to your account and API usage.

- Keep your API token private.
- Do not expose tokens in frontend code or public repositories.
- Rotate tokens regularly when needed.
- Revoke compromised tokens immediately from the dashboard.

<br>

### :material-robot-outline: Built for Automation
---

FindMyClient API tokens can be used with:

| Use Case                         | Primary Users                   | Purpose                                                                        | Example                                                                 |
| -------------------------------- | ------------------------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| AI Agents                        | AI Developers, SaaS Builders    | Allow AI agents to autonomously discover and qualify prospects.                | An AI sales assistant finds local businesses matching a target profile. |
| CRM Enrichment                   | Sales Teams, CRM Administrators | Enhance existing CRM records with additional business and contact information. | Enrich company records before launching an outreach campaign.           |
| Internal Lead Generation Systems | Organizations, Growth Teams     | Power proprietary lead generation platforms with fresh prospect data.          | A company builds its own lead dashboard using FindMyClient APIs.        |
| Workflow Automation              | Operations Teams, Agencies      | Automate lead discovery and data processing tasks.                             | Automatically send newly discovered leads to a CRM or database.         |
| n8n Pipelines                    | Automation Builders             | Integrate lead generation into no-code and low-code workflows.                 | Trigger lead searches and route results to Google Sheets or Slack.      |
| Business Intelligence Tools      | Analysts, Researchers           | Use business data for reporting, market analysis, and decision-making.         | Analyze business density and market opportunities in a region.          |
| Developer Integrations           | Software Developers             | Embed lead generation and enrichment capabilities into applications.           | Build a custom prospecting platform using the FindMyClient API.         |


<br><br><br><br><br><br><br><br><br><br>