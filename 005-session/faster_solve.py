import re
import itertools


def faster_solve(formula):
    letters, f = compile_formula(formula)
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
        item = ["%s*%s" % (v, 10**i) for i, v in enumerate(word[::-1])]
        return '(' + '+'.join(item) + ')'
    else:
        return word


def compile_formula(formula, verbos=True):
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