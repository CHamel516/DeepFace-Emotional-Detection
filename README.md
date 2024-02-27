# DeepFace-Emotional-Detection
Using DeepFace to detect emotional with facial expressions

Working to add this to ARTHUR to detect emotion using video/facial expression.



SQL:
CREATE TABLE emotion_logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    emotion VARCHAR(255) NOT NULL
);
