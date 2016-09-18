import os
import json
import numpy

class RandomLetterGenerator(object):

	def __init__(self):
		script_dir = os.path.dirname(__file__)
		freq_filename = "letter_freq.json"
		with open(os.path.join(script_dir, freq_filename)) as freq_file:
			letter_frequencies = json.load(freq_file)
		self._letters, weights = zip(*letter_frequencies.items())
		self._weights = numpy.array(weights)
		self._weights /= self._weights.sum()


	def get_letter(self):
		return numpy.random.choice(self._letters, p=self._weights).upper()
