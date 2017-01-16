from abc import ABCMeta, abstractmethod

class SearchState(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def result(self):
		pass
	@abstractmethod
	def get_result(self):
		pass
	@abstractmethod
	def next_states(self):
		pass

	@abstractmethod
	def descend(self, i):
		pass

def search(state):
	if state.result():
		yield state.get_result()
	for i in state.next_states():
		with state.descend(i):
			for result in search(state):
				yield result
