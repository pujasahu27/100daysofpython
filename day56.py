#Write a Python program to import a built-in array module and display the namespace of the said module
import array
for name in array.__dict__:
    print(name)
