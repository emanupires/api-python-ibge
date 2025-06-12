import requests
import pandas as pd
import streamlit as st

def obter_request(url, params=None):
    try:
        respose = requests.get(url, params=params)
        respose.raise_for_status()
        return respose.json()
    except requests.HTTPError as e:
        print(f"Erro no request: {e}")
        return None
    
def frequencia_nome(nome):
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
    dados_nome = obter_request(url) or []
 #   return {     dados["periodo"]:dados["frequencia"] for dados in dados_nome[0].get("res", [])}
    dados_dict = {dados["periodo"]:dados["frequencia"] for dados in dados_nome[0].get("res", [])}
    df = pd.DataFrame.from_dict(dados_dict, orient="index")
    return df

def main():
    st.title("Web App API")
    st.header("Dados da API IBGE)")
    input_nome = st.text_input("Digite um nome: ")
    if not input_nome:
        st.stop()
    df = frequencia_nome(input_nome)
    col1, col2 = st.columns([0.2, 0.7])
    with col1:
        st.write("Frequência por década")
        st.dataframe(df)
    with col2:
        st.write("Série temporal")
        st.line_chart(df)
   # print(frequencia_nome(input_nome))

if __name__ == "__main__":
    main()