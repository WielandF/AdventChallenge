import numpy as np

f = open('InputDec1.txt', 'r')
message = f.readlines()
message=list(map(int,message))
arr= np.array(message)
#print(message)
#print(len(message))
zah=0
i=0
frequenz=[]
found= False

while found == False:
    
    zah+=arr[i]
  #  print(i)
    if i == len(arr)-1:
        print("hello")
        i=0
    else:    
     i+=1
    if zah in frequenz:
        found=True
        print(zah)
    else:
      frequenz.append(zah)
    

print('done')
#print(zah)
f.close()