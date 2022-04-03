def	data_types():
	lst = [1, "1", 1.0, True, [1], {1 : 1}, (1, 1), {1}]
	types_lst = [type(i).__name__ for i in lst]
	types_str = "["
	for i in types_lst:
		types_str += i
		types_str += ", "
	types_str = types_str[:-2]
	types_str += "]"
	print(types_str)


if __name__ == '__main__':
	data_types()