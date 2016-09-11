import json
from numpy import random

class RandomLetterGenerator(object):

	def __init__(self):
		letter_frequencies = json.loads(letter_freq.json)
		self.letters, self.weights = zip(*letter_frequencies.items())


	def get_letter(self):
		return random.choice(self.letters, p=self.weights)
