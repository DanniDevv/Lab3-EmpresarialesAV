# TiemposListas
Creamos una api con Python y la publicamos con Flask, recibimos con PHP y medimos el tiempo de recuperación de datos

Modo de Uso Recomendado

1 - Clonamos el repositorio

    git clone https://github.com/cesarbobadilla/TiemposListas
    
2 - Ingresamos a la carpeta TiemposListas

    Validamos con 'dir' o 'ls' el contenido del repositorio. Debería estar:
    
    Dockerfile        README.md         linkextractor.py  main.py           requirements.txt
    
3 - Creamos la imagen de docker

    docker image build -t gifextractor:lista .
    
4 - Ejecutamos la imagen 

    docker container run -d -p 5000:5000 --name=gifextractor gifextractor:lista
    
5 - Accedemos al dominio pertinente a través del puerto 5000, en la ruta 'api', y luego especificamos el índice de la imagen que queramos mostrar.

    Ejemplo:
    
    localhost:5000/api/3
    
    Si estamos en labs de play-with-docker.com, algo como:
    
    http://ip172-18-0-87-chjaaaqe69v000am7cg0-5000.direct.labs.play-with-docker.com/api/3

    La respuesta debe ser parecida a:
    
    // 20230518175024
    // http://ip172-18-0-87-chjaaaqe69v000am7cg0-5000.direct.labs.play-with-docker.com/api/3

    [
      {
        "href": "https://media.tenor.com/-JhgP2FK1O8AAAAD/excited.png",
        "text": "26136233"
      }
    ]    
    
6 - Una vez que validamos que esta funcionando correctamente, en replit, en otro contenedor, en su local host o donde uste desee, ejecute un apache para correr el archivo   php e ingresa al final del dominio ?url=3, si esta en su localhost sería algo como http://localhost/?url=3 y debería ver la imagen que generó su búsqueda.

![Captura de pantalla 2023-05-18 a la(s) 18 46 59](https://github.com/cesarbobadilla/TiemposListas/assets/35129284/49113000-12eb-4db2-96db-33d107afc098)


7 - Después de validar que estamos consumiendo correctamente la api de Python con PHP, procedemos a medir el tiempo de consumo, en el ejemplo adjunto, busco la referencia    43 es decir ?url=43, si deseo otra referencia, podría ser 55, 700, etc. de ese modo ?url=55, ?url=700 y asi. El siguiente comando almacena el resultado en un archivo demol.txt, para posteriormente hacer una comparación de tiempo con el que se genero con el de listas enlazadas, explicado aquí https://github.com/cesarbobadilla/TiemposListasEnlazadas .

    curl -s -w %{time_total}\\n -o /dev/null "http://localhost/?url=43" >> demol.txt
