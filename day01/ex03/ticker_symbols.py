import sys


def	get_price(company_name, COMPANIES, STOCKS):
	price = STOCKS.get(COMPANIES.get(company_name))
	if price is None:
		return "Unknown company"
	return price

def find_company_and_price(ticker):
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
	company = None
	for i in COMPANIES.keys():
		if COMPANIES[i].lower() == ticker.lower():
			company = i
			break
	if company is None or STOCKS.get(ticker.upper()) is None:
		return None
	return (company, STOCKS.get(ticker.upper()))

def	main():
	if len(sys.argv) != 2:
		return 0
	ans = find_company_and_price(sys.argv[1])
	if ans is None:
		print("Unknown ticker")
	else:
		print("{} {}".format(ans[0], ans[1]))


if __name__ == '__main__':
	main()