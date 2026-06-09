Parte 4: Explicación técnica
Descripción general de la API elegida

La API principal utilizada fue PokéAPI, una API pública REST que proporciona información relacionada con el universo Pokémon.
Esta API permite consultar datos sobre pokémones, habilidades, estadísticas, movimientos, evoluciones y tipos mediante endpoints accesibles por HTTP.

Además, para probar métodos como POST y DELETE, se utilizó JSONPlaceholder, una API de pruebas diseñada para simular operaciones CRUD (Create, Read, Update y Delete) sin afectar datos reales.

Las APIs REST funcionan mediante el intercambio de información entre un cliente y un servidor utilizando solicitudes HTTP y respuestas estructuradas generalmente en formato JSON.

Solicitud 1 — GET
Método HTTP utilizado

GET

Endpoint utilizado
{{base_url}}/pokemon/pikachu
Objetivo de la solicitud

La solicitud GET se utilizó para obtener información específica sobre el pokémon Pikachu.

El método GET sirve para consultar información almacenada en un servidor sin modificarla.

Cómo funciona internamente
El cliente (Postman) envía una solicitud HTTP GET al servidor de PokéAPI.
El servidor recibe el request y busca la información solicitada en su base de datos.
El servidor procesa la consulta.
El servidor devuelve una response en formato JSON.
Postman interpreta y muestra la información recibida.
Parámetros utilizados

No se enviaron parámetros adicionales ni body porque la información ya se identifica directamente mediante el endpoint /pokemon/pikachu.

Código de estado recibido
200 OK

Este código indica que la solicitud fue exitosa y que el servidor encontró correctamente el recurso solicitado.

Headers relevantes observados
Content-Type: application/json
Content-Length: 12345
Explicación
Content-Type
Indica el formato de la respuesta enviada por el servidor.
En este caso es JSON.
Content-Length
Indica el tamaño de la respuesta enviada.
Fragmento de respuesta JSON
{
  "name": "pikachu",
  "height": 4,
  "weight": 60,
  "base_experience": 112
}
Análisis de la respuesta

La respuesta contiene atributos del pokémon solicitado.
El servidor devuelve la información estructurada en pares clave-valor utilizando JSON.

Por ejemplo:

"name" representa el nombre.
"height" representa la altura.
"weight" representa el peso.

Esto demuestra cómo las APIs REST entregan información organizada para que aplicaciones frontend puedan utilizarla fácilmente.

Solicitud 2 — POST
Método HTTP utilizado

POST

Endpoint utilizado
https://jsonplaceholder.typicode.com/posts
Objetivo de la solicitud

La solicitud POST se utilizó para enviar información al servidor y simular la creación de un nuevo recurso.

El método POST se utiliza normalmente para:

registrar usuarios,
crear reservas,
guardar formularios,
insertar información en bases de datos.
Body enviado en la solicitud
{
  "title": "Nueva reserva",
  "body": "Reserva creada desde Postman",
  "userId": 1
}
Cómo funciona internamente
El cliente crea un body con información en formato JSON.
Postman envía un request HTTP POST al servidor.
El servidor recibe y valida los datos.
El servidor simula guardar la información en la base de datos.
El servidor devuelve una respuesta confirmando la creación del recurso.
Código de estado recibido
201 Created

Este código indica que el recurso fue creado correctamente.

Headers relevantes observados
Content-Type: application/json
Fragmento de respuesta JSON
{
  "id": 101,
  "title": "Nueva reserva",
  "body": "Reserva creada desde Postman",
  "userId": 1
}
Análisis de la respuesta

El servidor devuelve los mismos datos enviados y agrega un identificador (id) para representar el nuevo recurso creado.

Esto simula el comportamiento típico de un backend conectado a una base de datos.

En una aplicación real de reservas en línea, esta operación podría guardar:

nombre del cliente,
fecha de reserva,
horario,
número de confirmación.
Solicitud 3 — DELETE
Método HTTP utilizado

DELETE

Endpoint utilizado
https://jsonplaceholder.typicode.com/posts/1
Objetivo de la solicitud

La solicitud DELETE se utilizó para eliminar un recurso existente.

Este método se usa comúnmente para:

cancelar reservas,
eliminar usuarios,
borrar registros,
eliminar productos.
Cómo funciona internamente
El cliente envía una solicitud DELETE indicando el ID del recurso.
El servidor busca ese recurso.
El servidor elimina la información de la base de datos.
El servidor devuelve una respuesta indicando éxito.
Código de estado recibido
200 OK
Fragmento de respuesta JSON
{}
Análisis de la respuesta

El objeto vacío indica que la operación fue procesada correctamente.

Aunque JSONPlaceholder no elimina datos reales, simula perfectamente el comportamiento de una API REST real.

Comunicación entre cliente y servidor

Durante todas las pruebas se observó el modelo request/response.

Las APIs normalmente funcionan como intermediarias entre el frontend y la base de datos.

Por ejemplo:

Una solicitud GET puede consultar información almacenada.
Una solicitud POST puede insertar nuevos registros.
Una solicitud DELETE puede eliminar datos.

Las bases de datos utilizadas comúnmente en APIs modernas incluyen:

MySQL
PostgreSQL
MongoDB
SQL Server

El backend procesa las solicitudes y ejecuta operaciones sobre la base de datos antes de responder al cliente.

Importancia de HTTP y HTTPS

Las solicitudes realizadas utilizaron HTTP/HTTPS.

HTTP

Permite la comunicación entre cliente y servidor.

HTTPS

Es una versión segura de HTTP que cifra la información transmitida.

HTTPS es fundamental en aplicaciones modernas porque protege:

contraseñas,
tokens,
información personal,
pagos y reservas.
Qué aprendí técnicamente

Durante el ejercicio comprendí cómo:

* una API expone endpoints,
* el cliente realiza requests,
* el servidor procesa información,
* se utilizan distintos métodos HTTP,
* las respuestas JSON transportan datos estructurados,
* los códigos de estado indican el resultado de la operación,
* cómo Postman facilita el análisis completo de la comunicación cliente-servidor.

Parte 5: Reflexión final

Aprendí que las APIs permiten conectar aplicaciones y compartir información de manera estructurada mediante requests y responses. También entendí cómo los métodos HTTP definen la acción que se desea realizar sobre un recurso.

Postman me ayudó a visualizar claramente la comunicación entre cliente y servidor, permitiéndome probar endpoints, revisar respuestas JSON, analizar headers y comprender mejor el funcionamiento interno de una API REST.