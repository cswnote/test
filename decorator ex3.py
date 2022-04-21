class Trace:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print(self.func.__name__, 'start method')
        self.func()
        print(self.func.__name__, 'end method')

a = 0

if a == 1:
    @Trace
    def hello():
        print('hello')
else:
    def hello():
        print('hello')

if a == 1:
    hello()
else:
    trace_hello = Trace(hello)
    trace_hello()