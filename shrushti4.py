#find last digit of the input number
number=int(input("Enter a number"))
last_digit=number%9
print(last_digit)


#check whether a number is odd or even
number=(input("Enter a number"))
if number%2==0:
    print("Number is Even")
else:
     print("Number is odd")

#Check whether a number is divisible by 3 or 5
number=(input("Enter a number"))
if number%3==0 and number%5==0:
    print("Number is divisible 3 and 5")
if number%3==0 and number%5!=0:
    print("Number is divisible by 3 but not 5")
if number%5==0 and number%3!=0:
    print("Number is divisible by 5 but not 3")
if number%3!=0 and number%5!=0:
    print("Number is niether divisible by 3 nor 5")



#User inputs one of the 3 colours red,green,yellow based on program should print: 'stop' for RED , 'get ready' for yellow, 'go' for green
colour=(input("Enter a colour"))
if colour=="R":#R=RED
    print("STOP")
if colour=="Y":#Y=YELLOW
    print("GET READY")
if colour=="G":#G=GREEN
    print("GO")