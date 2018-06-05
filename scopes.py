loc1=1

def someFunc():
	global j
	j=9090
	loc1=100
	print(loc1,j,"inside the function scope")

someFunc()
print(loc1," out ",j)

