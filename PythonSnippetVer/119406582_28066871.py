import weakref
class Single(object):

	_instance = None

	def __init__(self):
		print "I've been born"

	def __del__(self):
		print "I'm dying"

	@classmethod
	def get_instance(cls):
		if cls._instance is not None and cls._instance() is not None:
			return cls._instance()
		instance = cls()
		cls._instance = weakref.ref(instance)
		return instance