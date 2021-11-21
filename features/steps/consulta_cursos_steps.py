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


@when(u'se realiza una búsqueda por categoría utilizando un filtrado por categoria "WEB_DEVELOPMENT"')
def step_impl(context):
    context.vars['type'] = 'WEB_DEVELOPMENT'
    context.response = context.client.get(
        "/courses?type={}".format(context.vars['type']),
        headers=json_headers()
    )

    assert context.response.status_code == 200
    assert isinstance(context.response.json(), list)


@then(u'se retornan los cursos que cumplan dichas categorías')
def step_impl(context):
    for course in context.response.json():
        assert course['type'] == context.vars['type']


@given(u'que existen cursos con suscripción')
def step_impl(context):
    context.vars['total_courses'] = 0
    for row in context.table:
        new_course = create_course({'subscription': row['subscription']})
        response = context.client.post(
            "/courses",
            headers=json_headers(),
            json=new_course
        )
        assert response.status_code == 201
        context.vars['total_courses'] += 1
        print("Creados {} cursos".format(context.vars['total_courses']))


@when(u'se realiza una búsqueda utilizando como filtro el tipo de suscripción de un curso "free"')
def step_impl(context):
    context.vars['subscription'] = 'free'
    context.response = context.client.get(
        "/courses?subscription={}".format(context.vars['subscription']),
        headers=json_headers()
    )

    assert context.response.status_code == 200
    assert isinstance(context.response.json(), list)


@then(u'se retornan los cursos que cumplan dicha suscripción')
def step_impl(context):
    courses = context.response.json()

    assert context.vars['total_courses'] == len(courses)
    for course in courses:
        assert course['subscription'] == context.vars['subscription']


@when(u'se realiza una búsqueda utilizando un filtrado y no existen cursos que cumplan tal condición')
def step_impl(context):
    context.response = context.client.get(
        "/courses?type=WEB_DEVELOPMENT",
        headers=json_headers()
    )


@when(u'se realiza una búsqueda por suscripción utilizando un filtrado y no existen cursos que cumplan tal condición')
def step_impl(context):
    context.response = context.client.get(
        "/courses?subscription=free",
        headers=json_headers()
    )


@then(u'se deberá notificar al usuario que no existen resultados para su búsqueda')
def step_impl(context):
    assert context.response.status_code == 404
    assert isinstance(context.response.json(), dict)
