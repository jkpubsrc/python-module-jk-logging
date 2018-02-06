Extending The Framework
=======================

Implementing own log message formatters
---------------------------------------

Log message formatters are subclassed from `AbstractLogMessageFormatter` which is the base class for all these formatters. Such formatters typically implement a single method:

* `format(logEntryStruct)`

If you want to have a custom output format due to special, very propietary requirements, you can implement your own log message formatter. Just derive from that class and provide your own implementation of `format(...)`. Then pass an instance of your class to the loggers.





