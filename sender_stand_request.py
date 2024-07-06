import data
import config
import requests
def create_order(body):
    return requests.post (config.URL_STAND + config.CREATE_ORDER_URL, json=body)
def get_order(track_number):
    get_order_url = f"{config.URL_STAND}{config.GET_ORDER_NUMBER}{track_number}"
    response = requests.get(get_order_url)
    return response


