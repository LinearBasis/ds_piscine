from functools import reduce
import sys
import timeit

class Tester:
	def __init__(self, iters, number) -> None:
		self.test_funcs = {
			"reduce" : self._test_reduce,
			"loop" : self._test_loop,
		}
		self.iters = iters
		self.number = number

	def	_test_reduce(self):
		return reduce(lambda x, y: x + y * y, range(1, self.number + 1))
	
	def _test_loop(self):
		a = 0
		for i in range(1, self.number + 1):
			a = a + i * i
		return a

	def test_one_func(self, func_name):
		get_time_of_exec = lambda x : timeit.timeit(x, number=self.iters)
		testing_result = get_time_of_exec(self.test_funcs[func_name])
		print(testing_result)

	def test_all(self):
		get_time_of_exec = lambda x : timeit.timeit(x, number=self.iters)
		testing_result = {}
		for i in self.test_funcs.keys():
			testing_result[i] = get_time_of_exec(self.test_funcs[i])

		print(testing_result)
		sorted_names = sorted(testing_result, key=testing_result.get)
		print(f"it's better to use a {sorted_names[0]}")
		print(" vs ".join([str(i) for i in testing_result.values()]))


def main():
	if len(sys.argv) != 4:
		raise Exception("invalid args")
	iters = int(sys.argv[2])
	number = int(sys.argv[3])
	a = Tester(iters, number)
	if sys.argv[1] not in a.test_funcs.keys():
		raise Exception(
			"wrong func name (not loop,list comprehension, map or filter)"
		)
	# a.test_one_func(sys.argv[1])
	a.test_all()

if __name__ == "__main__":
	main()