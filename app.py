# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

dados_armazenados = {"name":"Rohling"}

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        dados = request.get_json()
        dados_armazenados.update(dados)
        return jsonify(dados), 201
    elif request.method == 'GET':
        return jsonify(dados_armazenados), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
