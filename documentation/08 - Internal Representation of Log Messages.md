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

| Field index	| Data type			| Field name			| Description												|
| ------------- | ----------------- | --------------------- | --------------------------------------------------------- |
| 0				| `str`				| `sType`				| The type of the log entry: "txt", "ex", "desc"			|
| 1				| `int`				| `logEntryID`			| The ID of the log entry or `None` if unused				|
| 2				| `int`				| `indentationLevel`	| The indentation level										|
| 3				| `str`				| `parentLogEntryID`	| The ID of the parent log entry or `None` if unused		|
| 4				| `float`			| `timeStamp`			| The time stamp in seconds since epoch						|
| 5				| `EnumLogLevel`	| `logLevel`			| The type of the log entry									|

There will be additional fields depending on the type of log entry.



Additonal Data for Text Entries (Type: "`txt`")
----------------------------------------------------------------

Additionally a text message entry will have the following field:

| Field index	| Data type			| Field name			| Description												|
| ------------- | ----------------- | --------------------- | --------------------------------------------------------- |
| 6				| `str`				| `logMsg`				| The text of the log message								|



Additonal Data for Exception Entries (Type: "`ex`")
----------------------------------------------------------------

Additionally an exception log message entry will have the following field:

| Field index	| Data type			| Field name			| Description												|
| ------------- | ----------------- | --------------------- | --------------------------------------------------------- |
| 6				| `str`				| `exClass`				| The exception class name									|
| 7				| `str`				| `exMsg`				| The exception text message								|
| 8				| `list`			| `exStackTrace`		| A `list` or `tuple` of stack trace elements (or `None`)	|

### Stack Trace Elements

Each stack trace element is a `tuple` and consist of the following fields:

| Field index	| Data type			| Field name			| Description												|
| ------------- | ----------------- | --------------------- | --------------------------------------------------------- |
| 0				| `str`				| `filePath`			| The path of the source code file							|
| 1				| `int`				| `lineNo`				| The line number in the source code file					|
| 2				| `str`				| `moduleName`			| The source code module name (optional)					|
| 3				| `str`				| `sourceCode`			| The line in plain text where the error occurred			|



Additonal Data for Descending Entries (Type: "`desc`")
----------------------------------------------------------------

Additionally a descending log message entry will have the following field:

| Field index	| Data type			| Field name			| Description												|
| ------------- | ----------------- | --------------------- | --------------------------------------------------------- |
| 6				| `str`				| `logMsg`				| The text of the log message								|
| 7				| `list`			| `nestedList`			| A `list` for nested log messages							|

