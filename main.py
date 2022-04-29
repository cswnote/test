# def type_check(type_a, type_b):
#     def real_decorator(func):
#         def wrapper(a, b):
#             if isinstance(a, type_a) and isinstance(b, type_b):
#                 return func(a, b)
#             else:
#                 raise RuntimeError('is not match on type.')
#         return wrapper
#     return real_decorator
#
# @type_check(int, int)
# def add(a, b):
#     return a + b
#
# print(add(10, 20))
# print(add('a', 'b'))

def html_tag(tag_name):
    def deco(func):
        def wrapper():
            print('<' + tag_name + '>', end='')
            print(func(), end='')
            print('</' + tag_name + '>', end='')
            # print('<{0}>{1}</{0}>'.format(tag_name, func()))
        return wrapper
    return deco



# a, b = input().split()
a, b = 'p', 'span'

@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'


print(hello())