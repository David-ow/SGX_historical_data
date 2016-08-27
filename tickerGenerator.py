import re

content = open('/home/david/PythonProjects/ticker_raw.txt','r').read()

regex = re.compile("NC:'(.+?)'")
tickers = re.findall(regex, content)

with open('SGX_tickers.txt', 'w') as f:
	for items in tickers:
		f.write(items + '\n')
f.closed	
