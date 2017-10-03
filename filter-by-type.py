#If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"


#If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."

#If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."
#Variables to be tested
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

test = [sI, mI, bI, eI, spI, sS, mS, bS, eS, aL, mL, lL, eL, spL]
print test
print("We have printed all of the variables we are testing")
for i in test: # loop to run through all the variables
	test = [sI, mI, bI, eI, spI, sS, mS, bS, eS, aL, mL, lL, eL, spL]
	if type(i) == int: #test for type of i
    		if test >= 100:
        		print "That's a big number!"
        		print type(i)
    		else:
        		print "That's a small number."
        		print type(i)
	elif type(i) == str: #test for type of i -string
    		if len(i) >= 50:
        		print "This is a long sentence."
       			print type(i)
    		else:
        		print "This is a short sentence."
        		print ("type(i)
	elif type(i) ==  list: #test for type of i - list
    		if len(i) >= 10:
        		print "Wow, you've got quite a big list!"
        		print type(i)
    		else:
    			print "Short list."
    			print type(i)
	else:
    		print("I don't know what that is!")
    		print type(i)