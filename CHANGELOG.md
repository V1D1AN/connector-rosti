# Changelog

## [1.0.0] - 2026-02-03

### Fixed
- **Date filtering**: Filter on real `Event.date` from JSON instead of unreliable manifest metadata
- **Manifest regeneration**: Handle feeds that regenerate manifest.json daily (like Rosti)
- **UUID deduplication**: Track processed events by UUID to prevent re-processing
- **Field access safety**: Safe access for `to_ids`, `Orgc`, `timestamp`, `comment`, `Object.Attribute`, `EventReport` fields
- **Timestamp propagation**: Propagate event timestamp to attributes missing their own
- **Per-event error handling**: Continue processing on individual event failures
- **Progress logging**: Log processing progress (X/Y events)

### Changed
- Manifest is now used only as a list of UUIDs, not for filtering
- State format changed to `last_event_date` (YYYY-MM-DD) + `processed_uuids` list
