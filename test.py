#Максим Янученя, 18-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_re

def test_order_create():
    response = sender_stand_request.create_order(data.order_body)
    track_number = response.json()["track"]
    print ("Номер заказа", track_number)
    order_response = sender_stand_request.get_order(track_number)
    assert order_response.status_code == 200
