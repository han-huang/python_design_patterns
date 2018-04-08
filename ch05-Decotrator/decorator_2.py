# decorator.md
# https://gist.github.com/jcfrank/9c2f3b4d4bd2d6ec44b7

def simpledecorator(func):
    print("This function is decorated with a decorator with no argument.")
    def actual(*args, **kwargs):
        return func(*args, **kwargs)
    return actual

"""
Followings are the same as:
def simpleprint(message):
    print("Hello %s" % message)

simpledecorator(simpleprint)("simple decorator!")
"""
@simpledecorator
def simpleprint(message):
    print("Hello %s" % message)

simpleprint("simple decorator!")

print("\n========\n")

def decorator_with_args(arg1, arg2):
    def innerdecorator(func):
        print("This function is decorated with with a decorator with argument %s, %s" % (arg1, arg2))
        def actual(*args, **kwargs):
            return func(*args, **kwargs)
        return actual
    return innerdecorator

"""
Followings are the same as:
def print_again(message):
    print("Hello %s" % message)

decorator_with_args(arg1, arg2)(print_again)("decorator with arguments!")
"""
@decorator_with_args("a1", "a2")
def print_again(message):
    print("Hello %s" % message)

print_again("decorator with arguments!")
