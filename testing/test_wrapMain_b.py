#!/usr/bin/python3


import jk_logging



with jk_logging.wrapMain() as log:

	raise Exception("Some exception")

#









"""
This test will print:

[2021-01-04 16:55:20] STACKTRACE: ./test_wrapMain_b.py:10 <module>    # raise Exception("Some exception")
[2021-01-04 16:55:20]      ERROR: Exception: Some exception

And then exit gracefully with exit code 1.
"""









