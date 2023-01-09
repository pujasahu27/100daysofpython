#KBC 
questions = [
["The International Literacy Day is observed on" ,"Sep 8", "Nov 28","May 2" ,"Sep 2","None",1],
["The language of Lakshadweep. a Union Territory of India", "Tamil", "Hindi", "Malayam","Telgu""None",3],
["Bahubali festival is related to","Islam","Hindusism" , "buddhism","Jainism","None",4],
["Which day is observed as the World Standards  Day","June 26","Oct 14","nov 15","dec 2","None",2],
["September 27 is celebrated every year as","Teachers' Day","National Integration Day", "World Tourism Day","International Literacy Day","None",3],
["Who is the author of 'Manas Ka-Hans","Khushwant Singh", "Prem Chand", "Jayashankar Prasad", "Amrit Lal Nagar","None",4],
["The death anniversary of which of the following leaders is observed as Martyrs' Day?","Smt. Indira Gandhi","PI. Jawaharlal Nehru","Mahatma Gandhi","Lal Bahadur Shastri","None",3],
["September 27 is celebrated every year as","Teachers' Day","National Integration Day", "World Tourism Day","International Literacy Day","None",3],
["Who is the author of 'Manas Ka-Hans","Khushwant Singh", "Prem Chand", "Jayashankar Prasad", "Amrit Lal Nagar","None",4],
["Who is the author of the epic 'Meghdoot","Vishakadatta", "Valmiki", "Banabhatta" "Kalidas","None",4],
]
levels = [1000, 2000, 3000, 5000, 10000, 20000,40000, 80000,160000,320000]
money=0

for i in range(0,len(questions)):
    question= questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"a.{question[1]}        b.{question[2]} ")
    print(f"c.{question[3]}        d.{question[4]} ")
    reply=int(input("Enter your answer(1-4)or 0 to quit:\n"))
    if(reply==0):
        money=levels[i-1]
        break
    if(reply==question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if(i==4):
            money = 10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000    
    else:
        print("wrong answer!")
        break
print(f"Your take home money is {money}")    
    
    
