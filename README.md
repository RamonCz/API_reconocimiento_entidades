# API_reconocimiento_entidades

Este repositorio solo es para una prueba tecnica 

## Como ejecutar

Instala las dependencia de requirements.txt


Para ejecutar la aplicacion entra en la carpeta /app/


$ python main.py


### en otro casos con make 
solo si tienes intalado make
$ make install_conda

or 

$ make install_env

para correr la app
$ make run-main


## Como utilizar

Entrar a la url http://127.0.0.1:3000/

: Si quieres enviar una sola peticion 


entrar a http://127.0.0.1:3000/receive-list

: Si solo quieres enviar la lista en json y recibir como respuesta como json. Recomiendo usar postman


## Carpetas

app/ contiene toda la aplicacion

  app/modelo/ model.py contiene el modelo de spacy y funciones auxiliares

  app.py  archivo python para lanzar la app

test/ pequeños test para probar el modelo
