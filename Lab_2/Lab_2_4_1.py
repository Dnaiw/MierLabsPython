import random
import string
import os

def get_random_filename():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

def add_folder_to_project_dir(folder_name):
    if not(os.path.exists(folder_name)):
        os.mkdir(folder_name)

def add_random_files(dir_name, number):
    for i in range(number):
        file = open(fr"{dir_name}\{get_random_filename()}.txt", "w")
        file.close()

add_folder_to_project_dir("example")
add_random_files("example", 1000)