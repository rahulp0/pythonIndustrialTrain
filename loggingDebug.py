import logging 
import pdb
logging.basicConfig(filename="MAMALOG.txt",level=logging.INFO, format =' %(asctime)s-%(levelname)s-%(message)s')
logging.debug("Start the program")

def tesa(a):
	logging.info("into the function tesa ")
	#logging.critical("the function got the value "+str(a))
	logging.critical("the function got the value "+str(a))
	logging.error("the function got the value "+str(a))
	logging.warning("the function got the value "+str(a))
	pdb.set_trace()
	logging.info("the function got the value "+str(a))
	logging.debug("the function got the value "+str(a))

	try:
		b=a/2
	except Exception as ex:
		logging.DEBUG("an exception has occured DEBUG")

		logging.INFO("an exception has occuredINFO")

		logging.WARNING("an exception has occuredWARNING")

		logging.ERROR("an exception has occuredERROR")

		logging.CRITICAL("an exception has occuredCRITICAL")
		logging.CRITICAL(str(ex))
		logging.ERROR(str(ex))
		logging.WARNING(str(ex))
		logging.INFO(str(ex))
		logging.DEBUG(str(ex))


tesa(1)

#5 logging levels in priority orders:
#DEBUG,INFO,WARNING,ERROR,CRITICAL