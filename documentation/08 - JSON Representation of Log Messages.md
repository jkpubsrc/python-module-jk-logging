JSON Representation of Log Messages
================================================================

For log messages stored as JSON specific JSON data formats are used. The next section(s) describe details of these data formats.

BufferLogger
----------------------------------------------------------------

The following loggers are capable of producing JSON data:

* `BufferLogger`

General JSON format
----------------------------------------------------------------

All JSON data produced will be conform to the following general structure:

```JavaScript
{
	"magic": {
		"magic": ....,
		"version": ....
	},
	....
}
```

As you can see the root element of the JSON is a JSON object/dictionary with at least one main proprety:

* "`magic`": Contains a JSON object that precisely identifies the data format used. This property is mandatory and always present.

The `magic` section
----------------------------------------------------------------

The `magic` main section in the JSON data is mandatory. It defines the format of the JSON data. Everything else except of the `magic` section depends on this format.

Via this `magic` section the exact type of the file format is specified. The following properties in this section are used:

* "`str magic`" : Defines a string identifier that names the exact type of the file format.
* "`int version`" : Defines a version identifier for the file format.

The following file format types are supported:

| `magic`					| `version`				|
| ---						| ---					|
| "jk-logging-compact"		| 1						|
| "jk-logging-verbose"		| 1						|

Structure common to all file formats
----------------------------------------------------------------

All file formats will have the following main sections:

* "`logData`": Contains a JSON list. Each list entry is a JSON data structure representing a single log entry. This property is mandatory and always present. The exact format of these log entries listed here depend on the file format. See below.
* `extraProperties` : Contains a JSON object with extra key value pairs. This property is optional and may be omitted. If omitted this means that no extra key value pairs are associated with this group of log entries. All file formats will follow the same conventions here in storing data. See below.

Therefore a typical layout of JSON data will be:

```JavaScript
{
	"magic": {
		"magic": ....,
		"version": ....
	},
	"logData": [
		....
	],
	"extraProperties": {
		....
	},
}
```

The `extraProperties` section
----------------------------------------------------------------

If present `extraProperties` always holds a JSON object/dictionary with zero or more key value pairs.

The keys must be strings. The values can be of any type that is supported by JSON.

Example:

```JavaScript
{
	"foo": "bar",
	"foobar": 123456,
	"more data": null,
	"and even more data": [ true, false, 1.23, "abc", {} ],
}
```

`jk-logging-compact`, version 1, section `logData`
----------------------------------------------------------------

In compact form log data consists of log entries.
Each log entry is represented by a list.
The first field in this list determines the exact nature of such a log entry.

The following different log entries exist:

* Type "`txt`"
	* A regular text entry.
	* Text entries have 4 fields:
		* Element 0 `str type` : containing "`txt"`"
		* Element 1 `float timeStamp` : containing the time stamp in seconds since Epoch
		* Element 2 `int logLevel` : The integer representation of the log level
		* Element 3 `str logMsg` : The log message
* Type "`desc`"
	* A descending log entry.
	* Text entries have 5 fields:
		* Element 0 `str type` : containing "`desc"`"
		* Element 1 `float timeStamp` : containing the time stamp in seconds since Epoch
		* Element 2 `int logLevel` : The integer representation of the log level
		* Element 3 `str logMsg` : The log message
		* Element 4 `list children` : Zero, one or more child log entries of the same kind as defined here.
* Type "`ex`"
	* An exception entry.
	* Text entries have 6 fields:
		* Element 0 `str type` : containing "`ex"`"
		* Element 1 `float timeStamp` : containing the time stamp in seconds since Epoch
		* Element 2 `int logLevel` : The integer representation of the log level
		* Element 3 `str exClass` : The class name of the exception
		* Element 4 `str exMsg` : The message stored in the exception object that has been raised
		* Element 5 `list exStackTrace` : Zero, one or more stack trace entries.

Stack trace entries as used by `ex` type are JSON lists and have the following fields:
* `str filePath` : The path of the source code file the exception has been raised in.
* `int lineNo` : The line number of where the exception has been raised.
* `str moduleName` : A module name (if available).
* `str sourceCode` : The source code line itself (if available) where the error occurred.

`jk-logging-verbose`, version 1, section `logData`
----------------------------------------------------------------

In compact form log data consists of log entries.
Each log entry is represented by a JSON object/dictionary.
The value associated with "`type`" in this object/dictionary determines the exact nature of such a log entry.

The following different log entries exist:

* Type "`txt`"
	* A regular text entry.
	* Text entries have these key value pairs:
		* `str type` : containing "`txt"`"
		* `obj timeStamp` : containing a JSON object representing the time stamp in seconds since Epoch
		* `list logLevel` : The log level. Data is stored as a list with exactly two values:
			* Element 0: The integer representation of the log level
			* Element 1: The string representation of the log level
		* `str text` : The log message
* Type "`desc`"
	* A descending log entry.
	* Text entries have 5 fields:
		* `str type` : containing "`txt"`"
		* `obj timeStamp` : containing a JSON object representing the time stamp in seconds since Epoch
		* `list logLevel` : The log level. Data is stored as a list with exactly two values:
			* Element 0: The integer representation of the log level
			* Element 1: The string representation of the log level
		* `str text` : The log message
		* `list children` : Zero, one or more child log entries of the same kind as defined here.
* Type "`ex`"
	* An exception entry.
	* Text entries have 6 fields:
		* `str type` : containing "`txt"`"
		* `obj timeStamp` : containing a JSON object representing the time stamp in seconds since Epoch
		* `list logLevel` : The log level. Data is stored as a list with exactly two values:
			* Element 0: The integer representation of the log level
			* Element 1: The string representation of the log level
		* `str exception` : The class name of the exception
		* `str text` : The message stored in the exception object that has been raised
		* `list stacktrace` : Zero, one or more stack trace entries.

Stack trace entries as used by `ex` type are JSON object/dictionary entries and have the following fields:
* `str file` : The path of the source code file the exception has been raised in.
* `int line` : The line number of where the exception has been raised.
* `str module` : A module name (if available).
* `str sourceCode` : The source code line itself (if available) where the error occurred.

Time stamps in all entries are JSON object/dictionary entries and have the following fields:
* `float t` : The time stamp in seconds since Epoch
* `int year` : Year
* `int month` : Month
* `int day` : Day
* `int hour` : Hour
* `int minute` : Minute
* `int second` : Seconds
* `int ms` : Milliseconds
* `int us` : Microseconds

Please note that `t` is specified in UTC while all other time information is specified in local time for convenience.









