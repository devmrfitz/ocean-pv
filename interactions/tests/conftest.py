import csv
import random

import pytest

from interactions.models import SelfQuestion, RelationQuestion


@pytest.fixture
def create_self_questions(db):
    def _create_self_questions():
        with open('personal/resources/.dictionary.csv') as f:
            f_reader = csv.DictReader(
                f, fieldnames=['subclass', 'factor', 'text'], delimiter='|')
            lst = []
            for row in f_reader:
                lst.append(row)
            random.shuffle(lst)
            for index, row in enumerate(lst, 1):
                SelfQuestion.objects.create(
                    overall_question_number=index,
                    question_text=row['text'],
                    ocean_subclass=row['subclass'],
                    question_factor=row['factor']
                )
            for question in SelfQuestion.objects.all():
                question.save()
    return _create_self_questions


@pytest.fixture
def create_relation_questions(db):
    def _create_relation_questions():
        with open('personal/resources/.dictionary_friends.csv') as f:
            f_reader = csv.DictReader(
                f, fieldnames=['subclass', 'factor', 'text'], delimiter='|')
            lst = []
            for row in f_reader:
                lst.append(row)
            random.shuffle(lst)
            for index, row in enumerate(lst, 1):
                RelationQuestion.objects.create(
                    overall_question_number=index,
                    question_text=row['text'],
                    ocean_subclass=row['subclass'],
                    question_factor=row['factor']
                )
            for question in RelationQuestion.objects.all():
                question.save()
    return _create_relation_questions
