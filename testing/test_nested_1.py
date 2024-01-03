#!/usr/bin/python3

import sys

import jk_logging
import jk_exceptionhelper





def foo():
	a = 0
	b = 5 / a
#

def bar():
	foo()
#




with jk_logging.wrapMain() as log:

	try:
		try:
			bar()
		except Exception as ee:
			ex = Exception("Calculation failed", jk_exceptionhelper.ExceptionObject.fromException(ee))
			raise ex

	except Exception as ee:
		ex = Exception("An error occurred", jk_exceptionhelper.ExceptionObject.fromException(ee))
		raise ex


	









