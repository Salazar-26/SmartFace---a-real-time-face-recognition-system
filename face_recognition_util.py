import face_recognition
import cv2
import numpy as np
import os
from database import initialize_database
initialize_database()
from database import update_instances, get_students

# Load known student faces from the database
def load_students():
    """Load known students and their face encodings from the database."""
    known_encodings = []
    known_names = []

    try:
        students = get_students()  # Fetch students from the database

        for student in students:
            name, photo_path = student[1], student[2]  # Extract name and image path
            
            if not os.path.exists(photo_path):
                print(f"Warning: Image file not found for {name}: {photo_path}")
                continue  # Skip if the file doesn't exist

            image = face_recognition.load_image_file(photo_path)
            encodings = face_recognition.face_encodings(image)
            
            if encodings:  # Only add if encoding exists
                known_encodings.append(encodings[0])
                known_names.append(name)
            else:
                print(f"Warning: No face encoding found for {name}")

    except Exception as e:
        print(f"Error loading students: {e}")

    return known_encodings, known_names


# Load known encodings once (Avoid reloading for every frame)
known_encodings, known_names = load_students()


def recognize_faces(frame):
    """Detect and recognize faces in a video frame."""
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect face locations and encodings
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    detected_faces = []  # Store (name, location) tuples

    for encoding, location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_encodings, encoding, tolerance=0.5)
        name = "UNKNOWN"

        if True in matches:
            match_index = matches.index(True)
            name = known_names[match_index]
            update_instances(name)  # Update attendance in the database

        detected_faces.append((name, location))  # Store name and location

    return detected_faces  # Return list of (name, location)
