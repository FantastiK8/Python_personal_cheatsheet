# https://www.edureka.co/blog/hash-tables-and-hashmaps-in-python/


################
"DICTIONARIES"
################
# Unlike lists and tuples, there is no add(), insert(), or append() method that 
# you can use to add items to your data structure. Instead, you have to create a 
# new index key, which will then be used to store the value you want to store in 
# your dictionary.

scones = {
	"Fruit": 22,
	"Plain": 14,
	"Cinnamon": 4,
	"Cheese": 21
}
#syntax for adding a new value to a dictionary:
dictionary_name[key] = value

# Adding new item into dictionary

scones["Cherry"] = 10
print(scones)
# Our code returns:
{'Fruit': 22, 'Plain': 14, 'Cinnamon': 4, 'Cheese': 21, 'Cherry': 10}