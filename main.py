from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find_all('table')[1]

ths = table.find_all('th')
column_data = table.find_all('tr')


world_table_titles = [th.text.strip() for th in ths]
df = pd.DataFrame(columns=world_table_titles)
#print(df)

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    #print(individual_row_data)

    length = len(df)
    df.loc[length] = individual_row_data
print(df)

df.to_csv(r'C:\Users\Danil-Danjubas\OneDrive\Рабочий стол\scrap\Companies1.csv', index=False, sep=';')