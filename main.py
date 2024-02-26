import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace

def capture_image_from_camera():
    # Initialize the camera
    cap = cv2.VideoCapture(0) # '0' is usually the default value for the primary camera

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Could not open webcam")
        return None

    # Capture a single frame
    ret, frame = cap.read()

    # Release the camera
    cap.release()

    # Check if the frame is captured successfully
    if not ret:
        print("Failed to capture image")
        return None

    return frame

def analyze_emotion(image):
    # Analyze the image for emotions
    try:
        result = DeepFace.analyze(image, actions=['emotion'])
        return result
    except Exception as e:
        print(f"An error occurred during emotion analysis: {e}")
        return None

def main():
    # Capture image from the camera
    img = capture_image_from_camera()

    if img is not None:
        # Convert color from BGR to RGB for plotting
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Display the captured image
        plt.imshow(img_rgb)
        plt.show()

        # Analyze emotion
        result = analyze_emotion(img)

        if result is not None:
            # Print the result
            print(result)

if __name__ == "__main__":
    main()
