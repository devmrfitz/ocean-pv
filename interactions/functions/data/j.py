import json
import os

with open('json_data.json') as f:
    j_data = json.load(f)

    with open('json_data2.json', 'w') as t:
        for dictionary in j_data:
            said_by = dictionary['said_by']
            if said_by == 'Dipu':
                dictionary['said_by'] = 'Mota Kahika'
            elif said_by == 'Gun':
                dictionary['said_by'] = 'Gun'

        json.dump(j_data, t, indent=4)

os.remove('json_data.json')
os.rename('json_data2.json', 'json_data.json')
