import cv2
from deepface import DeepFace
import datetime
import psycopg2

# Function to insert emotion log into the database
def insert_emotion_log(timestamp, emotion):
    # Establish a database connection
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_db_user",
        password="your_db_password",
        host="your_db_host"
    )
    cur = conn.cursor()
    # Insert the emotion data into the table
    cur.execute("INSERT INTO emotion_logs (timestamp, emotion) VALUES (%s, %s)", (timestamp, emotion))
    conn.commit()
    # Close the database connection
    cur.close()
    conn.close()

def start_realtime_emotion_detection():
    cap = cv2.VideoCapture(0) # Start the webcam
    if not cap.isOpened():
        print("Could not open webcam")
        return

    while True:
        ret, frame = cap.read() # Read frame from webcam
        if not ret:
            print("Failed to grab frame")
            break

        try:
            # Analyze the frame to get the dominant emotion
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            emotion = result['dominant_emotion']

            # Display the detected emotion on the frame
            cv2.putText(frame, emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_4)
            
            # Log the emotion with the current timestamp in the PostgreSQL database
            current_time = datetime.datetime.now()
            insert_emotion_log(current_time, emotion)
        except Exception as e:
            # Handle cases where the face is not detected or other processing errors
            cv2.putText(frame, "Processing Error", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_4)

        # Show the frame
        cv2.imshow('Real-time Emotion Detection', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

# Ensure to replace 'your_db_name', 'your_db_user', 'your_db_password', and 'your_db_host'
# with your actual PostgreSQL database credentials.
