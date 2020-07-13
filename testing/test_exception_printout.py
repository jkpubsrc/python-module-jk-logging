#!/usr/bin/env python3



import jk_logging





log = jk_logging.ConsoleLogger.create(logMsgFormatter=jk_logging.COLOR_LOG_MESSAGE_FORMATTER)

try:

	with log.descend("Some test outer") as log2:
		with log2.descend("Some test inner") as log3:
			x = 0
			print(3 / x)
			print("This line is not executed")
		print("This line is not executed as well")
	print("And this line is not executed as well as an exception is raised")

except jk_logging.ExceptionInChildContextException as ee:
	pass







