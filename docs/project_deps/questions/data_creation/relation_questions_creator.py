import random
import csv

from interactions.models import RelationQuestion

with open('docs/questions/data/relation_questions.csv') as f:
    fieldnames = ['subclass', 'text', 'factor']
    f_reader = csv.DictReader(f, fieldnames=fieldnames, delimiter='|')
    mylst = list(f_reader)
    random.shuffle(mylst)

    for index, row in enumerate(mylst, 1):
        RelationQuestion.objects.create(
            overall_question_number=index,
            question_text=row['text'],
            ocean_subclass=row['subclass'],
            question_factor=row['factor']
        )
print('done')
