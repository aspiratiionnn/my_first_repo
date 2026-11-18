# marks1=94.4
# makrs2=87.5
# marks3=95.2
# marks4=66.4
# marks5=45.1

# mark=[94.4 , 87.5, 95.2 , 66.4 , 45.1 ]
# print(mark)
# print(type(mark))
# print(mark[4])
# print(mark[3])
# print(len(mark))

# WE CAN STORE MULTIPLE TYPE OF DATA IN A SINGLE LIST
# STRINGS ARE IMMUTABLE
# LISTS ARE MUTABLE
# student_details=["Karan" , 19 , 87.9 , "Delhi"]
# print(student_details[0])

# str="hello"
# print(str[0])
# str[0]="y"
# ERROR

# student_details=["Karan" , 19 , 87.9 , "Delhi"]
# print(student_details[0])
# student_details[0]="ARJUN"
# print(student_details)

# student_details=["Karan" , 19 , 87.9 , "Delhi"]
# print(student_details[5])
# ERROR

# LIST SLICING
# student_details=["Karan" , 19 , 87.9 , "Delhi"]
# print(student_details[1:4])

# student_details=["Karan" , 19 , 87.9 , "Delhi"]
# print(student_details[:4])

# student_details=["Karan" , 19 , 87.9 , "Delhi"]
# print(student_details[1:])

# student_details=["Karan" , 19 , 87.9 , "Delhi"]
# print(student_details[-4:-1])

# student_details=["Karan" , 19 , 87.9 , "Delhi"]
# print(student_details[-5:])

# student_details=["Karan" , 19 , 87.9 , "Delhi"]
# print(student_details[:-1])

# LIST METHODS
# append=adding an element at the end of the list

# list=[1,2,5,4]
# list.append(9)
# print(list)
# This is called mutating the list(changing the list)

# sort()=SORTS IN ASCENDING ORDER
# list=[1,2,5,4]
# list.append(9)
# print(list.sort())
# print(list)

# list=[1,2,5,4]
# list.append(9)
# print(list.sort(reverse=True))
# print(list)


# list=["banana" , "litchi" , "apple"]
# list.append("mango")
# list.sort()
# print(list)

# list=["banana" , "litchi" , "apple"]
# list.append("mango")
# print(list.sort(reverse=True))
# print(list)


# reverse()=reverses the list
# lis=['a' , 'd' , 'e' , 'f' , 'c' , 'b']
# lis.reverse()
# print(lis)

# insert(idx , el)=insert element at index
# list=['a' , 'd' , 'e' , 'f' , 'c' , 'b']
# list.insert(1 , 'g')
# print(list)

# remove(1)=removes the first occurance of element
# list=[1 , 9 , 8 , 0 , 9 , 1]
# list.remove(9)
# print(list)

# pop(idx)=removes element at idx
# list=[1 , 9 , 8 , 0 , 9 , 1]
# list.pop(5)
# print(list)

# TUPLES ARE IMMUTABLE
# tup=(1 , 9 , 8 , 0 , 9 , 1)
# print(tup)
# print(type(tup))
# print(tup[1])
# print(tup[4])
# # tup[0]=5 - not allowed

# tup=(1,)
# print(tup)
# print(type(tup))

# tup=(1) - python sees it as an integer unless you put a comma at the end
# print(tup)
# print(type(tup))

# tup=(1,6,7,5,4,3,2,8,)
# print(tup[0:6])

# index(el)=returns index of first occurence

# tup=(1,6,7,5,4,3,2,8,)
# print(tup.index(3)) input-element,output-index

# count(el)=returns no. of occurances of the entered element
# tup=(1,6,7,5,4,3,2,8,)
# print(tup.count(2))


# lis=[input("Enter your first fav movies")]
# lis2=[input("Enter your second fav movies")]
# lis3=[input("Enter your third fav movies")]
# print(lis,lis2,lis3)

# movies=[]
# a=input("Enter your first fav movie:")
# b=input("Enter your Second fav movie:")
# c=input("Enter your third fav movie:")

# movies.append(a)
# movies.append(b)
# movies.append(c)
# print(movies)

# movies=[]
# a=movies.append(input("Enter your first fav movie:"))
# b=movies.append(input("Enter your Second fav movie:"))
# c=movies.append(input("Enter your third fav movie:"))
# print(movies)


# movies=[]
# a=input("Enter your first fav movie:")
# b=input("Enter your Second fav movie:")
# c=input("Enter your third fav movie:")


# list=[1,2,1]
# list2=[1,2,3]
# copy_list=list.copy()
# copy_list.reverse()

# if(copy_list==list):
#     print("List is Palindrome")
# else:
#     print("List is not Palindrome")

# students_grade=['C' , 'D' , 'A' , 'A' , 'B' , 'B' , 'A']
# A=students_grade.count('A')
# print("No. of students with grade A=",A)

