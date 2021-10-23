def create_course(replacement: dict):
    example_course = {
        "title": "title",
        "description": "description",
        "exams": 1,
        "subscription": "free"
    }

    example_course.update(parse_course(replacement))

    return example_course


def parse_course(course: dict):
    if "exams" in course:
        course["exams"] = int(course["exams"])

    return course


def json_headers():
    return {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }


@when(u'un creador realice un nuevo curso con')
def step_impl(context):
    body = {}
    for row in context.table:
        body[row['key']] = row['value']

    context.vars['body'] = create_course(body)

    context.response = context.client.post(
        "/courses",
        headers=json_headers(),
        json=body
    )


@then(u'recibo el curso creado correctamente')
def step_impl(context):
    request = context.vars['body']
    response_body = context.response.json()

    assert context.response.status_code == 201
    for key in request:
        assert response_body[key] == request[key]


@given(u'que existe un curso')
def step_impl(context):
    context.response = context.client.post(
        "/courses",
        headers=json_headers(),
        json=create_course({})
    )

    response = context.response.json()
    context.vars['created'] = response

    assert context.response.status_code == 201


@when(u'lo consulto')
def step_impl(context):
    course_id = context.vars['created']['id']
    context.response = context.client.get(
        f'/courses/{course_id}',
        headers=json_headers()
    )


@then(u'este curso podrá ser visualizado y realizado por los estudiantes.')
def step_impl(context):
    assert context.response.status_code == 200
    body = context.response.json()
    for key in body:
        assert context.vars['created'][key] == body[key]
