# Аслан Беров 33-я когорта 11-й спринт
# импоритруем файлы которые нам будут нужны при ране автотеста
import create_order
import configuration
import requests

# задаем имя проверки
def test_get_order_by_track():
    #1: получаем трек номер заказа
    track = create_order.create_order()

    #2: выполняем запрос по трек номеру
    response = requests.get(configuration.URL_SERVICE + "/api/v1/orders/track", params={"t": track})

    #3: проверки
    assert response.status_code == 200, "ожидался статус 200, получен {response.status_code}"
    response_data = response.json()
    assert response_data.get("order") is not None, "данные невозхмодно получить"
    assert response_data["order"].get("track") == track, "трек номер не совпадает" 