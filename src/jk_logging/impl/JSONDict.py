



import typing




class JSONDict(dict):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __setitem__(self, key:str, value:typing.Union[str,int,float,bool,tuple,list,dict,None]):
		assert isinstance(key, str)
		if value is not None:
			assert isinstance(value, (str,int,float,bool,tuple,list,dict))
		super().__setitem__(key, value)
	#

#






