def create_course(replacement={}):
    example_course = {
        "title": "title",
        "description": "description",
        "exams": 1,
    }
    example_course.update(parse_course(replacement))
    return example_course


def parse_course(course):
    course["exams"] = int(course["exams"])
    return course


@when(u'un creador realice un nuevo curso con')
def step_impl(context):
    json_headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    body = {}
    for row in context.table:
        body[row['key']] = row['value']

    context.vars['body'] = create_course(body)

    context.response = context.client.post(
        "/courses",
        headers=json_headers,
        json=body
    )


@then(u'recibo el curso creado correctamente')
def step_impl(context):
    assert context.response.status_code == 201
    request = context.vars['body']
    response = context.response.json()
    for key in request:
        assert response[key] == request[key]
