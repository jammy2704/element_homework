from fastapi import status
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_missing_parameter_array():
    response = client.post("/top_n", json={"n": "3"})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["msg"] == "field required"


def test_missing_parameter_n():
    response = client.post("/top_n", json={"arr": [10, 30, 20]})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["msg"] == "field required"


def test_invalid_type_array():
    response = client.post("/top_n", json={"n": "3", "arr": "arr"})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["msg"] == "value is not a valid list"


def test_invalid_type_n():
    response = client.post("/top_n", json={"n": "invalid", "arr": [10, 30, 20]})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["msg"] == "value is not a valid integer"


def test_negative_n():
    response = client.post("/top_n", json={"n": "-1", "arr": [10, 30, 20]})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["msg"] == "ensure this value is greater than 0"


def test_n_equals_0():
    response = client.post("/top_n", json={"n": "0", "arr": [10, 30, 20]})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["msg"] == "ensure this value is greater than 0"


def test_n_greater_than_array_size():
    response = client.post(
        "/top_n",
        json={"n": "15", "arr": [10, 30, 20, 21, 11, 22, 33, 44, 15, 33, 10, 30]},
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert (
        response.json()["detail"][0]["msg"] == "length of array should be more than n"
    )


def test_valid_input():
    response = client.post(
        "/top_n",
        json={"n": "5", "arr": [10, 30, 20, 21, 11, 22, 33, 44, 15, 33, 10, 30]},
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"arr": [44, 33, 33, 30, 30]}


def test_valid_input_with_int_n():
    response = client.post(
        "/top_n",
        json={"n": 5, "arr": [10, 30, 50, 21, 11, 22, 33, 44, 15, 33, 10, 30, 55]},
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"arr": [55, 50, 44, 33, 33]}


def test_n_equals_array_size():
    response = client.post(
        "/top_n",
        json={"n": "12", "arr": [10, 30, 20, 21, 11, 22, 33, 44, 15, 33, 10, 30]},
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"arr": [44, 33, 33, 30, 30, 22, 21, 20, 15, 11, 10, 10]}


def test_large_array():
    n = 100
    arr = list(range(1, 1000001))
    response = client.post("/top_n", json={"n": n, "arr": arr})
    assert response.status_code == status.HTTP_200_OK
    arr = response.json()["arr"]
    assert len(arr) == n
    assert arr == list(range(1000000, 1000000 - n, -1))
