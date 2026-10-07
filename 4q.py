# WAP to find the greatest of 3 numbers entered by the user.

a = int(input("ENTER FIRST NUMBER " )) 
b = int(input("ENTER SECOUND NUMBER " )) 
c = int(input("ENTER THIRD NUMBER " )) 

if a>b and a>c :
    print("GREATEST NUMBER = " , a  )
    
elif b>a and b>c :
    print("GREATEST NUMBER = " , b  )
    
else :
    print("GREATEST NUMBER = " , c  )