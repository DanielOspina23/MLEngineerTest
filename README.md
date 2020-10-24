# Taken probabiity

La aplicación permite enviar un array con datos de órdenes y devuelve por cada order_id la probabilidad de que la orden sea tomada.

## Comenzando 🚀

Estas instrucciones permiten obtener una copia del proyecto en funcionamiento de forma local para hacer pruebas.

En la sección **Deployment** se explica cómo desplegar el proyecto.


## Pre-requisitos 📋

Para instalar la API se debe tener instalado lo siguiente:

**Windows**

Descargar e instalar Docker. Para instrucciones de cómo descargarlo ver el siguiente enlace. [Instalar Docker Desktop on Windows](https://docs.docker.com/docker-for-windows/install/)

**Linux**

Correr el siguiente comando para descargar la versión actual de Docker Compose:

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

Luego ejecutar:

```
sudo chmod +x /usr/local/bin/docker-compose
```

## Instalación 🔧

Para tener una versión corriendo de forma local, abrir una terminal y entrar a la carpeta donde está el proyecto.

Ejecutar el siguiente comando:

```
docker-compose build
```

Después de construída la imagen, correr las migraciones para tener una base de datos local donde se guardará la información.

```
docker-compose run web alembic upgrade head
```

Por último, levantar el servidor:

```
docker-compose up
```

Una vez ejecutados estos comandos, el servidor debería estar funcionando de forma local.

## Ejecutando una prueba 🔩

En el siguiente link pueden ver una documentación del petición y de la respuesta de la API. [Documentación de la API](https://app.swaggerhub.com/apis-docs/Prueba77/TakenProbability/1.0.0#/).

Sin embargo, a continuación se muestra un ejemplo de la petición y de la respuesta. 

**Request**
```
[
  {
    "order_id": 0,
    "store_id": 0,
    "to_user_distance": 0,
    "to_user_elevation": 0,
    "total_earning": 0,
    "created_at": "string"
  }
]
```

La lista puede tener las órdenes que uno quiera para consultar la probabilidad de ser tomada.

**Response**

```
{"order_id": taken_probability]
```

La respuesta tiene tantos elementos como órdenes se hayan enviado en la petición.

El siguiente curl puede enviarse desde Postman o cualquier otro método para enviar peticiones.

```
curl --location --request POST 'http://localhost:8080/api/prediction-taken/get_prediction' \
--header 'content-type: application/json' \
--data-raw '[{"order_id":1111, "store_id":1111, "to_user_distance":1.1, "to_user_elevation":1.1, "total_earning":5000, "created_at":"2020-10-23"},
{"order_id":1112, "store_id":1113, "to_user_distance":3.5, "to_user_elevation":1.1, "total_earning":10000, "created_at":"2020-10-23"},
{"order_id":1113, "store_id":2222, "to_user_distance":4.4, "to_user_elevation":6.1, "total_earning":1000, "created_at":"2020-10-25"}]'
```

El servidor debe responder de la siguiente forma:

```
{"1111": 0.9440765380859375, "1112": 0.9328768849372864, "1113": 0.6267786026000977}
```

Para consultar que se hayan agregado los campos a la base de datos, se puede consultar de la siguiente manera:

Primero, con el servicio levantado, en otro terminal ejecutar el siguiente comando:

```
docker ps
```

Copiar el nombre de la imagen de la base de datos y ejecutar el siguiente comando para acceder a la base de datos:

```
docker exec -it nombre_de_la_imagen psql -U postgres
```

Ahora se puede escribir un query para consultar la información:

```
select * from taken_order;
```

## Construído con 🛠️

El proyecto fue construído con las siguientes herramientas.

* Python.
* Docker.

## Autores ✒️

* **Daniel Ospina** - *Trabajo Inicial* 
