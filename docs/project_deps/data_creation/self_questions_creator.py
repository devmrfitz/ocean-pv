""" This module can be used to insert self questions into the
database for initial setup. Run 
`cat docs/project_deps/data_creation/self_questions_creator.py | python manage.py shell` 
to use this. Alternatively, you can also run 
`python manage.py loaddata questions.json` to load the fixtures present in 
'users/fixtures/questions.json' """

import random
import csv

from interactions.models import SelfQuestion

with open('docs/questions/data/self_questions.csv') as f:
    fieldnames = ['subclass', 'text', 'factor']
    f_reader = csv.DictReader(f, fieldnames=fieldnames, delimiter='|')
    mylst = list(f_reader)
    random.shuffle(mylst)

    for index, row in enumerate(mylst, 1):
        SelfQuestion.objects.create(
            overall_question_number=index,
            question_text=row['text'],
            ocean_subclass=row['subclass'],
            question_factor=row['factor']
        )
print('done')
