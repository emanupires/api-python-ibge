import requests
from pprint import pprint

nome = input("Digite o nome para pesquisa:\n")
url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"

params = {
    "localidade": 33
}

respose = requests.get(url, params=params)

try:
    respose.raise_for_status()
except requests.HTTPError as err:
    print(f"Erro no request: {err}")
    resultado = None
else:
    resultado = respose.json()
    pprint(resultado[0]["res"])