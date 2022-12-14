# Working on Country data

from json import load

with open("countrydata.json", encoding="UTF=8") as f:
    data = load(f)
# print(len(data))

# To print all country name
all_country_names = [c.get("name") for c in data]
# print(all_country_names)

# To get details of specified country

def get_country_details(name):
    return [c for c in data if c.get("name")==name][0]

# details = get_country_details("")
# print(details)

# To get capital of a country of your choice

def get_country_capital(name):
    c_data = get_country_details(name)
    if c_data:
        return c_data.get("capital")

# print(get_country_capital("India"))

# To get the population of a country of our choice
def get_country_population(name):
    c_data = get_country_details(name)
    if c_data:
        return c_data.get("population")

# print(get_country_population("India"))


# To get the currency of a country of your choice
def get_country_currencyname(name):
    c_data = get_country_details(name)
    if c_data:
        return c_data.get("currencies")[0].get("name")

# print(get_country_currencyname("China"))


# To get the border name list of a country of your choice
def get_cuntry_border_list(name):
    c_data = get_country_details(name)
    border_list = c_data.get("borders")
    b_names = [c.get("name") for c in data if c.get("alpha3Code") in border_list]
    return b_names

# print(get_cuntry_border_list("India"))


# To get maximum populated country
def get_maxpopulated_country():
    c_data = max(data, key=lambda c: c.get("population"))
    return c_data.get("name")
# print(get_maxpopulated_country())

# OR

max_population_country = max(data, key=lambda c: c.get("population"))
# print(max_population_country.get("name"))

# To get least populated country
def get_minpopulated_country():
    c_data = min(data, key=lambda c: c.get("population"))
    return c_data.get("name")
# print(get_minpopulated_country())
# OR
min_population_country = min(data, key=lambda c:c.get("population"))
# print(min_population_country.get("name"))


# To get the languages of a country of your choice
def get_country_language(name):
    c_data = get_country_details(name)
    return [l.get("name") for l in c_data.get("languages")]

print(get_country_language("Italy"))

