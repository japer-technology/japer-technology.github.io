import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "generate_endpoints_md",
    Path(__file__).resolve().parents[1] / "scripts" / "generate_endpoints_md.py",
)
gen_md = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen_md)


def test_get_raw_url_string():
    req = {"url": "https://example.com/foo"}
    assert gen_md.get_raw_url(req, "Foo") == "https://example.com/foo"


def test_get_raw_url_dict():
    req = {"url": {"raw": "https://example.com/bar"}}
    assert gen_md.get_raw_url(req, "Bar") == "https://example.com/bar"


def test_get_raw_url_missing_raw(capsys):
    req = {"url": {}}
    assert gen_md.get_raw_url(req, "Baz") is None
    captured = capsys.readouterr()
    assert "missing raw URL" in captured.err
