""" 
在 if/else 语句中我们返回 greet 和 welcome，而不是 greet() 和 welcome()。为什么那样？
这是因为当你把一对小括号放在后面，
这个函数就会执行；然而如果你不放括号在它后面，
那它可以被到处传递，并且可以赋值给别的变量而不去执行它。

"""

def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"
 
    def welcome():
        return "now you are in the welcome() function"
 
    if name == "yasoob":
        return greet
    else:
        return welcome
 
a = hi()
print(a)
#outputs: <function hi.<locals>.greet at 0x00000235288CD9E0>
 
#上面清晰地展示了`a`现在指向到hi()函数中的greet()函数
#现在试试这个
 
print("#######################") 
print(a())
#outputs: now you are in the greet() function


print("LLLLLLLLLLLLLLLLLLLLLLLLLLLL")
print(hi()())


print("TTTTTTTTTTTTTTTTTTTTTTTTTTTT")
print(hi("ali")())


