# tests/tagifai/test_config.py
# Test tagifai/config.py components.

from app import config


def test_config():
    assert config.logger.name == "root"
