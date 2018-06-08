import re
msg="My no is 345-565-789-321"
cmplvar=re.compile(r'\d\d\d-\d\d\d')
#print(cmplvar.findall(msg))


msg="My no is 345-565-789-321"
cmplvar=re.compile(r'(\d\d\d)-\d\d\d')
mo=cmplvar.finditer(msg)
l=list(mo)

for r in mo:
	print(r.group())


msg="batwoman is with batman"
p=re.compile(r'(bat)*(man){1,2}')
ms=p.finditer(msg)
l=list(ms)
for r in ms:
	print(r.group())

p=re.compile(r'[^aeiouAEIOU]')
m=p.findall(msg)
k=list(m)
k=' '.join(k)
print(k)
