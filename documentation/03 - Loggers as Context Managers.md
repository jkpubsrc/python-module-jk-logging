Loggers as Context Managers
===========================

For convenience loggers are context managers. This simplifies logging errors. Let's explain this example based in the next sections.

Using Loggers with descend()
----------------------------

Please have a look at this example:

```python
clog = ConsoleLogger()

with clog.descend("Now we run the following in an own context") as log:
	log.debug("This is a test for DEBUG.")
	log.notice("This is a test for NOTICE.")
	log.info("This is a test for INFO.")
	log.warning("This is a test for WARNING.")
```

In this example a console logger is created first. This is necessary to have an instance in order to make then use of this feature. This feature is demonstrated in line three: The `with` statement is used to create a context and store it in a variable, which is named `log` here for simplicity. `log` will now contain a console logger that descends from the original one. The following lines then just demonstrate how to produce some output.

The overall output of the lines above will look like this:

```
[2018-01-26 21:53:10]       INFO:  Now we run the following in an own context
	[2018-01-26 21:53:10]      DEBUG:  This is a test for DEBUG.
	[2018-01-26 21:53:10]     NOTICE:  This is a test for NOTICE.
	[2018-01-26 21:53:10]       INFO:  This is a test for INFO.
	[2018-01-26 21:53:10]    WARNING:  This is a test for WARNING.
```

Note: It is mandatory to use a variable name different than `clog`. Variables declared within `with`-based contexts do not automatically seize to exit if the context ends. Therefor a statement such as `with clog.descend(...) as clog` would have replaced `clog` with the nested logger. The consequence: As nested logger will now be kept in `clog` the original parent level logger is lost. Future log attempts below the `with`-context will therefor never be able to make use of the original logger.

Logging Errors in a Context
---------------------------

Please have a look at this example:

```python
with clog.descend("Now let's try to have an exception in a context") as log:
	log.notice("Now let's try a calculation that will fail ...")
	produceError()
```

Please assume that `produceError()` is a method that will fail and raise an exception in consequence.

The context used in this will automatically perform logging for you. Therefor the lines above will lead to the following output:

```
[2018-01-26 21:53:10]       INFO:  Now let's try to have an exception in a context
	[2018-01-26 21:53:10]     NOTICE:  Now let's try a calculation that will fail ...
	[2018-01-26 21:53:10]   EXCEPTION:  ZeroDivisionError: division by zero
	[2018-01-26 21:53:10]  STACKTRACE:  ./test-context-manager.py:48 <module>    # produceError()
	[2018-01-26 21:53:10]  STACKTRACE:  ./test-context-manager.py:40 produceError    # c = a / b
```

As you can see the exception is automatically logged. The stacktrace is printed in reverse order so that the topmost stack frame will be printed last: The last line is the line you then need to look for the reason for this exeption. In our case it has been a statement that always causes an exception in order to be able to demonstrate that feature.

Logging Errors in Nested Contexts
---------------------------------

Please have in mind that such a context will - to some extend - "swallow" the exception raised. An exception still get's raised by the context but this will not be the original exception but a replacement exception instead. Let's have a look at the following example to understand why:

```python
with clog.descend("Now let's try to have an exception in a context") as log:
	log.notice("We do something ...")
	log.notice("We do something more ...")
	with log.descend("Now let's try to have an exception in a context") as log2:
		log2.notice("Now let's try a calculation that will fail ...")
		produceError()
	log.notice("We would like to do something else here but that's not possible because of the exception raised.")
```

Here we descend into some more fine grained activity where the error occurs. Of course this could be the case by invoking another method as well: This example just is kept very simple in order to let you focus on the feature currently discussed.

Here in the second context an exception is raised. This will cause the context to log the error immediately. Then a replacement exception is raised. This is the only way to tell the wrapping context in python to terminate: A context must receive an exception in order to terminate. Nevertheless the logging context are implemented in such a way so that they don't output these replacement exceptions. This will cause only the innermost context to log the exception, all outer contexts will ignore it.

So the output of the example above will look like this:

```
[2018-01-26 22:29:23]       INFO:  Now let's try to have an exception in a context
	[2018-01-26 22:29:23]     NOTICE:  We do something ...
	[2018-01-26 22:29:23]     NOTICE:  We do something more ...
	[2018-01-26 22:29:23]       INFO:  Now let's try to have an exception in a context
		[2018-01-26 22:29:23]     NOTICE:  Now let's try a calculation that will fail ...
		[2018-01-26 22:29:23]   EXCEPTION:  ZeroDivisionError: division by zero
		[2018-01-26 22:29:23]  STACKTRACE:  ./test-context-manager.py:67 <module>    # produceError()
		[2018-01-26 22:29:23]  STACKTRACE:  ./test-context-manager.py:40 produceError    # c = a / b
```

Please have in mind that even the outer context will raise an exception. An interruption caused somewhere deep within your code - here intentionally done in `prduceError()` for demonstration purposes - must not be swalled but passed on to the top most level of your program. In that case here you might simply discard the (replacement) exception received from the outmost context as the error already has been logged. And you probably want to terminate your program with exit code 1 in such a situation.





