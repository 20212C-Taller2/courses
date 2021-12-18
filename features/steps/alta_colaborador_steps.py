from behave import when, then

from features.steps.support import json_headers


@when(u'su creador asigna al usuario "{}" como colaborador')
def step_impl(context, collaborator):
    course = context.response.json()

    course_id = context.vars['created']['id']
    context.vars['course_id'] = course['id']
    context.vars['collaborator'] = collaborator
    context.response = context.client.post(
        f"/courses/{course_id}/collaborators/{context.vars['collaborator']}",
        headers=json_headers()
    )


@then(u'será asignado a cumplir dicha función en el curso')
def step_impl(context):
    response = context.client.get(
        f"/courses/{context.vars['course_id']}",
        headers=json_headers()
    )

    course = response.json()

    assert context.response.status_code == 201
    assert context.vars['collaborator'] in course['collaborators']
