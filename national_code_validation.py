# in the name of God
# Seyyed Mahdi HassanPour
# SeyyedMahdiHP@gmail.com
"""

"""
import re


def check_national_code_pattern_with_regex(ncode):
    match = re.match("[0-9]{3}\-[0-9]{6}\-[0-9]", ncode)
    search = re.search("[0-9]{3}\-[0-9]{6}\-[0-9]", ncode)
    findall = re.findall("[0-9]{3}\-[0-9]{6}\-[0-9]", ncode)  # findall will find  all matched
    # and return them in a list
    information = [match, search, findall, ncode]
    print(information)
    return information


def check_validity(ncode):
    code = ncode[2]
    if not code:
        valid_flag = False
    else:
        code = code[0].replace("-", "")
        if code in [str(item) * 10 for item in range(0, 10)]:  # 0000000000 or 1111111111 , ..., 999999999
            valid_flag = False
        else:
            sum1 = 0
            checksum = int(code[9])
            for i in range(0, 9):
                sum1 += int(code[i]) * (10 - i)
            redundant = sum1 % 11
            if redundant < 2:
                if redundant == checksum:
                    valid_flag = True
                else:
                    valid_flag = False
            elif checksum == (11 - redundant):
                valid_flag = True
            else:
                valid_flag = False
    if valid_flag:
        print("the national code %s is valid!" % ncode[2], "\r\n")
    else:
        print("you have entered a wrong national code!{0} ".format(ncode[3]), "\r\n")


national_code_valid = "470-945055-2"
national_code_invalid1 = "1321454645"
national_code_invalid2 = "111-111111-1"
check_validity(check_national_code_pattern_with_regex(national_code_valid))
check_validity(check_national_code_pattern_with_regex(national_code_invalid1))
check_validity(check_national_code_pattern_with_regex(national_code_invalid2))
