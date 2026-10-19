# Detector de objetos en tiempo real con Google Cloud Vision

Script en Python que captura video desde una cámara, envía cuadros a la API Google Cloud Vision y muestra sobre el video los objetos detectados.

![Python](https://img.shields.io/badge/Python-3.9-3776AB?style=flat&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white)
![Google Cloud Vision](https://img.shields.io/badge/Google%20Cloud-Vision%20API-4285F4?style=flat&logo=googlecloud&logoColor=white)
![Estado](https://img.shields.io/badge/estado-terminado-blue?style=flat)
![Licencia](https://img.shields.io/badge/licencia-Apache--2.0-blue?style=flat)
![Último commit](https://img.shields.io/github/last-commit/ViceAguilera/script-detector-google-vision-api?style=flat)

<!-- Demo: agrega una captura o GIF en docs/demo.gif y descomenta la línea siguiente -->
<!-- <p align="center"><img src="docs/demo.gif" alt="Demostración del detector con Google Cloud Vision" width="800"></p> -->

## Tabla de contenidos

- [Descripción](#descripción)
- [Estado del proyecto](#estado-del-proyecto)
- [Características](#características)
- [Tecnologías](#tecnologías)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Licencia](#licencia)
- [Autores](#autores)

## Descripción

El script abre la cámara con OpenCV y, cada 10 cuadros, envía una imagen en un hilo aparte al servicio de localización de objetos de Google Cloud Vision. Los nombres y puntuaciones de confianza más recientes se dibujan sobre el video en vivo, de modo que la interfaz no se bloquea mientras se espera la respuesta de la API.

## Estado del proyecto

**Terminado.** Script completo y funcional que no recibe mantenimiento activo.

## Características

- Captura de video en vivo desde la cámara por defecto (índice 0).
- Detección de objetos con `object_localization` de Google Cloud Vision.
- Procesamiento en hilos con acceso sincronizado a los resultados.
- Superposición de la etiqueta y la puntuación de cada objeto sobre el video.
- Al cerrar con `q`, muestra el total de cuadros procesados y el tiempo.

## Tecnologías

- Python 3.9
- [OpenCV](https://opencv.org/) 4.10.0.84
- [Google Cloud Vision](https://cloud.google.com/vision/docs) (`google-cloud-vision` 3.9.0)
- NumPy y `threading` de la biblioteca estándar

## Requisitos

- Python 3.9
- Una cámara disponible en el equipo
- Cuenta de Google Cloud con la API de Vision habilitada ([guía](https://cloud.google.com/vision/docs/quickstart-client-libraries)) y una clave de cuenta de servicio en formato JSON. El uso de la API puede generar costos según tu plan de Google Cloud.

## Instalación

```bash
git clone https://github.com/ViceAguilera/script-detector-google-vision-api.git
cd script-detector-google-vision-api
python -m venv venv
./venv/Scripts/activate        # En Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
```

### Credenciales de Google Cloud

La carpeta `credentials/` está vacía en el repositorio (solo contiene `.gitkeep`) y las credenciales no se incluyen.

1. Descarga la clave JSON de tu cuenta de servicio desde Google Cloud y guárdala en `credentials/`.
2. En `main.py`, reemplaza la ruta asignada a `GOOGLE_APPLICATION_CREDENTIALS` (líneas 8 a 10) por la ruta completa de tu archivo JSON.

Importante: la clave da acceso a tu proyecto de Google Cloud y no debe subirse al repositorio. El `.gitignore` excluye `credentials/*.json`; aun así, verifica con `git status` antes de hacer commit.

## Uso

```bash
python main.py
```

Presiona `q` en la ventana de video para salir.

## Estructura del proyecto

```
main.py            # Captura de video, llamadas a Vision y visualización
requirements.txt   # Dependencias con versiones fijadas
credentials/       # Aquí va tu clave JSON de Google Cloud (no se versiona)
```

## Licencia

Distribuido bajo la licencia Apache 2.0. Ver [LICENSE](LICENSE).

## Autores

**Vicente Aguilera Arias** — [Portafolio](https://portfolio.iamsirius.cl) · [GitHub](https://github.com/ViceAguilera) · [LinkedIn](https://www.linkedin.com/in/vicenteaguilera/)

Colaborador: [Camilo Sáez Garrido](https://github.com/camjasaez)
