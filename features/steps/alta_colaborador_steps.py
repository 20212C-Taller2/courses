from behave import when, then

from features.steps.support import json_headers


@when(u'su creador asigna al usuario "{}" como colaborador')
def step_impl(context, collaborator):
    course = context.response.json()

    context.vars['course_id'] = course['id']
    context.vars['collaborator'] = collaborator
    context.response = context.client.post(
        "/courses/{}/collaborators/{}".format(context.vars['course_id'], context.vars['collaborator']),
        headers=json_headers()
    )

    assert context.response.status_code == 201


@then(u'será asignado a cumplir dicha función en el curso')
def step_impl(context):
    response = context.client.get(
        "/courses/{}".format(context.vars['course_id']),
        headers=json_headers()
    )

    course = response.json()

    assert context.vars['collaborator'] in course['collaborators']
