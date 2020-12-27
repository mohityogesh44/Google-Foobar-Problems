#Note: Break in comments mean the "/" in question
#Functtion to calculate xor of n numbers (1 to n)
def xor(n):
    val = n%4
    if val==0:
        return n
    elif val==1:
        return 1
    elif val==2:
        return n+1
    return 0

def solution(start,length):

    #if only one element is present then just return that element
    
    if length==1:
        return start
    
    #calculate xor of the last element before first break (1--->last element before first break)
    #This is the xor value of numbers from 1 to last element until break
    
    val = xor(start + 2*(length-1))
    
    if start>1:
        
        #Now calculate the xor from 1 to start-1 and xor it with previous value to get the xor of start-->element until first break
        
        val = val^xor(start - 1)
    
    #Since so far we have covered two rows so the loop range will be length - 2
    
    for i in range(length-2):
        
        #no. of elements present in that specific row
        
        elements = (length-2)-i
        
        #element before the starting element of that row(xor in range (l,r) is xor(1,l-1)^xor(1,r))
        
        left = start + length*(2+i)-1
        
        #now calculate the xor value....left + elements gives us the last element of that row before break
        
        val = val^xor(left)^xor(left+elements)
    
    return val
