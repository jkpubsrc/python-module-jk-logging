#!/usr/bin/python3

#
# This is a simple example taken from https://stackoverflow.com/questions/63700879/python-try-except-block-re-raising-exception/63703359
# It does not do complex error handling, so if you execute this program you will encounter a stack trace such as this:
#
# ```
# Traceback (most recent call last):
#   File "./example_simple_1a.py", line 29, in <module>
#     bar(6)
#   File "./example_simple_1a.py", line 25, in bar
#     return foo(a, 0)
#   File "./example_simple_1a.py", line 22, in foo
#     return a / b
# ZeroDivisionError: division by zero
# ```
#



def foo(a, b):
	return a / b

def bar(a):
	return foo(a, 0)



bar(6)








