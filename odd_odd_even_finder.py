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

    return


solve("ODD + ODD == EVEN")
solve("CRACK + HACK == ERROR ")
solve("CRACK / HKD == ER ")
