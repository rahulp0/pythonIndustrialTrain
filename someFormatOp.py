import copy
y="pqrst"
output=copy.copy(y)

for i in range(0,len(y)):
	print("*"*3,end="")
	print(y[i],end="")
	print("*"*3)

print(output)

pi=['dfxbdfgch','fgsvdrxfcyhbn','weasdgvb']

for i in range(0,len(pi)):
	if i<len(pi)-1:
		print(pi[i],", ",end="")
	else:
		print("and ",pi[i])

print("Similarly!,")

pp=copy.copy(pi[:-1])
pp=pp.split(",")
print(pp)
print("and",pp[-1]) 
