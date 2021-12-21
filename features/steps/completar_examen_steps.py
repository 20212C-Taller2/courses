import requests_mock
from behave import *

from features.steps.support import json_headers

use_step_matcher("re")


@step(u'un estudiante inscripto')
def step_impl(context):
    course_id = context.vars['created']['id']
    student_id = "student@example.com"

    with requests_mock.Mocker(real_http=True) as m:
        m.get(
            f'https://ubademy-users-api.herokuapp.com/users/{student_id}',
            json={
                "id": f'{student_id}'
            },
            status_code=200,
            headers=json_headers()
        )

        m.post(
            f"https://ubademy-subscriptions-api.herokuapp.com/courses/{course_id}/subscribeStudent",
            json={
                "course_id": f"{course_id}",
                "owner_id": student_id,
                "subscription_code": "subscription_code"
            },
            headers=json_headers()
        )

        context.vars['student'] = context.client.post(
            f"/courses/{course_id}/students/student@example.com",
            headers=json_headers()
        ).json()


@step(u'el estudiante completa un examen de manera exitosa')
def step_impl(context):
    exam = context.vars['exam']
    context.vars['exam_submit'] = {
        "student": context.vars['student']['student_id'],
        "answers": [{"question_id": question['id'], "text": "answer"} for question in exam['questions']]
    }


@step(u'se enviará el examen para su corrección')
def step_impl(context):
    course_id = context.vars['created']['id']
    exam_id = context.vars['exam']['id']

    context.response = context.client.post(
        "/courses/{}/exams/{}".format(course_id, exam_id),
        json=context.vars['exam_submit'],
        headers=json_headers()
    )

    assert context.response.status_code == 201


@step(u'el estudiante no podrá completarlo nuevamente')
def step_impl(context):
    course_id = context.vars['created']['id']
    exam_id = context.vars['exam']['id']
    student_id = context.vars['student']['student_id']

    context.response = context.client.post(
        "/courses/{}/exams/{}/students/{}".format(course_id, exam_id, student_id),
        json=context.vars['exam_submit'],
        headers=json_headers()
    )

    assert context.response.status_code != 201
