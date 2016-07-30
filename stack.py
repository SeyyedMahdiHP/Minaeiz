l = "(({}))".split()
l2 = list()
n = 0
for i in l:
	if i == "(":
		l2.append("(")
	elif  i == "{":
		l2.append("{")
	elif i == ")":
		if l2[n] == "(":
			l2[n].pop()
		else:
			return -1
	elif i == "}":
		if l2[n] == "{":
			l2[n].pop()
		else:
			return -1
	
	n += 1