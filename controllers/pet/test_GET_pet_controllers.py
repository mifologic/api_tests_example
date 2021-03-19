import pytest
import requests

from http import HTTPStatus
from jsonschema import validate

from conftest import BASE_URL
from schemas.pet_controllers_schemas import pet_by_id_schema, pet_by_status_schema


def test_GET_pet_by_id(pet_id=13998999813):
    """
    Find pet by id. Check status code - should be=200.
    Compare response data with -json-schema.
    :param pet_id: pet id
    """
    response = requests.get(f'{BASE_URL}/v2/pet/{pet_id}')
    assert response.status_code == HTTPStatus.OK
    validate(instance=response.json(), schema=pet_by_id_schema)


def test_GET_pet_by_wrong_id(pet_id=981981):
    """
    Find pet by wrong id. Check status code - should be=404.
    :param pet_id: pet id
    """
    response = requests.get(f'{BASE_URL}/v2/pet/{pet_id}')
    assert response.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.parametrize('status', ['available', 'pending', 'sold'])
def test_GET_pet_by_status(status):
    """
    Find pet by status. Status can be: available, pending, sold.
    Check status code - should be=200.
    Compare response with data schema.
    :param status: pet status
    """
    response = requests.get(f'{BASE_URL}/v2/pet/findByStatus?status={status}')
    assert response.status_code == HTTPStatus.OK
    validate(instance=response.json(), schema=pet_by_status_schema)
