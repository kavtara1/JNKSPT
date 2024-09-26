import time

import requests
import pytest
ENDPOINT = "https://todo.pixegami.io/"


def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


def test_can_create_task():
    payload = new_task_payload()
    response = create_task(payload)
    assert response.status_code == 200
    data = response.json()
    task_id = data["task"]["task_id"]
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data['content'] == payload["content"]
    assert get_task_data['user_id'] == payload["user_id"]


@pytest.mark.slow
def test_can_update_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    task_id = create_task_response.json()["task"]["task_id"]
    new_paylaod = {
        "user_id": payload["user_id"],
        "task_id": task_id,
        "content": "updated content",
        "is_done": True
    }
    update_response = update_task(new_paylaod)
    assert update_response.status_code == 200

def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)


def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")


def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)

def new_task_payload():
    payload = {
            "content": "test content",
            "user_id": "test_user",
            "is_done": False
        }
    return payload


