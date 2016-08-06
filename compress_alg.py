# in the name of God
# Seyyed Mahdi HassanPour
# SeyyedMahdiHP@gmail.com
"""

"""


def compress_alg1(user_input):
    compressed_userinput = str()
    temp = user_input[0]
    counter = 0
    for item, i in zip(user_input, list(range(len(user_input)))):
        if item == temp:
            counter += 1
        else:
            compressed_userinput += temp + str(counter)
            counter = 1
            temp = item
            if i == (len(user_input)-1):
                compressed_userinput += temp + str(counter)

    return compressed_userinput

user_input = "SeyyedMahdi HassanPour" \
             "Smahdi1991@gmail.com" \
             "SeyyedMahdiHP@gmail.com" \
             "aaabbbbddddddfffccccceeeersd"
print(compress_alg1(user_input))
