#!/usr/bin/python3


import sys

import jk_logging



with jk_logging.wrapMain() as log:

	with log.descend("Nested ...") as log2:

		raise Exception("Some exception")

	#

#



"""
This test will print:

[2021-01-04 16:54:05]       INFO: Nested ...
	[2021-01-04 16:54:05] STACKTRACE: ./test_wrapMain_c.py:14 <module>    # raise Exception("Some exception")
	[2021-01-04 16:54:05]  EXCEPTION: Exception: Some exception

And then exit gracefully with exit code 1.
"""








