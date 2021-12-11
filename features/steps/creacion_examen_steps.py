from behave import step, when, then

from features.steps.support import json_headers, create_exam


@step(u'un creador inicia la creación de un examen con titulo "{}"')
def step_impl(context, title):
    exam = {'title': title, 'published': True}

    context.vars['exam'] = exam


@step(u'contiene las preguntas')
def step_impl(context):
    exam = context.vars['exam']
    exam['questions'] = [{'number': int(question['number']), 'text': question['text']} for question in context.table]
    context.vars['exam'] = exam


@step(u'crea el examen')
def step_impl(context):
    course_id = context.response.json()['id']

    context.response = context.client.post(
        "/courses/{}/exams".format(course_id),
        json=context.vars['exam'],
        headers=json_headers()
    )

    context.vars['created-exam'] = context.response.json()


@then(u'se creará un nuevo examen')
def step_impl(context):
    assert context.response.status_code == 201

    expected_exam = context.vars['exam']
    actual_exam = context.response.json()

    assert expected_exam['title'] == actual_exam['title']
    assert expected_exam['published'] == actual_exam['published']

    assert len(expected_exam['questions']) == len(actual_exam['questions'])
    for expected_question, actual_question in zip(expected_exam['questions'], actual_exam['questions']):
        assert expected_question['number'] == actual_question['number']
        assert expected_question['text'] == actual_question['text']


@step(u'que existe un examen')
def step_impl(context):
    exam_body = create_exam()

    context.response = context.client.post(
        "/courses/{}/exams".format(context.vars['created']['id']),
        json=exam_body,
        headers=json_headers()
    )

    context.vars['exam'] = context.response.json()

    assert context.response.status_code == 201


@step("el creador lo publica")
def step_impl(context):
    published_exam = context.vars['exam']
    published_exam['published'] = True

    context.response = context.client.put(
        "/courses/{}/exams/{}".format(context.vars['created']['id'], published_exam['id']),
        json=published_exam,
        headers=json_headers()
    )

    context.vars['exam'] = context.response.json()

    assert context.response.status_code == 200


@when(u'se consulta por los exámenes del curso')
def step_impl(context):
    context.response = context.client.get(
        "/courses/{}/exams".format(context.vars['created']['id']),
        headers=json_headers()
    )


@then(u'obtengo el detalle de los exámenes del curso')
def step_impl(context):
    expected_exam = context.vars['exam']
    current_exam = context.response.json()

    assert context.response.status_code == 200
    assert len(current_exam) == 1

    current_exam = current_exam[0]
    assert expected_exam['title'] == current_exam['title']
    for expected_question, current_question in zip(expected_exam['questions'], current_exam['questions']):
        assert expected_question['number'] == current_question['number']
        assert expected_question['text'] == current_question['text']


@step("se consulta por los exámenes publicados del curso")
def step_impl(context):
    context.response = context.client.get(
        "/courses/{}/exams?published=true".format(context.vars['created']['id']),
        headers=json_headers()
    )

    assert context.response.status_code == 200


@step("obtengo el detalle de los exámenes publicados del curso")
def step_impl(context):
    current_exams = context.response.json()

    for current_exam in current_exams:
        assert current_exam['published'] == True


@step("se consulta por los exámenes no publicados del curso")
def step_impl(context):
    context.response = context.client.get(
        "/courses/{}/exams?published=false".format(context.vars['created']['id']),
        headers=json_headers()
    )

    assert context.response.status_code == 200


@step("obtengo el detalle de los exámenes no publicados del curso")
def step_impl(context):
    current_exams = context.response.json()

    for current_exam in current_exams:
        assert current_exam['published'] == False
