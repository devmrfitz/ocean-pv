import csv
import os


def get_file_loc():
    return os.path.dirname(os.path.abspath(__file__))


def get_data_fn():
    file_dir = get_file_loc()
    with open(os.path.join(file_dir, 'data', 'data_file.csv')) as f:
        return ({'name': '', 'image': '', 'description': ''})
