#!/usr/bin/python3
"""This is for finding peak"""

def find_peak(list_of_integers):
    """
    To find the peak in a given list of integers

    list_of_integers: This isthe list passed to the array
    
    Return - The Peak value or None
    
    """
    if list_of_integers is None or list_of_integers == []:
        return None
    if (len(list_of_integers) == 1):
        return list_of_integers[0]

    mov = "-ve"
    peak = list_of_integers[0]
    i = 1

    while i < len(list_of_integers):
        if (list_of_integers[i] - list_of_integers[i - 1] >= 0):
            mov = "+ve"
        if ((list_of_integers[i] - list_of_integers[i - 1] < 0) & (mov == "+ve")):
            peak = list_of_integers[i - 1]
            break
        i += 1

    return peak
