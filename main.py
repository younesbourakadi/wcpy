import os
import argparse


def wcpy(file_name):
    parser = argparse.ArgumentParser(
                    prog='pywc',
                    description='unix wc written in python',
                    epilog='Text at the bottom of help')

    file_stats = os.stat(file_name)
    return str(file_stats.st_size) + " " + file_name


print(wcpy('test.txt'))
