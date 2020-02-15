def outer_fun():
    message='hi'
    def inner_fun():# accessing variable oof outside fun
        print(message)
    return inner_fun
if __name__=="__main__":
    my_fun=outer_fun()
    print(my_fun)
    my_fun()
    """ closure is an inner function that remembers the variables in its scope and has access
    to variable in its local scope even after outside function is executed"""

    pass