#!/usr/bin/python3

#
# This code improves on `example_simple_1b.py` in such a way that it uses a context for the logging.
# This context performs all the `try ... except ...` handling on it's own. If an exception is raised within this context
# the error stack trace is immediately written to the logger. In order to not to swallow an exception, a
# `ExceptionInChildContextException` is raised. With this exception if you nest multiple log contexts only the inner most context will process
# the error, the outer context will simply fail without additional error. Nevertheless a `ExceptionInChildContextException` will remain on top
# level so you must catch these exceptions an simply drop them, as they are not important: Error output already has been peformed.
#
# ```
# [2020-09-02 12:41:16] STACKTRACE: ./example_simple_1b.py:36 <module>    # bar(6)
# [2020-09-02 12:41:16] STACKTRACE: ./example_simple_1b.py:29 bar    # return foo(a, 0)
# [2020-09-02 12:41:16] STACKTRACE: ./example_simple_1b.py:26 foo    # return a / b
# [2020-09-02 12:41:16]  EXCEPTION: ZeroDivisionError: division by zero
# ```
#



from jk_logging import *



def foo(a, b):
	return a / b

def bar(a):
	return foo(a, 0)



LOG = ConsoleLogger.create(logMsgFormatter=COLOR_LOG_MESSAGE_FORMATTER)
try:
	with LOG:
		bar(6)
except ExceptionInChildContextException as e:
	pass







