from behave import *

from features.steps.support import json_headers

use_step_matcher("re")


@step(u'un estudiante inscripto')
def step_impl(context):
    context.vars['student'] = context.client.post(
        '/courses/{}/students/{}'.format(context.vars['created']['id'], 'student@example.com'),
        headers=json_headers()
    ).json()


@step(u'el estudiante completa un examen de manera exitosa')
def step_impl(context):
    exam = context.vars['exam']
    context.vars['exam_submit'] = {
        "student": context.vars['student']['id'],
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
    student_id = context.vars['student']['id']

    context.response = context.client.post(
        "/courses/{}/exams/{}/students/{}".format(course_id, exam_id, student_id),
        json=context.vars['exam_submit'],
        headers=json_headers()
    )

    assert context.response.status_code != 201
