#!/usr/bin/python3

#
# This code extends on `example_simple_1c.py` to demonstrate the error context capabilitites.
#
# This example will output the following log:
#
# ```
# [2020-09-02 12:48:37]       INFO: Now doing something ...
#     [2020-09-02 12:48:37]       NOTICE: Just something unimportant.
# [2020-09-02 12:48:37]       INFO: Now invoking bar() ...
#     [2020-09-02 12:48:37]       INFO: Processing foo() ...
#         [2020-09-02 12:48:37] STACKTRACE: ./example_simple_1d.py:37 bar    # return foo(a, 0)
#         [2020-09-02 12:48:37] STACKTRACE: ./example_simple_1d.py:33 foo    # return a / b
#         [2020-09-02 12:48:37]  EXCEPTION: ZeroDivisionError: division by zero
# ```
#
# As you can see the log messages are nested hierarchically. But not only are they hierarchically, the exception is caught in the inner most log context.
# The error is therefore logged on exactly that level in the hierarchy and *not* on main program level. This is what we want: We now can see more easily
# where the error occurred.
#
# As mentioned before to output the error the exception needs to be caught. In order to not allow the execution to continue `ExceptionInChildContextException`
# is raised. As mentioned before this exception needs to be caught and swallowed on main program level.
#



from jk_logging import *



def foo(a, b):
	return a / b

def bar(a, log):
	with log.descend("Processing foo() ...") as log2:
		return foo(a, 0)



LOG = ConsoleLogger.create(logMsgFormatter=COLOR_LOG_MESSAGE_FORMATTER)
try:
	with LOG:
		# ... do something ...
		with LOG.descend("Now doing something ...") as log2:
			log2.notice("Just something unimportant.")
			pass
		# ... do something more ...
		with LOG.descend("Now invoking bar() ...") as log2:
			bar(6, log2)
		# ...
except ExceptionInChildContextException as e:
	pass







