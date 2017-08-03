"""This is an average function where we receive an input variable(list) to this function. The values 
   will be parsed around and check if the values a verified or not. Then the result will be displayed"""

#we imported os so that whenever the user access this function its on a clear page 
import os
#this is the average function according to the menu
def average_function(parse_value):
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
            
            #we used a float variable in case of precautions that the user might use a decimal value 
            average_value=float(parse_str[0])
            i=1
            #to parse thru the string
            while i < parse_len:
                #we check the value at each position if there is any error
                convert_value=float(parse_str[i])
                #if there isn't the value keeps summing up
                average_value=average_value+convert_value
                i=i+1
            
            #too find the average we divide it by the number of values you have put 
            if i == parse_len:
                average_value=average_value/i

            #we then print the final average value
            print 'The average is :%d' %average_value
            return 0
        #here is where we catch an invalid value or a keyboard interrupt
        except ValueError,KeyboardInterrupt:
            print 'Invalid value! Average was not possible.'
            parsed = True