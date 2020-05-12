try:
    k=1
    while k<=100:        
        i = int(input("Enter your Number: "))
        print('Input a number')
        t=i
        g=t*10
        while t<=g:
            for x in range(1,11):
                print(i,'*',x,'=',t)
                t=t+i     
    k=k+1
except: print('\n\n\t\tInput a number\n\n')