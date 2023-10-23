import configuration
import requests
import data


#Создание пользователя
def post_new_user(user_body):
 return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)


def get_new_user_token():
	response = post_new_user(data.user_body)
	return response.json().get("authToken")

#Создание набора
def post_new_client_kit(kit_body, auth_token):
	headers_with_token = data.headers.copy()
	headers_with_token["Authorization"] = "Bearer " + auth_token
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
						 json=kit_body,
						 headers=headers_with_token)
