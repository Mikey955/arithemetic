#maximization function   
def tenth():
    def con_max(a_val,pos):                                                 #This is the maxima function
        b_val=""                                                            #declaring string type
        b_val=b_val.join(a_val)                                             #converting tuple value to string value
        b_val=b_val.split(',')                                              #spliting values
        b_len=len(b_val)
        val=0
        count=0

        print ('%d Maximum Value:' %pos)

        ch=1
        print '1. Maximization from whole list.'
        print '2. Maximization from position to position'
        print 'Enter you choice:' ,
        ch=input()

        parsed = False                                                      #to catch invalid value
        while not parsed:
            try:
                if ch == 1:
                    if val == 0:
                        maxi=float(b_val[val])
                    while val < b_len:
                        a=float(b_val[val])
                        if maxi < a:
                            maxi=a
                        val=val+1
                elif ch == 2:
                    print 'Enter start position:',
                    val=input()
                    print 'Enter end position:',
                    n_len=input()
                    if n_len > b_len:
                        ch=3
                    else:
                        maxi=float(b_val[val-1])
                        while val < n_len:
                            a=float(b_val[val])
                            if maxi < a:
                                maxi=a
                            val=val+1
                        val=b_len
                else:
                    print 'Invalid Option'
                    print '1. Maximization from whole list.'
                    print '2. Maximization from position to position'  
                    print 'Enter you choice:' ,
                    ch=input()
                    print

                if val == b_len:
                    print 'There were %d invalid values' %count
                    print 'The maximum value is %d' %maxi
                    return 0
            except ValueError:
                val=val+1
                count=count+1
    parsed = False                                              
    while not parsed:
        try:
            int_list=[]
            entitiy=input('Number of Values:')                              #number of values
            entitiy=int(entitiy)
            print "Enter the values to be added (eg: '2,3,..' => 2>3>..):"  #entering values
            val=0
            while val < entitiy:
                a=input()
                int_list.append(a)
                val=val+1

            val=0
            while val < entitiy:
                con_max(int_list[val],val+1)
                val=val+1
            return 0
        except SyntaxError,KeyboardInterrupt:
            print 'Invalid value!'
            parsed = True