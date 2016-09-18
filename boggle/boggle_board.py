from . import random_letter

GRID_DIMENSIONS = 5

def get_directions():
	base_directions = range(-1,2)
	return [(row, column)
		for row in base_directions
		for column in base_directions
		if row or column
	]

DIRECTIONS = get_directions()

class BoggleBoard(object):
	def __init__(self, letters=None):
		self._letters = letters or self._random_letters()

	@staticmethod
	def _random_letters():
		random_letter_generator = random_letter.RandomLetterGenerator()
		return [
				[random_letter_generator.get_letter() for i in range(GRID_DIMENSIONS)]
			for j in range(GRID_DIMENSIONS)
		]

	def __str__(self):
		return '\n'.join('|'.join(row) for row in self._letters)
