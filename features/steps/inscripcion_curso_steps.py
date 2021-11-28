from behave import when, then

from features.steps.support import json_headers


@when(u'el usuario "{}" solicita la inscripción a un curso')
def step_impl(context, student):
    course = context.response.json()

    context.response = context.client.post(
        "/courses/{}/students/{}".format(course['id'], student),
        headers=json_headers()
    )


@then(u'se deberá ejecutar el flujo correspondiente para establecer dicha inscripción.')
def step_impl(context):
    assert context.response.status_code == 201
