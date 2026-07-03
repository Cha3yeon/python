a, b = map(int, input().split())
K = []

for i in range(10):
    if i %2 == 0:
        K.append(a)
        a =a + b
    else:
        K.append(b)
        b = a + b

for  i in K:
    i = str(i)
    print(i[-1], end =" ")


   
   

    



    
   