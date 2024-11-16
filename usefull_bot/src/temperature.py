import requests


# Функция для запроса температуры с сайта wttr.in
def get_temperature():
    try:
        response = requests.get("https://wttr.in/Volgograd?format=j1")
        data = response.json()
        temp_C = data['current_condition'][0]['temp_C']
        windspeed = data['current_condition'][0]['windspeedKmph']
        #############

        return f"Температура в Волгограде: {temp_C}°C, скорость ветра: {windspeed} км/ч"

        #############
    except Exception as e:
        return f"Ошибка при получении данных: {e}"
