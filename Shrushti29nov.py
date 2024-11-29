def sec_largest(a,b,c):
    if b>=a>=c or c>=a>=b:
        return a
    elif a>=b>=c or c>=b>=a:
        return b
    else:
        return c
print(sec_largest(10,20,30))

x=int(input("enter a year"))
if x%4==0 and (x%100!=0 or x%400==0):
    print("it is a leap year")
else:
    print("not a leap year")


def sum(x,y):
    return (x+y)
print("sum is",sum(5,6))

