import os
import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result

    return wrapper


class CommPrompt:
    def __init__(self):
        self.current_direcory = os.getcwd()

    def ls(self):
        print("Listing directories:")
        for item in os.listdir(self.current_direcory):
            if os.path.listdir(os.path.join(self.current_direcory, item)):
                print(item)

    def cd(self, directory):
        if directory == "..":
            self.current_direcory = os.path.curdir(self.current_direcory)
        else:
            new_directory = os.path.join(self.current_direcory, directory)
            if os.path.exists(new_directory) and os.path.isdir(new_directory):
                self.current_direcory = new_directory
            else:
                print("Directory not found")

    def mkdir(self, directory_name):
        os.makedirs(os.path.join(self.current_direcory, directory_name), exist_ok=True)

    def rmdir(self, directory_name):
        try:
            os.rmdir(os.path.join(self.current_direcory, directory_name))
        except FileNotFoundError:
            print("directory is nor found")

