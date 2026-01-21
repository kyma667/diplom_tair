# Таир Искаков, когорта 38
# Финальный проект — вторая часть (Яндекс Самокат)

import time
from sender_stand_requests import create_order, get_order
import data


def test_create_order():
    response = create_order(data.order_body)
    assert response.status_code in (200, 201)


def test_get_order_by_track():
    response = create_order(data.order_body)
    track = response.json().get("track")
    assert track is not None

    time.sleep(0.3)

    get_response = get_order(track)
    assert get_response.status_code == 200
