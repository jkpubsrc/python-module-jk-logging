The LoggerInstanceManager
=========================

This class is a simple manangement class for automatic creation of logger instances.

You will very likely **not** require to use this class as you will very likely either instantiate your loggers explicitely or provide an explicite specification for how to instantiate a logger from within a configuration file of your application. This management class is provided for the specific purpose that you will require a variety of loggers based on a configuration template and need to create these loggers dynamically as needed.

To give an example: This might be required if you have a multi-threaded application and want to monitor the log activity of each thread individually, and your program even decides dynamically which threads to spawn. In this situation an instance of `LoggereInstanceManager` might exactly be what you need.

Specifying a configuration for LoggerInstanceManager
----------------------------------------------------

The configuration you need to provide for an instance of `LoggereInstanceManager` is a dictionary where it's keys rerpresent a so called log category and it's associated values represent either a set of styles (containing a log configuration) a log configuration itself with a "style" keyword.

Example:

```python
cfg = {
	"main": {
		"style": "static",
		"type": "ConsoleLogger"
	},
	"extra": {
		"type": "FileLogger",
		"filePath": "./log/test-A-$(id).log",
		"rollOver": None
	},
	"mixed": {
		"dynamic": {
			"type": "FileLogger",
			"filePath": "./log/test-B-$(id).log",
			"rollOver": None
		},
		"static": {
			"type": "ConsoleLogger"
		},
	}
}
```

This configuration provided above will define three different categories:
* `main`, which (for simplicity) defines a `ConsoleLogger`
* `extra`, which (for simplicity) defines a `FileLogger`
* `mixed`, which defines a static `ConsoleLogger` and a dynamic logger `FileLogger`.

"Static" in this context means this configuration will not change and is not dependend on an identifier. "Dynamic" in this context means this configuration will be adapted according to an identifier specified. Adaption means that each string value will be searched for certain variables which - if found - are replaced accordingly. These variables are:

* `category` which will be replaced by the category name specified
* `id` which will be replaced by the logger identifier specified

So if an identifier is specified with the `createLogger()` method *and* the logger contains a configuration of style "dynamic" the value `"./log/test-B-$(id).log"` will be replaced by `"./log/test-B-myid.log"` (if `"myid"` was the identifier specified).

All things must fit: If you want to instantiate a dynamic or static logger for a certain category
* you must provide a configuration for this category, and
* you must provide an appropriate dynamic or static configuration.

Instantiating the LoggerInstanceManager
---------------------------------------

If you have a configuration ready at hand you can instantiate the `LoggerInstanceManager` as follows:

```python
logMgr = jk_logging.LoggerInstanceManager(cfg)
```

Now you're ready to instantiate loggers.

Please be aware that the configuration is parsed dynamically as needed. No prior check is applied if the configuration specified is correct. Therefor you will experience exceptions at runtime if your configuration contains errors.

Instantiating loggers
---------------------

A "static" logger can be instantiated like this:

```python
log = logMgr.getCreateLogger("mixed")
```

Please note that no identifier is specified for `getCreateLogger()`, just a category name. This indicates that you want to instantiate a "static" logger. That implies that you have provided a suitabl configuration for `"mixed"` earlier at instantiation.

A "dynamic" logger can be instantiated like this:

```python
log = logMgr.getCreateLogger("mixed", "myid")
```

Please note that to create "dynamic" loggers an identifier `"myid"` is specified here for `getCreateLogger()`, not just a category name. That implies that you have provided a suitabl configuration for `"mixed"` earlier at instantiation.









