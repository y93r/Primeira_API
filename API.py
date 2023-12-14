import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

#Construir as funcionalidades
@app.route('/')
def homepage():
	arquivo = r'C:\Users\Usuário\Documents\Cursos\HashtagTreinamentos\Python_Impressionador\22-Integração Python com APIs e JSON\API\.venv\Criando API no Python.csv'
	tabela = pd.read_csv(arquivo)
	totais_colunas = tabela.sum().round(2).to_dict() #Calcula o total de cada coluna
	return jsonify(totais_colunas)

#Roda a API
app.run(debug=True)