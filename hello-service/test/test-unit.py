from app.main import hello


def test_hello_unit():
    result = hello()
    assert result["message"] == "Hello World"
