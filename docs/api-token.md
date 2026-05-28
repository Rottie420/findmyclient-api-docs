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
---

Include your API token in the request headers when making API calls.

```http
token: YOUR_API_TOKEN
```

<br>

### :material-api: Example Request
---

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

- AI agents
- CRM enrichment systems
- Internal business tools
- Workflow automation platforms
- n8n pipelines
- Custom developer integrations


<br><br><br><br><br><br><br><br><br><br>