#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    rom_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    summ = 0
    count = 1
    for n in roman_string:
      if count < len(roman_string) and rom_dict[n] < rom_dict[roman_string[count]]:
        summ -= rom_dict[n]
      else:
        summ += rom_dict[n]
      count += 1
    return summ  
