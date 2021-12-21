import requests_mock
from behave import when, then, step, use_step_matcher

use_step_matcher("re")

from features.steps.support import json_headers


@step('el usuario "(?P<student>.+)" se encuentra inscripto')
def step_impl(context, student):
    course = context.response.json()
    context.vars['course_id'] = course['id']
    context.vars['student'] = student

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
            f"https://ubademy-subscriptions-api.herokuapp.com/courses/{course['id']}/subscribeStudent",
            json={
                "course_id": f"{course['id']}",
                "owner_id": f"{student}",
                "subscription_code": "subscription_code"
            },
            headers=json_headers()
        )

        context.client.post(
            f"/courses/{course['id']}/students/{student}",
            headers=json_headers()
        )


@when(u'solicita la desinscripción a un curso')
def step_impl(context):
    course_id = context.vars['course_id']
    student_id = context.vars['student']

    with requests_mock.Mocker(real_http=True) as m:
        m.delete(
            f'https://ubademy-subscriptions-api.herokuapp.com/courses/{course_id}/subscribeStudent/{student_id}',
            status_code=200,
            headers=json_headers()
        )

        context.response = context.client.delete(
            "/courses/{}/students/{}".format(course_id, student_id),
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
