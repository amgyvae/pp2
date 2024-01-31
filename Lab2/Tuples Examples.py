#Python Tuples
#1st example
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#2nd example
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
  
#3rd example
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#4th example
thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple")
print(type(thistuple))

#5th example
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#6th example
tuple1 = ("abc", 34, True, 40, "male")

#7th example
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#8th example
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)



#Python - Access Tuple Items

#1st example
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#2nd example
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
  
#3rd example
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#4th example
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#5th example
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#6th example
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#7th example
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")



#Python - Update Tuples

#1st example
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#2nd example
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
  
#3rd example
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#4th example
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#5th example
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)




#Python - Unpack Tuples

#1st example
fruits = ("apple", "banana", "cherry")

#2nd example
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
  
#3rd example
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#4th example
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)




#Python - Loop Tuples

#1st example
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#2nd example
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  
#3rd example
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1






#Python - Join Tuples

#1st example
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#2nd example
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)







#Python - Tuple Methods
"""
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""


