import requests

# url = "https://httpbin.org/get"
url = "https://httpbin.org/post"
data = {
    "pessoa":{
        "nome": "Manu",
        "profissao": "Implantação"
    }
}

params = {
    "dataIni": "2025-01-01",
    "dataFim": '2025-12-31'
}

# response = requests.post(url)
response = requests.post(url, json=data, params=params)
print(response.request)
print(response.text)