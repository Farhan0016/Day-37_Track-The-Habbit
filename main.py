import requests
from datetime import datetime

USERNAME = "farhanmalik"
TOKEN = "ifoidkmqd9210kdmiwq@"  # Between 8-128
GROUP_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

# user_params = {
#     'token': TOKEN,
#     'username': USERNAME,
#     'agreeTermsOfService': "yes",
#     'notMinor': "yes"
# }
# # Create the User
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

header = {
    'X-USER-TOKEN': TOKEN
}

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_params = {
#     'id': GROUP_ID,
#     'name': "Farhan's Coding",
#     'unit': "commit",
#     'type': "int",
#     'color': "ajisai",
# }
# # Create a brand-new graph
# response = requests.post(url=graph_endpoint, json=graph_params, headers=header)
# print(response.text)
# response = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/graph1", headers=header)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GROUP_ID}"
today = datetime.today()
pixel_data = {
    'date': today.strftime("%Y%m%d"),
    'quantity': input("How many times you write the code today? "),
}

# # Create the pixel
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=header)
print(response, response.text, sep="-->")


# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GROUP_ID}/{today.strftime('%Y%m%d')}"
# new_pixel_data = {
#     'quantity': "3"
# }
# # Update the Pixel
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=header)
# print(response.text)


# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GROUP_ID}/{today.strftime('%Y%m%d')}"
# # Delete today's pixel
# response = requests.delete(url=delete_endpoint, headers=header)
# print(response.text)
