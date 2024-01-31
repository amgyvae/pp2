#1st example
print(10 > 9)
print(10 == 9)
print(10 < 9)

#2nd example
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
#3rd example
print(bool("Hello"))
print(bool(15))

#4th example
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#5th example
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#6th example
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#7th example
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#8th example
def myFunction() :
  return True

print(myFunction())

#9th example
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
#10th Final example
x = 200
print(isinstance(x, int))

