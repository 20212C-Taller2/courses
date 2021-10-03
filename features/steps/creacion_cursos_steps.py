import json


@when(u'un creador realice un nuevo curso con')
def step_impl(context):
    json_headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    body = {}
    for row in context.table:
        body[row['key']] = row['value']

    context.response = context.client.post(
        "/courses",
        headers=json_headers,
        json=body
    )


@then(u'recibo el curso creado correctamente')
def step_impl(context):
    assert context.response.status_code == 201
