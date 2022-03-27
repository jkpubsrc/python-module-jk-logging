This file contains the approximate history of the changes this module has experienced. Unfortunately it is not complete but it provides enough information for developers to see where major changes occurred and how they affect their own software using `jk_logging`.

* 2020-01-23
	* Fixing bug in log message type detection (DetectionLogger);

* 2020-01-31
	* Colors modified; order of excetion text and stacktrace lines modified;

* 2020-12-17
	* Major reformatting and cleanup (without functional changes);

* 2020-12-17
	* Renaming the existing `DetectionLogger` to `DetectionLogger_v0`;

* 2020-12-17
	* Providing a completely new implementation of `DetectionLogger` with a much better architecture and API;

* 2020-12-17
	* Added a variety of bugfixes to test cases as the test cases unfortunately had errors (not the implementation);

* 2021-01-04
	* Improved `wrapMain()` to exit gracefully as expected if `sys.exit()` is invoked.

* 2021-01-14
	* Bug fixed in LogStats returning information about maximum log level

* 2021-03-02
	* Added additional variables for building file paths

* 2021-04-07
	* Extended the processing of log data
	* Added interface `ILogger`

* 2021-11-25
	* Beginning: Enhancements in log message buffering
	* Refactoring
	* JSON serialization
	* Improved documentation

* 2021-12-08
	* Added: descend() now supports log level NOTICE and INFO

* 2021-12-14
	* Improved: Interrupting generators

* 2022-01-29
	* Improved: descend() now using type hinting

* 2022-03-27
	* Added: Example `example_catch_and_print.py`


