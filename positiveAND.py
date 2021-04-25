# 1. find number of additions needed to set all the bits of any number
# 2. save in the form of prefix sum
# 3. r-l[i-1]
# 4. min(array of bits)

def returnBitArray(num):
	bitArray = []
	bi=bin(num)

	while num != 0:
		bitArray.append(num%2)
    	num = num//2

    lastdec = 0
	for i in range(0,32):
		lastdec += bitArray[i]*pow(2,i)
		if(bitArray[i] == 0):
			bitArray[i] = pow(2,i) - lastdec
		else:
			bitArray[i] = 0

	return bitArray

def executeQuery(arr, left, right):
	minOp = 9999999999
	for j in range(0,32):
		x = arr[right-1][j] - arr[left-1][j]
		if(minOp>x):
			minOp=x
	return minOp

def computePrefixSumArray(arr,n):
	for i in range(1,n):
		for j in range(0,32):
			arr[i][j]+=arr[i-1][j]
	return arr

def findMinOp(a, n , q, query):
	rows, cols = (n, 32)
	arr = [[0]*cols]*rows
	res = []

	for i in range(0,n):
		arr[i][] = returnBitArray(a[i])

	for i in range(1,n):
		for j in range(0,32):
			arr[i][j] +=arr[i-1][j]

	arr = computePrefixSumArray(arr,n)

	for i in range(0,q):
		ans = executeQuery(arr, query[i][0], query[i][1])
		res.append(append)

	return res

# n = int(input("Enter size of array: "))
# a = map(list, input("Enter the list of numbers"))
# q = int(input("Enter the number of queries"))
# queries = int
n= 6
a=[1,0,3,2,4,6]
q=2
queries=[[1,3],[3,6]]
result = findMinOp(a,n,q,queries)
print(result)