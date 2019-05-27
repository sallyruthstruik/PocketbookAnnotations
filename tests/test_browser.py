import csv
import functools
import re
from pathlib import Path
from unittest.mock import Mock, patch

import pytest
from flask import Response
from flask.testing import FlaskClient

from core.data_extractor import DataExtractor


_cur_dir = Path(__file__).parent


@functools.lru_cache()
def get_csv_fixture_contents(name: str):
    with open(_cur_dir/f"fixtures/{name}.csv") as fd:
        return list(csv.reader(fd))[1:]


@pytest.fixture()
def mock_cursor():
    return Mock()


@pytest.fixture
def mock_data_extractor(mock_cursor):
    with patch("core.data_extractor.sqlite3.connect") as sqliteConnectMock:
        connMck = Mock()
        connMck.execute.return_value = mock_cursor
        sqliteConnectMock.return_value = connMck

        de = DataExtractor("")
        yield de


@pytest.fixture
def client(mock_data_extractor: DataExtractor):
    import logging
    logging.basicConfig(level="DEBUG")
    logging.getLogger("").setLevel("DEBUG")

    from guis.browser.server import app, controller
    controller.data_extractor = mock_data_extractor

    return app.test_client()


def test_browser_renders_env_and_js(client: FlaskClient):
    index: Response = client.get("/")

    assert index.status_code == 200

    # find all static link and check they are accesible
    for item in re.findall(r"/static/.*?(?:\.css|\.js)", index.data.decode("utf8")):
        r: Response = client.get(item)
        assert r.status_code == 200, f"can't get {item}: {r.status_code}"


def test_api_annotations(client: FlaskClient, mock_cursor: Mock):
    mock_cursor.fetchall.side_effect = [
        # books query first
        get_csv_fixture_contents("get_books"),
        get_csv_fixture_contents("get_tags"),
        get_csv_fixture_contents("get_items_parent_map"),
    ]
    resp: Response = client.get("/api/annotations")
    assert resp.status_code == 200
    assert resp.json == []


def test_api_books(client: FlaskClient):
    resp: Response = client.get("/api/books")
    assert resp.status_code == 200
