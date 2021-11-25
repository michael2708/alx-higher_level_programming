#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    if roman_string == "":
        return 0
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    for i in range(len(roman_string) - 1):
        left = roman_string[i]
        right = roman_string[i + 1]
        if dic[left] < dic[right]:
            sum -= dic[left]
        else:
            sum += dic[left]
    sum += dic[roman_string[-1]]
    return sum
