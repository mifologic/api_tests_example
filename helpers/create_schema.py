import requests

from genson import SchemaBuilder


def create_json_schema(method):
    """
    Create new json-schema from method.
    :param method: link for schema creation
    :return: created json-schema
    """
    response = requests.get(method)
    builder = SchemaBuilder()
    builder.add_object(response.json())
    return builder.to_schema()


print(create_json_schema('https://petstore.swagger.io/v2/pet/findByStatus?status=available'))
