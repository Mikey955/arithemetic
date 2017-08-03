"""This is an factorial function where we receive an input variable(list) to this function. The values 
   will be parsed around and check if the values a verified or not. Then the result will be displayed"""

#we imported os so that whenever the user access this function its on a clear page 
import os
#this is the factorial function according to the menu
def factorial_function(parse_value):
    parsed = False                                                      
    while not parsed:
        try:
            #to clear the screeen so that the user has no problem in reading its results 
            os.system('clear')
            print "Your given values: %s" %parse_value

            #we created a string so that we could read each character and implement on finding the error of
            #an invalid value
            parse_str=""
            #we used join to convert the values from the list to the string
            parse_str=parse_str.join(parse_value)
            #we then split each of the values wherever there was a ',' character
            parse_str=parse_str.split(',')
            #we found the length to string so that we could check each value from the string 
            parse_len=len(parse_str)

            #if a number is parsed this variable is used to collect that value
            num_value=1
            
            #if user inputs more than one values display message and return
            if parse_len > 1:
                print 'OOPS. Too many values.'
                return 0
            else:
                i=1
                #to parse thru the string
                while i <= int(parse_str[0]):
                    num_value=num_value*i                               
                    i=i+1
                print 'The factorial value is: %d' %num_value 
                return 0
        #here is where we catch an string value or a keyboard interrupt
        except ValueError,KeyboardInterrupt:
            print "Invalid Values!"
            parsed = True      