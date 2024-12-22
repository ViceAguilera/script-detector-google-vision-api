import cv2
from google.cloud import vision
import threading
import time
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "" # Path completo del archivo json

# Configuración del cliente de Google Vision
client = vision.ImageAnnotatorClient()
print("Autenticación exitosa. Cliente inicializado.")

# Variable para almacenar resultados recientes
latest_results = []
lock = threading.Lock()  # Controla el acceso a los resultados


def process_frame(frame):
    """Procesa un frame directamente desde la memoria con Google Vision"""
    try:
        # Convierte el frame de OpenCV a bytes
        _, buffer = cv2.imencode('.jpg', frame)
        content = buffer.tobytes()

        # Llama a Google Vision
        image = vision.Image(content=content)
        response = client.object_localization(image=image)

        # Procesa los resultados
        results = [(obj.name, obj.score) for obj in response.localized_object_annotations]

        # Actualiza los resultados más recientes
        with lock:
            latest_results.clear()
            latest_results.extend(results)
    except Exception as e:
        print(f"Error procesando el frame: {e}")


def display_results(frame):
    """Muestra los resultados en el frame"""
    with lock:
        for i, (name, score) in enumerate(latest_results):
            text = f"{name}: {score:.2f}"
            cv2.putText(frame, text, (10, 30 + i * 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)


# Captura de video
cap = cv2.VideoCapture(0)
frame_count = 0
start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    # Enviar un frame cada N frames para análisis
    if frame_count % 10 == 0:  # Ajusta según la frecuencia deseada
        threading.Thread(target=process_frame, args=(frame.copy(),)).start()

    # Mostrar resultados en el frame actual
    display_results(frame)
    cv2.imshow("Video en vivo con detección", frame)

    # Presiona 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Limpieza
cap.release()
cv2.destroyAllWindows()
end_time = time.time()

# Estadísticas
print(f"Procesados {frame_count} frames en {end_time - start_time:.2f} segundos.")
