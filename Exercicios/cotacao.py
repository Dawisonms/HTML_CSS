import requests

# Substitua 'YOUR_API_KEY' pela chave da API Alpha Vantage
api_key = 'J5I0S2INF4N25H9Z'

# Símbolo da ação que você deseja consultar
symbol = "BBAS3.SA"  # Exemplo: PETR4 (Petrobras)

# URL da API Alpha Vantage para cotações em tempo real
'''https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=PETR4.SA&interval=5min&apikey=SUA-CHAVE'''
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&interval=1min&apikey={api_key}'
'''     https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'''

# Faz a solicitação HTTP para a API
response = requests.get(url)

# Converte a resposta em formato JSON
data = response.json()

# Exibe os dados
print(data)
