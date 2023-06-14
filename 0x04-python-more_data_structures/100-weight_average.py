#!/usr/bin/python3
def weight_average(my_list=[]):
    div = 0
    avr = 0

    if not my_list:
        return 0
    for n in my_list:
        avr += n[0] * n[1]
        div += n[1]
    return float(avr / div)
