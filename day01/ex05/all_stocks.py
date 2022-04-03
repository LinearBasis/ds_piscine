import sys


def all_stocks(lst_of_names : list):
	# print(lst_of_names)
	COMPANIES = {	'Apple': 'AAPL',
					'Microsoft': 'MSFT',
					'Netflix': 'NFLX',
					'Tesla': 'TSLA',
					'Nokia': 'NOK'  }

	STOCKS = {  	'AAPL': 287.73,
					'MSFT': 173.79,
					'NFLX': 416.90,
					'TSLA': 724.88,
					'NOK': 3.37		}

	for ticker_or_name in lst_of_names:
		used = set()
		for company_name in COMPANIES.keys():
			if ticker_or_name.lower() == company_name.lower():
				price = STOCKS[COMPANIES[company_name]]
				print("{} stock price is {}".format(company_name, price))
				used.add(ticker_or_name)
				break
			if COMPANIES.get(company_name) is not None and COMPANIES.get(company_name) == ticker_or_name:
				print("{} is a ticker symbol for {}".format(company_name, COMPANIES[company_name]))
				used.add(ticker_or_name)
				break
		if ticker_or_name not in used:
			print("{} is an unknown company or an unknown ticker symbol".format(ticker_or_name))

def main():
	if len(sys.argv) != 2:
		print()
		return 0
	lst = [i.rstrip().lstrip() for i in sys.argv[1].split(",")]
	if "" in lst:
		print()
		return 0
	all_stocks(lst)

if __name__ == "__main__":
	main()