#!/usr/bin/env python3



import os
import typing

import jk_typing
import jk_utils
import jk_logging
import jk_json
import jk_prettyprintobj







with jk_logging.wrapMain() as log:

	print("-")

	with log.descend("Now descending (without error) ...", bWithhold=True) as log2:
		log2.notice("Foo Bar")
		with log2.descend("Descending once more ...") as log3:
			log3.notice("Foo Bar 2")

	#

	print("-")

	with log.descend("Now descending (with error) ...", bWithhold=True) as log2:
		log2.notice("Foo Bar")
		with log2.descend("Descending once more ...") as log3:
			raise Exception("Some exception")

	#

	print("-")

#












