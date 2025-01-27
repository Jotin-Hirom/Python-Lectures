# # function and class decorator
# def start_end_decorator(func):

#     def wrapper():
#         print("start")
#         func() # call the decorated func here.
#         print("End")
#     return wrapper

# @start_end_decorator
# def print_name():
#     print("Alex")

# # print_name = start_end_decorator(print_name)
# print_name()

# import functools
# def start_end_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("start")
#         result = func(*args, **kwargs) # call the decorated func here.
#         print("End")
#         return result
#     return wrapper

# @start_end_decorator 
# def add5(x):
#     return x + 5;

# # result = add5(10)
# # print(result)
# print(help(add5))
# print(add5.__name__)

# import functools
# def repeater(num_times):
#     def decorator_repeats(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range (num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeats
# @repeater(3)
# def greetings(name):
#     print(f"Hello {name}")

# greetings("Alex")


# nested decorator
# import functools
# from typing import Any
# def debug(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         # print(args)
#         for k,v in kwargs.items():
#             j = "{v!r}"
#             print(j)
#         kwargs_repr = [f"{k}= {v!r}" for k,v in kwargs.items()]
#         # print(kwargs_repr)
#         signature = ", ".join(args_repr + kwargs_repr)
#         print(signature)
#         print(f"Calling {func.__name__}({signature})")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__!r} returned {result!r}")
#         return result
#     return wrapper

# def start_end_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("start")
#         result = func(*args, **kwargs) # call the decorated func here.
#         print("End")
#         return result
#     return wrapper

# @debug
# @start_end_decorator 
# def say_name(name):
#     greeting = f'Hello {name}'
#     print(greeting)
#     return greeting

# say_name("Alex")


# Class decorator
class CountCalls:
    def __init__(self, func) -> None:
        self.func = func
        self.num_count = 0
    def __call__(self, *args, **kwds):
        self.num_count += 1
        print(f"This is executed {self.num_count} times")
        return self.func(*args, **kwds)


# cc = CountCalls(None)
# cc() # -> This calls the __call__() function
@CountCalls
def say_hello():
    print("Hello")

say_hello()
say_hello()
say_hello()

# This can be used for debugging, providing information, calculation etc 