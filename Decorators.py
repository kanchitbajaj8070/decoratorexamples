def decorator_function(original_function):# simplest decorator example
    def wrapper_function(*args,**kwargs):# just like first class function but with a function
        print(" about to execute", original_function.__name__)
        return original_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def display2():
    print(" in display 2 ")
@decorator_function
def display3(name,age): # we need to add args and kwargs for adding variable
    print(" in display 3 ",name,age)
def display():
    print("!!!!!!!!!!")

if __name__=="__main__":
    display2()
    display3("kunal",3)
    # usally we use this way with @
    # dec_ex= decorator_function(display) # general way of defining functions
    # dec_ex() # without using @
    # pass
