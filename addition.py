"""This is an addition function where we receive an input variable(list) to this function. The values 
   will be parsed around and check if the values a verified or not. Then the result will be displayed"""

#we imported os so that whenever the user access this function its on a clear page 
import os
#this is the addition function according to the menu
def add_function(parse_value):
    parsed = False                                                      
    while not parsed:
        try:
            #to clear the screeen so that the user has no problem in reading its results 
            os.system('clear')
            print "Your given values: %s" %parse_value

            #addition of two numbers will be stored in add_value
            add_value=0
            #to check how many values are being entered
            count=0

            #the for loop will go thru the entire list 
            for i in parse_value:
                #incrementing the number of elements to be cross checked
                count = count + 1 
                #to check if the value is a float variable
                #if i is type(int):
                add_value = add_value + i

            #if the number of elements is more than two or not 
            if count > 2:
                print 'More than two values.'
            else:
                print 'The addition is :%d' %add_value

            return 0
        #here is where we catch an invalid value or a keyboard interrupt
        except (ValueError,KeyboardInterrupt,TypeError):
            print 'Invalid value! Addition was not possible.'
            parsed = True