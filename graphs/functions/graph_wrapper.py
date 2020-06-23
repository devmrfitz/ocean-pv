import plotly.graph_objects as go
from plotly.offline import plot

from interactions.models import (
    SelfAnswerGroup,
    UserAnswerChoice
)


def return_group_and_score(primary_key):
    score_list_dictionary = {}
    answer_group = SelfAnswerGroup.objects.get(pk=primary_key)

    answers = [
        answer.answer_choice for answer in UserAnswerChoice.objects.filter(
            self_answer_group=answer_group)
    ]

    question_factors = [
        answer.question.question_factor for
        answer in UserAnswerChoice.objects.filter(
            self_answer_group=answer_group)
    ]

    final_scores = [answer*question_factor for answer,
                    question_factor in zip(answers, question_factors)]

    qn_subclasses = [
        answer.question.ocean_subclass for
        answer in UserAnswerChoice.objects.filter(
            self_answer_group=answer_group)
    ]

    scores = [0, 0, 0, 0, 0]
    for final_score, question_subclass in zip(final_scores, qn_subclasses):
        if question_subclass == 'openness':
            scores[0] = scores[0]+final_score
        elif question_subclass == 'conscientiousness':
            scores[1] = scores[1]+final_score
        elif question_subclass == 'extraversion':
            scores[2] = scores[2]+final_score
        elif question_subclass == 'agreeableness':
            scores[3] = scores[3]+final_score
        elif question_subclass == 'neuroticism':
            scores[4] = scores[4]+final_score

    score_list_dictionary[
        f"{answer_group.id}: {answer_group.user_profile.user.username}"
    ] = scores

    return score_list_dictionary


def return_list_of_dictionaries(*args, **kwargs):
    list_of_dictionaries = list(return_group_and_score(arg) for arg in args)
    return list_of_dictionaries


def plotly_draw(list_of_dictionaries):
    ocean_subclasses = [
        'Openness',
        'Conscientiousness',
        'Extraversion',
        'Agreeableness',
        'Neuroticism'
    ]

    score_list = []
    tag_list = []
    for dictionary in list_of_dictionaries:
        score_list.append(list(dictionary.values())[0])
        tag_list.append(list(dictionary.keys())[0])

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


def return_ocean_descriptions(scores):
    return scores


def return_ocean_descriptions_with_graph(*args, **kwargs):
    list_of_dictionaries = return_list_of_dictionaries(*args)
    description_list = return_ocean_descriptions(
        list(list_of_dictionaries[0].values())[0])
    return plotly_draw(list_of_dictionaries)


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
