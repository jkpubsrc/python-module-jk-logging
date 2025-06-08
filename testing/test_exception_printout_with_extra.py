#!/usr/bin/env python3



import jk_logging






class CustomException(Exception):

	def __init__(self, extraFloatValue:float):
		super().__init__("Custom exception!")
		self.extraValues = { "aFloat": extraFloatValue }
	#

#










log = jk_logging.ConsoleLogger.create(logMsgFormatter=jk_logging.COLOR_LOG_MESSAGE_FORMATTER)

try:

	with log.descend("Some test outer") as log2:
		with log2.descend("Some test inner") as log3:
			raise CustomException(3.1415927)
		print("This line is not executed as well")
	print("And this line is not executed as well as an exception is raised")

except jk_logging.ExceptionInChildContextException as ee:
	pass







