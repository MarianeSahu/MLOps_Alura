# bibliotecas
# region
import pandas as pd
from textblob import TextBlob
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

path = 'G:/.shortcut-targets-by-id/120EU9gkG9oO1ilsmtz23VjxiJA4I7ehL/Alura/'
# endregion

# Modelo para analise de sentimentos
# region
frase = 'Python é ótimo para Machine Learning'
tb = TextBlob(frase)
tb_en = tb.translate(to = 'en')
tb_en.sentiment.polarity

# endregion

# Precos de casas
# region
df_dados = pd.read_csv(path + 'Formação ML e Negócios Digitais/casas_precos.csv')
df_dados.head()

# modelagem
X = df_dados.drop(columns='preco')
Y = df_dados.preco
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.7, random_state=42)
X_train.head()

modelo = LinearRegression()
modelo.fit(X_train, Y_train)

# salvando o modelo
file = open(path + 'Formação ML e Negócios Digitais/'+ 'modelo_preco_casas.sav', 'wb')
pickle.dump(modelo, file)
file.close()
# endregion