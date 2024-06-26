import requests
from datetime import datetime

"""
This excercise comes from the course on udemy "100 days of code: the Complete Python Pro Bootcamp" 
This is not so much a project as it is an exercise in using the requests module
"""

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "markdefaoite"
TOKEN = "mnbv96385yrtew145nbvc"
GRAPHID = "graph1"


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
    "id": GRAPHID,
    "name": "Study Graph",
    "unit": "Hours",
    "type": "float",
    "color": "shibafu",

}

headers = {
    "X-USER-TOKEN": TOKEN
}

# https://pixe.la/v1/users/markdefaoite/graphs/graph1.html
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

today = datetime.now()
# today.strftime("%Y%m%d")
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "4.5",
}

# response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

# Edit yesterday's entry

yesterday = datetime(year=2024, month=6, day=25)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{yesterday.strftime("%Y%m%d")}"

put_pixel_config = {
    "quantity": "2.5"
}

# response = requests.put(url=update_pixel_endpoint, json=put_pixel_config, headers=headers)
# print(response.text)


# Delete yesterday's entry

# response = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(response.text)