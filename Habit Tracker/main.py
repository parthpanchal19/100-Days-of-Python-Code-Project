import requests
from datetime import *


USERNAME = "XXXXXX"
TOKEN = "XXXXXX"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":GRAPH_ID,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixela_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixela_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How Many Kilometers You Cycle Today?"),
}

response = requests.post(url=pixela_create_endpoint,json=pixela_data,headers=headers)
print(response.text)

update_pixela_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_data = {
    "quantity":"10.50",
}

delete_pixela_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
