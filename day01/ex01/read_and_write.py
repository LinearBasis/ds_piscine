

def read_and_write():
	f_csv = open("ds.csv", "r")
	f_tsv = open("ds.tsv", "w")
	csv_text = f_csv.read()

	f_csv.close()
	quote_number = 0
	comma = ","
	quote = '\"'
	tsv_text = ""

	for i in range(len(csv_text)):
		if csv_text[i] == quote and i == 0 or (i > 0 and csv_text[i - 1] != "\\"):
			quote_number += 1
		if csv_text[i] == comma and quote_number % 2 == 0:
			tsv_text += "\t"
		else:
			tsv_text += csv_text[i]
	f_tsv.write(tsv_text)

if __name__ == "__main__":
	read_and_write()




