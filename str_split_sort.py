# sort by len after split:
# using n**2 order
words_list = "Seyyed Mahdi HassanPOur matikolaee smahdi1991@gmail.com".split()
for i in range(len(words_list)):
    for j in range(len(words_list) - 1):
        if len(words_list[j]) > len(words_list[j+1]):
            words_list[j], words_list[j+1] = words_list[j+1], words_list[j]

print(words_list)

# using 