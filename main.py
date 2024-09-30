import os

user_directory = input("Directory of files: ")  # takes the director path of files

files_list = [] # store old files' names
new_filename_list = []  # store new files' names

# loop to get new file names from user and rename
for file in os.listdir(user_directory):
    files_list.append(file)

    user_filename = input(f"{file}'s new name: ")   # takes new file name
    new_filename_list.append(user_filename)

    # directory paths of files
    new_filename = f"{user_directory}\\{user_filename}"
    old_filename = f"{user_directory}\\{file}"

    os.rename(old_filename, new_filename)   # renames the files

print("\n")

# shows the old and new names of files in lists
print(files_list)
print(new_filename_list)
