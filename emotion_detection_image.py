import cv2
from deepface import DeepFace
import datetime
import psycopg2

# Function to insert emotion log into the database
def insert_emotion_log(timestamp, emotion):
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_db_user",
        password="your_db_password",
        host="your_db_host"
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO emotion_logs (timestamp, emotion) VALUES (%s, %s)", (timestamp, emotion))
    conn.commit()
    cur.close()
    conn.close()

def emotion_detection_image(image_path):
    # Read the image
    img = cv2.imread(image_path)

    try:
        # Analyze the image to get the dominant emotion
        result = DeepFace.analyze(img, actions=['emotion'])
        emotion = result['dominant_emotion']

        # Log the emotion with the current timestamp in the database
        current_time = datetime.datetime.now()
        insert_emotion_log(current_time, emotion)

        # Optionally, show the image and emotion detected
        print(f"Emotion detected: {emotion}")
        cv2.putText(img, emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_4)
        cv2.imshow("Image Emotion Detection", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print("Error in emotion detection or database logging:", e)

# Replace 'your_db_name', 'your_db_user', 'your_db_password', and 'your_db_host'
# with your actual PostgreSQL database details.
