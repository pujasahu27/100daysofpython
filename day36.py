#Error Handling
a=input("enter the number:") #hello
print(f"Multiplication table of {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)


print("Some imp lines of code")
print("End of program")



a=input("enter the number:") 
print(f"Multiplication table of {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invalid Input!")



print("Some imp lines of code")
print("End of program")

try:
    num = int(input("Enter an integer:"))
    a =[6,3]
    print(a[num])
except ValueError:
    print("number is not integer:")
except IndexError:
    print("Index Error")

