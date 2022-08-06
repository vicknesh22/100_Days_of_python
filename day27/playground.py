# *args allow as to give unlimited positional arguments in to the function
# since it is tuple we can access it by index
# args[0] or args[3]
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(8, 4, 6, 10))
