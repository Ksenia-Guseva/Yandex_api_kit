import configuration
import requests
import data


#Создание пользователя
def post_new_user(user_body):
 return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)

response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())
auth_token = response.json().get("authToken")
def get_new_user_token():
	response = post_new_user(data.user_body)
	return response.json().get("authToken")

#Создание набора
def post_new_client_kit(kit_body, auth_token):
	data.headers["Authorization"] += auth_token
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
						 json=kit_body,
						 headers=data.headers)
response = post_new_client_kit(data.kit_body, auth_token)
print(f"newClientKitStatus: {response.status_code}")
print(response.json())