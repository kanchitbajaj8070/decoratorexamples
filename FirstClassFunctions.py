""" first class functions-
treat a function just like another entity like variable, objecct"""

def square(x):# first-class function
    return x*x

def my_map(func, list):# first-class function passed as an arguement
    result=[]
    for i in list:
        result.append(func(i))
    return result
def cube(x):# first-class function
    return x*x*x

def logger(msg): # slightly tricky first-class function
    def log_msg():
        print("log : ",msg)
    return log_msg # returns a function from another function
# practical advantage of this type of inner function return
def print_html(tag):
    def wrap_text(msg):
        print(" <{0}>{1}</{0}>".format(tag,msg))
    return wrap_text
if __name__=="__main__":
    # f=square
    # print(f)
    # print(f(5))
    # print(my_map(f,[1,2,3,4]))
    # f1=cube # very useful as just we have to pass new function
    # print(my_map(f1, [1, 2, 3, 4]))
    #
    #log=logger("hi")
    # print(log)# basically log=log_msg
    #log()# it will always print hi
    #log('kk') error will occur
    header=print_html('h1')
    header('kunal')
    header('bajaj')
    para= print_html('h1')
    para('kunal')
    para('bajaj')



