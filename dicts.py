ip=input("Print message\n")
d=dict()
for i in ip:
	d[i]=d.get(i,0)+1#return value of that char or default
'''
print(d.keys())
print(d.values())
'''
for key,value in d.items():
	print(key,value)
