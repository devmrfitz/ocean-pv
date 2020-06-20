import math


def calculate_coordinates(list_of_dictionaries: list) -> list:
    """ Calculate the coordinates using trigonometry 

    This takes a list of dictionaries of the format `[{'testuser':[6, 4, 3, 10, 5]},
     {'testuser2':[1, 5, 17, 20, 6]}]` and 
    then returns a list of coordinates. These coordinates can be used to 
    represent an irregular polygon whose area 
    can be calculated using shoelace method. 

    :param list_of_dictionaries: List of dictionaries having key-value of 
    `{username:[score_list]}`

    :type list_of_dictionaries: list

    :returns: A list of coordinates `[(2, 0.00), (1, 3.34)]` in the format of (x1, y1)
    :rtype: list """

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


def find_determinant(matrix: list) -> float:
    if len(matrix) == 2:
        return (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
    else:
        raise TypeError("Only 2*2 determinants are supported")


def find_summation(matrix: list) -> float:
    """ Find the area of an irregular polygon

    This function uses the shoelace method to find the area of an irregular
    polygon (pentagon in this case). """

    matrix.append(matrix[0])
    determinants = []
    for index, coordinate in enumerate(matrix, 1):
        sub_matrix = []
        sub_matrix.append(coordinate)
        try:
            sub_matrix.append(matrix[index])
        except IndexError:
            sub_matrix.append(matrix[0])
        determinants.append(find_determinant(sub_matrix))
    return abs(sum(determinants))*0.5


def calculate_areas(list_of_dictionaries: list) -> list:
    """ A function that takes a list of dictionaries and returns the area of the graphs that these dictionaries would generate. 

    This function acts as a wrapper for all the above functions and returns the required area """
    
    matrices = calculate_coordinates(list_of_dictionaries)
    areas_list = list()
    for matrix in matrices:
        areas_list.append(find_summation(matrix))
    return areas_list


#print(calculate_areas([{'testuser': [6,, 4, 3, 10, 5]},
#                       {'testuser2': [1, 5, 17, 20, 6]}]))
