

def main():
	list_of_tuples = [
		('Russia', '25'),
		('France', '132'),
		('Germany', '132'),
		('Spain', '178'),
		('Italy', '162'),
		('Portugal', '17'),
		('Finland', '3'),
		('Hungary', '2'),
		('The Netherlands', '28'),
		('The USA', '610'),
		('The United Kingdom', '95'),
		('China', '83'),
		('Iran', '76'),
		('Turkey', '65'),
		('Belgium', '34'),
		('Canada', '28'),
		('Switzerland', '26'),
		('Brazil', '25'),
		('Austria', '14'),
		('Israel', '12') ]
	dict_with_countries = dict()
	for i in list_of_tuples:
		if dict_with_countries.get(i[1]) is not None:
			dict_with_countries[i[1]].append(i[0])
		else:
			dict_with_countries[i[1]] = [i[0]]
	for key, values in dict_with_countries.items():
		for value in values:
			print(key, ":" ,value)

	# print(dict_with_countries)
	# for value, key in list_of_tuples:
		# for i, j in dict_with_countries.items():
			# if i == key and value in j:
				# print("'{}' : '{}'".format(key, value))
		


if __name__ == "__main__":
	main()