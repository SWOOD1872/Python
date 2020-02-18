"""
Example #1:

    1. Runs the outer function
    2. Message variable gets set in the outer functions local scope
    3. Inner function gets created in the local scope of the outer function
    4. Outer function returns the in-place execution of the inner function i.e. the result of inner() gets returned by outer()
    5. The message 'Yo' gets printed

    So essentially, by running the outer function, you actually run the inner function. However, the inner function never gets
    exposed - only the outer function is exposed (callable in the global scope).
"""

def outer():
    message = 'Yo'

    def inner():
        print(message)
    
    return inner()

outer()

"""
Example #2:
    1. Variable ex2 gets assigned to the result of outer_2() i.e. ex2 equals the return value of outer_2()
    2. Message variable gets set to to the msg parameter, in this case 'Ello', in the local scope of outer_2()
    3. Function inner_2() gets created in the local scope of outer_2()
    4. Function outer_2() returns inner_2() - NOT the execution or return value of inner_2(), inner_2() is returned to ex2 itself
    5. Variable ex2 is now equal to inner_2() with a reference to the message variable, created in the local scope of outer_2() - 
    so ex2 can now be called as if it were inner_2()
    6. The newly created function, ex2(), gets executed and prints 'Ello' as per inner_2()
"""
def outer_2(msg):
    message = msg

    def inner_2():
        print(message)
    
    return inner_2

ex2 = outer_2('Ello')
ex2() # Prints 'Ello'