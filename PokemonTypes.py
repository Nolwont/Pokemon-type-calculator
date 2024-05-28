class PokemonType(object):
	"""docstring for PokemonType"""
	def __init__(self, name):
		super(PokemonType, self).__init__()
		self.name = name

	def addTypeInteractions(self,weak,resist,immune):
		self.weak=weak
		self.resist=resist
		self.immune=immune