from behave import given, when, then, use_step_matcher

from features.steps.support import create_course, json_headers

use_step_matcher("re")


@given(u'que existen cursos con tipo')
def step_impl(context):
    for row in context.table:
        new_course = create_course({'type': row['type']})
        response = context.client.post(
            "/courses",
            headers=json_headers(),
            json=new_course
        )
        assert response.status_code == 201


@when(u'se realiza una búsqueda utilizando un filtrado por categoria "WEB_DEVELOPMENT"')
def step_impl(context):
    context.response = context.client.get(
        "/courses?type=WEB_DEVELOPMENT",
        headers=json_headers()
    )

    assert context.response.status_code == 200
    assert isinstance(context.response.json(), list)


@then(u'se retornan los cursos que cumplan dichos filtros.')
def step_impl(context):
    for course in context.response.json():
        assert course['type'] == 'WEB_DEVELOPMENT'


@when(u'se realiza una búsqueda utilizando un filtrado y no existen cursos que cumplan tal condición')
def step_impl(context):
    context.response = context.client.get(
        "/courses?type=WEB_DEVELOPMENT",
        headers=json_headers()
    )


@then(u'se deberá notificar al usuario que no existen resultados para su búsqueda.')
def step_impl(context):
    assert context.response.status_code == 404
    assert isinstance(context.response.json(), dict)
