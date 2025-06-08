Internal Representation of Log Messages
================================================================

Log messages are packed into specific data structures so that they can be processed by loggers. This is done as soon as
someone invokes something like `info(...)`. These raw log messages are then stored or forwarded, depending on which
loggers are used. Details about this raw log format is described in th the following section(s).



General Format Aspects
----------------------------------------------------------------

The raw log messages are represented as tuples in Python. There are three kinds of raw log messages generated:

* A text message (identifier: `txt`)
* An exception message (identifier: `ex`)
* Descending to a nested level with text message (identifier: `desc`)

All log entries will contain the following fields in raw format:

| Field index | Data type              | Field name         | Required? | Description                                           |
|-------------|------------------------|--------------------|-----------|-------------------------------------------------------|
| 0           | `str`                  | `sType`            | required  | The type of the log entry: "txt", "ex", "ex2", "desc" |
| 1           | `int`, `str` (unclear) | `logEntryID`       | optional  | The ID of the log entry or `None` if unused           |
| 2           | `int`                  | `indentationLevel` | required  | The indentation level                                 |
| 3           | `int`, `str` (unclear) | `parentLogEntryID` | optional  | The ID of the parent log entry or `None` if unused    |
| 4           | `float`                | `timeStamp`        | required  | The time stamp in seconds since epoch                 |
| 5           | `EnumLogLevel`         | `logLevel`         | required  | The type of the log entry                             |

*Required* means that this field can not be (null). *Optional* means that this field might be (null) if there is no data.

There will be additional fields depending on the type of log entry.



Additional Data for Text Entries (Type: "`txt`")
----------------------------------------------------------------

Additionally a text message entry will have the following field:

| Field index | Data type | Field name | Required? | Description                 |
|-------------|-----------|------------|-----------|-----------------------------|
| 6           | `str`     | `logMsg`   | required  | The text of the log message |

*Required* means that this field can not be (null). *Optional* means that this field might be (null) if there is no data.



Additional Data for Exception Entries (Type: "`ex`")
----------------------------------------------------------------

Additionally an exception log message entry will have the following field:

| Field index | Data type | Field name        | Required? | Description                                             |
|-------------|-----------|-------------------|-----------|---------------------------------------------------------|
| 6           | `str`     | `exClass`         | required  | The exception class name                                |
| 7           | `str`     | `exMsg`           | required  | The exception text message                              |
| 8           | `list`    | `exStackTrace`    | optional  | A `list` or `tuple` of stack trace elements (or `None`) |
| 9           | `list`    | `nextedException` | optional  |                                                         |

*Required* means that this field can not be (null). *Optional* means that this field might be (null) if there is no data.



Additional Data for Exception Entries (Type: "`ex2`")
----------------------------------------------------------------

Additionally an exception log message entry will have the following field:

| Field index | Data type       | Field name        | Required? | Description                                             |
|-------------|-----------------|-------------------|-----------|---------------------------------------------------------|
| 6           | `str`           | `exClass`         | required  | The exception class name                                |
| 7           | `str`           | `exMsg`           | required  | The exception text message                              |
| 8           | `list`          | `exStackTrace`    | optional  | A `list` or `tuple` of stack trace elements (or `None`) |
| 9           | `dict[str,any]` | `exValues`        | optional  | A `dict` of key value pairs (or `None`)                 |
| 10          | `list`          | `nextedException` | optional  |                                                         |

*Required* means that this field can not be (null). *Optional* means that this field might be (null) if there is no data.



### Stack Trace Elements

Each stack trace element is a `tuple` and consist of the following fields:

| Field index | Data type | Field name   | Required? | Description                                     |
|-------------|-----------|--------------|-----------|-------------------------------------------------|
| 0           | `str`     | `filePath`   | required  | The path of the source code file                |
| 1           | `int`     | `lineNo`     | required  | The line number in the source code file         |
| 2           | `str`     | `moduleName` | optional  | The source code module name (optional)          |
| 3           | `str`     | `sourceCode` | required  | The line in plain text where the error occurred |

*Required* means that this field can not be (null). *Optional* means that this field might be (null) if there is no data.



Additional Data for Descending Entries (Type: "`desc`")
----------------------------------------------------------------

Additionally a descending log message entry will have the following field:

| Field index | Data type | Field name   | Required? | Description                      |
|-------------|-----------|--------------|-----------|----------------------------------|
| 6           | `str`     | `logMsg`     | required  | The text of the log message      |
| 7           | `list`    | `nestedList` | required  | A `list` for nested log messages |

*Required* means that this field can not be (null). *Optional* means that this field might be (null) if there is no data.


