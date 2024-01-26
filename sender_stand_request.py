import configuration
import requests
import data


# Запрос на создание нового пользователя
def post_new_order():
    return requests.post(configuration.BASE_URL + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                         json=data.user_body,  # тут тело
                         headers=data.headers)  # а здесь заголовки


# Запрос на получение данных заказа по его номеру
def get_order(track):
    return requests.get(configuration.BASE_URL + configuration.GET_ORDER_PATH + track)
