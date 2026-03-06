import requests
import datetime as dt
# so far we have been using the GET request to get data via API
# requests.get()

# HTTP POST REQUESTS
# we give the external service some data e.g. saving data to google sheets 
# requests.post()

# HTTP PUT REQUESTS
# update a piece of data in the external service

# HTTP DELETE REQUESTS
# delete the data in an external service

USERNAME = "daysofcodeproject1"
TOKEN = "fjjfdjfksjdkjlajdskfal"
GRAPHID = "graph1"

# Create an Account

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

# Create a Graph 
graph_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs"
graph_config = {
    "id": GRAPHID,
    "name": "Youtube Graph",
    "unit": "video",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# access the graph: https://pixe.la/v1/users/daysofcodeproject1/graphs/graph1.html

today = dt.datetime.now()
pixel_creation_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5"
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# Updating the graph - use a PUT request

update_graph = {
    "color": "momiji",
    "description" : "this is a test to update the graph color"
}

response = requests.put(url=pixel_creation_endpoint, json=update_graph, headers=headers)
print(response.text)

# Update a pixel or add a pixel if it does not exist - use a PUT request
update_pixel_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}/{today.strftime('%Y%m%d')}"
new_pixel_data = {"quantity": "7"}
response = requests.put(url=update_pixel_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

# Deleting a pixel - use a DELETE request
delete_pixel_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)