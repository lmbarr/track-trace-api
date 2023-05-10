import pytest
from main import app as flask_app


@pytest.fixture()
def app():
    app = flask_app
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_request_article_200(client):
    response = client.get("article?tracking_number=TN12345679&carrier=UPS")
    assert response.status_code == 200, 'Should return 200 answer'


def test_request_article_200_no_record(client):
    response = client.get("article?tracking_number=TN12345679&carrier=UPDDS")
    assert response.status_code == 200, 'Should return 200 answer'


def test_request_article_bad_request(client):
    response = client.get("article")
    assert response.status_code == 400, 'Should return 400 answer'