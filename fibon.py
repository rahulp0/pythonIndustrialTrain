n=int(input("Enter val of fib"))

i=0
print(i)
i=1
arr=[0,1]
while i<=n:
	#print(i)
	arr.append(arr[i-1]+arr[i])
	i=i+1
print (arr)
