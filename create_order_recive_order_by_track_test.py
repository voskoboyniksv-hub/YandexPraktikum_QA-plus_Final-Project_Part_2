# Сергей Воскобойник, 40-я когорта - Дипломный проект. Инженер по тестированию плюс

import sender_stand_request
import data

def test_create_order():
    response = sender_stand_request.post_new_order(data.order_body)

def test_get_order_by_track():
    create_response = sender_stand_request.post_new_order(data.order_body)
    track_number = create_response.json()["track"]
    get_response = sender_stand_request.get_order_by_track(track_number)
    
    assert get_response.status_code == 200