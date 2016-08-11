# in the name of God
# Seyyed Mahdi HassanPour
# SeyyedMahdiHP@gmail.com
"""

"""
import re


def check_national_code_pattern_with_regex(ncode):
    match = re.match("[0-9]{3}\-[0-9]{6}\-[0-9]", ncode)
    search = re.search("[0-9]{3}\-[0-9]{6}\-[0-9]", ncode)
    findall = re.findall("[0-9]{3}\-[0-9]{6}\-[0-9]", ncode)
    return (match, search, findall)


def check_validity(ncode):
    pass

national_code_valid = "204-045625-3"
national_code_invalid1 = "1321454645"
national_code_invalid2 = "111-111111-1"
print(check_national_code_pattern_with_regex(national_code_valid),
      check_national_code_pattern_with_regex(national_code_invalid1),
      check_national_code_pattern_with_regex(national_code_invalid2))


