import time
import requests
while 1 > 0:
    time.sleep(5)
    url = requests.get('https://economia.awesomeapi.com.br/last/BTC-BRL')
    dados=url.json()
    valor = int(dados['BTCBRL']['bid'])
    moeda= dados['BTCBRL']['name']
    #texto=(f'Cotação: {moeda} com valor de: {valor:_.2f}').replace('.',',').replace('_','.')
    print((f'Cotação: {moeda} com valor de: {valor:_.2f}').replace('.',',').replace('_','.'))