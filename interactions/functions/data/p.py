import csv
import json
import random


with open('json_data.json', 'w') as t:
    with open('data_file.csv') as f:
        fieldnames = ['title', 'img_loc', 'said_by', 'desc']
        f_reader = csv.DictReader(f, fieldnames=fieldnames, delimiter='|')
        lst = []
        for row in f_reader:
            img = row['img_loc']
            title = row['title']
            said_by = row['said_by']
            desc = row['desc']
            valid_dict = {
                'img': f"interactions/images/{img}",
                'title': title,
                'said_by': said_by,
                'desc': desc
            }
            lst.append(valid_dict)
        random.shuffle(lst)
        json.dump(lst, t, indent=4, sort_keys=True)
