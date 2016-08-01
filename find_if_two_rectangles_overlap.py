# in the name of God
# Seyyed Mahdi HassanPour
# SeyyedMahdiHP@gmail.com
"""
Given two rectangles, find if the given two rectangles overlap or not.

Note that a rectangle can be represented by two coordinates, top left and bottom right. So mainly we are given following four coordinates.
l1: Top Left coordinate of first rectangle.
r1: Bottom Right coordinate of first rectangle.
l2: Top Left coordinate of second rectangle.
r2: Bottom Right coordinate of second rectangle.
http://www.geeksforgeeks.org/find-two-rectangles-overlap/
"""

from matplotlib import pyplot as plt

def draw_rects(cords):
    X = range(100)
    Y = [2**n for n in X]
    plt.plot([0,10],[10,10])
    plt.show()


draw_rects(1)
def check_overlap1(l1, l2, r1, r2):
    if l1[0] > r2[0] or l2[0] > r1[0]:
        return False

    if l1[1] < r2[1] or l2[1] < r1[1]:
        return False

    return True


l1 = [0, 10]
r1 = [10, 0]
l2 = [5, 5]
r2 = [15, 0]
if check_overlap1(l1, l2, r1, r2):
    print("Rectangles Overlap")
else:
    print("Rectangles Don't Overlap")

    #######################checkoverlap2##############################


def calculate_cord(rect):
    x = (rect["x"], rect["y"]+rect["h"])
    y = (rect["x"] + rect["w"], rect["y"])
    return list(x), list(y)


rect1 = {"x": 2, "y": 3, "h": 2, "w": 5}
rect2 = {"x": 3, "y": 6, "h": 5, "w": 2}

l1, r1 = calculate_cord(rect1)
l2, r2 = calculate_cord(rect2)
if check_overlap1(l1, l2, r1, r2):
    print("Rectangles Overlap")
else:
    print("Rectangles Don't Overlap")