import requests
import datetime as dt

USERNAME = "your_username"
TOKEN = "your_token"
GRAPH_ID = "your_graph_id"

CURRENT_DATE = dt.datetime.now().strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

change_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{CURRENT_DATE}"


user_parameters = {
  "token": TOKEN,  
  "username": USERNAME, 
  "agreeTermsOfService":"yes", 
  "notMinor":"yes", 
}

graph_parameters = {
  "id":"id_graph",
  "name":"Name_of_the_graph",
  "unit": "units_graph",
  "type": "float",
  "color": "sora",
}

pixel_parameters = {
  "date": CURRENT_DATE,
  "quantity": "1.30",
}

header = {
  "X-USER-TOKEN": TOKEN
}

#quantity has to be in a string
update_pixel_parameters = {
  "quantity": "3.2", 
}

#create a user account
# response = requests.post(url=pixela_endpoint, json=user_parameters)
#see the response if your account has been create 
# print(response.text)


#create a graph page 
# graph_response = requests.post(url=graph_endpoint, json=graph_parameters, headers=header)
# print(graph_response.text)

#To see your graph page go on : https://pixe.la/v1/users/your_username/graphs/your_graphID.html


#put a pixel on the graph 
# pixel_response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=header)
#see if the pixel has been successfully create
# print(pixel_response.text)


#update a pixel
update_pixel_response = requests.put(url=change_pixel_endpoint, json=update_pixel_parameters, headers=header)
print(update_pixel_response) 



#delete a pixel 
# delete_pixel_response = requests.delete(url=delete_pixel_endpoint, headers=header)
# print(delete_pixel_response)


