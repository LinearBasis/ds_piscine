import sys

def get_message_to_email(email : str):
	f = open("employees.tsv", "r")
	empl_list = f.read().split("\n")
	empl_info_list = [(i.split("\t")[0], i.split("\t")[2]) for i in empl_list if i is not ""]
	for empl in empl_info_list:
		if empl[1] == sys.argv[1]:
			return (f"Dear {empl[0]}, welcome to our team. " +
					"We are sure that it will be a pleasure to work with you. " +
					"hat’s a precondition for the professionals that our company hires.")

def main():
	if len(sys.argv) != 2:
		return 0
	return get_message_to_email(sys.argv[1])

	
if __name__ == "__main__":
	print(main())