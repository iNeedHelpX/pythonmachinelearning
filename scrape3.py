#web scraping Toronto.ca list of fire stations
#Total list of all 84 fire stations in Toronto and thier addresses. Exported as csv.
#useful for "address in every neighbourhood" type searches as every neighbourhood has a fire station!

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.toronto.ca/community-people/public-safety-alerts/understanding-emergency-services/fire-station-locations/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class':'table table-bordered table-striped table-hover cot-table cotui-map'})
rows = table.find_all('tr')
columns = [v.text for v in rows[0].find_all('th')]

#set up pandas data frame
df = pd.DataFrame(columns=columns)
for i in range(1, len(rows)):
	tds = rows[i].find_all('td')

	if len(tds) == 1:
		values = [tds[0].text, tds[1].text.replace('\n', '')]
	else:
		values = [td.text.replace('\n', '') for td in tds]

	df = df.append(pd.Series(values, index=columns), ignore_index=True)
	print(df)

	#export to csv
	df.to_csv(r'/Users/juliapak/Documents/listfireaddresses' + '\\firestationsadd.csv', index=False)
