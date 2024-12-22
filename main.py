import os
import cv2
import threading
import time
from google.cloud import vision

# Environment variable configuration for credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
    "C:/Users/vicen/OneDrive/Escritorio/AlarApps/demo-detector-epp/credentials/diesel-charge-440421-a2-04bb46321270.json"
) # Full path of the json file

if not os.path.exists(os.environ["GOOGLE_APPLICATION_CREDENTIALS"]):
    raise Exception("Google Cloud credentials file not found.")

# Google Vision client configuration
client = vision.ImageAnnotatorClient()
if client is None:
    raise Exception("Error initializing Google Vision client.")

print("Authentication successful. Client initialized.")

# Variable to store recent results
latest_results = []
lock = threading.Lock()  # Controls access to results

def process_frame(frame):
    """Processes a frame directly from memory using Google Vision."""
    try:
        # Convert the OpenCV frame to bytes
        _, buffer = cv2.imencode('.jpg', frame)
        content = buffer.tobytes()

        # Call Google Vision
        image = vision.Image(content=content)
        response = client.object_localization(image=image)

        # Process results
        results = [(obj.name, obj.score) for obj in response.localized_object_annotations]

        # Update the most recent results
        with lock:
            latest_results.clear()
            latest_results.extend(results)
    except Exception as e:
        print(f"Error processing frame: {e}")


def display_results(frame):
    """Displays the results on the frame."""
    with lock:
        for i, (name, score) in enumerate(latest_results):
            text = f"{name}: {score:.2f}"
            cv2.putText(frame, text, (10, 30 + i * 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)


# Video capture
cap = cv2.VideoCapture(0)
frame_count = 0
start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    # Send one frame every N frames for analysis
    if frame_count % 10 == 0:  # Adjust as per desired frequency
        threading.Thread(target=process_frame, args=(frame.copy(),)).start()

    # Display results on the current frame
    display_results(frame)
    cv2.imshow("Live Video with Detection", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
end_time = time.time()

# Statistics
print(f"Processed {frame_count} frames in {end_time - start_time:.2f} seconds.")
