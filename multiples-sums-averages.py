#print all odd numbers from 1 to 1000
for i in range (1,1000, 2):
	print i
#print all multiples from 5 to 1,000,000
multiples = []
for i in range(5,1000000):
    if (i%5==0):
        multiples.append(i)
print(multiples)

#program to print sum
print("Sum")
a = [1, 2, 5, 10, 255, 3]
total = 0
for i in a:
    total += i
print(total)

#Print Average
a = [1, 2, 5, 10, 255, 3]
print(total/len(a))
