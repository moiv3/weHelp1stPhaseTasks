def get_number(index):
    #your code here
    y = 0
    
    for x in range(index+1):
        if x == 0:
            y = 0
        elif x%3 == 0:
            y -= 1
        else:
            y += 4
    
    print(y)
        
get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70

#additional test data
#get_number(2) # print 8
#get_number(4) # print 11
#get_number(20) # print 50