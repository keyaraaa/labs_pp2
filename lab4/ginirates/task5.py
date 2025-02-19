def countdown(n):
    for num in range(n,-1,-1):
        yield num
n = 10
for num in countdown(n):
    print(num)