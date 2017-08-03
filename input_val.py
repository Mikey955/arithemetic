"""This is an input function will will be called before going to any function because the value needs 
   to be parsed to the desired function for further calcuations"""

def user_getval():
    parsed = False                                              
    while not parsed:
        try:
            #created an empty variable
            user_input=input()

            #we are returning the user data to the variable so that operations can occur
            return user_input
        except SyntaxError,KeyboardInterrupt:
            print 'Invalid value!'
            parsed = True