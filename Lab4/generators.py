#1st task
def funkSquare(n):
    for i in range(n):
        yield i ** 2

n = int(input())
cntSquare = funkSquare(n)
for i in cntSquare:
    print(i)
