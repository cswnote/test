def number_coroutine():
    try:
        while True:
            x = (yield)
            print(x, end=' ')
    except GeneratorExit:
        print()
        print('closed coroutine!!!!')

co = number_coroutine()
co.__next__()

for i in range(20):
    co.send(i)

co.close()