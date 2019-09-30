#!/usr/bin/env python3



import jk_logging




cfg = {
	"main": {
		"style": "static",
		"type": "ConsoleLogger"
	},
	"extra": {
		"style": "dynamic",
		"type": "ConsoleLogger"
	},
	"mixed": {
		"dynamic": {
			"type": "FileLogger",
			"filePath": "./log-test-$(id).log",
			"rollOver": None
		},
		"static": {
			"type": "ConsoleLogger"
		},
	}
}





logMgr = jk_logging.LoggerInstanceManager(cfg)

logger = logMgr.getCreateLogger("main")
logger.info("Test")

logger = logMgr.getCreateLogger("extra", "foo")
logger.info("Test")

logger = logMgr.getCreateLogger("mixed")
logger.info("Test")

logger = logMgr.getCreateLogger("mixed", "foo")
logger.info("Test")



