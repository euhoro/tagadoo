import json

from starlette.testclient import TestClient

from main import app


def test_results_are_the_same():
    client = TestClient(app)
    result_mongo = json.loads(client.get("/records/1").content.decode('utf-8'))
    result_python = json.loads(client.get("/records_py/1").content.decode('utf-8'))

    shared_items = {k: result_mongo[k] for k in result_mongo if k in result_python and result_mongo[k] == result_python[k]}
    assert len(shared_items) == len(result_mongo)
