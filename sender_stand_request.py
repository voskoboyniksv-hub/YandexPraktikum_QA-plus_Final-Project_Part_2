import requests
import configuration
import data

def post_new_order(order_body):
   
    url = configuration.BASE_URL + configuration.CREATE_ORDER_ENDPOINT
    response = requests.post(url, json=order_body)
    return response

def get_order_by_track(track_number):

    url = configuration.BASE_URL + configuration.GET_ORDER_ENDPOINT
    params = {"t": track_number}
    response = requests.get(url, params=params)
    return response