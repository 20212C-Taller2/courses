import requests_mock
from behave import then, use_step_matcher, step

use_step_matcher("re")

from features.steps.support import json_headers


@step('el usuario "(?P<student>.+)" solicita la inscripción al curso')
def step_impl(context, student):
    course_id = context.vars['created']['id']

    with requests_mock.Mocker(real_http=True) as m:
        m.get(
            f'https://ubademy-users-api.herokuapp.com/users/{student}',
            json={
                "id": f"{student}"
            },
            status_code=200,
            headers=json_headers()
        )

        m.post(
            f"https://ubademy-subscriptions-api.herokuapp.com/courses/{course_id}/subscribeStudent",
            json={
                "course_id": f"{course_id}",
                "owner_id": "owner@example.com",
                "subscription_code": "subscription_code"
            },
            headers=json_headers()
        )

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


@step('el usuario "(?P<student>.+)" solicita la inscripción al curso por duplicado')
def step_impl(context, student):
    context.execute_steps(f'cuando el usuario "{student}" solicita la inscripción al curso')
    context.execute_steps(f'cuando el usuario "{student}" solicita la inscripción al curso')
