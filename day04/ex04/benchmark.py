from collections import Counter
import sys
import timeit
import random

class Tester:
	def __init__(self, number=10**6) -> None:
		self.debug = False
		self.test_funcs = {
			"my function" : self._test_dict_no_counter,
			"Counter" : self._test_dict_counter,
			"my top" : self._test_most_common_no_counter,
			"Counter's top" : self._test_most_common_counter
		}
		self.counter_list_cache = None
		self.no_counter_list_cache = None
		self.data = [random.randint(0, 100) for _ in range(number)]
		self.number = number

	def	_test_dict_counter(self):
		self.counter_list_cache = Counter(self.data)
		return self.counter_list_cache
	
	def _test_dict_no_counter(self):
		dict_counts = {}
		for i in range(101):
			dict_counts[i] = 0
		for i in self.data:
			dict_counts[i] += 1
		if self.debug:
			print(dict_counts)
		self.no_counter_list_cache = dict_counts
		return self.no_counter_list_cache

	def _test_most_common_counter(self):
		if self.counter_list_cache is None:
			self._test_dict_counter()
		a = self.counter_list_cache.most_common(10)
		if self.debug:
			print(a)
		return a
	
	def _test_most_common_no_counter(self):
		if self.no_counter_list_cache is None:
			self._test_dict_no_counter()
		dict_counts = self.no_counter_list_cache
		sorted_values = sorted(self._test_dict_no_counter(), key=lambda x: -1 * dict_counts.get(x))
		most_common = []
		for i in sorted_values[:10]:
			most_common.append((i, dict_counts[i]))
		if self.debug:
			print(most_common)
		return most_common



	def test_one_func(self, func_name):
		get_time_of_exec = lambda x : timeit.timeit(x, number=self.iters)
		testing_result = get_time_of_exec(self.test_funcs[func_name])
		print(testing_result)

	def test_all(self):
		for i in self.test_funcs.keys():
			print(f'{i}: {timeit.timeit(self.test_funcs[i], number=1)}')
			# self.test_funcs[i]()



def main():
	a = Tester()
	a.test_all()

if __name__ == "__main__":
	main()