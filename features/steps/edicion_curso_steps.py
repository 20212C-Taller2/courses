import requests_mock
from behave import given, when, then

from features.steps.support import create_course, json_headers, post_course


@given(u'que existe un curso con "{}" "{}"')
def step_impl(context, key, value):
    course = create_course({key: value})

    context.response = post_course(context, course)


@when(u'su creador realice la edición del campo "{}" con el valor "{}"')
def step_impl(context, key, new_value):
    course = context.response.json()
    course[key] = new_value

    context.vars['new_value'] = new_value

    with requests_mock.Mocker(real_http=True) as m:
        m.get(
            'https://ubademy-subscriptions-api.herokuapp.com/subscriptions',
            json=[{"code": "free"}],
            headers=json_headers()
        )

        context.response = context.client.patch(
            "/courses/{}".format(course['id']),
            headers=json_headers(),
            json=create_course(course)
        )


@then(u'al confirmar los nuevos cambios, el campo "{}" se verá reflejado en el curso con el valor "{}"')
def step_impl(context, key, new_value):
    edited_course = context.response.json()

    assert context.response.status_code == 200
    assert str(edited_course[key]) == str(context.vars['new_value'])
