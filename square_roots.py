# in the name of God
# Seyyed Mahdi HassanPour
# SeyyedMahdiHP@gmail.com
"""
https://www.mathsisfun.com/square-root.html
http://code.activestate.com/recipes/577821-integer-square-root-function/
http://stackoverflow.com/questions/1623375/writing-your-own-square-root-function
"""


def squareroot1(num):
    for i in range(num):
        square = i ** 2
        if square == num:
            return str("square root:%d" % square)
        elif square > num:
            return str("square root:%d" % (i - 1) ** 2)


print(squareroot1(5))
