from flask import Flask, request, jsonify
from datetime import date
import json
from buscador import BuscadorDeImagensCBERS4A

app = Flask(__name__)

fetcher = BuscadorDeImagensCBERS4A()

@app.route('/receber_coordenadas', methods=['POST'])
def receber_coordenadas():
    data = request.get_json()

    required_fields = ['lat1', 'lon1', 'lat2', 'lon2', 'data_inicio', 'data_fim']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Campo obrigatório ausente: {field}'}), 400

    lat1 = data['lat1']
    lon1 = data['lon1']
    lat2 = data['lat2']
    lon2 = data['lon2']

    coordenadas = (lat1, lon1, lat2, lon2)

    try:
        data_inicio = date.fromisoformat(data['data_inicio'])
        data_fim = date.fromisoformat(data['data_fim'])
    except ValueError:
        return jsonify({'error': 'Formato de data inválido. Use yyyy-mm-dd.'}), 400

    imagem_path = None

    try:
        imagem_path = fetcher.buscar_imagem_por_coordenadas(coordenadas, data_inicio, data_fim)
        return jsonify({
            'message': 'Coordenadas recebidas com sucesso',
            'imagem_path': imagem_path,
            'coordenadas': {
                'lat1': lat1, 'lon1': lon1,
                'lat2': lat2, 'lon2': lon2
            }
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3003)