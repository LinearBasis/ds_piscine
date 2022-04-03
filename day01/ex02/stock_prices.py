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
	
	company_name = company_name[0].upper() + company_name.lower()[1:]
	ticker = COMPANIES.get(company_name)
	if ticker is None:
		return "Unknown company"
	price = STOCKS.get(ticker.upper())
	if price is None:
		return "Unknown company"
	return price

def	main():
	if len(sys.argv) != 2:
		return 0
	print(get_price(sys.argv[1]))

if __name__ == '__main__':
	main()
