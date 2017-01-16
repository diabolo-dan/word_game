



class PrefixTreeNode(object):
	def __init__(self, parent, letter):
		self._letter = _letter
		self._nodes = [None] * 26

	def add_word(self, word):
		if word == self._letter:
			self._is_word = True
		else:
			self._is_prefix = True
			self._add_descendant(suffix)

	def _add_descendant(self, suffix):
		next_letter = word[0]
		index = self._index(next_letter)
		if self._nodes[index] == None:
			self._nodes[index] = PrefixTreeNode(self, next_letter)
		self._nodes[index].add_word(word)


	@staticmethod
	def _index(letter):
		return letter.upper() - 'a'

