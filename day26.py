#exercise
import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
if(hour>=0 and hour<12):
   print("Good Morning sir!")
elif(hour>=12 and hour<17):
   print("Good Afternoon Sir!")
elif(hour>=17 and hour<0):
    print("Good Night Sir!")



   
   
