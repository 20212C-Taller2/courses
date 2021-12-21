import requests_mock
from behave import when, then, use_step_matcher, step

use_step_matcher("re")

from features.steps.support import json_headers


@when('su creador asigna al usuario "(?P<collaborator>.+)" como colaborador')
def step_impl(context, collaborator):
    course_id = context.vars['created']['id']
    context.vars['collaborator'] = collaborator

    with requests_mock.Mocker(real_http=True) as m:
        m.get(
            f'https://ubademy-users-api.herokuapp.com/users/{collaborator}',
            json={
                "id": f"{collaborator}"
            },
            status_code=200,
            headers=json_headers()
        )

        context.response = context.client.post(
            f"/courses/{course_id}/collaborators/{collaborator}",
            headers=json_headers()
        )


@then(u'será asignado a cumplir dicha función en el curso')
def step_impl(context):
    course_id = context.vars['created']['id']

    response = context.client.get(
        f"/courses/{course_id}",
        headers=json_headers()
    )

    course = response.json()

    assert context.response.status_code == 201
    assert context.vars['collaborator'] in course['collaborators']


@step('su creador asigna al usuario "(?P<collaborator>.+)" como colaborador por duplicado')
def step_impl(context, collaborator):
    context.execute_steps(f'cuando su creador asigna al usuario "{collaborator}" como colaborador')
    context.execute_steps(f'cuando su creador asigna al usuario "{collaborator}" como colaborador')
