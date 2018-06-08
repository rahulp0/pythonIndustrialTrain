import os
path="/Users/rahulprakash/summerPy/d4"
print(os.path.exists(path))

print("IS file? ",os.path.isfile(path))
print(os.path.isdir(path))
print("Listing the diles in the directory: ",os.path.dirname(path))
print( os.listdir(os.path.dirname(path)))
print( os.path.getsize(path+"/os101.py"))

totsize=0

for fname in os.listdir(path):
	totsize+=os.path.getsize(os.path.join(path,fname))
print(totsize)

