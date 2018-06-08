import traceback
try:
	raise Exception("err1")
except:
	errorFile = open('errorInfo.txt','w')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('The traceback info is written to file')

podBayDoorStatus='open'
assert podBayDoorStatus=='opn',"Fookitimout"