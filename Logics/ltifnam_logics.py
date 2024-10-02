from tkinter import filedialog

def explore_files(file_path_label):
    file_path = filedialog.askopenfilename()
    return file_path_label.configure(text=file_path)


