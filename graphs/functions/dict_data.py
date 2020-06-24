from .cleaner import clean_multiple_results_data
from .scores import update_dict_with_score
from .plotter import draw_plot
from .percentages import (
    calculate_coordinates,
    calculate_areas,
    calculate_percentages
)


def return_plot_and_view_data(view_dict: dict, *args, **kwargs) -> tuple:
    """ This function will take in a dict with 2 keys 'master' and 'primary_keys' from 'multiple_result_view'
    and do the following:
    1) clean up the data for unavailable and duplicate keys
    2) create and returns the plot
    3) calculates the areas and the percentage difference

    It will return a dictionary list of the following format:
    data = {
    'name': str,
    'master': bool,
    'percentage': float,
    'answer_group_pk': int }
    and the plot too """

    valid_dict, unavailable_pks, duplicate_pks = clean_multiple_results_data(
        view_dict['master'], *view_dict['to_plot'])
    valid_dict = update_dict_with_score(valid_dict)
    plot = draw_plot(valid_dict)
    valid_dict = calculate_percentages(calculate_areas(valid_dict))

    return valid_dict, unavailable_pks, duplicate_pks, plot
