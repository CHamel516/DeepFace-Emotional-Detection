document.addEventListener('DOMContentLoaded', function() {
    // Get references to the video and canvas elements
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const captureButton = document.getElementById('capture');
    
    // Set up the video stream
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function(stream) {
            video.srcObject = stream;
            video.play();
        })
        .catch(function(error) {
            console.error("Error accessing the webcam", error);
        });
    
    // Handle the capture button click
    captureButton.addEventListener('click', function() {
        // Draw the current video frame to the canvas
        const context = canvas.getContext('2d');
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
        
        // Convert the canvas content to a blob and send it to the server
        canvas.toBlob(function(blob) {
            const formData = new FormData();
            formData.append('file', blob, 'webcam.jpg');
            
            fetch('/upload-image', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                // Assuming the server responds with a JSON object that includes the detected emotion
                // For example: { "emotion": "Happiness" }
                console.log("Detected emotion:", data.emotion);
                
                // Update the webpage to display the detected emotion
                // This could be a redirection to a result page or updating an element's text
                // Here's an example of updating an element's text directly:
                const resultElement = document.getElementById('emotionResult');
                if (resultElement) {
                    resultElement.textContent = `Detected Emotion: ${data.emotion}`;
                } else {
                    // If there's no specific element to display the result, you might redirect or display an alert
                    alert(`Detected Emotion: ${data.emotion}`);
                }
            })
            .catch(error => {
                console.error('Error sending image to the server:', error);
            });
        }, 'image/jpeg');
    });
});
