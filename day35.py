#for loop with else
for i in range(5):
    print(i)
else:
    print("Sorry no i")

    
for i in []:
     print(i)
else:
    print("Sorry no i")


for i in range(5):
    print(i)
    if i==4:
        break
else:
    print("Sorry no i")


for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")    
     
   
