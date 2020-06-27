import json
import random


def return_questions(model: str) -> list:
    """ This loads the questions from ``docs/project_deps/data/*.json`` as
    per requirement and raises an ``Exception`` if the requested question
    is not among the ones available. """

    if model == 'SelfAnswerGroup':
        file = 'self_questions'
    elif model == 'RelationAnswerGroup':
        file = 'relation_questions'
    else:
        raise Exception(f"Invalid model ({model}) used")
    with open(f"docs/project_deps/data/{file}.json") as f:
        json_data = json.load(f)
        random.shuffle(json_data)
        return json_data
