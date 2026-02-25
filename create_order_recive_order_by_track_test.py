# Сергей Воскобойник, 40-я когорта - Дипломный проект. Инженер по тестированию плюс

import sender_stand_request
import data

def test_create_order():
    # Проверка успешного создания заказа
    response = sender_stand_request.post_new_order(data.order_body)
    assert response.status_code == 201, \
        f"Ожидался код 201, получен {response.status_code}"
    assert response.json()["track"] is not None, "Трек заказа не получен"

def test_get_order_by_track():
    # Проверка получения заказа по треку
    create_response = sender_stand_request.post_new_order(data.order_body)
    track_number = create_response.json()["track"]
    get_response = sender_stand_request.get_order_by_track(track_number)
    
    assert get_response.status_code == 200, \
        f"Ожидался код 200, получен {get_response.status_code}"