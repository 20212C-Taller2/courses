from behave import step

from features.steps.support import json_headers


@step(u'un creador edite el titulo por "{title}"')
def step_impl(context, title):
    context.vars['exam']['title'] = title


@step("edite las preguntas")
def step_impl(context):
    context.vars['exam']['questions'] = [
        {
            'number': int(question['number']),
            'text': question['text']
        }
        for question in context.table]


@step("el examen será actualizado con esta nueva información")
def step_impl(context):
    course_id = context.vars['created']['id']
    exam_id = context.vars['created-exam']['id']

    expected_exam = context.vars['exam']

    context.response = context.client.put(
        "/courses/{}/exams/{}".format(course_id, exam_id),
        json=expected_exam,
        headers=json_headers()
    )

    current_exam = context.response.json()
    assert context.response.status_code == 200
    assert current_exam['id'] == exam_id
    assert current_exam['title'] == expected_exam['title']
    assert current_exam['published'] == expected_exam['published']

    for expected_question, current_question in zip(expected_exam['questions'], current_exam['questions']):
        assert expected_question['number'] == current_question['number']
        assert expected_question['text'] == current_question['text']
