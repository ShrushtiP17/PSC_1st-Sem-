x=int(input("enter age of the person"))
if x<18:
     print("Teenager")
if x>18 and x<30:
     print("Adult")
elif x>30:
     print("Senior")

def age(age1):
    if age1<18:
        return"Teenager"
    if age1>=18 and age1<=30:
        return "Adult"
    if age1>30:
        return "Senior"
x=int(input("enter age of the person"))
y=int(input("enter age of the person"))
z=int(input("enter age of the person"))

print(age(x))
print(age(y))
print(age(z))