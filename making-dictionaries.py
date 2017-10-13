#he keys should include name, age, country of birth, favorite language.
cassie = {'Name': 'Cassie', 'Age': '25', 'Country' : 'United States', 'Favorite-Language': 'Python'}
print cassie['Age']

def making_dictionaries(arr):
	print "My name is " + cassie['Name']
	print "My age is " + cassie['Age']
	print "My country of birth is " + cassie['Country']
	print "My favorite language is " + cassie['Favorite-Language']


making_dictionaries(cassie)