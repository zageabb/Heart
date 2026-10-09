"""Test proxy prefix and local links without reading or modifying private data."""
import app as heart

def test_proxy_prefix_and_lan(tmp_path, monkeypatch):
    monkeypatch.setattr(heart, "DATA_FILE", str(tmp_path / "test-readings.json"))
    client = heart.app.test_client()
    local=client.get("/")
    assert local.status_code==200
    assert 'action="/add"' in local.get_data(as_text=True)
    headers={"X-Forwarded-Prefix":"/apps/heart",
             "X-Forwarded-Host":"tanyaanne.ddns.net",
             "X-Forwarded-Proto":"https"}
    proxy=client.get("/",headers=headers)
    assert proxy.status_code==200
    html=proxy.get_data(as_text=True)
    assert 'action="/apps/heart/add"' in html
    assert 'href="/apps/heart/download"' in html
