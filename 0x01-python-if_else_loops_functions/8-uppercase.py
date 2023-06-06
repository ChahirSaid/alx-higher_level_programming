#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if islower(i):
            result += chr(ord(i) - 32)
        else:
            result += i
    print('{}'.format(result))
