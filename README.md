# OpenCTI MISP Feed Connector (Rosti-compatible)

This connector imports MISP feed data into OpenCTI. It includes specific fixes for feeds like Rosti that regenerate their manifest daily with incorrect timestamps.

## Key Features

- **Real date filtering**: Uses `Event.date` from actual JSON files instead of unreliable manifest metadata
- **UUID-based deduplication**: Tracks processed events by UUID to avoid re-processing
- **Robust error handling**: Per-event try/catch with detailed logging
- **Safe field access**: Handles missing fields gracefully (to_ids, Orgc, timestamp, etc.)

## Configuration

| Parameter | Description | Default |
|-----------|-------------|---------|
| `MISP_FEED_URL` | URL of the MISP feed | - |
| `MISP_FEED_IMPORT_FROM_DATE` | Only import events with date >= this value (YYYY-MM-DD) | Today |
| `MISP_FEED_CREATE_REPORTS` | Create report entities | true |
| `MISP_FEED_CREATE_INDICATORS` | Create indicator entities | true |
| `MISP_FEED_CREATE_OBSERVABLES` | Create observable entities | true |

## Why this fork?

The upstream OpenCTI MISP feed connector filters events based on the `timestamp` field in `manifest.json`. Some feeds (like Rosti) regenerate their manifest daily, resetting all timestamps to the current time. This causes:

1. **All events appear "new"** on every run
2. **IMPORT_FROM_DATE is ignored** because manifest dates are all today's date
3. **Events can be skipped** due to timestamp collisions

This fork fixes these issues by:
- Using the manifest only as a list of UUIDs
- Downloading each event JSON and filtering on the real `Event.date` field
- Maintaining consistent filtering throughout the entire run

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for details.
