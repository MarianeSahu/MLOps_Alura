######################## MLOps: API para ML ######################################
# Criando uma aplicacao para interagir com modelos de ML
# Usando Postman para executar os testes
# (https://www.postman.com/ no mariane.sahu@unisoma.com)
###########################################################################

# bibliotecas
import os
from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth # autenticacao
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
import pickle

# instancia o api
app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD')
basic_auth = BasicAuth(app)

# modelo de preco das casas: so executa uma vez assim que a instancia subir
# region
path = 'G:/.shortcut-targets-by-id/120EU9gkG9oO1ilsmtz23VjxiJA4I7ehL/Alura/'
modelo = pickle.load(
    open(path + 'Formação ML e Negócios Digitais/' +  'modelo_preco_casas.sav', 'rb')
)
# endregion

# paginas
# region
@app.route('/')
def home():
    return 'Primeira API para ML'

@app.route('/sentimento/<frase>')
@basic_auth.required # exigir autenticacao
def sentimento(frase):
    tb = TextBlob(frase)
    tb_en = tb.translate(to='en')
    polaridade = tb_en.sentiment.polarity
    return 'Polaridade: {}'.format(polaridade)

@app.route('/cotacao/',  methods = ['POST'])
# se tem mais de uma informacao, passar com json
def cotacao():
    dados = request.get_json()
    dados_input =  [dados[col] for col in ['tamanho', 'ano', 'garagem']]
    preco = modelo.predict([dados_input])
    return jsonify(preco=preco[0])
# endregion

# executando a api - restart com as novas alteracoes salvas
app.run(debug=True, host='0.0.0.0')

