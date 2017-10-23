
from random import choice
from colors import Gold, Blue, Red, Yellow, Orange, Black, White, Purple, Silver

#places = [] or {}
#places connected by paths

path = {}
places = {}

places['A'] = generate_colors()
places['B'] = generate_colors()
places['C'] = generate_colors()
places['D'] = generate_gold()

path['A-D'] = 1 #connected
path['A-B'] = 1
path['B-C'] = 1
path['C-D'] = 1

def random_color():
	return choice([Gold, Blue, Red, Yellow, Orange, Black, White, Purple, Silver])

def generate_colors(amount = 12)
	
	l = []
	for i in range(1, amount):
		l.append(random_color())

	return l

def generate_gold():
	pass