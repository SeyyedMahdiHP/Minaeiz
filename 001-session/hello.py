# identifiers:
#   +meaningful, +English, -WS, leading digits, keyword, ...
#   get_full_name
# types : int, float, str, bool, .....
# dynamic + strong
# a = 1
# a = 1.1
# a = 's'
# a = True
# a = 'ALI'
# b = 'KALAN'
# print(a + b)
# print("ALI       KALAN")
# print(abs(-100))
# import math
# print(math.log(100))

# built in
# number
# a = 1
# print(type(a))
# print(type(print))
# print(type(1))
# print(type(1.1))
# print(type(1j))
# print(0b10)
# print(0o10)
# print(0x10)
# print(type(int('12')))
# print(type(float('12.5')))
# print(bin(12))
# print(oct(12))
# print(hex(12))

# operations: +, -, *, /, //, **, %
# a = 3
# b = 4
# print(3 // 4)
# print(3 ** 4)
# print(3 % 4)
# a = 'ali'
# print(a * 4)

# bool
# falsy values: 0, 0.0, 0j, '', False, None
#   [], {}, set(), __len__, __bool__
# block
# a = 10
# if 5 < a < 10:
#     print("BOOD")
# a = 10
# if a > 10:
#     print("BOOD")
#     print("ALI")
# elif a > 5:
#     print("NABOOD")
# else:
#     print("INJA")
# a = 10
# b = 20
# a, b = b, a
# print(a, b)
# a = 0
# while a < 10:
#     print(a)
#     a += 1
import random
# print(random.randint(10, 20))
# print(chr(97))
# print(chr(122))
password = ''
a = 0
while a < 8:
    if random.randint(0, 61) < 10:
        password += chr(random.randint(48, 57))
    elif random.randint(0, 1) == 1:
        password += chr(random.randint(65, 90))
    else:
        password += chr(random.randint(97, 122))
    a += 1
print(password)
# concept + tools









