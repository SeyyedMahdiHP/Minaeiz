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


def draw_rects(topleft_point, bottomright_point):
    from matplotlib import pyplot as plt
    print(topleft_point, bottomright_point)
    x1, y1 = topleft_point
    x2, y2 = bottomright_point
    plt.plot([x1, x2], [y1, y1])
    plt.plot([x1, x1], [y1, y2])
    plt.plot([x1, x2], [y2, y2])
    plt.plot([x2, x2], [y1, y2])
    plt.axis([0, 15, 0, 15])
    plt.show()


def check_overlap1(l1, l2, r1, r2):
    draw_rects(l1, r1)
    draw_rects(l2, r2)
    if l1[0] > r2[0] or l2[0] > r1[0] or l1[1] < r2[1] or l2[1] < r1[1]:
        print("Rectangles Don't Overlap")
        return False
    print("Rectangles Overlap")
    return True


l1 = [0, 10]  # top left point of rect1
r1 = [10, 0]  # bottom right point of rect1
l2 = [5, 5]  # top left point of rect2
r2 = [15, 0]  # bottom right point of rect2
check_overlap1(l1, l2, r1, r2)
    #######################checkoverlap2##############################


def calculate_cord_dictionary_to_list(rect):
    l = (rect["x"], rect["y"] + rect["h"])
    r = (rect["x"] + rect["w"], rect["y"])
    return list(l), list(r)


rect1 = {"x": 2, "y": 3, "h": 2, "w": 5}
rect2 = {"x": 3, "y": 6, "h": 5, "w": 2}
l1, r1 = calculate_cord_dictionary_to_list(rect1)
l2, r2 = calculate_cord_dictionary_to_list(rect2)
check_overlap1(l1, l2, r1, r2)
