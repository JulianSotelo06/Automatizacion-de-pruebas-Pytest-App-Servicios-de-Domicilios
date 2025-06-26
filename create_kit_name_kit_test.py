import sender_stand_request
import data

# Función para cambiar los valores en el parámetro "name" al crear un kit - Corregida
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Función incluida para la obtener el Token generado al crear un nuevo usuario
def get_new_user_token():
    user_body = data.user_body
    response_user = sender_stand_request.post_new_user(user_body)
    return response_user.json()["authToken"]

#Función Prueba Positiva - Corregida
def positive_assert(kit_body):
    user_kit_body_response = sender_stand_request.post_new_cliente_kit(kit_body, get_new_user_token())
    assert user_kit_body_response.status_code == 201

#Función Prueba Negativa - Corregida
def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_cliente_kit(kit_body, get_new_user_token())
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Has introducido un nombre no válido. " \
                                         "La longitud debe ser de 1 a 511 caracteres."

#PRUEBAS LISTA DE COMPROBACIÓN

# PRUEBA No. 1 Corregida: Creación de un kit
# El parámetro "name" contiene un carácter
def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)

# Prueba No. 2 Corregida: El parámetro "name" contiene 511 caracteres
def test_create_kit_511_letter_in_name_get_success_response():
     kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
     positive_assert(kit_body)

#Prueba No. 3 Corregida: Creación de un kit
#El parámetro "name" no contiene caracteres
def test_create_kit_0_letter_in_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

#Prueba No. 4 Corregida: Creación de un kit
#El parámetro "name" contiene 512 caracteres
def test_create_kit_512_letter_in_name_get_error_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body)

#Prueba No. 5 Corregida: Creación de un kit
#El parámetro "name" contiene caracteres especiales
def test_create_kit_special_letter_in_name_get_success_response():
    kit_body = get_kit_body("N%@,")
    positive_assert(kit_body)

#Prueba No. 6 Corregida: Creación de un kit
#El parámetro "name" contiene espacios
def test_create_kit_spaces_in_name_get_success_response():
    kit_body = get_kit_body("A Aaa ")
    positive_assert(kit_body)

#Prueba No. 7 Corregida: Creación de un kit
#El parámetro "name" contiene números
def test_create_kit_numbers_in_name_get_success_response():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

#Prueba No. 8 Corregida: Creación de un kit
#El parámetro "name" se pasa vacío
def test_create_kit_empty_name_get_error_response():
    kit_body = get_kit_body()
    negative_assert_code_400(kit_body)

#Prueba No. 9 Corregida: Creación de un kit
#El parámetro "name" tiene un parámetro diferente (números)
def test_create_kit_parameternumber_in_name_get_error_response():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)