words = "It's thanksgiving day. It's my birthday, too!" 
print words 
print words.index(" day") 
print words.replace(" day", " month")
x = [2,54,-2,7,12,98]
print min(x)
print max(x)
y = ["hello",2,54,-2,7,12,98,"world"]

#print first and last
print y[0]
print(y[len(y)-1])



#new list
x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
print("New List")
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
length = len(x)
first_half = []
second_half = []
for i in range(0,len(x)):
    if (i<length/2-1):
        first_half.append(x[i])
    else:
        second_half.append(x[i])
second_half.insert(0, first_half)
print(second_half)