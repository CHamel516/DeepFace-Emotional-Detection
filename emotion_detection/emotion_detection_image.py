from deepface import DeepFace

def analyze_emotion_from_file(image_path):
    analysis = DeepFace.analyze(img_path = image_path, actions = ['emotion'])
    return analysis['dominant_emotion']
