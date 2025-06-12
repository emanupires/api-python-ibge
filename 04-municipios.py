import requests
from pprint import pprint

url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

params = {
    "view": "nivelado"
}

respose = requests.get(url, params=params)

try:
    respose.raise_for_status()
except requests.HTTPError as err:
    print(f"Erro no request: {err}")
    resultado = None
else:
    resultado = respose.json()
    pprint(resultado)