# Script detector Google Vision API

_Este repositorio contiene un script diseñado para detectar objetos en tiempo real utilizando la API de Google Vision. El sistema está optimizado para analizar imágenes capturadas desde una cámara en vivo y mostrar resultados sobre el video en tiempo real, proporcionando un flujo eficiente y rápido para tareas de detección visual._

- [Python v3.9](https://www.python.org/downloads/release/python-390/): Lenguaje principal para el desarrollo del script.
- [OpenCV](https://opencv.org/): Biblioteca utilizada para capturar y procesar video en tiempo real.
- [Google Cloud Vision API](https://cloud.google.com/vision/docs?hl=es-419): Servicio de Google utilizado para el análisis de imágenes y detección de objetos.
- [Threading](https://docs.python.org/3/library/threading.html): Manejo de hilos para garantizar un procesamiento eficiente y sin interrupciones.
- [NumPy](https://numpy.org/): Utilizado para manejar datos de imágenes durante la conversión y procesamiento.

## Instalación 🔧
<details>
  <summary>Windows</summary>

1. Se clona el repositorio de GitHub
    ```bash
    git clone https://github.com/ViceAguilera/script-detector-google-vision-api.git
    ```
  
2. Se ingresa a la carpeta del proyecto
    ```bash
    cd script-detector-google-vision-api
    ```
  
3. Se crea un entorno virtual
    ```bash
    python -m venv venv
    ```
    
4. Se activa el entorno virtual
    ```bash
    ./venv/Scripts/activate
    ```
   
5. Se instala los requerimientos del proyecto
    ```bash
    pip install -r requirements.txt
    ```

8. Para el uso de la API de Google Vision se debe tener una cuenta de Google Cloud y se debe habilitar la API de Vision. [Guía](https://cloud.google.com/vision/docs/quickstart-client-libraries?hl)

9. Debes agregar a la Carpeta `credentials` el archivo `credentials.json` que se descarga al habilitar la API de Google Vision.

12. Con la API configurada, se puede ejecutar el script.
    ```bash
    python main.py
    ```
</details>

## Licencia 📄

Este proyecto está bajo el _Apache License 2.0_ - mira el archivo [LICENSE](LICENSE) para detalles

## Autores ✒️

[**Camilo Sáez Garrido**](https://github.com/camjasaez) & [**Vicente Aguilera Arias**](https://github.com/ViceAguilera)