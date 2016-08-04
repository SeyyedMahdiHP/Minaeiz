# in the name of God
# Seyyed Mahdi HassanPour
# SeyyedMahdiHP@gmail.com
"""

"""
import random

strnum = str()
for i in range(0, 1000):
    strnum += str(random.randint(1, 9))
print("number string:", strnum)
mylist = list(strnum)
mylist = list(map(int, mylist))
print("number list: ", mylist)
index = 0
maxn = mylist[0] * mylist[1] * mylist[2] * mylist[3] * mylist[4]
print("first maximum five con:", maxn)
current = maxn
for i in range(5, 1000):
    current *= mylist[i]
    current = current // mylist[i - 5]
    if current > maxn:
        maxn = current
        index = i - 4

print("maximum:%d and starting index:%d" %(maxn, index))

