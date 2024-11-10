import requests


# Функция для запроса температуры с сайта wttr.in
def get_temperature():
    try:
        response = requests.get("https://wttr.in/Volgograd?format=j1")
        data = response.json()
        temp_C = data['current_condition'][0]['temp_C']
        #############

        if int(temp_C) > 0:
            return f"жара: +{temp_C}°C"
        else:
            return f"холодно: {temp_C}°C"
        return temp_C

        #############
    except Exception as e:
        return f"Ошибка при получении данных: {e}"
