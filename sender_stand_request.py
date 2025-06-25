import configuration
import requests
import data

#Función de solicitud de creación de usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados
response = post_new_user(data.user_body)
print(response.json())
print(response.status_code)

#Función para recibir el Token generado
def get_new_user_token():
    user_body = data.user_body
    response_user = post_new_user(user_body)
    return response_user.json()["authToken"]
    return auth_token == get_new_user_token()

#Función para crear un kit con el token generado
def post_new_cliente_kit(kit_body, auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             json=kit_body,
                             headers=data.create_kit_header)
    response = post_new_client_kit(data.kit_body, auth_token)
    print(response.json())
    print(response.status_code)
