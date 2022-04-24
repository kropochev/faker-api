from fastapi.testclient import TestClient

from main import app
from faker import Faker

client = TestClient(app)
faker = Faker()


def test_get_person():
    """Test get person method"""
    response = client.post(
        "/person",
        params={"sex": "Male", "age": 20}
        )
    person = response.json()

    assert response.status_code == 200
    assert person["first_name"] in faker._first_names_male
    assert person["last_name"] in faker._last_names_male


def test_get_persons():
    """Test get persons method"""
    response = client.post(
        "/persons",
        params={"sex": "Female", "age": 20, "count": 10}
        )
    persons = response.json()
    assert response.status_code == 200
    assert len(persons) == 10
