import re
msg='callmetomorrow.Mynumberis455567299999090989839264783284009 (636)-7359-9263'

re1=re.compile(r"\d\d\d\d\d")
p=re1.search(msg)
#g=p.group()
#g=p.findall(msg)
print(re1.findall(msg))

re2=re.compile(r"\(\d\d\d\)-\d\d\d\d-\d\d\d\d")
d=re2.search(msg)
print(d.group())

msg="Ran and Shyam are mutual frineedv"
p=re.compile(r"Ran|hyam")
print(p.findall(msg))
'''


z=p.search(msg)
print(z.group())
print(z.group(0))
#print(z.group(1))
'''
msg="Batman has Batmobile"
m=re.compile (r"(Bat)(man|mobile)")	


print(m.findall(msg))
'''
p=m.search(msg)
print(p.group())
print(p.group(1))
print(p.group(2))
print(p.group(3))'''


