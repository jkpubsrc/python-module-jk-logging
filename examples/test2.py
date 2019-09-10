#!/usr/bin/env python3



import os
import time
import traceback
import sys
import abc

import sh

from jk_logging import *



print()
print("-- FileLogger --")
print("(writing output to various files ...)")

flog = FileLogger("testoutput-%Y-%m-%d-%H-%M-%S.log", "second")

flog.debug("This is a test for DEBUG.")
flog.notice("This is a test for NOTICE.")
flog.info("This is a test for INFO.")
flog.warning("This is a test for WARNING.")
flog.error("This is a test for ERROR.")

flog2 = flog.descend("Nested log messages ...")
flog2.notice("Some log data.")
flog2.info("Some more log data.")

flog2 = flog.descend("Frequent log messages ...")

i = 0
while i < 20:
	flog2.info("Sleeping ...")
	time.sleep(0.5)
	flog2.info("Doing something ...")
	i += 1

print()















