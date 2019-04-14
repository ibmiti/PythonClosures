#  Closures


# Wikipedia says, "A closure is a record storing a function together with
# an environment: a mapping associating each free variable of the function
# with the value of storage location to which the name was bound when them
# closure was created. A closure, unlike a plain function, allows the function to access those captured variables through the closures
# reference to them, even when the function is invoked outside their scope."


#  an example of closure


def outer_func():
    message = 'Hi' # 2. it then moves to this because out_func was called, and it assigns hi to message

    def inner_func():  # 3. this is ran next
        print(message) # this is a free variable because it is not defined within this inner func which is nested within outer func so we have access to it since we are still within the outer_func

    return inner_func() #4. this is now returned and it printed the message var and its contents of 'Hi'

outer_func() # 1. the js engine runs this envocation first or call..


# heres another example where we will assign this entire function and its nested function to another function
def outer1_func():
    message1 = "hey"

    def inner_func1():
        print(message1)

    return inner_func1  # instead of executing this func and returning it, we will return the func without executing it

my_func = outer_func1()  # my_func is now equal to inner_func1 because we returned it


print(my_func.__name__) # will display inner_func

my_func1() # will print 'Hi'

# so in simple terms,, an closure is an inner function that remembers and have access to the variables in the local scope in which it was created even when the outer func has finished executing


def outer_func2(msg):
    message = msg

    def inner_func2():
        print(message)

    return inner_func2

hi_func = outer_func2("Hi")
hello_func = outer_func("hello")

hi_func()
hello_func()



    # a closure closes over the free variables in their environment
