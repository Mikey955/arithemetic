from addition import add_function
from subtraction import sub_function
'''from multipy import mutiply_function
from division import division_function
from power import power_function
from factorial import factorial_function
from summation import summation_function
from minimal import minimum_function
from maximal import maximum_function
from average import average_function
from percentage import percent_function
from fibonacci import fibonacci_function'''
from input_val import user_getval
import sys
import os

ret_val='y'
user_list=None
parsed = False                                                      #to catch invalid value
while not parsed:
    try:
        if ret_val in ('y','Y'):
            os.system('clear')
            print "        Arithemetic Function       "
            print "1. Addition"
            print "2. Subtraction"
            print "3. Multiplication"
            print "4. Division"
            print "5. Exponential"
            print "6. Factorial"
            print "7. Fibonacci Series"
            print "8. Summation"
            print "9. Minimum Value"
            print "10. Maximum Value"
            print "11. Average"
            print "12. Percentage"
            print 'Enter your choice:',
            choice=input()
            

            if choice == 1: 
                print 'Enter your vaules (eg: only two decimal values):'
                user_list=user_getval()                                        
                add_function(user_list)
            elif choice == 2:
                print 'Enter your values (eg: 1,2,3)'
                user_list=list(user_getval())
                sub_function(user_list)
            elif choice == 3:
                print 'Enter your values (eg: 1,2,a,b,...)'
                user_list=list(user_getval())
                mutiply_function(user_list)
            elif choice == 4:
                print 'Enter your values (eg: only two decimal values)'
                user_list=list(user_getval())
                division_function(user_list)
            elif choice == 5:
                print 'Enter your values (eg: only two integer values)'
                user_list=list(user_getval())
                power_function(user_list)
            elif choice == 6:
                print 'Enter your values (eg: only one integer value)'
                user_list=list(user_getval())
                factorial_function(user_list)
            elif choice == 7:
                print 'Enter your values (eg: only one sequence)'
                user_list=list(user_getval())
                fibonacci_function(user_list)
            #elif choice == 8:
             #   print 'Enter your values (eg: 1,2,3,...)'
              #  user_list=list(user_getval())
               # summation_function(user_list)
            elif choice == 9:
                print 'Enter your values (eg: 1,2,3,...)'
                user_list=list(user_getval())
                minimum_function(user_list)
            elif choice == 10:
                print 'Enter your values (eg: 1,2,3,...)'
                user_list=list(user_getval())
                maximum_function(user_list)
            elif choice == 11:
                print 'Enter your values (eg: 1,2,3,...)'
                user_list=list(user_getval())
                average_function(user_list)
            elif choice == 12:
                print 'Enter your values (eg: enter only 5 values less than or equal too 100)'
                user_list=list(user_getval())
                average_function(user_list)
        
            print " " 
            print 'Do you wish to continue [y/n]:'
            ret_val=raw_input()
        elif ret_val in ('n','N'):
            sys.exit()
        else:
            print " " 
            print 'Invalid Option'
            print 'Do you wish to continue [y/n]:'
            ret_val=raw_input() 
    except KeyboardInterrupt:                                       #error catcher
        print " " 
        print 'Do you wish to continue [y/n]:'
        ret_val=raw_input()                