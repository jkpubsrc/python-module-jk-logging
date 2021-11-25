



class IDCounter(object):

	################################################################################################################################
	## Constants
	################################################################################################################################

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self):
		self.__value = 0
	#

	################################################################################################################################
	## Properties
	################################################################################################################################

	@property
	def value(self):
		return self.__value
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def next(self):
		v = self.__value
		self.__value += 1
		return v
	#

	def __int__(self):
		return self.__value
	#

	def __str__(self):
		return str(self.__value)
	#

	def __repr__(self):
		return str(self.__value)
	#

#




