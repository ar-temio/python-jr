import requests


# Функция для запроса температуры с сайта wttr.in
def get_temperature():
    try:
        response = requests.get("https://wttr.in/Volgograd?format=j1")
        data = response.json()
        temp_C = data['current_condition'][0]['temp_C']
        windspeed = data['current_condition'][0]['windspeedKmph']
        windspeed = int(windspeed) * 1000 / 3600
        weather_description = data["current_condition"][0]["weatherDesc"][0]["value"]
        #############

        return f"температура: {temp_C}°C, wind: {windspeed} м/c\nпогодные условия: {weather_description} "

        #############
    except Exception as e:
        return f"Ошибка при получении данных: {e}"
    
