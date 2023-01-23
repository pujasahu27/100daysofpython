#read(), readlines() and other methods 
"""f = open('myfile50.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)"""



"""f = open('myfile50.txt', 'r')
i=0
while True:
    i=i+1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of student {i} in math is:{m1*2}")
    print(f"Marks of student {i} in English is:{m2*2}")
    print(f"Marks of student {i} in GK is:{m3*3}")
    print(line)"""



f = open('myfile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()
