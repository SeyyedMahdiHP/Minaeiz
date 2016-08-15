# def say_hello():
#     print('hello 1')
#
#
# def say_hello():
#         print('hello 2')


# def add(a, b):
#     return a + b
#
# print(add(10, 20))

# + - * /

# def add(a, b):
#     return a + b
#
#
# def minus(a, b):
#     return a - b
#
#
# def mul(a, b):
#     return a * b
#
#
# def divide(a, b):
#     return a / b

# op1 = int(input("Enter first operand: "))
# op2 = int(input("Enter second operand: "))
# operator = input("Enter your operator: ")

# if operator == '+':
#     print(add(op1, op2))
# elif operator == '-':
#     print(minus(op1, op2))
# elif operator == '*':
#     print(mul(op1, op2))
# elif operator == '/':
#     print(divide(op1, op2))

# s = "print('ALI KALAN')"
# eval(s)

# import ast
# print(type(ast.literal_eval('[1, 2, 3, 4]')))
import ast


def add(X, Y):
    # s = []
    # for v in X:
    #     s.append(v + Y[X.index(v)])
    # for i in range(len(X)):
    #     s.append(X[i] + Y[i])
    # return s
    return [x + y for x, y in zip(X, Y)]


def mul(X, Y):
    return sum([x * y for x, y in zip(X, Y)])


# v1 = ast.literal_eval(input("Enter a vector: "))
# v2 = ast.literal_eval(input("Enter a vector: "))
# op = input("Enter an operator: ")
#
# if op == '+':
#     print(add(v1, v2))
# elif op == '.':
#     print(mul(v1, v2))
#
# X = [1, 2, 3]
# Y = [3, 2, 1]
# print(zip(X, Y))
# x = 10
# y = x
# print(id(x))
# print(id(y))
# for x, y in zip(X, Y):
#     print(x, y)
# print([x + y for x, y in zip(X, Y)])
# s = [X[i] + Y[i] for i in range(len(X))]
# print(s)

# X = [1, 2, 3, 4]
# print([x ** 2 for x in X if x != 3])


# import string
# import random
# alphabets = string.digits + string.ascii_letters
# password = ''
# for _ in range(8):
#     password += random.choice(alphabets)
# print(password)
# print(''.join([random.choice(alphabets) for _ in range(8)]))
# p1 = random.choice(string.digits) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase)
# p2 = ''.join([random.choice(alphabets) for _ in range(5)])
# p3 = list(p1 + p2)
# random.shuffle(p3)
# print(''.join(p3))

# words = "This is some text !!!".split()
# words.sort(key=len)
# print(words)

# l = [1, 2, 3, -4]
# l.sort(key=abs, reverse=True)
# print(l)
# def my_def(item):
#     print(item)
#     return item
#
#
# l = [1, 2, 3, 4]
# l.sort(key=my_def)

# def f(pos, keyword, *args, **kwargs):
#     pass

# def f(a, b, arg1='harchi', arg2="bazam harchi"):
#     print(a, b, arg1, arg2)
#
# f(20, arg2="baz ye chiz dge", 30)

# def f(*args):
#     print(args)
#
# f(12, 'x', [12])

# def f(**kwargs):
#     print(kwargs)
# f(one=1, two=2, three=3)


# def my_generator():
#     num = 0
#     while num < 5:
#         yield num
#         num += 1

# g = my_generator()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))  # StopIteration
# for i in g:
#     print(i)

# for i in range(10):
#     print(i)




