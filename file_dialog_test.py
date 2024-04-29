import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open file dialog
    file_path = filedialog.askopenfilename()

    return file_path

# selected_file = open_file_dialog()

# split_file = selected_file.split("/")
# print("Selected file:", split_file[-1])
