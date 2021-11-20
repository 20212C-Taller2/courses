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
