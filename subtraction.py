#subtraction function 
import os
def second():
    def con_sub(a_val,pos):                                                 #This is the subtraction function
    
        parsed = False                                                      #to catch invalid value
        while not parsed:
            try:
                b_val=""                                                    #declaring string type
                b_val=b_val.join(a_val)                                     #converting tuple value to string value
                b_val=b_val.split(',')                                      #spliting values
                print '%d Subtraction:' %pos
                a=float(b_val[0])                                           #checking for invalid value
                b=float(b_val[1])
                print (a-b)
                return 0
            except ValueError:
                print 'Invalid value!'
                parsed = True

    parsed = False                                              
    while not parsed:
        try:
            os.system('clear')
            int_list=[]
            entitiy=input('Number of Values:')                              #number of values
            entitiy=int(entitiy)
            print "Enter the values to be subtracted (eg: '2,3' => 2-3):"   #entering values
            val=0
            while val < entitiy:
                a=input()
                int_list.append(a)
                val=val+1

            val=0
            while val < entitiy:
                con_sub(int_list[val],val+1)
                val=val+1

            return 0
        except SyntaxError,KeyboardInterrupt:
            print 'Invalid value!'
            parsed = True