import requests
from datetime import datetime

USERNAME = "mrcnbsb79"
TOKEN = "kkddkksskksskkss"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# criar usuário
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":GRAPH_ID,
    "name":"Reading Graph",
    "unit":"page",
    "type":"int",
    "color":"shibafu",
}

headers = {
    "X-USER-TOKEN":TOKEN,
}

# # criar gráfico
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many pages did you read today? "),
}

# criar pixel
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

pixel_update_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

pixel_update_data = {
    "quantity":"7",
}

# atualizar pixel
# response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print(response.text)

pixel_delete_endpoint = pixel_update_endpoint

# deletar pixel
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
