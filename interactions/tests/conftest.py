import csv
import random

import pytest
from mixer.backend.django import mixer 


@pytest.fixture
def create_questions(db):
    def _create_self_questions(question_model):
        return mixer.cycle(44).blend(f"interactions.{question_model}")
    return _create_self_questions