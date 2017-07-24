#minimum function   
def ninth():
    def con_min(a_val,pos):                                                 #This is the minima function
        b_val=""                                                            #declaring string type
        b_val=b_val.join(a_val)                                             #converting tuple value to string value
        b_val=b_val.split(',')                                              #spliting values
        b_len=len(b_val)
        val=0
        count=0

        print ('%d Minimum Value:' %pos)

        ch=1
        print '1. Minimization from whole list.'
        print '2. Minimization from position to position'
        print 'Enter you choice:' ,
        ch=input()

        parsed = False                                                      #to catch invalid value
        while not parsed:
            try:
                if ch == 1:
                    if val == 0:
                        mini=float(b_val[val])
                    while val < b_len:
                        a=float(b_val[val])
                        if mini > a:
                            mini=a
                        val=val+1
                elif ch == 2:
                    print 'Enter start position:',
                    val=input()
                    print 'Enter end position:',
                    n_len=input()
                    if n_len > b_len:
                        ch=3
                    else:
                        mini=float(b_val[val-1])
                        while val < n_len:
                            a=float(b_val[val])
                            if mini > a:
                                mini=a
                            val=val+1
                        val=b_len
                else:
                    print 'Invalid Option'
                    print '1. Minimization from whole list.'
                    print '2. Minimization from position to position'  
                    print 'Enter you choice:' ,
                    ch=input()
                    print

                if val == b_len:
                    print 'There were %d invalid values' %count
                    print 'The minimum value is %d' %mini
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
            print "Enter the values to be added (eg: '2,3,..' => 2<3<..):"  #entering values
            val=0
            while val < entitiy:
                a=input()
                int_list.append(a)
                val=val+1

            val=0
            while val < entitiy:
                con_min(int_list[val],val+1)
                val=val+1
            return 0
        except SyntaxError,KeyboardInterrupt:
            print 'Invalid value!'
            parsed = True