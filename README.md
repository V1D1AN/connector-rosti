# OpenCTI MISP Feed Connector (Rosti-compatible)

This connector imports MISP feed data into OpenCTI. It includes specific fixes for feeds like Rosti that regenerate their manifest daily with incorrect timestamps.

## Key Features

* **Real date filtering**: Uses `Event.date` from actual JSON files instead of unreliable manifest metadata
* **UUID-based deduplication**: Tracks processed events by UUID to avoid re-processing
* **Robust error handling**: Per-event try/catch with detailed logging
* **Safe field access**: Handles missing fields gracefully (to_ids, Orgc, timestamp, etc.)

## Configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `MISP_FEED_URL` | URL of the MISP feed | - |
| `MISP_FEED_SOURCE_TYPE` | Source type (`url` or `s3`) | `url` |
| `MISP_FEED_SSL_VERIFY` | Verify SSL certificates | `true` |
| `MISP_FEED_IMPORT_FROM_DATE` | Only import events with date >= this value (YYYY-MM-DD) | Today |
| `MISP_FEED_CREATE_REPORTS` | Create report entities | `true` |
| `MISP_FEED_CREATE_INDICATORS` | Create indicator entities | `false` |
| `MISP_FEED_CREATE_OBSERVABLES` | Create observable entities | `false` |
| `MISP_FEED_CREATE_OBJECT_OBSERVABLES` | Create object observables | `false` |
| `MISP_FEED_CREATE_TAGS_AS_LABELS` | Convert tags into labels | `true` |
| `MISP_FEED_GUESS_THREATS_FROM_TAGS` | Infer threats from tags | `false` |
| `MISP_FEED_AUTHOR_FROM_TAGS` | Infer authors from tags | `false` |
| `MISP_FEED_MARKINGS_FROM_TAGS` | Infer markings from tags | `false` |
| `MISP_FEED_REPORT_TYPE` | Report type to create | `misp-event` |
| `MISP_FEED_IMPORT_WITH_ATTACHMENTS` | Import attachments | `false` |
| `CONNECTOR_DURATION_PERIOD` | Time between runs (ISO 8601 duration) | `PT5M` |

## Quick Start

### Docker Compose

```bash
# Copy and edit the configuration
cp docker-compose.yml docker-compose.override.yml
# Edit docker-compose.override.yml with your settings

# Start the connector
docker-compose up -d
```

### Manual

```bash
# Clone the repository
git clone https://github.com/V1D1AN/connector-rosti.git
cd connector-rosti

# Install dependencies
pip install -r requirements.txt

# Copy and edit configuration
cp src/config.yml.sample src/config.yml
# Edit src/config.yml with your settings

# Run
cd src
python main.py
```

## Why this fork?

The upstream OpenCTI MISP feed connector filters events based on the `timestamp` field in `manifest.json`. Some feeds (like Rosti) regenerate their manifest daily, resetting all timestamps to the current time. This causes:

1. **All events appear "new"** on every run
2. **IMPORT_FROM_DATE is ignored** because manifest dates are all today's date
3. **Events can be skipped** due to timestamp collisions

This fork fixes these issues by:

* Using the manifest only as a list of UUIDs
* Downloading each event JSON and filtering on the real `Event.date` field
* Maintaining consistent filtering throughout the entire run

## Development

### Prerequisites

- Python 3.10+
- Docker (optional, for testing)
- Access to an OpenCTI instance

### Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src --cov-report=html
```

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## About

Connector Rosti for OpenCTI
