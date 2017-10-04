list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

i = 0
samsies =""
for i in list_one:
	if list_one[0] == list_two[0]:
		samsies= samsies + " " + i
	else:
		print("The lists are not the same")
		break
if len(samsies) == len(list_one):
	print("The lists are the same")
else:
	print("The lists are not the same")