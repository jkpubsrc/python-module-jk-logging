#!/usr/bin/env python3
# -*- coding: utf-8 -*-



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



print()
print("-- StringListLogger --")

slog = jk_logging.StringListLogger.create()
doLogTest(slog.descend("TEST"))

print(slog.toStr())

print()
print("-- BufferLogger forwarding to StringListLogger --")

blog = jk_logging.BufferLogger.create()
doLogTest(blog.descend("TEST"))

slog = jk_logging.StringListLogger.create()
blog.forwardTo(slog)

print(slog.toStr())

print()
print("-- MulticastLogger --")
print("\t-- ConsoleLogger --")
print("\t-- StringListLogger --")
print("\t-- BufferLogger --")

clog = jk_logging.ConsoleLogger.create(logMsgFormatter = jk_logging.COLOR_LOG_MESSAGE_FORMATTER)
slog = jk_logging.StringListLogger.create()
blog = jk_logging.BufferLogger.create()
mlog = jk_logging.MulticastLogger.create(clog.descend("DESCENDING"), slog.descend("DESCENDING"), blog.descend("DESCENDING"))
doLogTest(mlog.descend("TEST"))

print(slog.toStr())
blog.forwardTo(jk_logging.ConsoleLogger.create())














