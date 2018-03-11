from numpy import *


def find_euclidean_distance(data_set, in_val):
    """
    this function finds euclidean distance between input and data set points    
    :param data_set: Training Data
    :param in_val: Input Value
    :return: list of distances
    """
    diff_mat = data_set - in_val
    sqre_mat = power(diff_mat, 2)
    sum_of_rows = sum(sqre_mat, axis=1)
    return sqrt(sum_of_rows)


def classify_with_knn(data_set, labels, in_val, k=2):
    """
    this function returns list of top k nearest neighbours of in_val from data set 
    :param data_set: 
    :param labels: 
    :param in_val: 
    :param k: 
    :return: 
    """
    distance = find_euclidean_distance(array(data_set), array(in_val))
    values = zip(labels, distance)
    sorted_values = sorted(values, key=lambda value: value[1])
    if k > 0:
        sorted_values = sorted_values[:k]
    return sorted_values
