import sys
import os

# Add the 'scripts' folder to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))
from database import initialize_database
from gui import run_gui

if __name__ == "__main__":
    initialize_database()  # Ensure the database and table exist
    run_gui()



