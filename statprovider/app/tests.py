import psycopg2
import os
import pytest
from logger import Logger


@pytest.fixture(scope="session", autouse=True)
def run_pre_post():
    with psycopg2.connect(
        host=os.environ["DB_CONTAINER_NAME"],
        port=os.environ["DB_PORT"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    ) as conn:
        query = ""
        cur = conn.cursor()
        with open("/tools/test_data.sql", "r") as reader:
            query = reader.read()

        cur.execute(query)
        conn.commit()

    yield

    Logger.info("Starting post")
    query = ""
    with open("/tools/clear_db.sql", "r") as reader:
        query = reader.read()

    with psycopg2.connect(
        host=os.environ["DB_CONTAINER_NAME"],
        port=os.environ["DB_PORT"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    ) as conn:
        cur = conn.cursor()
        cur.execute(query)
        Logger.info("In connection")
        conn.commit()
    Logger.info("Finish post")


def test_api_get_stats_wo_params():
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)
    response = client.get("/stats")
    response_json = response.json()
    assert response.status_code == 200
    assert "data" in response_json
    assert "msg" in response_json["data"]
    assert "amount" in response_json["data"]
    assert response_json["data"]["msg"]["count"] > 0
    assert response_json["data"]["amount"]["total"] > 0


def test_api_get_stats_w_from_time_params():
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)
    response = client.get("/stats?from_time=2001-01-01T01:02:00")
    response_json = response.json()
    assert response.status_code == 200
    assert "data" in response_json
    assert response_json["data"]["msg"]["count"] == 4


def test_api_get_stats_w_to_time_params():
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)
    response = client.get("/stats?to_time=2001-01-01T01:02:00")
    response_json = response.json()
    assert response.status_code == 200
    assert "data" in response_json
    assert response_json["data"]["msg"]["count"] == 1


def test_api_get_stats_w_from_time_to_time_params():
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)
    response = client.get(
        "/stats?from_time=2001-01-01T01:02:00&to_time=3001-01-01T01:01:00"
    )
    response_json = response.json()
    assert response.status_code == 200
    assert "data" in response_json
    assert response_json["data"]["msg"]["count"] == 3


def test_api_get_stats_w_customerId_params():
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)
    response = client.get("/stats?customerId=2")
    response_json = response.json()
    assert response.status_code == 200
    assert "data" in response_json
    assert response_json["data"]["msg"]["count"] == 3


def test_api_get_stats_w_type_params():
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)
    response = client.get("/stats?msg_type=Type1")
    response_json = response.json()
    assert response.status_code == 200
    assert "data" in response_json
    assert response_json["data"]["msg"]["count"] == 2


def test_api_get_stats_w_customerId_and_type_params():
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)
    response = client.get("/stats?customerId=2&msg_type=Type1")
    response_json = response.json()
    assert response.status_code == 200
    assert "data" in response_json
    assert response_json["data"]["msg"]["count"] == 1


def test_api_get_stats_w_wrong_time_format():
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)
    response = client.get("/stats?from_time=undefined")
    response_json = response.json()
    assert response.status_code == 200
    assert "data" in response_json
    assert response_json["data"]["msg"]["count"] == 0


def test_api_get_stats_w_non_existent_customerId():
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)
    response = client.get("/stats?customerId=999")
    response_json = response.json()
    assert response.status_code == 200
    assert "data" in response_json
    assert response_json["data"]["msg"]["count"] == 0


def test_api_get_stats_w_non_existent_type():
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)
    response = client.get("/stats?msg_type=None")
    response_json = response.json()
    assert response.status_code == 200
    assert "data" in response_json
    assert response_json["data"]["msg"]["count"] == 0
