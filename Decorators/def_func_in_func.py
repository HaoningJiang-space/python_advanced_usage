#在一个函数中定义另一个函数


def hi(name = "yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")
    
# a = hi()
# print(hi())


print(hi())



# print(greet())
""" 
    print(greet())
          ^^^^^
NameError: name 'greet' is not defined
"""
