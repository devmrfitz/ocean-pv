""" This module can be used to insert self questions into the
database for initial setup. Run 
`cat docs/project_deps/data_creation/self_questions_creator.py | python manage.py shell` 
to use this. Alternatively, you can also run 
`python manage.py loaddata questions.json` to load the fixtures present in 
'users/fixtures/questions.json' """

import random
import csv
import json

with open('docs/project_deps/data/questions_dictionary.csv') as f:
    fieldnames = ['subclass', 'text', 'factor']
    f_reader = csv.DictReader(f, fieldnames=fieldnames, delimiter='|')
    mylst = list(f_reader)
    random.shuffle(mylst)

    with open('docs/project_deps/data/questions.json', 'w') as t:
        json.dump(mylst, t, indent=4)
