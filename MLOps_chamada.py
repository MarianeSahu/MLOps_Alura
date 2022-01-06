##################### Chamando o API MLOps ##################################

# bibliotecas
import requests

# criando os dados
url = 'http://127.0.0.1:5000/'
dados = {
    "tamanho": 200,
    "ano": 2001,
    "garagem": 2
}
frase = 'Python é ótimo'
auth = requests.auth.HTTPBasicAuth('mariane', 'senha')

# chamando a API
resultado = requests.post(url + '/cotacao/', json=dados)
resultado.status_code
resultado.json()

resultado = requests.get(url + '/sentimento/' + frase, auth=auth)
resultado.status_code
resultado.text
