#assignment names
#print first and last names for each dictionary in array
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


def print_names(arr):
	for x in students:
		print x['first_name'] + " " + x['last_name']

print_names(students)

#part two
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def students_instructors(dict):
    num = 1
    for x in dict:
        print x
        for value in dict[x]:
            upper_name = str.upper(value["first_name"]+ " " + value["last_name"])
            length = len(value["first_name"] + value["last_name"])
            print str(num) + " - " + upper_name + " - " + str(length)
            num += 1

students_instructors(users)

