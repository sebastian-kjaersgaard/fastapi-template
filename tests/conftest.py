# -*- coding: utf-8 -*-
"""Example Google style docstrings.

"""
import pytest
from starlette import testclient
import fastapi_template
import subprocess
import pathlib


@pytest.fixture
def app():
    """app.
    """
    return fastapi_template.create_app()


@pytest.fixture
def client(app):
    """client.

    Args:
        app:
    """
    cwd = pathlib.Path(__file__).parent.parent
    subprocess.check_call(["alembic", "upgrade", "head"], cwd=cwd)
    with testclient.TestClient(app) as client:
        yield client
    # TODO this should only be called if tests fail?
