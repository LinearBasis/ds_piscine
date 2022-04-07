import email
import timeit


class Tester:
	def __init__(self, iters) -> None:
		self.test_func = {
			"list comprehension" : self._test_list_comprehension,
			"loop" : self._test_loop_creating,
			# "map" : self._test_map_creating
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
	
	def _test_map_creating(self):
		new_emails = list(map(lambda mail : None if mail.find("@gmail.com") == -1 else mail, self.mail_list))

	def test_all(self):
		get_time_of_exec = lambda x : timeit.timeit(x, number=self.iters)
		testing_result = {}
		for i in self.test_func.keys():
			testing_result[i] = get_time_of_exec(self.test_func[i])

		sorted_names = sorted(testing_result, key=testing_result.get)
		print(f"it's better to use a {sorted_names[0]}")
		print(" vs ".join([str(i) for i in testing_result.values()]))

if __name__ == "__main__":
	a = Tester(10**5)
	a.test_all()
	# a.test_func["map"]()