#!/usr/bin/env python3



from jk_logging import *




dl = DetectionLogger_v0.create(NullLogger.create())

myLog = BufferLogger.create()
myLog2 = myLog.descend("Subsection")
myLog2.notice("Test 1")
myLog2.notice("Test 2")

myLog.forwardTo(dl)


print()
for k, v in dl.getLogMsgCountsStrMap().items():
	print(k, " : ", v)
print()



