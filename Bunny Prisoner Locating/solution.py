#Function to get the corner value(x) of the given line(y)

def cornerx(x,y):
    #By corner value we mean the first ID (for x=1) in a given line(y)
    #So if y == 1 i.e. first line then we know that (1,1) has an ID 1
    
    if(y==1):
        return 1
    
    #Change in y
    dy = y-1
    
    #Corresponding corner ID( for x==1) for each value of y
    cx = 1 + dy
    return cx
     
def sol(x,y):
    
    #If x is 1 then we only need the corner value for that y
    
    if(x==1):
        return cornerx(x,y)
        
    #Else just get the corner value of that line and iterate to the xth value of that line
    #corner = cornerx(x,y)
    
    temp = cornerx(x,y)
    
    #Since our value start from 1.
    #Also each next value of ID is calculated by adding (x+y) to the previous value.
    #So fetch the corner ID and then start adding (x+y) to that value until the target is reached.
    
    for i in range(1,x):
        temp += i+y
        
    return str(temp)

print(sol(3,2))

#Output: 9
