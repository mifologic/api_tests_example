import requests

from random import randint
from http import HTTPStatus
from jsonschema import validate
from mimesis import Person

from conftest import BASE_URL
from schemas.pet_controllers_schemas import pet_by_id_schema


def test_POST_add_new_pet():
    """
    Add new pet to the store. Check status code – should be 200.
    Pet id and pet name generate automatically.
    """
    new_pet_data = {
        "id": randint(111111, 999999),
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": Person('en').name(),
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 13,
                "name": "cats"
            }
        ],
        "status": "available"
    }
    response = requests.post(f'{BASE_URL}/v2/pet', json=new_pet_data)
    assert response.status_code == HTTPStatus.OK
    validate(response.json(), pet_by_id_schema)
