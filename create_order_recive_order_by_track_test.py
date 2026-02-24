# Сергей Воскобойник, 40-я когорта - Дипломный проект. Инженер по тестированию плюс

import sender_stand_request
import data

def test_create_order_and_get_by_track():
   
    # Создание заказа
    create_response = sender_stand_request.post_new_order(data.order_body)
    
    # Проверка успешного создания заказа
    assert create_response.status_code == 201, \
        f"Ожидался код 201, получен {create_response.status_code}"
    
    # Сохранение номера трека
    track_number = create_response.json()["track"]
    assert track_number is not None, "Трек заказа не получен"
    print(f"Заказ создан. Номер трека: {track_number}")
    
    # Получение заказа по треку
    get_response = sender_stand_request.get_order_by_track(track_number)
    
    # Проверка кода ответа
    assert get_response.status_code == 200, \
        f"Ожидался код 200, получен {get_response.status_code}"
    
    print(f"Заказ успешно получен по треку {track_number}")
    print("Тест пройден успешно!")

# Запуск теста
if __name__ == "__main__":    
    try:
        test_create_order_and_get_by_track()
    except AssertionError as e:
        print(" Тест не пройден: {e}")
    except Exception as e:
        print(" Произошла ошибка: {e}")