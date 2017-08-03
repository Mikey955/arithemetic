"""This is an division function where we receive an input variable(list) to this function. The values 
   will be parsed around and check if the values a verified or not. Then the result will be displayed"""

#we imported os so that whenever the user access this function its on a clear page 
import os
#this is the division function according to the menu
def division_function(parse_value):
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
            
            #if the user puts more than two values
            if parse_len > 2:
                print 'OOPS. You inserted more than two values.'
                return 0
            else:
                #we created the divisor and divident depended on waht values come first
                divident=float(parse_str[0])
                divisor=float(parse_str[1])
                #the first print statement will show us the quotient
                print 'The quotient is :%d' %(float(divident/divisor))
                #the second print will show us the remainder
                print 'The remainder is :%d' %(divident%divisor)
            return 0
        #here is where we catch an invalid value or a keyboard interrupt
        except ValueError,KeyboardInterrupt:
            print 'Invalid values! Division was not possible.'
            parsed = True