import contextlib
import collections
from .abstract_search import SearchState

class WordFinder(SearchState):

	def __init__(self, board, prefix_dictionary):
		self._board = board
		self._prefix_dictionary = prefix_dictionary

	def result(self):
		return self._prefix_dictionary.result()

	def get_result(self):
		return self._prefix_dictionary.get_result()

	def next_states(self):
		return [s for s in self._board.next_states() if s.letter in self._prefix_dictionary.next_states()]

	@contextlib.contextmanager
	def descend(self, s):
		with  self._board.descend(s), self._prefix_dictionary.descent(s.letter):
			yield


BoardPos = collections.namedtuple('BoardPos', 'location, letter')

class BoardState(SearchState):
	def __init__(self, boggle_board):
		self._base_board = boggle_board
		self._visited = []


	def result(self):
		pass

	def get_result(self):
		pass

	def next_states(self):
		return [BoardPos(location, self._base_board.get_index(location)) for location in self._get_locations() if location not in self._visited]

	def _get_locations(self):
		if not self._visited:
			return self._base_board.get_all_indexes()
		else:
			return self._base_board.get_links(self._visited[-1])

	@contextlib.contextmanager
	def descend(self, s):
		try:
			self._visited.append(s.location)
			yield
		finally:
			self._visited.pop(-1)
