# Таир Искаков, когорта 38
# Финальный проект — вторая часть (Яндекс Самокат)

import time
import requests
from configuration import BASE_URL, TIMEOUT
from sender_stand_requests import create_order, get_order
import data


def test_order_creation_and_retrieval():
    # необязательная проверка доступности swagger
    try:
        r = requests.get(f"{BASE_URL}docs/", timeout=TIMEOUT)
        print("DOCS status =", r.status_code)
    except Exception:
        pass

    # 1. Создание заказа
    response = create_order(data.order_body)
    assert response.status_code in (200, 201), f"Ошибка создания: {response.text}"

    body = response.json()
    track = body.get("track") or body.get("trackNumber") or body.get("track_number")
    assert track, f"В ответе нет track: {body}"

    print("TRACK =", track)

    # 2. Получение заказа по треку
    time.sleep(0.3)
    get_response = get_order(track)
    assert get_response.status_code == 200, f"Ошибка получения: {get_response.text}"