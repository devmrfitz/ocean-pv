import plotly.graph_objects as go
from plotly.offline import plot

from interactions.models import (
    SelfAnswerGroup,
)
from .plotter import draw_plot
from .scores import update_dict_with_score


def return_valid_dict(pk: int) -> list:
    
    answer_group = SelfAnswerGroup.objects.get(pk=pk)
    valid_dict = [{
    'name': answer_group.self_user_profile.user.username,
    'master': True,
    'answer_group_pk': pk
    }]
    valid_dict = update_dict_with_score(valid_dict)
    
    return valid_dict
    
    
def return_ocean_descriptions_with_graph(pk: int, *args, **kwargs)-> tuple:
    
    valid_dict= return_valid_dict(pk)
    
    return draw_plot(valid_dict)
