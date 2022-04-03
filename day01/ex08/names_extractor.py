import sys

def main():
	if len(sys.argv) != 2:
		return 0
	f = open(sys.argv[1], "r")
	mail_list = f.read().split("\n")
	f.close()
	name_surname_list = [i.split("@")[0] for i in mail_list]
	names = [i.split(".")[0] for i in name_surname_list]
	surnames = [i.split(".")[1] for i in name_surname_list]
	names = list(map(lambda x: x[0].upper() + x[1:], names))
	surnames = list(map(lambda x: x[0].upper() + x[1:], surnames))
	f = open('employees.tsv', "w")
	f.write("Name\tSurname\tE-mail\n")
	for name, surname, email in zip(names, surnames, mail_list):
		f.write(f"{name}\t{surname}\t{email}\n")
	

if __name__ == "__main__":
	main()