Implementation Details
======================

Internal Representation of Log Messages
---------------------------------------

As a user you don't have to know and take care of raw log messages: If you are using the log API within
your computer program you will not get in contact with these data structures. Only if you implement your
own loggers or log message formatters you will need to know about these data structures. For that purpose
they are discussed here.

The raw log messages are represented as tuples in Python. There are three kinds of raw log messages generated:

* A text message (identifier: `txt`)
* An exception message (identifier: `ex`)
* Descending to a nested level with text message (identifier: `desc`)

#### Basic Fields

All log entries will contain the following fields in raw format:

* `str` : The type of the log entry: "txt", "ex", "desc"
* `str` : The ID of the log entry or `None` if unused
* `int` : The indentation level
* `str` : The ID of the parent log entry or `None` if unused
* `float` : The time stamp in seconds since epoch
* `EnumLogLevel` : The type of the log entry

#+## Additonal Fields

Additionally a text message entry will have the following field:

* `str` : The text of the log message

Additionally a descending log message entry will have the following field:

* `str` : The text of the log message
* `list` : A list of nested log messages

Additionally an exception log message entry will have the following field:

* `str` : The exception class name
* `str` : The exception text
* `int` : A list of stack trace elements or `None`

Each stack trace element will in turn be a tuple and consist of the following fields:

* `str` : The source code file path
* `int` : The source code line number
* `str` : The source code module name
* `str` : The source code line in plain text where the error occurred






