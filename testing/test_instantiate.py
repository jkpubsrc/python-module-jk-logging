#!/usr/bin/env python3



################################################################################################################################
##
## This test script tests instantiation of various loggers and log forwarding of BufferLogger log messages.
##
################################################################################################################################



import jk_logging
import jk_logging.fmt
import jk_logging.debugging

import jk_testing
import jk_testing.utils
import jk_json







# ----------------------------------------------------------------
# instantiate console logger



cfgConsole = {
	"type": "ConsoleLogger",
	"logMsgFormatter": {
		"type": "color",
		"timeStampFormatter": "default",
	},
}

clog = jk_logging.instantiate(cfgConsole)
jk_testing.Assert.isInstance(clog, jk_logging.ConsoleLogger)
jk_testing.Assert.isInstance(clog.logMsgFormatter, jk_logging.fmt.ColoredLogMessageFormatter)
jk_testing.Assert.isInstance(clog.logMsgFormatter.timeStampFormatter, jk_logging.fmt.DefaultTimeStampFormatter)



# ----------------------------------------------------------------
# instantiate string list logger



cfgStringList = {
	"type": "StringListLogger",
	"logMsgFormatter": {
		"type": "default",
		"timeStampFormatter": "debug",
	},
}

slog = jk_logging.instantiate(cfgStringList)
jk_testing.Assert.isInstance(slog, jk_logging.StringListLogger)
jk_testing.Assert.isInstance(slog.logMsgFormatter, jk_logging.fmt.LogMessageFormatter)
jk_testing.Assert.isInstance(slog.logMsgFormatter.timeStampFormatter, jk_logging.debugging.DebugTimeStampFormatter)

slog2 = jk_logging.instantiate(cfgStringList)



# ----------------------------------------------------------------
# instantiate buffer logger
# write some log messages



cfgBuffer = {
	"type": "BufferLogger",
}

blog = jk_logging.instantiate(cfgBuffer)
jk_testing.Assert.isInstance(blog, jk_logging.BufferLogger)
jk_testing.Assert.isNone(blog.logMsgFormatter)



blog.debug("Log line to BufferLogger: debug")
blog.notice("Log line to BufferLogger: notice")
blog.info("Log line to BufferLogger: info")
blog.warn("Log line to BufferLogger: warning")
blog.error("Log line to BufferLogger: error")
blog.success("Log line to BufferLogger: success")
with blog.descend("Descending ...") as blog2:
	blog2.debug("Log line to BufferLogger: debug")
	blog2.notice("Log line to BufferLogger: notice")
	blog2.info("Log line to BufferLogger: info")
	blog2.warn("Log line to BufferLogger: warning")
	blog2.error("Log line to BufferLogger: error")
	blog2.success("Log line to BufferLogger: success")
	with blog2.descend("Descending ...") as blog3:
		blog3.debug("Log line to BufferLogger: debug")
		blog3.notice("Log line to BufferLogger: notice")
		blog3.info("Log line to BufferLogger: info")
		blog3.warn("Log line to BufferLogger: warning")
		blog3.error("Log line to BufferLogger: error")
		blog3.success("Log line to BufferLogger: success")



# ----------------------------------------------------------------
# forward buffer content



mlog = jk_logging.MulticastLogger.create(slog, clog)

print()
mlog.info("First line, direct logging to MulticastLogger.")
with mlog.descend("Now descending ...") as mlog2:
	blog.forwardTo(mlog2)
mlog.info("Last line, direct logging to MulticastLogger.")
print()

# ----

#jk_json.saveToFilePretty(blog.toJSON(), "out1.json")
blog2 = jk_logging.BufferLogger.create(blog.toJSON())
#jk_json.saveToFilePretty(blog2.toJSON(), "out2.json")

mlog2 = jk_logging.MulticastLogger.create(slog2, clog)

print()
mlog2.info("First line, direct logging to MulticastLogger.")
with mlog2.descend("Now descending ...") as mlog22:
	blog2.forwardTo(mlog22)
mlog2.info("Last line, direct logging to MulticastLogger.")
print()



# ----------------------------------------------------------------
# verify



EXPECTED = jk_testing.utils.StringList.fromSequenceWithTabs([
	"[DEBUG TIMESTAMP 0]       INFO: First line, direct logging to MulticastLogger.",
	"[DEBUG TIMESTAMP 1]       INFO: Now descending ...",
	"	[DEBUG TIMESTAMP 2]      DEBUG: Log line to BufferLogger: debug",
	"	[DEBUG TIMESTAMP 3]     NOTICE: Log line to BufferLogger: notice",
	"	[DEBUG TIMESTAMP 4]       INFO: Log line to BufferLogger: info",
	"	[DEBUG TIMESTAMP 5]    WARNING: Log line to BufferLogger: warning",
	"	[DEBUG TIMESTAMP 6]      ERROR: Log line to BufferLogger: error",
	"	[DEBUG TIMESTAMP 7]    SUCCESS: Log line to BufferLogger: success",
	"	[DEBUG TIMESTAMP 8]       INFO: Descending ...",
	"		[DEBUG TIMESTAMP 9]      DEBUG: Log line to BufferLogger: debug",
	"		[DEBUG TIMESTAMP 10]     NOTICE: Log line to BufferLogger: notice",
	"		[DEBUG TIMESTAMP 11]       INFO: Log line to BufferLogger: info",
	"		[DEBUG TIMESTAMP 12]    WARNING: Log line to BufferLogger: warning",
	"		[DEBUG TIMESTAMP 13]      ERROR: Log line to BufferLogger: error",
	"		[DEBUG TIMESTAMP 14]    SUCCESS: Log line to BufferLogger: success",
	"		[DEBUG TIMESTAMP 15]       INFO: Descending ...",
	"			[DEBUG TIMESTAMP 16]      DEBUG: Log line to BufferLogger: debug",
	"			[DEBUG TIMESTAMP 17]     NOTICE: Log line to BufferLogger: notice",
	"			[DEBUG TIMESTAMP 18]       INFO: Log line to BufferLogger: info",
	"			[DEBUG TIMESTAMP 19]    WARNING: Log line to BufferLogger: warning",
	"			[DEBUG TIMESTAMP 20]      ERROR: Log line to BufferLogger: error",
	"			[DEBUG TIMESTAMP 21]    SUCCESS: Log line to BufferLogger: success",
	"[DEBUG TIMESTAMP 22]       INFO: Last line, direct logging to MulticastLogger.",
])

received = jk_testing.utils.StringList.fromSequenceWithTabs(slog.toList())

print()
if EXPECTED == received:
	print(">> slog: as expected")
else:
	print(">> slog: differs from expected!")
jk_testing.utils.StringListDiff(
	"expected",
	EXPECTED,
	"encountered",
	received,
).dump()
print()


received2 = jk_testing.utils.StringList.fromSequenceWithTabs(slog2.toList())

print()
if EXPECTED == received:
	print(">> slog2: as expected")
else:
	print(">> slog2: differs from expected!")
jk_testing.utils.StringListDiff(
	"expected",
	EXPECTED,
	"encountered",
	received,
).dump()
print()


















