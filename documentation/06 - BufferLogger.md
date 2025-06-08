BufferLogger
============

General Description
-------------------

The `BufferLogger` logger writes all log messages to an internal buffer. Later on you can work with the collected log messages.

Forwarding Data
---------------

**TODO**

Converting Data to JSON
-----------------------

The buffer logger is capable of convering the log data to a JSON data structure. This is convienent if you want to analyse or postprocess
this data or simply format this data in HTML pages.

In obtain data as JSON you need to invoke the method `getDataAsPrettyJSON()` on the instance of a `BufferLogger`. This function will then
return a *list of data records*. Every data record will be a JSON object and have the following properties:

| Property     | Data Type | Regular Log Text | Log Descent | Log Exception | Log Exception | Description                                                                                                                                      |
|--------------|-----------|------------------|-------------|---------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `type`       | `str`     | `"txt"`          | `"desc"`    | `"ex"`        | `"ex2"`       | Stores the type of the log entry.                                                                                                                |
| `id`         | `int`     | (yes)            | (yes)       | (yes)         | (yes)         | A numeric ID of the log entry.                                                                                                                   |
| `indent`     | `int`     | (yes)            | (yes)       | (yes)         | (yes)         | The current indentation level of this log entry, starting at zero.                                                                               |
| `timestamp`  | `obj`     | (yes)            | (yes)       | (yes)         | (yes)         | A time stamp record (see below).                                                                                                                 |
| `loglevel`   | `str`     | (yes)            | (yes)       | (yes)         | (yes)         | The log level. One of the following strings: "TRACE", "DEBUG", "NOTICE", "INFO", "STDOUT", "SUCCESS", "WARNING", "ERROR", "STDERR", "EXCEPTION". |
| `logleveln`  | `int`     | (yes)            | (yes)       | (yes)         | (yes)         | The log level. One of the following integers: 10, 20, 30, 40, 41, 50, 60, 70, 71, 80.                                                            |
| `text`       | `str`     | (yes)            | (yes)       | (yes)         | (yes)         | The log message. In case of an exception this is the text message of an exception raised.                                                        |
| `exception`  | `str`     | -                | -           | (yes)         | (yes)         | The class name of the exception raised.                                                                                                          |
| `stacktrace` | `list`    | -                | -           | (yes)         | (yes)         | A list of stack trace elements (see below).                                                                                                      |
| `children`   | `list`    | -                | (yes)       | -             | -             | A list of nested log messages.                                                                                                                   |
| `exValues`   | `dict`    | -                | -           | -             | (yes)         | A map of key value paris.                                                                                                                        |

A time stamp record is a JSON object and has the following properties:

| Property | Data Type | Description                                    |
|----------|-----------|------------------------------------------------|
| `t`      | `float`   | The time stamp in seconds since epoch.         |
| `year`   | `int`     | The year in local time (not UTC).              |
| `month`  | `int`     | The month in local time (not UTC).             |
| `day`    | `int`     | The day in local time (not UTC).               |
| `hour`   | `int`     | The hour in local time (not UTC).              |
| `minute` | `int`     | The minute in local time (not UTC).            |
| `second` | `int`     | The second in local time (not UTC).            |
| `ms`     | `int`     | The millisecond value in local time (not UTC). |
| `us`     | `int`     | The microsecond value in local time (not UTC). |

Every stack trace element is a JSON object and has the following properties:

| Property     | Data Type | Description                                                  |
|--------------|-----------|--------------------------------------------------------------|
| `file`       | `str`     | The source code file path.                                   |
| `line`       | `int`     | The source code line number.                                 |
| `module`     | `str`     | The source code module name.                                 |
| `sourcecode` | `str`     | The source code line in plain text where the error occurred. |













