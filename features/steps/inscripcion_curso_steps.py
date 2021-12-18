from behave import when, then, use_step_matcher, step

use_step_matcher("re")

from features.steps.support import json_headers


@when('el usuario "(?P<student>.+)" solicita la inscripción al curso')
def step_impl(context, student):
    course = context.response.json()
    course_id = context.vars['created']['id']
    context.response = context.client.post(
        f"/courses/{course_id}/students/{student}",
        headers=json_headers()
    )


@then(u'se deberá ejecutar el flujo correspondiente para establecer dicha inscripción.')
def step_impl(context):
    assert context.response.status_code == 201


@step('el flujo de inscripción no se completará con error "(?P<error_code>.+)"')
def step_impl(context, error_code):
    actual_error = context.response.json()

    assert context.response.status_code == 409
    assert actual_error['code'] == error_code
