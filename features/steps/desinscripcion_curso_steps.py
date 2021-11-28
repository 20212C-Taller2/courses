from behave import given, when, then

from features.steps.support import json_headers


@given(u'el usuario "{}" se encuentra inscripto')
def step_impl(context, student):
    course = context.response.json()
    context.vars['course_id'] = course['id']
    context.vars['student'] = student

    context.client.post(
        "/courses/{}/students/{}".format(context.vars['course_id'], context.vars['student']),
        headers=json_headers()
    )


@when(u'solicita la desinscripción a un curso')
def step_impl(context):
    context.response = context.client.delete(
        "/courses/{}/students/{}".format(context.vars['course_id'], context.vars['student']),
        headers=json_headers()
    )

    assert context.response.status_code == 204


@then(u'se deberá ejecutar el flujo correspondiente para establecer dicha desinscripción.')
def step_impl(context):
    response = context.client.get(
        "/courses/{}".format(context.vars['course_id']),
        headers=json_headers()
    )

    course = response.json()

    assert context.vars['student'] not in course['students']
