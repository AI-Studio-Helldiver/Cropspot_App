$(document).ready(function() {
    $('#takePicture').click(function() {
        // Pause the image updating by removing the src attribute
        $('#videoFeed').removeAttr('src');

        // Create and show the loading wheel
        var loadingWheel = $('<div class="loader"></div>');
        $('#videoFeed').replaceWith(loadingWheel);

        $.ajax({
            type: "GET",
            url: "/capture_image",
            success: function(response) {
                window.location.href = "/results"; // Redirect to /results
            }
        });
    });

    $('#uploadFile').change(function() {
        var formData = new FormData();
        formData.append('file', this.files[0]);

        // Show the loading wheel while the file is being uploaded
        var loadingWheel = $('<div class="loader"></div>');
        $('#uploadArea').append(loadingWheel);

        $.ajax({
            type: "POST",
            url: "/upload",
            data: formData,
            processData: false, // Important for file uploads
            contentType: false, // Important for file uploads
            success: function(response) {
                // Remove the loading wheel
                loadingWheel.remove();
                window.location.href = "/results"; // Redirect to /results
            },
            error: function(error) {
                // Handle errors if the upload fails
                console.error("Error uploading file:", error);
                loadingWheel.remove();
                alert("File upload failed. Please try again.");
            }
        });
    });
});
