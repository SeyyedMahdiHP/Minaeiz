# in the name of GOD
# SeyyedMahdiHassanpour
# smahdi1991@gmail.com
""" do not mistake with language compiling
 ""Compile"" sth in an interpreter language:
  in regular solve, we put the numbers in a permutation in one big for in the input expression to make
  an number expression and then use eval function to evaluate each new expression, and because eval
   is an expensive or slow function our performance is really bad, when we have a 10 second
   to do sth it means that we do our work bad.

  in the faster_solve we told ourselves , we know what our program want, and it just needs to take number expression
  and test it is correct or not. so lets for just one time at the beginning,
    make the expression in an string and then make the string a python code statement with use an eval funtion
    and at the end send digits as parameters to new function to return result.
http://stackoverflow.com/questions/12467570/python-way-to-speed-up-a-repeatedly-executed-eval-statement
"""

import re
import itertools


def faster_solve(formula):
    letters, f = compile_formula(formula, True)
    for digits in itertools.permutations((1, 2, 3, 4, 5, 6, 7, 8, 9, 0), len(letters)):
        try:
            if f(*digits):
                table = str.maketrans(letters, ''.join(map(str, digits)))
                result = formula.translate(table)
                if not re.search(r'\b0[0-9]', result):
                    print(result)
                    return result
        except ArithmeticError:
            pass


def compile_word(word):
    if word.isupper():
        item = ["%s*%s" % (v, 10 ** i) for i, v in enumerate(word[::-1])]
        return '(' + '+'.join(item) + ')'
    else:
        return word


def compile_formula(formula, verbos=False):
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    parameters = ', '.join(letters)
    body = ''.join(map(compile_word, re.split('([A-Z]+)', formula)))
    f = "lambda %s: %s" % (parameters, body)
    if verbos:
        print(f)
    return letters, eval(f)


def test():
    assert faster_solve("SEND + MORE == MONEY") == '9567 + 1085 == 10652'
    assert faster_solve("CRACK + HACK == ERROR") == '42641 + 9641 == 52282'
    assert faster_solve("ODD + ODD == EVEN") == '655 + 655 == 1310' or '855 + 855 == 1710'

    return 'tests passes'


print(test())
