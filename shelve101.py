import shelve
shelveFile1=shelve.open("data1.txt")
test1="Hello!"
shelveFile1["var1"]=test1
shelveFile1.close()
#print(shelveFile1["var1"])

shelveFile1=shelve.open("data1.txt")
print(shelveFile1["var1"])
shelveFile1.close()
shelveFile1.keys()

