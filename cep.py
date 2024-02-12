import requests
cep=input('Insira o CEP: ')
requests.Session.cookies.add_cookie_header()
url = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}')
retorno=url.json()
if url.status_code == 200:
    print(f'CEP: {retorno['cep']}, Endereço: {retorno['address']}, Bairro: {retorno['district']}, Cidade: {retorno['city']} - {retorno['state']} - \n Link Google maps: https://www.google.com/maps/search/{retorno['lat']},+{retorno['lng']} ')
elif url.status_code == 404:
    print(f'CEP: {cep} não encontrado!')
else:
    print(f'CEP: {cep} invalido!')