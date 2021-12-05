from urllib.parse import urlencode

from behave import given, when, then

from features.steps.support import json_headers


@when(u'consulto los cursos del "{}" "{}"')
def step_impl(context, key, value):
    context.vars[key] = value
    query_string = urlencode({key: value})

    context.response = context.client.get(
        "/courses?{}".format(query_string),
        headers=json_headers()
    )


@then(u'obtengo los cursos que le pertenecen al "{}"')
def step_impl(context, creator_key):
    creator = context.vars[creator_key]
    courses = context.response.json()

    assert context.response.status_code == 200
    for course in courses:
        assert course[creator_key] == creator


@given(u'que está inscripto el "{}" "{}"')
def step_impl(context, role, user_id):
    course_id = context.response.json()['id']
    context.vars['userId'] = user_id
    context.response = context.client.post(
        "/courses/{}/{}/{}".format(course_id, role, user_id),
        headers=json_headers()
    )

    assert context.response.status_code == 201


@given(u'el "{}" no se encuentra inscripto como "{}"')
def step_impl(context, _user_id, _role):
    pass


@when(u'consulto los cursos a los que está inscripto el "{}" "{}"')
def step_impl(context, role, user_id):
    context.response = context.client.get(
        "/courses/{}/{}".format(role, user_id),
        headers=json_headers()
    )


@then(u'obtengo los cursos a los cuales está inscripto el "{}" "{}"')
def step_impl(context, role, user_id):
    courses = context.response.json()

    assert context.response.status_code == 200
    for course in courses:
        assert user_id in course[role]
