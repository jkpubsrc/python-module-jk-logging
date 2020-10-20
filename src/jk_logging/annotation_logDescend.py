


import jk_logging






def logDescend(logText, bWithFinalSuccessMsg:bool = False):
	if isinstance(logText, str):
		fLogText = None
	elif callable(logText):
		fLogText = logText
		logText = None
	else:
		raise Exception("Log text expected!")

	assert isinstance(bWithFinalSuccessMsg, bool)

	def wrapper(func):
		def func_wrapper(*args, **kwargs):
			if args:
				log = args[-1]
				if log is None:
					retVal = func(*args, **kwargs)
					return retVal
				elif isinstance(log, jk_logging.AbstractLogger):
					with log.descend(fLogText(args[0]) if fLogText else logText) as log2:
						args2 = list(args)
						args2[-1] = log2
						retVal = func(*args2, **kwargs)
						if bWithFinalSuccessMsg:
							log2.success("Success.")
						return retVal
				else:
					print("WARNING: Function wrapped did not receive a valid logger: " + str(func))
					retVal = func(*args, **kwargs)
					return retVal
			elif "log" in kwargs:
				log = kwargs["log"]
				if isinstance(log, jk_logging.AbstractLogger):
					with log.descend(fLogText(args[0]) if fLogText else logText) as log2:
						kwargs2 = dict(kwargs)
						kwargs2[log] = log2
						retVal = func(*args, **kwargs2)
						if bWithFinalSuccessMsg:
							log2.success("Success.")
						return retVal
				elif log is None:
					retVal = func(*args, **kwargs)
					return retVal
				else:
					print("WARNING: Function wrapped did not receive a valid logger: " + str(func))
					retVal = func(*args, **kwargs)
					return retVal
			else:
				print("WARNING: Function wrapped that does not have a logger: " + str(func))
		#

		return func_wrapper
	#

	return wrapper
#










