from . import random_letter

GRID_DIMENSIONS = 4

def get_directions():
	base_directions = range(-1, 2)
	return [(row, column)
		for row in base_directions
		for column in base_directions
		if row or column
	]

DIRECTIONS = get_directions()

class BoggleBoard(object):
	def __init__(self, dimensions=None, letters=None):
		self._dimensions = dimensions or GRID_DIMENSIONS
		self._letters = letters or self._random_letters()
		assert len(self._letters) == self._dimensions
		for row in self._letters:
			assert len(row) == self._dimensions

	@staticmethod
	def _random_letters():
		random_letter_generator = random_letter.RandomLetterGenerator()
		return [
				[random_letter_generator.get_letter() for _i in range(GRID_DIMENSIONS)]
			for _j in range(GRID_DIMENSIONS)
		]

	def get_all_indexes(self):
		return [(row, column) for row in range(self._dimensions) for column in range(self._dimensions)]

	def get_links(self, index):
		base_row, base_column = index
		locations = [(base_row + i, base_column+j) for (i, j) in get_directions()]
		return [(i, j) for (i, j) in locations if self._valid_dimensions(i, j)]

	def _valid_dimensions(self, i, j):
		return  0 < i < self._dimensions and 0 < j < self._dimensions

	def get_index(self, index):
		row, column = index
		return self._letters[row][column]

	def __str__(self):
		return '\n'.join('|'.join(row) for row in self._letters)
