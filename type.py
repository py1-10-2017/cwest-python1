list_one = ['magical unicorns',19,'hello',98.98,'world']
list_two = [2,3,1,7,4,12]
list_three = ['magical','unicorns']

sum= 0
new_string="String:"
for i in list_three:
	if type(i) == int or type(i) == float: #test for type of i
    		sum += i
	elif type(i) == str: #test for type of i -string
    		new_string = new_string + " " + i
print new_string
print sum

if sum != 0 and len(new_string) == 0: # test to see if mixed
	print "The list you entered is of mixed type."
	print new_string
	print sum
elif sum == 0 and len(new_string) > 0 :# test to see if string
	print ("The list you entered is a string")
	print new_string
else:
	print ("The list you entered is of integer type")
	print sum