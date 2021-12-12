from behave import *

from features.steps.support import json_headers

use_step_matcher("re")


@step("resuelve el examen")
def step_impl(context):
    context.execute_steps(u"cuando el estudiante completa un examen de manera exitosa")
    context.execute_steps(u"entonces se enviará el examen para su corrección")


@step("un colaborador inscripto")
def step_impl(context):
    context.execute_steps('cuando su creador asigna al usuario "collaborator@example.com" como colaborador')


@step('el "(?P<user_id>.+)" realiza la corrección de un examen de manera correcta con el comentario "(?P<feedback>.+)"')
def step_impl(context, user_id, feedback):
    course_id = context.vars['created']['id']
    exam_id = context.vars['exam']['id']

    context.vars['revised_exam'] = {
        "feedback": feedback,
        "user": user_id,
        "grade": 10
    }

    context.response = context.client.patch(
        "/courses/{}/exams/{}".format(course_id, exam_id),
        json=context.vars['revised_exam'],
        headers=json_headers()
    )


@step("el examen pasará a un estado finalizado y tendrá una nota asociada")
def step_impl(context):
    assert context.response.status_code == 200
