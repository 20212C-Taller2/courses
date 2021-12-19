from behave import given, when, then, step, use_step_matcher

use_step_matcher("re")

from features.steps.support import json_headers


@step('el usuario "(?P<student>.+)" se encuentra inscripto')
def step_impl(context, student):
    course = context.response.json()
    context.vars['course_id'] = course['id']
    context.vars['student'] = student

    context.client.post(
        f"/courses/{course['id']}/students/{context.vars['student']}",
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


@step("que transcurrió un día desde su inscripción")
def step_impl(context):
    raise NotImplementedError(u'STEP: Y que transcurrió un día desde su inscripción')


@step('el flujo de desinscripción no se completará con el error "(?P<error_code>.+)"')
def step_impl(context, error_code):
    error_body = context.response.json()

    assert context.response.status_code == 409
    assert error_body['code'] == error_code
