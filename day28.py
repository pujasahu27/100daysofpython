#f-string

letter = "Hey my name is {1} and I am from {0}"
country="India"
name="Puja"
print(letter.format(country,name))
print(f"Hey my name is {name} and I am from {country}")


"""subject="Maths"
print(f"I got 50 in {subject}")"""      


price=49.09999
txt=f"for only{price:.2f} dollars!"
print(txt)



val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")


name = 'rehan'
age = 20
print(f"Hello, My name is {name} and I'm {age} years old.")

print(f"{2 * 30}")

country="India"
name="Puja"
print(f"Hey my name is {{name}} and I am from {{country}}")
