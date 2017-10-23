
class NodeColorSpace()

class Activities(object):
	pass

class Node(object):
	mediation_minutes = 0
	blue_minutes = 0
	red_minutes = 0
	silver_minutes = 0
	gold_minutes = 0
	
	# things we have // currency
	gold = 0
	silver = 0

	# communication mediums

	orange = 2
	yellow = 4
	black = 8
	red = 16

	# personal spectrum

	blue = 32
	purple = 64

	colorspace = NodeColorSpace()

	def init(self):
		pass


class NodeColorSpace(object):
	colors = []

	# (# en) black