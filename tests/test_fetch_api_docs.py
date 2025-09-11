import sys
from pathlib import Path

import pytest

# Ensure the repository root is on sys.path for imports
sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.fetch_api_docs import validate_categories, EXPECTED_CATEGORIES


def build_data(categories):
    return {"item": [{"name": name} for name in categories]}


def test_validate_categories_success():
    data = build_data(EXPECTED_CATEGORIES)
    validate_categories(data)


def test_validate_categories_missing_category():
    categories = EXPECTED_CATEGORIES - {"Devices"}
    data = build_data(categories)
    with pytest.raises(ValueError, match="Missing categories.*Devices"):
        validate_categories(data)
