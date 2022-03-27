#!/bin/python3



import jk_logging




def doSomethingWrong(log:jk_logging.AbstractLogger):
	with log.descend("Now I'm doing something wrong:") as log2:
		log2.debug("a = 0")
		a = 0
		log2.debug("b = 3 / a")
		b = 3 / a
#





savedLog = None
savedException = None

with jk_logging.BufferLogger.create() as blog:
	try:
		doSomethingWrong(blog)
	except Exception as ee:
		savedLog = blog
		savedException = ee





print("-" * 120)
savedLog.forwardTo(jk_logging.ConsoleLogger.create(logMsgFormatter=jk_logging.COLOR_LOG_MESSAGE_FORMATTER))
print("-" * 120)
print(repr(savedException))
print("-" * 120)




