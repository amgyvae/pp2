#1st task
def funkSquare(n):
    for i in range(n):
        yield i ** 2

n = int(input())
cntSquare = funkSquare(n)
for i in cntSquare:
    print(i)

#2nd task
def funkEven(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
cntEven = funkEven(n)
print(*cntEven, sep=", ")
