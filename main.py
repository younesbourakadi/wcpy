import os

def wcpy(file_name):
    file_stats = os.stat(file_name)
    return str(file_stats.st_size) + " " + file_name

print(wcpy('test.txt'))
