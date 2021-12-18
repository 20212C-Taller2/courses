import requests_mock


def create_course(replacement: dict):
    example_course = {
        "title": "title",
        "description": "description",
        "subscription": "free",
        "type": "WEB_DEVELOPMENT",
        "creator": "creator@example.com",
        "location": "Buenos Aires",
        "tags": [],
        "media": []
    }

    example_course.update(parse_course(replacement))

    return example_course


def parse_course(course: dict):
    return course


def json_headers():
    return {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer 123.asd.!"#'
    }


def post_course(context, new_course):
    creator_id = new_course['creator'] if 'creator' in new_course else 'creator_id'
    subscription = new_course['subscription'] if 'subscription' in new_course else 'subscription_code'

    with requests_mock.Mocker(real_http=True) as m:
        m.get(
            'https://ubademy-subscriptions-api.herokuapp.com/subscriptions',
            json=[{"code": f"{subscription}"}],
            status_code=200,
            headers=json_headers()
        )

        m.get(
            f'https://ubademy-users-api.herokuapp.com/users/{creator_id}',
            json={
                "id": f"{creator_id}"
            },
            status_code=200,
            headers=json_headers()
        )

        return context.client.post(
            "/courses",
            headers=json_headers(),
            json=new_course
        )


def create_exam():
    example_exam = {
        "title": "dummy exam",
        "published": False,
        "questions": [
            {
                "number": 1,
                "text": "dummy question"
            }
        ]
    }
    return example_exam
