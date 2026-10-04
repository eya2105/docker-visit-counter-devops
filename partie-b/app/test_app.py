import app

class FakeRedis:
    def __init__(self):
        self.n = 0
    def incr(self, key):
        self.n += 1
        return self.n

def test_home(monkeypatch):
    monkeypatch.setattr(app, "cache", FakeRedis())
    client = app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert "1 fois" in response.get_data(as_text=True)