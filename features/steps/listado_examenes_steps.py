from behave import *

from features.steps.support import json_headers

use_step_matcher("re")


@step('un "(?P<rol>.+)" lista los exámenes y no selecciona ningún filtro')
def step_impl(context, rol):
    course_id = context.vars['created']['id']

    context.response = context.client.get(
        f"/courses/{course_id}/exams/submissions",
        headers=json_headers()
    )


@step("se listarán en pantalla todos los exámenes que ha creado, corregido o debe corregir")
def step_impl(context):
    submitted_exams = context.response.json()

    assert context.response.status_code == 200
    for submitted_exam in submitted_exams:
        assert 'review' in submitted_exam


@step('un "(?P<rol>.+)" lista los exámenes y filtra por el campo "(?P<campo>.+)" con el valor "(?P<valor>.+)"')
def step_impl(context, rol, campo, valor):
    course_id = context.vars['created']['id']

    context.response = context.client.get(
        f"/courses/{course_id}/exams/submissions?{campo}={valor}",
        headers=json_headers()
    )


@step(
    'se listaran en pantalla todos los exámenes que cumplan el filtro "(?P<campo>.+)" con el valor "(?P<valor>.+)"')
def step_impl(context, campo, valor):
    submitted_exams = context.response.json()

    assert context.response.status_code == 200
    for submitted_exam in submitted_exams:
        assert str(submitted_exam[campo]) == valor
