import sys


"""
Readonly code, однако.
1) берем номер буквы из словаря
2) прибавляем к этому номеру num, чтобы сдвинуть его шифром цезаря,
	и берем модуль по длине алфавита (чтобы не вылезти за его пределы, "z" + 1 == "a")
3) берем из алфавита по получившемуся индексу букву и вставляем
4) Если вдруг получившаяся буква была заглавная в изначальном слове, переводим ее в uppercase
"""

def	do_cypher(alphabet, alphabet_index, string, num):
	def	transform_number(char):
		if char not in alphabet:
			return char
		index_in_abc = (alphabet_index[char.lower()] + num) % len(alphabet) # 1 и 2 пункты
		if char.upper() == char:
			return alphabet[index_in_abc].upper() # 4 пункт
		return alphabet[index_in_abc] # 3 пункт
			
	return "".join( [transform_number(i) for i in string] )


"""
Этой функции хватит для случаев шифровки и дешифровки, ибо на самом деле сдвиг на -2 == сдвиг на -2 + len(alphabet)
"""
def	caesar_cypher(string : str, num : int) -> str:
	alphabet = "".join([chr(i) for i in range(ord("a"), ord("z") + 1)])
	# is_lower = "".join(["1" if i.lower() != i else "0" for i in string])
	num = (num % len(alphabet) + len(alphabet)) % len(alphabet)
	alphabet_index = dict( zip(alphabet, range(0, len(alphabet))) )
	return do_cypher(alphabet, alphabet_index, string, num)

def main():
	if len(sys.argv) != 4:
		raise Exception("invalid arguments number")
	if not all(ord(i) < 128 for i in sys.argv[2]):
		raise Exception("invalid string")
	if sys.argv[1] == "encode":
		print(caesar_cypher(sys.argv[2], int(sys.argv[3])))
	elif sys.argv[1] == "decode":
		print(caesar_cypher(sys.argv[2], -int(sys.argv[3])))

if __name__ == "__main__":
	main()