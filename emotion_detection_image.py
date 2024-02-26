import cv2
from deepface import DeepFace

def analyze_emotion_from_file(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print("Could not read the image.")
        return

    try:
        result = DeepFace.analyze(img, actions=['emotion'])
        emotion = result['dominant_emotion']
        print(f"Detected emotion: {emotion}")
    except Exception as e:
        print(f"An error occurred: {e}")
