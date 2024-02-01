#1st example
a = 33
b = 200
if b > a:
  print("b is greater than a")  

#2nd example
a = 33
b = 200
if b > a:
print("b is greater than a") #tut oshibka budet, potomushto nado postavit tab libo 4 probela
  
#3rd example
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#4th example
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#6th example
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#7th example
if a > b: print("a is greater than b")

#8th example
a = 2
b = 330
print("A") if a > b else print("B")

#9th example
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#10th example
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  
#11th example
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
  
#12th example
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
  
#13th example
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
#14th example
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

