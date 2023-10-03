from bs4 import BeautifulSoup
import requests
import pandas as pd
from pathlib import Path

def _get_country_and_name(row:list) -> tuple:
	data, *_ = row[3].split("\n") 
	country, *name = data.split()
	if country == "United":
		country = "UK"
		name.pop(0)

	if country == "Czech":
		country = "Czech Republic"
		name.pop(0)

	name = " ".join(name)

	return country, name

def _parse_row(row: list) -> list:
	parsed = []
	parsed.append(row[1])    # Place
	country, name = _get_country_and_name(row)
	parsed.append(country)
	parsed.append(name)
	for i in range(4, len(row)):
		x = row[i].split('\n')
		parsed.append(x[0])
	
	return parsed

def parse_data(df: pd.DataFrame, table):
	column_data = table.find_all('tr')
	for row in column_data[1:]:
		row_data = row.find_all('td')
		this_row_data = [data.text.strip() for data in row_data]
		d = _parse_row(this_row_data)
		df.loc[int(d[0]) - 1] = d
	return df 

def get_table_columns(table):
	titles = table.find_all('th')
	table_columns = [title.text for title in titles if title.text]
	# Manual clean up because some columns are not labled 
	table_columns.insert(1, "Country")
	table_columns.append("From Previous")
	table_columns.append("From First")

	return table_columns

if __name__ == "__main__":
	url = 'https://www.worldjigsawpuzzle.org/wjpc/2023/individual/Final'
	cwd = Path(__file__).absolute().parent
	output_dir = cwd / "results"
	if not output_dir.exists(): output_dir.mkdir()
	output_file = output_dir / "2023-World_individual-finals.csv"
	
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html')
	table = soup.find_all('table', id='participantes')[0]
	# Spanish/English mix because of Spanish website
	cols = get_table_columns(table)

	df = pd.DataFrame(columns=cols)
	df = parse_data(df, table)



	df.to_csv(output_file)