#factorial function 
def sixth():
    def con_fact(a_val):                                                    #This is the factorial function
        b_val=""                                                            #declaring string type
        b_val=b_val.join(a_val)                                             #converting tuple value to string value
        b_val=b_val.split(',')                                              #spliting values
        b_len=len(b_val)                                                    #finding length of the string
        val=0   
        parsed = False                                                      #to catch invalid value
        while not parsed:
            try:
                
                while val < b_len:
                    print '%d Factorial:' %(val+1)
                    a=int(b_val[val])                                       #checking for invalid value
                    val=val+1
                    if a < 0:
                        print("No Negative numbers")
                    elif a == 0:
                        print("1")
                    else:
                        fact=1                                              #finding fact
                        while a != 0:
                            fact=fact*a
                            a=a-1
                        print fact

                if val == b_len:
                    return 0
            except ValueError:
                print 'Invalid value!'
                val=val+1

    parsed = False                                              
    while not parsed:
        try:
            int_list=[]
            print "Enter the values to be added (eg: '2,3,..' => 2!,3!,..):"#entering values
            int_list=input()

            con_fact(int_list)
            return 0
        except SyntaxError,NameError:
            print 'Invalid value!'
            parsed = True