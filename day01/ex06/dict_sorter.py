


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

	dict_of_countries = dict(list_of_tuples)
	sorted_dict = dict(sorted(dict_of_countries.items(), key=lambda country_number : (-1 * int(country_number[1]), country_number[0])))
	for key in sorted_dict.keys():
		print(key)


if __name__ == "__main__":
	main()
