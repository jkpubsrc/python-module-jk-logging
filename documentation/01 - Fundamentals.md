Fundamentals
============

This python module provides a logging infrastructure. It contains various classes to implement a logging infrastructure for your python application.

The primary entities of relevance are so called 'loggers'. A logger is a software component that represents an output channel for log messages.

From a programming point of view this means that a loggere provides methods someone can invoke to write log output to the logger. Whatever the logger will then do with the log message strongly depends on the log object used for logging: It may pipe log messages to a buffer, the console, to a file or even drop all log messages completely.

Some loggers can be chained, this way building a more complex logging pipe. Log message detectors can be used, filters can be provided, and with multicast loggers you can pass on log events to multiple other loggers, this way implementing branching and complex log pipes.

Another very useful feature is to write log messages to a buffer. The buffer content can then later be forwarded to other loggers, f.e. a filter or a file. This way you can decide about how to proceed with these log messages after some processing is completed. If there have been errors you might want to have a different behaviour regarding your log messages as you might want to have on success.

All that this log framework offers.

How to import this module
-------------------------

To import this module use the following statement:

```python
import jk_logging
```

The Logging Classes
-------------------

The logging framework consists of a variety of log classes that perform logging. The log classes available for use are:

* `AbstractLogger` : This is the abstract base class for all loggers.
* `BufferLogger` : This logger writes all log messages to an internal buffer. Later on you can work with the collected log messages.
* `ConsoleLogger` : This logger writes all log messages to STDOUT.
* `DetectionLogger` : This logger creates a protocol about what log levels used during logging. Later on you can work with this information.
* `FileLogger` : A logger that writes to a text file. A new text file will automatically be generated every month/day/hour.
* `FilterLogger` : A filter logger will allow only certain log messages to pass through. Please note that `FileLogger` is replacing `SimpleFileLogger`.
* `MulticastLogger` : A multicast logger will forward all log messages to other loggers.
* `NamedMulticastLogger` : A named multicast logger will forward all log messages to other loggers.
* `NullLogger` : This logger will swallow all log messages without doing anything.
* `SimpleFileLogger` : A simple logger that writes to a text file. Please consider using `FileLogger` instead: This logger is basically a more simple version of `FileLogger` and therefor will likely be removed in future versions of this module. `FileLogger` is replacing `SimpleFileLogger`.
* `StringListLogger` : A logger that stores log messages internally as a list of strings. These strings can then later be retrieved.

All logging works synchroneously.

All logging is (currently) intendet for a single threaded environments. No internal synchronization is performed to ensure that calls to loggers are atomic.

Log Levels
----------

Each log event issued by an application will be associated with a log level. This defines the criticality of your log event.

By the enumeration class `EnumLogLevel` the following log levels are supported (in increasing order):

* `TRACE`: Use this log level for very detailed debugging purposes. Consider this log level a being ven more detailed than `DEBUG`. (You might not require to use this log level in your application, but of course you can.)
* `DEBUG`: Use this log level for debugging purposes.
* `NOTICE`: Use this log level if your log messages aren't very imporant.
* `INFO`: This log level is intendet for normal log messages. This is the log level you might use most.
* `STDOUT`: This log level is used if STDOUT data is sent to this logger.
* `WARNING`: Use this log level to write out warning messages.
* `ERROR`: Use this log level to write out error messages.
* `STDERR`: This log level is used if STDERR data is sent to this logger.
* `EXCEPTION`: Use this log level to write out exceptions. Consider this as being even more cricital than `ERROR`. (You might not require to use this log level in your application, but of course you can.)

Instantiation of Loggers
------------------------

There are two ways of how to instantiate loggers:
* You can explicitely invoke a static `create(...)` method defined at each logger class. This method will then provide a logger instance. Use this method of instantiation if you want to hard code logging capabilities in your application.
* You can call `jk_logging.instantiate(...)`. For this you need to provide a configuration data structure, which basically is a dictionary with key-value pairs. The instantiate-method will then create the required logger. Use this method of instantiation if you want users to provide a log section in a configuration file to your application.

### Static Instantiation

All log objects can be instantated with a specifically designed static `create(...)` method. This design had to be chosen because the
programming language Python does not support constructor (or method) overloading. Therefor constructor methods are designed to be
used by the API itself, and the static `create(...)` methods are provided for the convenience of users.

The loggers provide the following create methods:

* `BufferLogger.create(jsonRawData = None)`
* `ConsoleLogger.create(printToStdErr = False, logMsgFormatter = None)`
* `DetectionLogger.create(logger)`
* `FileLogger.create(filePath, rollOver, bAppendToExistingFile = True, bFlushAfterEveryLogMessage = True, fileMode = 0o600, logMsgFormatter = None)`
* `FilterLogger.create(logger, minLogLevel = EnumLogLevel.WARNING)`
* `MulticastLogger.create(*argv)`
* `NamedMulticastLogger.create(**kwargs)`
* `SimpleFileLogger.create(filePath, bAppendToExistingFile = True, bFlushAfterEveryLogMessage = True, fileMode = 0o0600, logMsgFormatter = None)`
* `StringListLogger.create(logMsgFormatter = None)`

### Configuration based Instantiation

To let the logging framework instantiate a logger in response to some configuration provided you need to invoke `jk_logging.instantiate(...)`. This configuration must be a dictionary object and must - at least - contain the following keys:

* `type`: The type of the logger to instantiate, which is the class name of the logger: `BufferLogger`, `ConsoleLogger`, etc.

Depending on the logger you want to instantiate various additional key-value pairs might be required:

| Logger						| Keys														|
|:------------------------------|:----------------------------------------------------------|
| BufferLogger					| ---														|
| ConsoleLogger					| `str logMsgFormatter` (optional)							|
| DetectionLogger				| `dict nested` (required)									|
| FilterLogger					| `str minLogLevel` (optional), dict nested (required)		|
| MulticastLogger				| `list nested` (required)									|
| NamedMulticastLogger			| `dict nested` (required)									|
| NullLogger					| ---														|
| FileLogger					| `str filePath` (required), `str rollOver` (required), `bool bAppendToExistingFile` (optional), `bool bFlushAfterEveryLogMessage` (optional), `int fileMode` (optional)	|
| StringListLogger				| ---														|

Example:

```python
log = jk_logging.instantiate({
	"type": "ConsoleLogger",
	"logMsgFormatter": "color"
})
```

Logging Some Data
-----------------

In order to log data each logger provides the following methods:

* `debug(...)`
* `error(...)`
* `exception(...)`
* `info(...)`
* `notice(...)`
* `stderr(...)`
* `stdout(...)`
* `trace(...)`
* `warn(...)`
* `warning(...)`

Therefor you can log data like this:

```python
log.notice("Something has happened.")
```

Or:

```python
try:
	log.info("We are going to do some calculation.")
	x = 3
	y = 0
	z = x/y
raise Exception as e:
	log.error("The calculation has failed!")
	log.error(e)
```











