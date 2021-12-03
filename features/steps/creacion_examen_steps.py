from behave import when, then

from features.steps.support import json_headers


@when(u'un creador inicia la creación de un examen con titulo "{}"')
def step_impl(context, title):
    exam = {'title': title}
    context.vars['exam'] = exam


@when(u'contiene las preguntas')
def step_impl(context):
    exam = context.vars['exam']
    exam['questions'] = [{'number': int(question['number']), 'text': question['text']} for question in context.table]
    context.vars['exam'] = exam


@when(u'publica el examen')
def step_impl(context):
    course_id = context.response.json()['id']

    context.response = context.client.post(
        "/courses/{}/exams".format(course_id),
        json=context.vars['exam'],
        headers=json_headers()
    )


@then(u'se creará un nuevo examen')
def step_impl(context):
    assert context.response.status_code == 201

    expected_exam = context.vars['exam']
    actual_exam = context.response.json()

    assert expected_exam['title'] == actual_exam['title']
    assert len(expected_exam['questions']) == len(actual_exam['questions'])
    for expected_question, actual_question in zip(expected_exam['questions'], actual_exam['questions']):
        assert expected_question['number'] == actual_question['number']
        assert expected_question['text'] == actual_question['text']
