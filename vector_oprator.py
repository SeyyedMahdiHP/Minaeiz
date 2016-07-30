# we are going  to take two vector and +-*
from ast import literal_eval


def input_vector():
    vec1 = input("please enter vec1:(default:vec1 = [1, 2, 3]) ")
    vec2 = input("please enter vec2:(default:vec2 = [2, 3, 4]) ")
    op = input("please enter op: ")
    if vec1 == "":
        vec1 = [1, 2, 3]
    else:
        vec1 = literal_eval(vec1)

    if vec2 == "":
        vec2 = [2, 3, 4]
    else:
        vec2 = literal_eval(vec2)
    return vec1, vec2, op


def addition(vec1, vec2):
    #    vec = list()
    #    for i in range(0, len(vec1)):
    #        vec.append(vec1[i] + vec2[i])
    #    return [vec1[i] + vec2[i] for i in range(len(vec1))]
    return [x + y for x, y in zip(vec1, vec2)]


# more pythonic modeT with using zip
def subtract(vec1, vec2):
    return [x - y for x, y in zip(vec1, vec2)]

# def cross(vec1, vec2):
#    vec = 0
#    for i in range(0, len(vec1)):
#        vec += vec1[i] * vec2[i]
#    return vec


# def dot(vec1, vec2):
#    vec = list()
#    for i in range(0, len(vec1)):
#        vec.append(vec1[i] * vec2[i])
#    return sum(vec)


# list comprehension:pythonic mode and much faster
def dot_list_comprehension(vec1, vec2):
    return sum([x * y for x, y in zip(vec1, vec2)])


vector1, vector2, operator = input_vector()
if operator == "+":
    vector = addition(vector1, vector2)
elif operator == "-":
    vector = subtract(vector1, vector2)
elif operator == "*":
    vector = dot_list_comprehension(vector1, vector2)  # dot(vector1, vector2)

print(vector)
