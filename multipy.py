"""This is an multiplication function where we receive an input variable(list) to this function. The values 
   will be parsed around and check if the values a verified or not. Then the result will be displayed"""

#we imported os so that whenever the user access this function its on a clear page 
import os
#this is the multiplication function according to the menu
def mutiply_function(parse_value):
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
    #if a string or character comes up this variable is used to store that string
    char_value=''
    #it is used to control the while loop to store the value
    i=0

    parsed = False                                                      
    while not parsed:
        try:
            #to parse thru the string
            while i < parse_len:
                #to check wheather the its an integer value
                temp_val=int(parse_str[i]) 
                #updating the num_value by multiplication 
                num_value=num_value*temp_val
                #control of the loop
                i=i+1
            
            #to check weather to entire user input is read  
            if i == parse_len:
                #reassigning to control loop
                i=0
                #loop will run untill num_val
                while i < num_value:
                    #print till condition is meet
                    print char_value ,
                    i=i+1
                return 0
        #here is where we catch an string value or a keyboard interrupt
        except ValueError,KeyboardInterrupt:
            #updating char_value by append method
            temp_val=str(parse_str[i])
            char_value+=temp_val
            #incrementing i if character is read 
            i=i+1       