# Limitations

The FindMyClient API has the following limitations to ensure stable and fair usage across all users.

---

## Rate Limits
Requests are subject to rate limiting. Excessive usage may result in throttling or temporary request delays. Please ensure your integration respects safe request pacing.

---

## Asynchronous Processing
All requests are processed asynchronously. After submitting a request, you must poll the result endpoint:

/result/{job_id}

to retrieve the final output once processing is complete.

---

## Processing Time
Processing time may vary depending on:

Query complexity
Current system load
Availability of external data sources

Some requests may complete quickly, while others may require additional time.

---

## Data Availability
Results depend on publicly available data. In some cases:

Business contact information may not exist
Email addresses may not be publicly accessible
Partial or limited data may be returned

---

## Concurrent Requests
Concurrent request volume is limited to ensure system stability. High parallel usage may result in throttling or delayed processing.
