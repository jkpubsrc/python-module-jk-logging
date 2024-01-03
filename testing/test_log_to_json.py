#!/usr/bin/env python3


import json

import jk_logging



def fail():
	raise Exception("Foo bar ex")
#



blog = jk_logging.BufferLogger.create()
with blog.descend("Descending ...") as blog2:
	blog2.debug("debug")
	blog2.notice("notice")
	blog2.info("info")
	blog2.warn("warn")
	blog2.error("error")
	blog2.exception("exception")
	with blog2.descend("Descending even deeper ...") as blog3:
		blog3.notice("Foo bar")
		try:
			fail()
		except Exception as ee:
			blog3.exception(ee)
		#blog3.exception(Exception("Foo bar ex"))

blog.forwardTo(jk_logging.ConsoleLogger.create())

jData = blog.toJSON()

print()
print(json.dumps(jData, indent="\t", sort_keys=True))
print()

blogB = jk_logging.BufferLogger.create(jData)
blogB.forwardTo(jk_logging.ConsoleLogger.create())











