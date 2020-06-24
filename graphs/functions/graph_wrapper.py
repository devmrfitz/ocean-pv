import plotly.graph_objects as go
from plotly.offline import plot

from interactions.models import (
    SelfAnswerGroup,
    UserAnswerChoice
)
from .plotter import draw_plot
from .scores import update_dict_with_score


def return_valid_dict(pk: int) -> list:
    
    answer_group = SelfAnswerGroup.objects.get(pk=pk)
    valid_dict = [{
    'name': answer_group.user_profile.user.username,
    'master': True,
    'answer_group_pk': pk
    }]
    valid_dict = update_dict_with_score(valid_dict)
    
    return valid_dict
    
    
def return_ocean_descriptions_with_graph(pk: int, *args, **kwargs)-> tuple:
    
    valid_dict= return_valid_dict(pk)
    
    return draw_plot(valid_dict)


def clean_multiple_results_data(*primary_keys):
    primary_keys = list(
        int(primary_key) for
        primary_key in primary_keys if primary_key.strip().isdigit()
    )
    valid_pks, unavailable_pks, duplicate_pks = set(), set(), set()
    for primary_key in primary_keys:
        if primary_key in [
            ans_gp['pk'] for ans_gp in SelfAnswerGroup.objects.values('pk')
        ]:
            if primary_key not in valid_pks:
                valid_pks.add(primary_key)
            else:
                duplicate_pks.add(primary_key)
        else:
            if primary_key not in unavailable_pks:
                unavailable_pks.add(primary_key)
            else:
                duplicate_pks.add(primary_key)

    return valid_pks, unavailable_pks, duplicate_pks
