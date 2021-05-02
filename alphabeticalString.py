t=int(input("Enter number of testcases"))
print(t)
alphabets = 'abcdefghijklmnopqrstuvwxyz'

for tc in range(0,t):
	s=input("Enter string")
	lastindex = 0
	indexes = []
	notFound = 0
	minNF = 100002
	print(len(s))
	for i in range(0, len(s), lastindex+1):
		for alpha in alphabets:
			if(s[lastindex:].find(alpha) != -1):
				lastindex = s.index(alpha)
				indexes.append(lastindex)
			else:
				indexes.append(-1)
				notFound = notFound + 1

		if(minNF > notFound):
			minNF = notFound

	print(minNF)