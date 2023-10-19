import sender_stand_request
import data

letters511 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
letters512 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
n = 0
def get_kit_body(name):
	current_kit_body = data.kit_body.copy()
	current_kit_body["name"] = name
	return current_kit_body

def positive_assert(name):
	kit_body = get_kit_body(name)
	kit_response = sender_stand_request.post_new_client_kit(kit_body, sender_stand_request.auth_token)
	assert kit_response.json()["name"] == name
	print(f"\nameNewKit: {name}")
	assert kit_response.status_code == 201

def negative_assert(name):
	kit_body = get_kit_body(name)
	response = sender_stand_request.post_new_client_kit(kit_body, sender_stand_request.auth_token)
	assert response.status_code == 400
	assert response.json()["code"] == 400
	assert response.json()["message"] == "Не все необходимые параметры были переданы"

#Функция для позитивной проверки Количество символов (1)
def test_create_kit_1_symbol_in_name_get_success_response():
	positive_assert("a")

# Функция для позитивной проверки Количество символов (511)
def test_create_kit_511_letters_in_name_get_success_response():
	positive_assert(letters511)

# Функция для негативной проверки Количество символов (0)
def test_create_kit_empty_name_get_error_response():
    negative_assert("")
# Функция для негативной проверки Количество символов (512)
def test_create_kit_512_letters_in_name_get_success_response():
	positive_assert(letters512)
# Функция для позитивной проверки Английские буквы
def test_create_kit_english_letters_in_name_get_success_response():
	positive_assert("QWErty")
# Функция для позитивной проверки Русские буквы
def test_create_kit_russian_letters_in_name_get_success_response():
	positive_assert("Мария")
# Функция для позитивной проверки Спецсимволы
def test_create_kit_has_special_symbols_in_name_get_success_response():
	positive_assert("\"№%@\",")
# Функция для позитивной проверки Пробелы
def test_create_kit_has_space_in_name_get_success_response():
	positive_assert("Человек и КО")

# Функция для позитивной проверки Цифры
def test_create_kit_has_number_in_name_get_success_response():
	positive_assert("123")
# Функция для негативной проверки Пааметр не передан
def test_create_kit_no_name_get_error_response():
	current_kit_body_negative_no_name = data.kit_body.copy()
	current_kit_body_negative_no_name.pop("name")
	negative_assert(current_kit_body_negative_no_name)
# Функция для негативной проверки Передан другой тип параметра
def test_create_kit_has_number_in_name_get_error_response():
    negative_assert("123")