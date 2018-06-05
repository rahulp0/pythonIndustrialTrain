'''
def starC(n):
	for i in range(1,n+1):
		print("*"*i)
	print("\n")

pin=int(input("Enter the level"))

#for j in range(0,pin):
starC(pin)
'''

def starC(n):
        for i in range(1,n+1):
                print("*",end="")
        print("\n")

pin=int(input("Enter the level"))

for j in range(0,pin):
	starC(j)
