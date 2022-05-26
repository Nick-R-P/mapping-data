import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Nick-R-P/mapping-data/main/sample_data/wine-ratings-small.csv')
#df.head()

regions = df.region.unique()

major_region = []
for region in regions:
    if ',' not in region:
        major_region.append(region)
#print (major_region)

num_of_wine = {}
for region in major_region:
    num_of_wine[region] = len(df[df['region'].str.contains(region)])
#print (num_of_wine)

num_of_red = {}
for region in major_region:
    country_list = df[df['region'].str.contains(region)]
    num_of_red[region] = len(country_list[country_list['variety'] == 'Red Wine'])
#print (num_of_red)

output = pd.DataFrame()
output['Major Region'] = major_region
red =[]
white = []
for i in major_region:
    red.append(num_of_red[i])
    white.append(num_of_wine[i] - num_of_red[i])

output['Number of Red Wines'] = red
output['Number of White Wines'] = white


print(output)
