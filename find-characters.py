# input
word_list = ['hello','world','my','name','is','Anna']
char= "o"
# output
new_list = []

for i in word_list:
	if char in i:
		new_list.append(i)
	else:
		print("Ohhhhhhh, No")
print new_list
