# dictionary = a changeable, unordered collection of unique KEY:VALUE pairs
## fast because they use hashing, which allows us to access a value quickly. uses curly braces {key:value}

capitals = {
    # key   :  value
    "USA"   : "Washington DC",
    "India" : "New Delhi",
    "China" : "Beijing",
    "Russia": "Moscow"
}

# instead of index brackets, we use the key name to access values

print(capitals["Russia"]) # Moscow

# If a key doesn't exist, we can get an error by directly accessing
# print(capitals["Germany"]) # KeyError: 'Germany'

# .get() is a safer way to access values in a dictionary
print(capitals.get("Germany")) # None
print(capitals.get("USA")) # Washington DC

# .keys() grab only the keys in our dictionary
print(capitals.keys()) # dict_keys(['USA', 'India', 'China', 'Russia'])

# .values() grab only the values in our dictionary
print(capitals.values()) # dict_values(['Washington DC', 'New Delhi', 'Beijing', 'Moscow'])

# .items() display all of the key:value pairs in our dictionary
print(capitals.items()) # dict_items([('USA', 'Washington DC'), ('India', 'New Delhi'), ('China', 'Beijing'), ('Russia', 'Moscow')])

# additionally you can iterate over dictionaries
for key, value in capitals.items():
    print(key, ":", value)
    
# dictionaries are muteable!

# .update() will add a new key:value pair OR update an existing one

## adding a new key:value pair via update
capitals.update({"Germany" : "Berlin"})
print(capitals.get("Germany")) # Berlin

## overwriting an existing key:value pair via update
capitals.update({"USA" : "Las Vegas"})
print(capitals.items()) # dict_items([('USA', 'Las Vegas'), ('India', 'New Delhi'), ('China', 'Beijing'), ('Russia', 'Moscow'), ('Germany', 'Berlin')])

# .pop() will remove a specific key:value pair from our dictionary
capitals.pop("China")
print(capitals.get("China")) # None

# .clear() will remove ALL key:value pairs from our dictionary
capitals.clear()
print(capitals) # {}
