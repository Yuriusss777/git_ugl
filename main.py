import requests
from datetime import datetime

# Дата и время, для которых вы хотите узнать цену (здесь указаны примеры)
desired_date = "2018-12-12"  # Желаемая дата
desired_time = "12:00:00"  # Желаемое время

# Преобразуйте желаемую дату и время в Unix timestamp
desired_datetime = f"{desired_date} {desired_time}"
desired_timestamp = int(datetime.timestamp(datetime.strptime(desired_datetime, "%Y-%m-%d %H:%M:%S")))

# URL CoinGecko API для получения исторических данных о ценах биткоина
url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'

# Параметры запроса
params = {
    'vs_currency': 'usd',  # Валюта, в которой вы хотите получить цену (например, USD)
    'from': desired_timestamp,  # Unix timestamp желаемой даты и времени
    'to': desired_timestamp,  # Unix timestamp желаемой даты и времени
    'days': 1  # В данном случае 1 день, так как мы ищем данные для конкретного времени
}

# Выполните запрос к API
response = requests.get(url, params=params)
data = response.json()

# Извлеките цену из полученных данных
price = data['prices'][0][1]  # Временная метка и цена, извлекаем цену

print(f"Цена на {desired_date} в {desired_time}: {price} USD")

