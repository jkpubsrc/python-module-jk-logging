#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import os
import time
import traceback
import sys
import json
import abc

import sh

from jk_logging import *





def logException(blog, text):
	try:
		raise Exception(text)
	except Exception as ee:
		blog.error(ee)




blog = BufferLogger.create()
clog = ConsoleLogger.create()
flog = FileLogger.create("/home/jknauth/DevOS/PythonModules/jk_logging/examples/test-output-%Y-%m-%d-%H-%M.log.txt", "minute")

log = MulticastLogger.create(clog, blog, flog)

log.error("This is a test.")
log2 = log.descend("Descending ...")
logException(log2, "This is an exception")

print(json.dumps(blog.getDataAsJSON(), indent = 4))



blog.forwardTo(clog)
log.close()











