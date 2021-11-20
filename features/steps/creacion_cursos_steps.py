from behave import given, when, then

from features.steps.support import create_course, json_headers


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

    context.response = context.client.post(
        "/courses",
        headers=json_headers(),
        json=new_course
    )


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
    context.response = context.client.post(
        "/courses",
        headers=json_headers(),
        json=create_course({})
    )

    response = context.response.json()
    context.vars['created'] = response

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


@when(u'un creador realice un nuevo curso con "{}" faltante.')
def step_impl(context, key):
    course = create_course({})
    del course[key]

    context.response = context.client.post(
        "/courses",
        headers=json_headers(),
        json=course
    )


@then(u'el sistema deberá informarle que no es una operación permitida.')
def step_impl(context):
    assert context.response.status_code == 422


@when(u'consulto las suscripciones')
def step_impl(context):
    context.response = context.client.get(
        "/courses/subscriptions",
        headers=json_headers()
    )


@then(u'recibo una lista con los distintos tipos de suscripciones')
def step_impl(context):
    body = context.response.json()

    assert context.response.status_code == 200
    assert isinstance(body, list)


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
