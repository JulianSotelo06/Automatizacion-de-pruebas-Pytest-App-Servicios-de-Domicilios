# PROYECTO SPRINT 7 - JULIÁN SOTELO - GRUPO 36
# AUTOMATIZACIÓN PRUEBAS LISTA DE COMPROBACIÓN CREACIÓN DE UN KIT EN APP URBAN GROCERS
 
# 📚Requisitos iniciales:

- Tener instalados los paquetes pytest y request para ejecutar las pruebas. ✅
- Ejecutar todas las pruebas con el comando pytest. ✅

# 📃 Creación de archivos:

🔵 "_configuration.py_"; en este archivo se almacenan las URL para interactuar con la API:

1. URL_SERVICE: se copia el link de pruebas del servidor entre "" y sin la / del final.
2. CREATE_USER_PATH: almacena la ruta para crear un usuario en esta variable.
3. KITS_PATH: almacena la ruta para crear un kit en esta variable.

🟢 "_data.py_"; en este archivo se almacenan las estructuras de encabezados y cuerpos para la creación de usuarios y kits:

1. "headers" y "user_body", para la creación de usuarios.
2. "create_kit_header" y "kit_body", para la creación de kits.

🔴 "_sender_stand_request.py_"; en este archivo se almacena la siguiente función:

⚠️ Se deben importar al archivo: configuration, data y requests

1. _def post_new_user(body):_ función para crear un nuevo usuario.
2. _def post_new_cliente_kit(kit_body)_ función para crear un kit.

🟡 "_create_kit_name_test.py_"; en este archivo se ejecutaran las pruebas de la lista de comprobación.

# 📝 Ejecución de pruebas:

En el archivo "_create_kit_name_test.py_", se escriben las siguientes funciones:

1. _def get_kit_body(name):_ función para cambiar los valores "name" al crear un kit.
2. _def get_new_user_token():_ función para recibir el token generado al crear el cliente.
3. _def positive_assert(kit_body):_ función para una prueba con resultado positivo.
4. _def negative_assert_code_400(kit_body):_ función para una prueba con resultado negativo.

Después de declarar las funciones anteriores, se diseñan las pruebas para cada ítem de la lista de comprobación, cambiando unicamente el valor de "name".

En el archivo "_create_kit_name_test.py_"❗ se encuentran las funciones ejecutadas para cada ítem de la lista. 




