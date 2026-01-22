import httpx

r = httpx.get('https://www.cnb.cz/en/financial-markets/foreign-exchange-market/central-bank-exchange-rate-fixing/central-bank-exchange-rate-fixing/daily.txt')
print(r.text)
print(r.status)
lines = r.text.split('\n')
print(lines[0])
