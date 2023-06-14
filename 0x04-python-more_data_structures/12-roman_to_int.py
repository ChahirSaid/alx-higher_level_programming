#!/usr/bin/python3
def roman_to_int(roman_string):
    romanN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    my_sum = 0
    length = len(roman_string)
    if type(roman_string) != str or not roman_string:
        return my_sum
    for i in range(length):
        num = romanN[roman_string[i]]
        if i + 1 < length and num < romanN[roman_string[i + 1]]:
            my_sum -= num
        else:
            my_sum += num
    return my_sum if my_sum >= 0 else 0
