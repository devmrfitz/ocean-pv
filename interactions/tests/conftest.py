import csv
import random

import pytest
from mixer.backend.django import mixer


@pytest.fixture
def create_questions(db):
    """ Creates random questions in the database. """
    
    def _create_questions(question_model):
        return mixer.cycle(44).blend(f"interactions.{question_model}")
    return _create_questions
