#seek(),tell() and other function
#seek()
with open('file.txt' ,'r') as f:
    print(type(f))
    f.seek(10)
    data =f.read(5)
    print(data)
#tell()
with open('file.txt' ,'r') as f:
    print(type(f))
    f.seek(10)
    print(f.tell())
    data =f.read(5)
    print(data)

#truncate()
with open('file.txt', 'w') as f:
  f.write('Hello World3!')
  f.truncate(3)

with open('file.txt', 'r') as f:
  print(f.read())    
