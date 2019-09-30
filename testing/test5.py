#!/usr/bin/env python3



import os
import time
import traceback
import sys
import abc

import sh

import jk_logging



def doLogTest(log):
	log.trace("This is a test for TRACE.")
	log.debug("This is a test for DEBUG.")
	log.notice("This is a test for NOTICE.")
	log.info("This is a test for INFO.")
	log.warning("This is a test for WARNING.")
	log.error("This is a test for ERROR.")
	log.success("This is a test for SUCCESS.")

	log2 = log.descend("Nested log messages ...")
	log2.notice("Some log data.")

	log3 = log2.descend("Even deeper nested log messages ...")
	log3.notice("Some other log data.")

	log2 = log.descend("Frequent log messages ...")
	log2.info("Some more log data.")
#



print()
print("-- BufferLogger --")

blog = jk_logging.BufferLogger.create()
doLogTest(blog.descend("TEST"))

print()
print("-- forwarding to ConsoleLogger --")

clog = jk_logging.ConsoleLogger.create()

blog.forwardTo(clog)

print()
print("-- reconstructing and forwarding to ConsoleLogger --")

clog = jk_logging.ConsoleLogger.create()

blog2 = jk_logging.BufferLogger.create(blog.getDataAsJSON())
blog2.forwardTo(clog)


















