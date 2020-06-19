import math


def calculate_coordinates(list_of_dictionaries: list) -> list:
    """ Calculate the coordinates using trigonometry 

    This takes a list of dictionaries of the format `[{'testuser':[6, 4, 3, 10, 5]}, {'testuser2':[1, 5, 17, 20, 6]}]` and 
    then returns a list of coordinates. These coordinates can be used to represent an irregular polygon whose area 
    can be calculated using shoelace method. 

    :param list_of_dictionaries: List of dictionaries having key-value of `{username:[score_list]}`
    :type list_of_dictionaries: list

    :returns: A list of coordinates `[(2, 0.00), (1, 3.34)]` in the format of (x1, y1)
    :rtype: list
    """

    score_list = []
    for dictionary in list_of_dictionaries:
        score_list.append(list(dictionary.values())[0])

    theta = (2*math.pi)/len(score_list[0])

    coordinate_list = []
    for score in score_list:
        coordinates = []
        for index, coordinate in enumerate(score):
            angle = (theta/(2*math.pi))*index
            slope = math.tan(angle)
            coordinates.append((coordinate, coordinate*slope))
        coordinate_list.append(coordinates)

    return coordinate_list


def calculate_area():
    pass
