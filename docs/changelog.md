# Changelog

Latest platform and API updates for FindMyClient.

### v0.0.1 - 13 May 2026
```
Added:

Rate Limiting

- Added request rate limiting to protect the API from excessive usage.
- Implemented a global handler for HTTP `429 Too Many Requests`.
- Returns a structured JSON response when rate limits are exceeded.


Search Request Validation
Introduced a centralized validation layer for all search requests.

Input Sources Supported

- JSON request body
- Form data
- Query parameters

Validation Rules

- Query must be a string.
- Minimum length: 3 characters.
- Maximum length: 50 characters.
- Maximum word count: 8 words.

Security Improvements
Added multiple safeguards to improve request safety and prevent abuse.

- Blocks URL-based inputs (e.g. `http://`, `www.`)
- Prevents common injection patterns (SQL-like and script-based inputs)
- Detects repeated-character spam patterns
- Rejects inputs with excessive non-alphanumeric content ratio


Content Filtering
Introduced keyword-based filtering to block unsafe or irrelevant queries.

- Fraud-related terms
- Credential/password-related terms
- Gambling-related terms
- Adult content-related terms


Input Normalization

- Trims leading and trailing whitespace
- Collapses multiple spaces into a single space
- Normalizes query formatting before processing
```

### v0.0.2 - 24 May 2026
```
Added:

Schema Improvements (Machine Readable Results)

- Improved API response schema for consistent machine-readable output.
- Standardized response structure across all endpoints.
- Added explicit typing for key fields (e.g. query, results, metadata).
- Ensured predictable JSON keys to for agents and integrations.
- Added structured error objects with consistent error codes and messages.


API Usage Enforcement (Anti-Abuse Layer)

- Strengthened API usage controls to reduce spam and automated abuse.
- Added stricter request validation at gateway level.
- Improved rate-limit enforcement consistency across distributed requests.
- Added early request rejection to reduce backend load from invalid traffic.


Dashboard Improvements (Minor Fixes)

- Fixed UI inconsistency in dashboard data rendering.
- Improved alignment and spacing in key metric panels.
- Corrected minor display bug affecting recent request logs.
- Enhanced stability of real-time update feed under high request volume.
```


<br><br><br><br><br><br><br><br><br><br>