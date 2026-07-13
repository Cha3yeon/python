a,b = map(int,input().split())

K = []
K.append(a)
K.append(b)
for i in range(2,10):
    K.append((K[i-2] + K[i- 1])%10)

for i in K:
    print(i, end =" ")



   
   

    



    
   