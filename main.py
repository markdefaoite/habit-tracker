import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "markdefaoite"
TOKEN = "mnbv96385yrtew145nbvc"



user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Study Graph",
    "unit": "Hours",
    "type": "float",
    "color": "shibafu",

}

headers = {
    "X-USER-TOKEN": TOKEN
}

# https://pixe.la/v1/users/markdefaoite/graphs/graph1.html
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

