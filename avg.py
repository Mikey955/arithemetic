#average function   
def eleventh():
    def con_avg(a_val,pos):                                                  #This is the avg function
        b_val=""                                                             #declaring string type
        b_val=b_val.join(a_val)                                              #converting tuple value to string value
        b_val=b_val.split(',')                                               #spliting values
        b_len=len(b_val)
        val=0
        avg=0
        count=0

        print '%d Average:' %pos

        parsed = False                                                       #to catch invalid value
        while not parsed:
            try:
                while val < b_len:
                    a=float(b_val[val])
                    avg=avg+a
                    val=val+1
                avg=avg/b_len
                if val == b_len:
                    print 'There were %d invalid values' %count
                    print 'The average is %d' %avg
                    return 0
            except ValueError:
                val=val+1
                count=count+1
    parsed = False                                              
    while not parsed:
        try:
            int_list=[]
            entitiy=input('Number of Values:')                               #number of values
            entitiy=int(entitiy)
            print "Enter the values to be added (eg: '2,3,..' => 2+3+../..):"#entering values
            val=0
            while val < entitiy:
                a=input()
                int_list.append(a)
                val=val+1

            val=0
            while val < entitiy:
                con_avg(int_list[val],val+1)
                val=val+1
            return 0
        except SyntaxError,KeyboardInterrupt:
            print 'Invalid value!'
            parsed = True