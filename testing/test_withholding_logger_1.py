#!/usr/bin/env python3



import os
import typing

import jk_typing
import jk_utils
import jk_logging
import jk_json
import jk_prettyprintobj




class LogSimlifyer(object):

	def __init__(self, descendMsg:str, mainLogger:jk_logging.AbstractLogger, bVerbose:bool = False) -> None:
		self.__descendMsg = descendMsg
		self.__mainLogger = mainLogger
		self.__bVerbose = bVerbose

		self.__bufferLogger = jk_logging.BufferLogger.create()
	#

	def __enter__(self):
		return self.__bufferLogger
	#

	def __exit__(self, ex_type:type, ex_value:Exception, ex_traceback):
		# print("X", ex_type, ex_value)

		if ex_type:
			if isinstance(ex_value, jk_logging.ExceptionInChildContextException):
				with self.__mainLogger.descend(self.__descendMsg) as log2:
					self.__bufferLogger.forwardTo(log2)
				return False
			if isinstance(ex_value, GeneratorExit):
				with self.__mainLogger.descend(self.__descendMsg) as log2:
					self.__bufferLogger.forwardTo(log2)
				return False
			else:
				self.__bufferLogger.exception(ex_value)
				with self.__mainLogger.descend(self.__descendMsg) as log2:
					self.__bufferLogger.forwardTo(log2)
				raise jk_logging.ExceptionInChildContextException(ex_value)

		else:
			if self.__bufferLogger.stats.hasAtLeastWarning or self.__bVerbose:
				with self.__mainLogger.descend(self.__descendMsg) as log2:
					self.__bufferLogger.forwardTo(log2)
			return False
	#

	@staticmethod
	def create(descendMsg:str, mainLogger:jk_logging.AbstractLogger, bVerbose:bool = False):
		return LogSimlifyer(descendMsg, mainLogger, bVerbose)
	#

#





with jk_logging.wrapMain() as log:

	print("-")

	with log.descend("Now descending (without error) ...") as log2:
		with jk_logging.WithholdingLogger.create(log2) as log3:

			log3.notice("Foo Bar")
			with log3.descend("Descending once more ...") as log4:
				log4.notice("Foo Bar 2")

	#

	print("-")

	with log.descend("Now descending (with error) ...") as log2:
		with jk_logging.WithholdingLogger.create(log2) as log3:

			log3.notice("Foo Bar")
			with log3.descend("Descending once more ...") as log4:
				raise Exception("Some exception")

	#

	print("-")

#












