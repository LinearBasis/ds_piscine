import timeit
import sys

class Tester:
	def __init__(self, iters) -> None:
		self.test_funcs = {
			"list_comprehension" : self._test_list_comprehension,
			"loop" : self._test_loop_creating,
			"map" : self._test_map,
			"filter" : self._test_filter
		}
		self.mail_list = [
			'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
			'anna@live.com', 'philipp@gmail.com'
		] * 5
		self.iters = iters

	def	_test_list_comprehension(self):
		new_emails = [i for i in self.mail_list if i.find("@gmail.com") != -1]
	
	def _test_loop_creating(self):
		new_emails = []
		for i in self.mail_list:
			if i.find("gmail.com") != 1:
				new_emails.append(i)
	
	def _test_map(self):
		new_emails = list(map(lambda mail : None if mail.find("@gmail.com") == -1 else mail, self.mail_list))

	def _test_filter(self):
		new_emails = list(filter(lambda x : x.find("@gmail.com") != -1, self.mail_list))

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

	if len(sys.argv) != 3:
		raise Exception("invalid args")
	iters = int(sys.argv[2])
	a = Tester(iters)
	if sys.argv[1] not in a.test_funcs.keys():
		raise Exception(
			"wrong func name (not loop,list comprehension, map or filter)"
		)
	a.test_one_func(sys.argv[1])



if __name__ == "__main__":
	main()