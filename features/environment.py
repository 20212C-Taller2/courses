import os
from behave import fixture, use_fixture
from fastapi.testclient import TestClient

from app.main import app


@fixture
def app_client(context, *args, **kwargs):
    context.client = TestClient(app)
    yield context.client


def before_all(context):
    os.environ["TEST_MODE"] = "1"


def before_scenario(context, scenario):
    if "wip" in scenario.effective_tags:
        scenario.skip("Marked with @wip")
        return


def before_feature(context, feature):
    if "wip" in feature.tags:
        feature.skip("Marked with @wip")
        return

    use_fixture(app_client, context)
    context.vars = {}  # Rollback de variables entre feature (vars permite compartir variables entre steps)


def after_all(context):
    del os.environ["TEST_MODE"]
