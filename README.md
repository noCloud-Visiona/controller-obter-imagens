# Buscador de Imagens CBERS4A

## Pré-requisitos

- Python 3.6+
- `pip` para gerenciar pacotes

## Criação do Ambiente Virtual

```sh
python -m venv venv


pip install -r requirements.txt

python app.py
```

# Fazer uma Requisição à API
# Endpoint /receber_coordenadas
# URL: http://localhost:3003/receber_coordenadas

# Método: POST

# Exemplo:
```sh
{
    "lat1": -23.2237,
    "lon1": -45.9254,
    "lat2": -23.1896,
    "lon2": -45.8362,
    "data_inicio": "2024-04-01",
    "data_fim": "2024-08-30"
}
```
