import requests_mock


def create_course(replacement: dict):
    example_course = {
        "title": "title",
        "description": "description",
        "exams": 1,
        "subscription": "free",
        "type": "WEB_DEVELOPMENT",
        "creator": "profe@domain.com",
        "location": "Buenos Aires",
        "tags": [],
        "media": []
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


def post_course(context, new_course):
    with requests_mock.Mocker(real_http=True) as m:
        m.get(
            'https://ubademy-subscriptions-api.herokuapp.com/subscriptions',
            json=[{"code": "free"}],
            headers=json_headers()
        )

        return context.client.post(
            "/courses",
            headers=json_headers(),
            json=new_course
        )
