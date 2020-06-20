from .graph_wrapper import (
    return_list_of_dictionaries,
    plotly_draw,
    clean_multiple_results_data
)
from .area_calculator import calculate_areas


def utility_function(*args, **kwargs) -> tuple:
    """ A utility function that takes the cleaned Test IDs from 
    'multiple_result_view' and then returns the graph as well as the area of 
    these graphs. This is meant to be used as a wrapper. """

    list_of_dictionaries = return_list_of_dictionaries(*args)
    areas_list = calculate_areas(list_of_dictionaries)
    return plotly_draw(list_of_dictionaries), areas_list


def calculate_percentages(username: str) -> list:
    """ Calculate the percentage difference from username's score """

    pass


def ultimate_wrapper(*args, **kwargs) -> tuple:
    """ This function will take in the unclean data from 'multiple_result_view'
    and do the following:
    1) clean up the data for unavailable and duplicate keys
    2) create and return the graph
    3) calculates the areas, and returns the percentage difference """

    list_of_dictionaries = return_list_of_dictionaries(*args)
    areas_list = calculate_areas(list_of_dictionaries)
    valid_pks, unavailable_pks, duplicate_pks = clean_multiple_results_data(
        *args)

    return (
        valid_pks, unavailable_pks, duplicate_pks
    )
