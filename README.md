==============================
# SmartFace---a-real-time-face-recognition-system
==============================

PROJECT DESCRIPTION:
--------------------
This project is a real-time Facial Recognition Attendance System developed using Python. It captures facial images of students via webcam, registers them in a local SQLite database, and uses face recognition to mark attendance automatically when a known face is detected. Unknown faces are flagged without updating the database.

SOFTWARE MODULES:
-----------------
1. main.py
2. gui.py
3. face_recognition_util.py
4. database.py

VARIABLE DETAILS:
-----------------
- `DB_PATH` (in database.py): Absolute path to the SQLite database file.
- `known_encodings`, `known_names` (in face_recognition_util.py): Store face encodings and corresponding student names for recognition.
- `self.cap` (in gui.py): Captures video feed from webcam.
- `student_name`, `photo_path` (in gui.py): Store name and path of registered student photo.

SALIENT FEATURES:
-----------------
- Real-time webcam face detection.
- Student registration with photo capture and database entry.
- Face encoding and recognition using dlib via the `face_recognition` library.
- Attendance is auto-updated on recognition of a known face.
- GUI built with Tkinter.
- Error handling for image capture and database operations.

PROCEDURE TO USE:
-----------------
1. Ensure all project files are in one folder with the following structure:
   - main.py
   - scripts/
     ├── gui.py
     ├── face_recognition_util.py
     ├── database.py

2. Make sure a webcam is connected and functional.

3. Run the application using the terminal/command prompt:
   ```bash
   python main.py
   ```

4. GUI will open:
   - Enter student name and click "Register Student" to capture and store their image.
   - Face recognition will auto-detect and update attendance if the student is recognized.

5. Close the application safely using the GUI's close button.

COMPILING PROCEDURE:
--------------------
- Python does not require compilation. Simply run the entry point script:
  ```bash
  python main.py
  ```

HARDWARE/SOFTWARE REQUIREMENTS:
-------------------------------
Minimum Hardware:
- A Windows/Linux/Mac system with at least 4GB RAM
- Integrated or external webcam

Software Requirements:
- Python 3.7+
- Required Python libraries:
  - face_recognition
  - opencv-python
  - numpy
  - tkinter (comes built-in with Python)
  - pillow
  - sqlite3 (built-in with Python)

To install missing libraries:
```bash
pip install face_recognition opencv-python pillow
```

ACKNOWLEDGMENT OF PUBLIC DOMAIN SOFTWARE:
-----------------------------------------
This project uses the following public domain/open-source libraries:

1. face_recognition
   - Website: https://github.com/ageitgey/face_recognition
   - Description: Python library for face detection and recognition using dlib.

2. OpenCV
   - Website: https://opencv.org/
   - Description: Open Source Computer Vision Library for real-time computer vision.

3. Pillow
   - Website: https://python-pillow.org/
   - Description: Python Imaging Library for image manipulation.

ACKNOWLEDGMENTS:
----------------
We acknowledge the creators of the open-source libraries mentioned above, without which this project would not have been possible. Full credits to:
- Adam Geitgey (Author of face_recognition)
- OpenCV community
- Python Software Foundation

The student team has only integrated and adapted these resources for academic purposes, as part of the final year software engineering project.

CONTACT / SUPPORT:
------------------
For any technical assistance, please contact the project team at:
[Prankur Dubey : prankurdubey01s@gmail.com
 Azam Khan : armankhan80808076@gmail.com]
