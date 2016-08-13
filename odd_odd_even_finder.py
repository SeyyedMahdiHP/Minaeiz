# in the name of God
# Seyyed Mahdi HassanPour
# SeyyedMahdiHP@gmail.com
"""
in this program  we want to take expression like "ODD + ODD == EVEN" and find out what numbers can be placed with
characters and  make a valid expression like : 655 + 655 == 1310
"""
import re
import itertools


def solve(formula):
    for f in fill_in(formula):
        if is_valid(f):
            print(f)
            return f


def fill_in(formula):
    letters = ''.join(set(re.findall("[A-Z]", formula)))
    for digits in itertools.permutations("1234567890", len(letters)):
        table = str.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


def is_valid(formula):
    try:
        # \b is word boundary
        return not re.search(r'\b0[0-9]+', formula) and eval(formula)
    # https://docs.python.org/3/library/exceptions.html
    except ArithmeticError:
        return False


def test_software():
    assert solve("SEND + MORE == MONEY") == '9567 + 1085 == 10652'
    assert solve("CRACK + HACK == ERROR") == '42641 + 9641 == 52282'
    assert solve("ODD + ODD == EVEN") == '655 + 655 == 1310' or '855 + 855 == 1710'
    assert solve("CRACK / HKD == ER") == '26524 / 349 == 76' or '19517 / 673 == 29'

    return "test passes"
print(test_software())
