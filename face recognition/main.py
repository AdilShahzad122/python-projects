import face_recognition  # Library for face detection and recognition
import cv2              # OpenCV library for image processing
import numpy as np      # Library for numerical operations
import csv             # Library for CSV file operations
from datetime import datetime  # For handling date and time

video_capture = cv2.VideoCapture(0)  # Initialize webcam (0 means default camera)

# Load and encode known faces
adil_image = face_recognition.load_image_file("faces/adil.jpg")  # Load Adil's image
adil_encoding = face_recognition.face_encodings(adil_image)[0]   # Create face encoding for Adil
haroon_image = face_recognition.load_image_file("faces/haroon.jpg")  # Load Haroon's image
haroon_encoding = face_recognition.face_encodings(haroon_image)[0]   # Create face encoding for Haroon

# Store known face encodings and names
known_face_encodings = [adil_encoding, haroon_encoding]  # List of known face encodings
known_face_names = ["Adil", "haroon"]                    # Corresponding names

# Create a copy of names for attendance tracking
students = known_face_names.copy()

# Will store locations of detected faces
face_locations = []

# Will store encodings of detected faces
face_encodings = []

# Get current date/time
now = datetime.now()

# Format date as YYYY-MM-DD
current_date = now.strftime("%Y-%m-%d")

# Create CSV file for attendance
f = open(f"{current_date}.csv", 'w+', newline='')
lnWriter = csv.writer(f)

while True:
    # Capture video frame
    _, frame = video_capture.read()  # Read a frame from webcam
    
    # Process frame for face recognition
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)  # Resize frame to 1/4 size
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

    # Detect faces in frame
    face_locations = face_recognition.face_locations(rgb_small_frame)  # Find faces
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)  # Encode faces

    # Process each detected face
    for face_encoding in face_encodings:
        # Compare with known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)  # Find best matching face

        if (matches[best_match_index]):
            name = known_face_names[best_match_index]  # Get name of matched person

            # Display name on video
            if name in known_face_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,100)
                fontScale = 1.5
                fontColor = (255,0,0)  # Blue color in BGR
                thickness = 3
                lineType = 2
                cv2.putText(frame, name + "Present", bottomLeftCornerOfText, 
                           font, fontScale, fontColor, thickness, lineType)

                # Record attendance
                if name in students:
                    students.remove(name)  # Remove from pending list
                    current_time = now.strftime("%H-%M-%S")  # Get current time
                    lnWriter.writerow([name, current_time])  # Write to CSV

    # Show the frame and check for exit condition
    cv2.imshow("Attendance", frame)  # Show processed frame
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Check for 'q' key press
        break

# Cleanup
video_capture.release()      # Release webcam
cv2.destroyAllWindows()     # Close all windows
f.close()                   # Close CSV file


