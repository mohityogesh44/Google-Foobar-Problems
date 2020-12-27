def solution(n):

  #n is given as a string so we have to convert it to integer.
  
  n = int(n)
  
  #Our goal is to transform the number of pellets(n) to 1 in minimum number of possible operations.
  #The following operations are allowed.
      #Add "one" pellet i.e. n+1
      #Remove "one" pellet i.e. n-1
      #Divide number of pellets by 2 i.e. n/2
  
  count = 0
  
  while(n>1):
    
    #If the number is divisible by 2....we can use bitwise AND to check if a number is even or odd.
    
    if n & 1==0:
      
    #If the number is even then divide by 2....This can be achieved by bitwise right shift operation.
      
      n>>=1
    #If the number is odd
    else:
     #If the odd number is a multiple of 3 then subtracting one will make it even such that it can be
     #continuously divided by 2 until it is 1.
      
      if(n==3 or n%4==1):
        n = n-1
      
      else:
      #And if the odd number is other than a multiple of 3 then increasing it by 1 will give us an even number such that it can be
      #continuously divided by 2 until it is 1.
        n = n+1
    
    #Increase the count each time we perform an operation
    count+=1
    
    return count
