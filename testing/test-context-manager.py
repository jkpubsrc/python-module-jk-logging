#!/usr/bin/env python3



import os
import time
import traceback
import sys
import abc

import sh

from jk_logging import *



print()
print("-- ConsoleLogger --")
print()

clog = ConsoleLogger()

# now descend and use the result as a new logger:
with clog.descend("Now we run this in a context") as log:
	log.debug("This is a test for DEBUG.")
	log.notice("This is a test for NOTICE.")
	log.info("This is a test for INFO.")
	log.warning("This is a test for WARNING.")
	log.error("This is a test for ERROR.")

print()
print("-- Exception Handling --")
print()

# let's define this method that will produce an exception if invoked
def produceError():
	a = 5
	b = 0
	c = a / b


try:

	# now descend and use the result as a new logger:
	with clog.descend("Now let's try to have an exception in a context") as log:
		log.notice("Now let's try a calculation that will fail ...")
		produceError()	# produce an error; the log context will log it automatically though the exception still get's raised
	clog.notice("We would like to do something else here but that's not possible because of the exception raised.")

except:
	# as the exception is already logged we don't need to do anything more here
	pass

print()
print("-- Exception Handling in nested contexts --")
print()

try:

	# now let's use multiple contexts:
	with clog.descend("Now let's try to have an exception in a context") as log:
		log.notice("We do something ...")
		log.notice("We do something more ...")
		with log.descend("Now let's try to have an exception in a context") as log2:
			log2.notice("Now let's try a calculation that will fail ...")
			produceError()	# produce an error; the log context will log it automatically though a replacement exception still get's raised
		log.notice("We would like to do something else here but that's not possible because of the exception raised.")

except:
	# as the exception is already logged we don't need to do anything more here;
	# anyway a replacement exception has been raised instead; we can't access the original exception anymore here;
	pass



















