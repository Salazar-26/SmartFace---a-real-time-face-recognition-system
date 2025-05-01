import cv2
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
from PIL import Image, ImageTk
import face_recognition_util
import os
import sqlite3
import database  # Import the database module
from face_recognition_util import recognize_faces

class AttendanceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Facial Recognition Attendance System")
        self.root.geometry("800x600")

        # Title Label
        self.label = Label(self.root, text="Face Recognition Attendance", font=("Arial", 16))
        self.label.pack()

        # Video Feed Label
        self.video_label = Label(self.root)
        self.video_label.pack()

        # Student Registration UI
        self.name_label = Label(self.root, text="Enter Student Name:")
        self.name_label.pack()
        self.name_entry = Entry(self.root)
        self.name_entry.pack()
        self.register_button = Button(self.root, text="Register Student", command=self.register_student)
        self.register_button.pack()

        # Start Video Capture
        self.cap = cv2.VideoCapture(0)
        self.update_video()

    def update_video(self):
        """ Continuously update the video feed and recognize faces. """
        ret, frame = self.cap.read()
        if ret:
            detected_faces = recognize_faces(frame)

            for name, (top, right, bottom, left) in detected_faces:
                if name == "UNKNOWN":
                    color = (0, 0, 255)  # Red for unknown faces
                    label = "UNKNOWN"
                else:
                    color = (0, 255, 0)  # Green for recognized faces
                    label = name
                    database.update_instances(name)  # Update attendance

                cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
                cv2.putText(frame, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        self.root.after(10, self.update_video)

    def register_student(self):
        """ Capture student image, save it, and store in database. """
        student_name = self.name_entry.get().strip()
        if not student_name:
            messagebox.showerror("Error", "Please enter a valid name!")
            return

        folder_path = "student_photos"
        os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exist
        file_path = os.path.join(folder_path, f"{student_name}.jpg")

        cap = cv2.VideoCapture(0)  # Open webcam
        ret, frame = cap.read()

        if ret:
            cv2.imwrite(file_path, frame)  # Save the captured image
            messagebox.showinfo("Success", f"Image saved for {student_name}")
            self.add_student_to_db(student_name, file_path)  # Store in database
        else:
            messagebox.showerror("Error", "Failed to capture image!")

        cap.release()
        cv2.destroyAllWindows()

    def add_student_to_db(self, name, photo_path):
        """ Store student details in the database. """
        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO students (name, photo_path) VALUES (?, ?)", (name, photo_path))
            conn.commit()
            messagebox.showinfo("Success", f"{name} registered successfully!")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to insert data: {e}")
        finally:
            conn.close()

    def close(self):
        """ Close video feed and GUI safely. """
        self.cap.release()
        self.root.destroy()

def run_gui():
    root = tk.Tk()
    gui = AttendanceGUI(root)
    root.protocol("WM_DELETE_WINDOW", gui.close)
    root.mainloop()
