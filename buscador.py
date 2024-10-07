from cbers4asat import Cbers4aAPI
from datetime import date
import requests

class BuscadorDeImagensCBERS4A:
    def __init__(self):
        self.email = 'jonasraf97@gmail.com'
        self.api = Cbers4aAPI(self.email)

    def buscar_imagem_por_coordenadas(self, coordenadas, data_inicio, data_fim, max_nuvens=100, limite=10):
        lat1, lon1, lat2, lon2 = coordenadas
        bounding_box = [lon1, lat1, lon2, lat2]

        try:
            lista_imagens = self.api.query(
                location=bounding_box,
                initial_date=data_inicio,
                end_date=data_fim,
                cloud=max_nuvens,
                limit=limite,
                collections=['CBERS4A_WPM_L2_DN']
            )

            if not lista_imagens or len(lista_imagens['features']) == 0:
                raise Exception("Nenhuma imagem encontrada para as coordenadas e datas fornecidas.")

            imagem = lista_imagens['features'][0]

            assets = imagem.get('assets', {})
            if 'nir' not in assets:
                raise Exception("Banda 'nir' não encontrada nos assets da imagem.")

            nir_asset = assets['nir']
            if 'eo:bands' in nir_asset and 4 in nir_asset['eo:bands']:
                tiff_url = nir_asset.get('href')
            else:
                raise Exception("Banda NIR não corresponde a 'eo:bands': [4].")

            if not tiff_url:
                raise Exception("Link de download não encontrado na resposta da API.")

            url_para_salvar = tiff_url + "?email=" + self.email

            return url_para_salvar

        except Exception as e:
            print(f"Erro ao buscar imagem: {e}")
            raise e
