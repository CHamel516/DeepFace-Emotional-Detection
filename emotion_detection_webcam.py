import cv2
from deepface import DeepFace
import datetime
import psycopg2

# Function to insert emotion log into the database
def insert_emotion_log(timestamp, emotion):
    conn = None
    try:
        # Connect to your database
        conn = psycopg2.connect(
            dbname="yourdbname", user="youruser", password="yourpassword", host="yourhost"
        )
        cur = conn.cursor()
        # Insert emotion record
        cur.execute("INSERT INTO emotion_logs (timestamp, emotion) VALUES (%s, %s)", (timestamp, emotion))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def start_realtime_emotion_detection():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open webcam")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            emotion = result['dominant_emotion']
            cv2.putText(frame, emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_4)
            
            # Log emotion with timestamp in the database
            current_time = datetime.datetime.now()
            insert_emotion_log(current_time, emotion)
        except Exception as e:
            cv2.putText(frame, "Processing Error", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_4)

        cv2.imshow('Real-time Emotion Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

