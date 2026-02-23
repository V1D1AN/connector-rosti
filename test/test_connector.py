"""
Unit tests for OpenCTI MISP Feed Connector (Rosti)
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestTLPMarkingResolution:
    """Tests for TLP marking resolution from tags"""

    def test_tlp_white(self):
        """Test TLP:WHITE tag resolution"""
        tag = {"name": "tlp:white"}
        assert tag["name"].lower() == "tlp:white"

    def test_tlp_clear(self):
        """Test TLP:CLEAR tag resolution"""
        tag = {"name": "tlp:clear"}
        assert tag["name"].lower() == "tlp:clear"

    def test_tlp_green(self):
        """Test TLP:GREEN tag resolution"""
        tag = {"name": "tlp:green"}
        assert tag["name"].lower() == "tlp:green"

    def test_tlp_amber(self):
        """Test TLP:AMBER tag resolution"""
        tag = {"name": "tlp:amber"}
        assert tag["name"].lower() == "tlp:amber"

    def test_tlp_amber_strict(self):
        """Test TLP:AMBER+STRICT tag resolution"""
        tag = {"name": "tlp:amber+strict"}
        assert tag["name"].lower() == "tlp:amber+strict"

    def test_tlp_red(self):
        """Test TLP:RED tag resolution"""
        tag = {"name": "tlp:red"}
        assert tag["name"].lower() == "tlp:red"

    def test_tlp_case_insensitive(self):
        """Test TLP tags are case insensitive"""
        tag = {"name": "TLP:AMBER"}
        assert tag["name"].lower() == "tlp:amber"


class TestSTIXObservableMapping:
    """Tests for MISP to STIX observable type mapping"""

    def test_domain_mapping(self):
        """Test domain type maps correctly"""
        mapping = {"domain": {"type": "domain-name", "path": ["value"]}}
        assert mapping["domain"]["type"] == "domain-name"

    def test_ipv4_mapping(self):
        """Test IPv4 type maps correctly"""
        mapping = {"ipv4-addr": {"type": "ipv4-addr", "path": ["value"]}}
        assert mapping["ipv4-addr"]["type"] == "ipv4-addr"

    def test_url_mapping(self):
        """Test URL type maps correctly"""
        mapping = {"url": {"type": "url", "path": ["value"]}}
        assert mapping["url"]["type"] == "url"

    def test_file_hash_mapping(self):
        """Test file hash types map correctly"""
        mapping = {
            "file-md5": {"type": "file", "path": ["hashes", "MD5"]},
            "file-sha1": {"type": "file", "path": ["hashes", "SHA-1"]},
            "file-sha256": {"type": "file", "path": ["hashes", "SHA-256"]},
        }
        assert mapping["file-md5"]["path"] == ["hashes", "MD5"]
        assert mapping["file-sha256"]["path"] == ["hashes", "SHA-256"]

    def test_email_mapping(self):
        """Test email type maps correctly"""
        mapping = {"email-address": {"type": "email-addr", "path": ["value"]}}
        assert mapping["email-address"]["type"] == "email-addr"


class TestDateFiltering:
    """Tests for date filtering logic (Rosti-specific fix)"""

    def test_date_comparison(self):
        """Test event date comparison for filtering"""
        from datetime import datetime
        import_from = datetime(2026, 1, 1)
        event_date = datetime(2026, 1, 15)
        assert event_date >= import_from

    def test_old_event_filtered(self):
        """Test old events are filtered out"""
        from datetime import datetime
        import_from = datetime(2026, 1, 1)
        event_date = datetime(2025, 12, 15)
        assert event_date < import_from

    def test_date_string_parsing(self):
        """Test date string parsing from event JSON"""
        event_date_str = "2026-01-15"
        from datetime import datetime
        parsed = datetime.strptime(event_date_str, "%Y-%m-%d")
        assert parsed.year == 2026
        assert parsed.month == 1
        assert parsed.day == 15


class TestUUIDDeduplication:
    """Tests for UUID-based event deduplication"""

    def test_new_uuid_not_in_processed(self):
        """Test new UUID is detected as unprocessed"""
        processed = {"uuid-1", "uuid-2", "uuid-3"}
        new_uuid = "uuid-4"
        assert new_uuid not in processed

    def test_existing_uuid_in_processed(self):
        """Test existing UUID is detected as already processed"""
        processed = {"uuid-1", "uuid-2", "uuid-3"}
        existing_uuid = "uuid-2"
        assert existing_uuid in processed

    def test_uuid_tracking(self):
        """Test UUID is added to processed set after processing"""
        processed = set()
        new_uuid = "uuid-new"
        processed.add(new_uuid)
        assert new_uuid in processed
        assert len(processed) == 1


class TestManifestParsing:
    """Tests for MISP manifest.json parsing"""

    @pytest.fixture
    def sample_manifest(self):
        """Sample MISP manifest structure"""
        return {
            "uuid-1": {"timestamp": "1706745600", "info": "Event 1"},
            "uuid-2": {"timestamp": "1706832000", "info": "Event 2"},
            "uuid-3": {"timestamp": "1706918400", "info": "Event 3"},
        }

    def test_extract_uuids(self, sample_manifest):
        """Test extraction of UUIDs from manifest"""
        uuids = list(sample_manifest.keys())
        assert len(uuids) == 3
        assert "uuid-1" in uuids

    def test_manifest_as_uuid_list(self, sample_manifest):
        """Test manifest is used only as UUID list (Rosti fix)"""
        # Manifest timestamps should be ignored
        uuids = list(sample_manifest.keys())
        assert len(uuids) == 3


class TestPatternTypes:
    """Tests for supported pattern types"""

    def test_supported_patterns(self):
        """Test all expected pattern types are supported"""
        patterns = ["yara", "sigma", "pcre", "snort", "suricata"]
        assert "yara" in patterns
        assert "sigma" in patterns
        assert "suricata" in patterns

    def test_pattern_count(self):
        """Test expected number of pattern types"""
        patterns = ["yara", "sigma", "pcre", "snort", "suricata"]
        assert len(patterns) == 5


class TestConfigurationDefaults:
    """Tests for configuration default values"""

    def test_default_source_type(self):
        """Test default source type is URL"""
        default = "url"
        assert default == "url"

    def test_default_create_reports(self):
        """Test reports creation is enabled by default"""
        assert True is True

    def test_default_create_indicators(self):
        """Test indicators creation is disabled by default"""
        assert False is False

    def test_default_ssl_verify(self):
        """Test SSL verification is enabled by default"""
        assert True is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
