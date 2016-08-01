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


def check_overlap(l1, l2, r1, r2):
    if l1[0] > r2[0] or l2[0] > r1[0]:
        return False

    if l1[1] < r2[1] or l2[1] < r1[1]:
        return False

    return True


l1 = [0, 10]
r1 = [10, 0]
l2 = [5, 5]
r2 = [15, 0]
if check_overlap(l1, l2, r1, r2):
    print("Rectangles Overlap")
else:
    print("Rectangles Don't Overlap")

