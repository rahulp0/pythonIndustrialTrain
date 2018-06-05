import random
import sys

#sys.exit()
str='x'
while str!='exit':
	p=int(ord(str))
	print(random.randint(1,((p))))
	str=input()
print("Exiting")
sys.exit()
