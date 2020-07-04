from os import path
import json

from interactions.models import (
    SelfAnswerGroup,
)
from .plotter import draw_plot
from .scores import update_dict_with_score


def return_valid_dict(pk: int) -> list:
    """ Makes a dict to be used in ``single_result_view`` """

    answer_group = SelfAnswerGroup.objects.get(pk=pk)
    valid_dict = [{
        'name': answer_group.self_user_profile.user.username,
        'master': True,
        'answer_group_pk': pk
    }]
    valid_dict = update_dict_with_score(valid_dict)

    return valid_dict


def return_descriptions(valid_dict: list) -> tuple:
    """ This constructs the file path to ``descriptions.json`` and then
    uses the ``valid_dict`` to match the scores from ``valid_dict`` and
    classify them as high or low and return the relevant descriptions. """

    file_dir = path.dirname(path.dirname(path.abspath(__file__)))
    file_path = path.join(file_dir, 'static',
                          'data', 'descriptions.json')
    with open(file_path) as f:
        json_data = json.load(f)

    for dictionary in valid_dict:
        dictionary.update({'descriptions': {}})
        scores = dictionary['score']
        for score in scores:
            for desc in json_data:
                if score == desc['subclass']:
                    if scores[score] > 10:
                        dictionary['descriptions'].update(
                            {
                                score: desc['descriptions']['high']
                            }
                        )
                    else:
                        dictionary['descriptions'].update(
                            {
                                score: desc['descriptions']['low']
                            }
                        )
    return valid_dict


def return_ocean_descriptions_with_graph(pk: int, *args, **kwargs) -> tuple:
    """ This is used for ``single_result_view`` to make a plot
    and then return the description of the personality related to that
    particular graph. """

    valid_dict = return_valid_dict(pk)
    valid_dict = return_descriptions(valid_dict)
    plot = draw_plot(valid_dict)
    for dictionary in valid_dict:
        descriptions = dictionary.pop('descriptions')

    return plot, descriptions
