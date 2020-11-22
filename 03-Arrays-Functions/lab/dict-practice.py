#Dictionaries practice
countries = [
  {"name": "USA", "population": 350, "gdp": 18000},
  {"name": "Russia", "population": 140, "gdp": 1000},
  {"name": "Azerbaijan", "population": 10, "gdp": 45},
  {"name": "Congo", "population": 85, "gdp": 50}
]
print(countries)

#Find country with the highest population

def highest_pop(lis):
  current_population = 0
  max_country = {}
  for country in lis:
    if country["population"] > current_population:
      current_population = country["population"]
      max_country = country
  return max_country
print(highest_pop(countries))

#Find country with the lowest gdp
def lowest_gdp(lis):
  current_gdp = 10000000
  min_gdp = {}
  for country in lis:
    if country["gdp"] < current_gdp:
      current_gdp = country["gdp"]
      min_gdp = country
  return min_gdp
print(lowest_gdp(countries))

#For each country, we are going to calculate gdp per person - gdp / population, gdp * 10**9, population * 10**6
#That function will take a list of countries and it will add a new key to each country that will contain gdp per person
def gdp_per_person(lis):
  for country in lis:
    av_gdp = (country["gdp"]*(10**9))/(country["population"]*(10**6))
    country["gdp_per_person"] = int(av_gdp)
gdp_per_person(countries)
print(countries)

#Microsoft Excel files, export it to csv - comma separated values
#Txt - simple text format
#csv file
#Name,Population,GDP
#USA,350,18000