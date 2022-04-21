def prime_number_generator(start, stop):
    for i in range(start, stop + 1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag == True:
            yield i

# start, stop = map(int, input().split())
start, stop = 50, 100

g = prime_number_generator(start, stop)
print(g)
print(type(g))
for i in g:
    print(i, end=' ')