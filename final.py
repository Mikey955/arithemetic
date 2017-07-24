from addition import first
from subtraction import second
from multipy import third
from division import fourth
from power import fifth
from fact import sixth
from fibo_func import seventh
from suma import eighth
from mini import ninth
from maxi import tenth
from avg import eleventh
from per import tweleth
import sys
import os

ret_val='y'
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
                first()
            elif choice == 2:
                second()
            elif choice == 3:
                third()
            elif choice == 4:
                fourth()
            elif choice == 5:
                fifth()
            elif choice == 6:
                sixth()
            elif choice == 7:
                seventh()
            elif choice == 8:
                eighth()
            elif choice == 9:
                ninth()
            elif choice == 10:
                tenth()
            elif choice == 11:
                eleventh()
            elif choice == 12:
                tweleth()
        
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
    except KeyboardInterrupt:
        print " " 
        print 'Do you wish to continue [y/n]:'
        ret_val=raw_input()                