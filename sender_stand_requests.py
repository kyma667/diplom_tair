import requests
from configuration import BASE_URL, CREATE_ORDERS, GET_ORDER, TIMEOUT


def create_order(body):
    url = f"{BASE_URL}{CREATE_ORDERS}"
    return requests.post(url, json=body, timeout=TIMEOUT)


def get_order(track_number):
    url = f"{BASE_URL}{GET_ORDER}?t={track_number}"
    return requests.get(url, timeout=TIMEOUT)