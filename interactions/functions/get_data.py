import random
import os
import json


def get_file_loc():
    return os.path.dirname(os.path.abspath(__file__))


def get_data_fn():
    file_dir = get_file_loc()
    with open(os.path.join(file_dir, 'data', 'json_data.json')) as f:
        j = json.load(f)
        for index, dictionary in enumerate(j, 1):
            dictionary.update({
            'index': index, 
            'color': random.choice(['danger', 'success', 'info', 'warning', 'dark'])
            })
        random.shuffle(j)
        return j
