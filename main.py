from tkinter import *
from Logics.ltifnam_logics import explore_files, change_filename

window = Tk()
window.title("LtifNam")

def select_file():
    explore_files(file_path_label)

def rename_file():
    change_filename(new_name_input.get())

file_path_label = Label(master=window, text="File path will be shown here.",
                  bg="#d9d9d9", width=45, height=5,
            )
file_select_btn = Button(master=window, text="Select File", width=20, height=2, command=select_file)
new_name_input = Entry(master=window, width=30)
rename_btn = Button(master=window, text="Rename", width=20, height=2, command=rename_file)

file_path_label.grid(row=0, column=0, columnspan=3)
file_select_btn.grid(row=1, column=1, pady=10)
new_name_input.grid(row=2, column=1, pady=10)
rename_btn.grid(row=3, column=1, pady=15)

window.mainloop()