#fibonacci function 
def seventh():
    def con_fib(a_val):                                                                 #This is the fibonacci function
        b_val=""                                                                        #declaring string type
        b_val=b_val.join(a_val)                                                         #converting tuple value to string value
        b_val=b_val.split(',')                                                          #spliting values
        b_len=len(b_val)                                                                #finding length of the string
        val=0   
        parsed = False                                                                  #to catch invalid value
        while not parsed:
            try:
                
                while val < b_len:
                    print
                    print '%d Fibonacci:' %(val+1)
                    a=int(b_val[val])                                                   #checking for invalid value
                    val=val+1
                    if a < 0:
                        print("No Negative numbers")
                    elif a == 0:
                        print("0"),
                    elif a == 1:
                        print("0 1 "),
                    else:
                        fib=1                                                          #finding fact
                        a=a-1
                        first=0
                        second=1
                        print first,' ',second,
                        while a != 0:
                            fib=first+second
                            print (' %d ' %fib),
                            first=second
                            second=fib
                            a=a-1

                if val == b_len:
                    return 0
            except ValueError:
                print 'Invalid value!'
                val=val+1

    parsed = False                                              
    while not parsed:
        try:
            int_list=[]
            print "Enter the values to be added (eg: '2,3,..' => series till position):"#entering values
            int_list=input()

            con_fib(int_list)
            return 0
        except SyntaxError,NameError:
            print 'Invalid value!'
            parsed = True

seventh()