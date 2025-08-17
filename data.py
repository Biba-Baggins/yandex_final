# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {
    "Content-Type": "application/json"
}

# данные пользователя для создания заказа в системе
user_body = {
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