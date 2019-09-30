#!/usr/bin/env python3



import os
import time
import traceback
import sys
import abc

from jk_logging import *



print()
print("-- ConsoleLogger --")
print()

clog = ConsoleLogger()

clog.debug("This is a test for DEBUG.")
clog.notice("This is a test for NOTICE.")
clog.info("This is a test for INFO.")
clog.warning("This is a test for WARNING.")
clog.error("This is a test for ERROR.")

print()
print("-- Exception Handling --")
print()

def produceError():
	a = 5
	b = 0
	c = a / b

try:
	clog.notice("Now let's try a calculation that will fail ...")
	produceError()
except Exception as ee:
	clog.error(ee)

print()
print("-- FilterLogger --")
print()

flog = FilterLogger(clog, EnumLogLevel.WARNING)

flog.notice("This message will not appear in the log output.")
flog.error("This message will appear in the log output.")

print()
print("-- DetectionLogger --")
print()

dlog = DetectionLogger(clog)
dlog.notice("A notice.")
dlog.debug("A debug message.")
dlog.info("An informational message.")
dlog.debug("Another debug message.")
print(dlog.getLogMsgCountsStrMap())
print("Do we have debug messages? Answer: " + str(dlog.hasDebug()))
print("Do we have error messages? Answer: " + str(dlog.hasError()))

print()
print("-- BufferLogger --")
print()

blog = BufferLogger()
blog.info("First we write something to a buffer.")
blog.info("And something more.")
blog.notice("And more.")
blog.debug("And even more.")
blog.info("Then we write it to the console by forwarding the data to another logger.")
blog.forwardTo(clog)

print()
print("-- MulticastLogger --")
print()

mlog = MulticastLogger([ clog, clog ])
mlog.info("This message gets written twice.")

print()
print("-- NamedMulticastLogger --")
print()

nmlog = NamedMulticastLogger()
nmlog.addLogger("log1", clog)
nmlog.addLogger("log2", clog)
nmlog.info("This message gets written twice.")
nmlog.removeLogger("log1")
nmlog.info("This message gets written once.")

print()
print("-- SimpleFileLogger --")
print()

filelog = SimpleFileLogger("test.log")
filelog.info("Perform log output to this file logger.")
filelog.close()

filelog = SimpleFileLogger("test.log")
filelog.info("Perform more log output to this file logger.")
filelog.close()















