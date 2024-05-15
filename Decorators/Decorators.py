""" 
装饰器是修改其他函数的功能的函数
使得python代码更加简洁，更加pythonic

"""


# 一切皆对象
def hi(name="yasoob"):
    return "hi " + name
print("#################")
print(hi())
# output: 'hi yasoob'

# 我们甚至可以将一个函数赋值给一个变量，比如
greet = hi
# 我们这不是在调用hi函数，而是在将它放在greet变量里头。这意味着我们现在可以通过greet()来调用hi()函数。
print("LLLLLLLLLLLLLLLLLLLLLLLL")
print(greet())


del hi
# print("QAQAQAQAQAQAQAQA")
# print(hi())
# """ 
#     print(hi())
#           ^^
# NameError: name 'hi' is not defined

# """



print("#################")
print(greet())


