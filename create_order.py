# импоритруем файлы которые нам будут нужны при создании заказа
import configuration
import requests
import data
# определяем функцию создания заказа
def create_order():
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=data.user_body        
    )
    # определяем содержимое респонс
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=data.user_body)
    # возвращаем респонс в формате джсон
    return response.json()["track"]
# перед тем как вывести содержимое полученного респонса нам надо определить переменную в которую будут падать данные с сервера
track = create_order()
# выводим номер заказа 
print("создан заказ с трек номером:", track)
