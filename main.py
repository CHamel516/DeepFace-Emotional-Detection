import emotion_detection_webcam as edw
import emotion_detection_image as edi

def main():
    choice = input("Enter '1' for real-time detection, '2' to analyze an image: ")

    if choice == '1':
        edw.start_realtime_emotion_detection()
    elif choice == '2':
        image_path = input("Enter the path to the image file: ")
        edi.analyze_emotion_from_file(image_path)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
