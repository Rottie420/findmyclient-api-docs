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