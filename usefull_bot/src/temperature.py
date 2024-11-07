import requests


# Функция для запроса температуры с сайта wttr.in
def get_temperature():
    try:
        response = requests.get("https://wttr.in/?format=j1")
        data = response.json()
        temp_C = data['current_condition'][0]['temp_C']
        # return f"Температура сейчас: {temp_C}°C"
        if int(temp_C) > 0:
            return f"Its hot today: +{temp_C}°C"
        else:
            return f"Its cold today: {temp_C}°C"
        return temp_C
    except Exception as e:
        return f"Ошибка при получении данных: {e}"
