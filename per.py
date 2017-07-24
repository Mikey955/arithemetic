#average function   
import os
def tweleth():
    def con_per(a_val,pos):                                                  #This is the avg function
        b_val=""                                                             #declaring string type
        b_val=b_val.join(a_val)                                              #converting tuple value to string value
        b_val=b_val.split(',')                                               #spliting values
        b_len=len(b_val)
        val=0
        per=0.0
        per_total=0
        count=0

        print '%d Percentage:' %pos

        parsed = False                                                       #to catch invalid value
        while not parsed:
            try:
                while val < b_len:
                    a=float(b_val[val])
                    if a > 100:
                        val=val+1
                        count=count+1
                    else:
                        per=per+a
                        val=val+1
                        per_total=per_total+1
                    
                per=(per/per_total)
                if val == b_len:
                    print 'There were %d invalid values' %count
                    print 'The percentage is %s' %(str(per))
                    return 0
            except ValueError:
                val=val+1
                count=count+1
    parsed = False                                              
    while not parsed:
        try:
            os.system('clear')
            int_list=[]
            entitiy=input('Number of Values:')                               #number of values
            entitiy=int(entitiy)
            print "Enter the values to be added (eg: '80,90,..(of 100)' => 80+90+../..):"#entering values
            val=0
            while val < entitiy:
                a=input()
                int_list.append(a)
                val=val+1

            val=0
            while val < entitiy:
                con_per(int_list[val],val+1)
                val=val+1
            return 0
        except SyntaxError,KeyboardInterrupt:
            print 'Invalid value!'
            parsed = True