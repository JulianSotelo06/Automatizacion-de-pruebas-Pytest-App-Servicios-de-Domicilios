import sender_stand_request
import data

#Función para cambiar los valores en el parámetro "name" al crear un kit
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

#Función Prueba Positiva
def positive_assert(kit_body):
    user_kit_body = get_kit_body(name)
    user_kit_body_response = sender_stand_request.post_new_cliente_kit(user_kit_body)
    assert user_kit_body_response.status_code == 201

#Función Prueba Negativa
def negative_assert_code_400(kit_body):
    user_kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_cliente_kit(user_kit_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Has introducido un nombre no válido. " \
                                         "La longitud debe ser de 1 a 511 caracteres."
#PRUEBAS LISTA DE COMPROBACIÓN

# PRUEBA No. 1: Creación de un kit
# El parámetro "name" contiene un carácter
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

#Prueba No. 2: Creación de un kit
# El parámetro "name" contiene 511 caracteres
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#Prueba No. 3: Creación de un kit
#El parámetro "name" no contiene caracteres
def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_code_400("")

#Prueba No. 4: Creación de un kit
#El parámetro "name" contiene 512 caracteres
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Prueba No. 5: Creación de un kit
#El parámetro "name" contiene caracteres especiales
def test_create_kit_special_letter_in_name_get_success_response():
    positive_assert("N%@,")

#Prueba No. 6: Creación de un kit
#El parámetro "name" contiene espacios
def test_create_kit_spaces_in_name_get_success_response():
    positive_assert("A Aaa ")

#Prueba No. 7: Creación de un kit
#El parámetro "name" contiene números
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert("123")

#Prueba No. 8: Creación de un kit
#El parámetro "name" se pasa vacío
def test_create_kit_empty_name_get_error_response():
    negative_assert_code_400()

#Prueba No. 9: Creación de un kit
#El parámetro "name" tiene un parámetro diferente (números)
def test_create_kit_parameternumber_in_name_get_error_response():
    negative_assert_code_400(123)