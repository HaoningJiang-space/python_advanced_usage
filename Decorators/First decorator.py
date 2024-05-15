def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")
   
   
# print("#############################################")    
# a_function_requiring_decoration()
#outputs: "I am the function which needs some decoration to remove my foul smell

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

# print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
# a_function_requiring_decoration()
""" 
Outputs:
I am doing some boring work before executing a_func()
I am the function which needs some decoration to remove my foul smell
I am doing some boring work after executing a_func()
"""

@ a_new_decorator
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

a_function_requiring_decoration()

""" 
I am doing some boring work before executing a_func()
I am the function which needs some decoration to remove my foul smell
I am doing some boring work after executing a_func()
"""

print("#############################################")
print(a_function_requiring_decoration.__name__)
""""
输出结果是wrapTheFunction，这并不是我们想要的。因为我们的函数被wrapTheFunction替代了
我们可以使用functools.wraps来解决这个问题
"""


from functools import wraps

def a_new_decorator_using_wraps(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

@a_new_decorator_using_wraps
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

print("#############################################")
print(a_function_requiring_decoration.__name__)
#输出结果是a_function_requiring_decoration，这就是我们想要的结果
