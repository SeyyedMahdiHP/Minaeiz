# in the name of God
# Seyyed Mahdi HassanPour
# SeyyedMahdiHP@gmail.com
"""
Given an expression string exp, write a program to examine whether
 the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
  For example, the program should print true for exp = “[()]{}{[()()]()}” and
   false for exp = “[(])”
"""


def parentheses_balance_checker(userinput):
    length = len(userinput)
    if not (0 == length % 2):
        return False
    open_exp = "[{("
    close_exp = "]})"
    stack_list = list()
    index = 0
    try:

        for item in userinput:
            if item in open_exp:
                stack_list.append(item)
                index += 1
            elif item in close_exp:
                if item == "}" and stack_list.pop() == "{":
                    index -= 1
                elif item == ")" and stack_list.pop() == "(":
                    index -= 1
                elif item == "]" and stack_list.pop() == "[":
                    index -= 1
                else:
                    return False
            else:
                return False
    except Exception:
        return False
    if index != 0:
        return False
    return True


userinput = "[()]{}{[()()]()}"
print(parentheses_balance_checker(userinput))
