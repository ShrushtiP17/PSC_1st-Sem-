temperature=int(input("Enter Temperature"))
if temperature<40:
     print("Cold")
else:
     print("Nice Weather")


hours=int(input("Enter total working hours"))
payroll=100
ob=5
if hours>40:
    a=hours*payroll*ob
    print("Overtime Pay",a)
else:
    b=hours*payroll
    print("Usual Pay",b)

x=5
if x>10:
    print("Bigger")
else:
    print("Smaller")

print("Finish")

x=5
if x==5:
    print("Equals to 5")
if x>4:
    print("Greater than 4")
if x>=5:
    print("Greater than equals to 5")
if x<6:
    print("lesser than 6")
if x<=5:
    print("Less than equals to 5")
if x!=6:
    print("Not equals to 6")
