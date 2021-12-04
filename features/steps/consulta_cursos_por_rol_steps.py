from behave import when, then
from urllib.parse import urlencode
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
