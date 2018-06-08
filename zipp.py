import zipfile,os
os.chdir('/Users/rahulprakash/Downloads')
exZip=zipfile.ZipFile('minipro.zip')

#print(exZip.namelist())
#exZip.extractall()

spamInfo=exZip.getinfo('minipro/miniproject/mainfunction/folder/platedetection.py')
print(spamInfo.file_size)

print("Compressed is %s times smaller" % (round(spamInfo.file_size/spamInfo.compress_size,2)))
os.chdir('/Users/rahulprakash/Downloads')

exZip=zipfile.ZipFile('minipro/miniproject/mainfunction/folder/platedetection.py')
exZip.extractall()
exZip.extract('minipro/miniproject/mainfunction/folder/platedetection.py')
exZip.extract('minipro/miniproject/mainfunction/folder/platedetection.py','Users/rahulprakash/summerPy/d5')