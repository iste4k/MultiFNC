import os
from tkinter import filedialog

def explore_files(file_path_label):
    file_path = filedialog.askopenfilename()
    global gfile_path
    gfile_path = file_path
    return file_path_label.configure(text=file_path)

def change_filename(new_name):
    s_index = gfile_path[::-1].index("/")
    fnew_name = f"{gfile_path[:-s_index]}{new_name}"

    os.rename(gfile_path, fnew_name)