# a=['C' , 'D' , 'A' , 'A' , 'B' , 'B' , 'A']
# a.sort()
# print(a)

# DICTINOARIES ARE MUTABLE
# dict={
#     "name":"Akansha",
#     "age":19,
#     "subject":["Python","C","Java","HTML"],
#     "topics":("dictionaries","sets"),
#     "class":"B.Sc. (Hons.) Data Science",
#     5:"STUDY HOURS"
# }
# print(dict)
# print(type(dict))
# print(dict["name"])
# print(dict["topics"])
# print(dict["subject"])
# print(dict["age"])

# dict={
#     "name":"Akansha",
#     "age":19,
#     "subject":["Python","C","Java","HTML"],
#     "topics":("dictionaries","sets"),
#     "class":"B.Sc. (Hons.) Data Science",
#     5:"STUDY HOURS"
# }
# dict["name"]="Akansha Singh" #overwrite 
# dict["surnmae"]="Favour"
# print(dict)

# null={}
# null["name"]="AKANSHA"
# print(null)

# NESTED DISCTIONARIES
# student={
#     "Name":"Rahul Kumar",
#     "Subjects":{"Physics":90,
#                 "Maths":87,
#                 "English":99 },
#     "Class":"12th",
#     "Age":19,
# }
# print(student)
# print(student["Subjects"]["English"])

# student={
#     "Name":"Rahul Kumar",
#     "Subjects":{"Physics":90,
#                 "Maths":87,
#                 "English":99 },
#     "Class":"12th",
#     "Age":19,
# }
# print(student.keys()) gives outer layer's keys

# student={
#     "Name":"Rahul Kumar",
#     "Subjects":{"Physics":90,
#                 "Maths":87,
#                 "English":99 },
#     "Class":"12th",
#     "Age":19,
# }
# print(tuple(student.keys()))
# print(len(student))
# print(len(list(student.keys())))
# print(list(student.keys()))

# student={
#     "Name":"Rahul Kumar",
#     "Subjects":{"Physics":90,
#                 "Maths":87,
#                 "English":99 },
#     "Class":"12th",
#     "Age":19,
# }
# print(student.values())
# print(list(student.values()))
# WE CAN STORE LIST IN DICTIONARIES AND DICTIONARIES IN LIST
# RETURNS THE COLLECTION OF ALL THE VALUES OF THE DICTIONARY

# student={
#     "Name":"Rahul Kumar",
#     "Subjects":{"Physics":90,
#                 "Maths":87,
#                 "English":99 },
#     "Class":"12th",
#     "Age":19,
# }

# print(student.items())
# # RETURNS ALL (KEY,VAL) PAIRS AS TUPLES
# print(list(student.items()))
# pairs=list(student.items())
# print(pairs[0])

# student={
#     "Name":"Rahul Kumar",
#     "Subjects":{"Physics":90,
#                 "Maths":87,
#                 "English":99 },
#     "Class":"12th",
#     "Age":19,
# }
# print("AFTER")
# print(student['Name2']) #ERROR
# print("BEFORE")
# DOESN'T RETURNS THE RIGHT CODE AFTER THE ERROR
# TO STAY AWAY FROM THESE KIND OF THINGS WE USE METHODS
# ------print(student.get("Name2")) #NONE


# student={
#     "Name":"Rahul Kumar",
#     "Subjects":{"Physics":90,
#                 "Maths":87,
#                 "English":99 },
#     "Class":"12th",
#     "Age":19,
# }

# student={
#     "Name":"Rahul Kumar",
#     "Subjects":{"Physics":90,
#                 "Maths":87,
#                 "English":99 },
#     "Class":"12th",
#     "Age":19
# }
# # student.update({"City":"Delhi"})
# # print(student)

# new_dict={"City":"Delhi"}
# student.update(new_dict)
# print(student)

# SETS
# CANNOT STORE LIST AND DICTIONARY IN SETS AS THEY ARE MUTABLE
# print(collection)
# print(type(collection))
# collection={1,2,2,3,4,"hello","world","hello"}
# print(len(collection))
# DUPLICATE VALUES ARE NOT ALLOWED.

# collection= set() #empty set
# print(type(collection))

# set.add(el) #adds an element
# SETS-MUTABLE BUT THE ELEMENTS OF THE SET IS IMMUTABLE
# collection=set()
# collection.add(1)
# collection.add(2)
# collection.add(2)
# collection.add("HI I AM AKANSHA")
# collection.add("I am 19 years old")
# # collection.remove(1)
# # collection.remove(7)
# # collection.add([1,2,3]) unhashable type error, hashing is a way to convert original value into anything else, list's hash value can change anytime as it is mutable
# collection.clear()
# print(len(collection))

collection={"hello","world","coding","python","hurrr"}
# print(collection.pop())
# print(collection.pop())

