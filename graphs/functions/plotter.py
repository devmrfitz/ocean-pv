import plotly.graph_objects as go
from plotly.offline import plot

from interactions.models import SelfAnswerGroup


def draw_plot(valid_dict: dict) -> str:
    ocean_subclasses = [
        'Openness',
        'Conscientiousness',
        'Extraversion',
        'Agreeableness',
        'Neuroticism'
    ]

    score_list = []
    tag_list = []
    for dictionary in valid_dict:
        score_list.append(dictionary['score'])
        tag_list.append(
            f"{dictionary['answer_group_pk']}: {dictionary['name']}"
        )

    fig = go.Figure()
    for score, legend_tag in zip(score_list, tag_list):
        fig.add_trace(go.Scatterpolar(
            r=score,
            theta=ocean_subclasses,
            fill='toself',
            connectgaps=True,
            name=legend_tag,
            # visible='legendonly', # confuses users where their graph is
        ))

    max_num = 0
    min_num = 0
    for score in score_list:
        if max_num < max(score):
            max_num = max(score)
        if min_num > min(score):
            min_num = min(score)

    max_num = round(max_num + 5.1, -1)
    min_num = round(min_num - 5.1, -1)
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[min_num, max_num]
            )),
        showlegend=True,
        legend=dict(x=1.15, y=0.8),
        font=dict(
            family="Courier New, monospace",
            size=15,
            color="#5a2f7c"
        )
    )
    return plot(
        fig, output_type='div',
        auto_open=False, image_filename='ocean_plot',
    )
