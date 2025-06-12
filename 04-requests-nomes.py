import requests
from pprint import pprint

def obter_request(url, params=None):
    try:
        respose = requests.get(url, params=params)
        respose.raise_for_status()
        return respose.json()
    except requests.HTTPError as e:
        print(f"Erro no request: {e}")
        return None
    
def busca_id_estado():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    dados_estados = obter_request(url, params={"view": "nivelado"}) or []
    return {
      estado["UF-id"]: estado["UF-nome"] for estado in dados_estados
    }

def frequencia_nome(nome):
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
    dados_frequencia = obter_request(url, params={"groupBy":"UF"}) or []
    return { 
        int(dado["localidade"]): dado["res"][0]["proporcao"] for dado in dados_frequencia 
    }

def main(nome):
    dict_estados = busca_id_estado()
    dict_frequencia = frequencia_nome(nome)
    print(f"=== Frequência do nome {nome} dos estados (por 100.000 habitantes===)")
    for id_estado, frequencia in sorted(dict_frequencia.items(),
                                        key=lambda item: item[1],
                                        reverse=True):
        print(f"-> {dict_estados.get(id_estado, 'Desconhecido')}: {frequencia}")

if __name__ == "__main__":
    main("Guilherme")