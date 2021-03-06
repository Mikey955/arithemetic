"""This is an percentage function where we receive an input variable(list) to this function. The values 
   will be parsed around and check if the values a verified or not. Then the result will be displayed"""

#we imported os so that whenever the user access this function its on a clear page 
import os
#this is the percentage function according to the menu
def percent_function(parse_value):
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
            
            #if the user puts more than the assigned values
            if parse_len > 5:
                print 'OOPS. Too many values.'
                return 0

            #we used a float variable in case of precautions that the user might use a decimal value 
            percent_value=float(parse_str[0])
            i=1
            #to parse thru the string
            while i < parse_len:
                #we check the value at each position if there is any error
                convert_value=float(parse_str[i])
                
                #to check if values are in range
                if convert_value > 100:
                    print 'Values were put higher than required.'
                
                #if there isn't the value keeps summing up
                percent_value=percent_value+convert_value
                i=i+1
            
            if i == parse_len:
                percent_value=(percent_value/(500))*100

            #we then print the final percentage value
            print 'The percentage is :%d' %percent_value ,
            print '%'
            return 0
        #here is where we catch an invalid value or a keyboard interrupt
        except ValueError,KeyboardInterrupt:
            print 'Invalid value! Percentage was not possible.'
            parsed = True