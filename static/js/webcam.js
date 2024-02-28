document.getElementById('capture').addEventListener('click', function() {
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, 640, 480);
    
    // Convert canvas image to a format that can be sent to the server
    canvas.toBlob(blob => {
        const formData = new FormData();
        formData.append('file', blob, 'webcam.jpg');

        fetch('/upload-image', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            // Process the response from the server here
            // For example, display the detected emotion
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }, 'image/jpeg');
});

// Access the webcam
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        const video = document.getElementById('video');
        video.srcObject = stream;
    })
    .catch(error => {
        console.log('Error accessing the webcam', error);
    });
