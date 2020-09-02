#!/usr/bin/python3

#
# This code improves on `example_simple_1a.py` in such a way that it makes use of `jk_logging`.
# It wraps the main function call into a `try ... except ...` and creates a more beautiful
# and readable output such as this:
#
# ```
# [2020-09-02 12:41:16] STACKTRACE: ./example_simple_1b.py:32 <module>    # bar(6)
# [2020-09-02 12:41:16] STACKTRACE: ./example_simple_1b.py:26 bar    # return foo(a, 0)
# [2020-09-02 12:41:16] STACKTRACE: ./example_simple_1b.py:23 foo    # return a / b
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
	bar(6)
except Exception as ee:
	LOG.exception(ee)







