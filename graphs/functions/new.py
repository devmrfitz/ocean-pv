import math
# [{'7: ignisda': [6, 1, 2, 1, 2]}]
# [{'9: ignisda': [9, 3, 11, -1, 7]}]


def calculate_coordinates(list_of_dictionaries: list) -> list:
    """ Calculate the coordinates using trigonometry """
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
    print(score_list, coordinate_list)


calculate_coordinates([{'9: ignisda': [9, 3, 11, 10, 7]}])


def calculate_area():
    pass


def multiply(a, b):
    """Multiplies two integers

    The first number does not have constraints, but the second number
    cannot be negative. Doing otherwise leads to unexpected behaviour.
    :param a: First number
    :type a: integer
    :param b: Second number
    :type b: positive integer

    :returns: Multiplication of a and b
    :rtype: integer"""
    # If any of the numbers is zero, result will be zero
    if a == 0 or b == 0:
        return 0
    # Define a variable to store the result temporarily
    res = 0
    # Sum the a to the temporary result b times
    for i in range(b):
        # Update the temporary result
        res += a
    return res
