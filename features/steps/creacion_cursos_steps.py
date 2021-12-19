import requests_mock
from behave import given, when, then, step, use_step_matcher

from features.steps.support import create_course, json_headers, post_course

use_step_matcher("re")


@given(u'que un creador realiza un nuevo curso con')
def step_impl(context):
    new_course = {}
    for row in context.table:
        new_course[row['key']] = row['value']

    context.vars['new_course'] = new_course


@given(u'tiene asociados los hashtags asociados')
def step_impl(context):
    context.vars['new_course']['tags'] = [tag['name'] for tag in context.table]


@given(u'tiene las URL de multimedia asociadas')
def step_impl(context):
    context.vars['new_course']['media'] = [media['url'] for media in context.table]


@when(u'lo crea')
def step_impl(context):
    new_course = create_course(context.vars['new_course'])

    context.response = post_course(context, new_course)


@then(u'recibo el curso creado correctamente')
def step_impl(context):
    request = context.vars['new_course']
    response_body = context.response.json()

    assert context.response.status_code == 201
    for key in request:
        if isinstance(request[key], list):
            assert sorted(request[key]) == sorted(response_body[key])
        else:
            assert response_body[key] == request[key]


@given(u'que existe un curso')
def step_impl(context):
    context.response = post_course(context, create_course({}))

    context.vars['created'] = context.response.json()

    assert context.response.status_code == 201


@when(u'lo consulto')
def step_impl(context):
    course_id = context.vars['created']['id']
    context.response = context.client.get(
        f'/courses/{course_id}',
        headers=json_headers()
    )


@then(u'este curso podrá ser visualizado y realizado por los estudiantes.')
def step_impl(context):
    assert context.response.status_code == 200
    body = context.response.json()
    for key in body:
        assert context.vars['created'][key] == body[key]


@when(u'consulto un curso que no existe')
def step_impl(context):
    context.response = context.client.get(
        f'/courses/1',
        headers=json_headers()
    )


@then(u'recibo un mensaje de error')
def step_impl(context):
    assert context.response.status_code == 404


@step('un creador realice un nuevo curso con "(?P<campo>.+)" faltante\.')
def step_impl(context, campo):
    course = create_course({})
    del course[campo]

    context.response = post_course(context, course)


@then(u'el sistema deberá informarle que no es una operación permitida')
def step_impl(context):
    assert context.response.status_code == 422


@when(u'consulto los tipos de cursos que ofrece la plataforma')
def step_impl(context):
    context.response = context.client.get(
        "/courses/types",
        headers=json_headers()
    )


@then(u'recibo una lista con los distintos tipos de cursos')
def step_impl(context):
    body = context.response.json()

    assert context.response.status_code == 200
    assert isinstance(body, list)


@step('que el id de usuario "(?P<user_id>.+)" no existe')
def step_impl(context, user_id):
    context.vars['creator_id'] = user_id


@step("intenta crear un curso")
def step_impl(context):
    creator_id = context.vars['creator_id']
    new_course = create_course({"creator": creator_id})
    subscription = new_course['subscription']

    with requests_mock.Mocker(real_http=True) as m:
        m.get(
            'https://ubademy-subscriptions-api.herokuapp.com/subscriptions',
            json=[{"code": f"{subscription}"}],
            status_code=200,
            headers=json_headers()
        )

        m.get(
            f'https://ubademy-users-api.herokuapp.com/users/{creator_id}',
            json={
                "message": f"There is no user with id: {creator_id}"
            },
            headers=json_headers(),
            status_code=404
        )

        context.response = context.client.post(
            "/courses",
            headers=json_headers(),
            json=new_course
        )


@step('el sistema deberá informar el error con código "(?P<error_code>.+)"')
def step_impl(context, error_code):
    response = context.response.json()
    print(response)
    assert context.response.status_code == 400
    assert response['code'] == error_code
