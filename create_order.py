# импоритруем файлы которые нам будут нужны при создании заказа
import configuration
import requests
# определяем функцию создания заказа
def create_order():
    # вносим данные в заказ по форме из документации к сайту
    order = {
        "firstName": "Джо",
        "lastName": "Пич",
        "address": "ул. Лубянка, д. 10",
        "metroStation": 200,
        "phone": "+76666666666",
        "rentTime": 5,
        "deliveryDate": "2025-08-16",
        "comment": "Пошустрее, пожалуйста",
        "color": ["BLACK"]
    }
# определяем содержимое респонс
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=order)
    # возвращаем респонс в формате джсон
    return response.json()["track"]
# перед тем как вывести содержимое полученного респонса нам надо определить переменную в которую будут падать данные с сервера
track = create_order()
# выводим номер заказа 
print("создан заказ с трек номером:", track)
