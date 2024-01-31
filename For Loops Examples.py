#1st example
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#2nd example
for x in "banana":
  print(x)
  
#3rd example
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#4th example
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  
#5h example
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
#6th example
for x in range(6):
  print(x)
  
#7th example
for x in range(2, 6):
  print(x)
  
#8th example
for x in range(2, 30, 3):
  print(x)
  
#9th example
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
#10th example
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
  
#11th example
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
#12th example
for x in [0, 1, 2]:
  pass