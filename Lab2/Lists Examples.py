#Python Lists
#1st example
thislist = ["apple", "banana", "cherry"]
print(thislist)

#2nd example
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
  
#3rd example
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#4th example
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#5th example
list1 = ["abc", 34, True, 40, "male"]

#6th example
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#7th example
thislist = list(("apple", "banana", "cherry")) 
print(thislist)



#Python - Access List Items

#1st example
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#2nd example
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
  
#3rd example
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#4th example
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#5th example
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#6th example
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#7th example
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")



#Python - Change List Items

#1st example
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#2nd example
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
  
#3rd example
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#4th example
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#5th example
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)




#Python - Add List Items

#1st example
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#2nd example
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
  
#3rd example
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#4th example
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)




#Python - Remove List Items

#1st example
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#2nd example
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
  
#3rd example
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#4th example
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#5th example
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#6th example
thislist = ["apple", "banana", "cherry"]
del thislist

#7th example
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)






#Python - Loop Lists

#1st example
thislist = ["apple", "banana", "cherry"]
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#2nd example
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
#3rd example
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#4th example
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]






#Python - List Comprehension

#1st example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#2nd example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
  
#3rd example
newlist = [x for x in fruits if x != "apple"]

#4th example
newlist = [x for x in fruits]

#5th example
newlist = [x for x in range(10)]

#6th example
newlist = [x for x in range(10) if x < 5]

#7th example
newlist = [x.upper() for x in fruits]

#8th example
newlist = ['hello' for x in fruits]

#9th example
newlist = [x if x != "banana" else "orange" for x in fruits]





#Python - Sort Lists

#1st example
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#2nd example
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
  
#3rd example
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#4th example
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#5th example
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#6th example
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#7th example
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#8th example
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)






#PPython - Copy Lists

#1st example
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#2nd example
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
  




#Python - Join Lists

#1st example
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#2nd example
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
  
#3rd example
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)




#Python - List Methods
"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""


