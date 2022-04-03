import sys



def	get_price(company_name):
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

	price = STOCKS.get(COMPANIES.get(company_name))
	if price is None:
		return "Unknown company"
	return price

def	main():
	if len(sys.argv) != 2:
		return 0
	print(get_price(sys.argv[1]))

if __name__ == '__main__':
	main()
