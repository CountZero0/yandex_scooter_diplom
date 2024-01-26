import sender_stand_request


# Функция на получение трекового номера
def create_order():
    response = sender_stand_request.post_new_order()
    return response.json()['track']


# Проверка получения данных заказа по трековому номеру
def test_create_and_get_new_order():
    track = create_order()
    response = sender_stand_request.get_order(str(track))
    assert response.status_code == 200
