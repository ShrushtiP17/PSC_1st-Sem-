
n=int(input("enter a number"))
sum=0
for x in range(1,n+1):
    sum=sum+x
print(sum)

n=int(input("enter a number"))
print(n*(n+1)/2)

n=int(input("enter a number"))
sum_odd=0
sum_even=0
for x in range(1,n+1):
    if x%2==0:
        sum_even=sum_even+x
    elif x%2!=0:
        sum_odd=sum_odd+x
print(sum_even)
print(sum_odd)

n=int(input("enter a number"))
n_even=n//2
n_odd=n//2
if n%2==1:
    n_odd=n_odd+1
sum_even=n_even*(n_even+1)
sum_odd=n_odd*n_odd
print(sum_even)
print(sum_odd)


n=int(input("enter a number"))
div=0
for x in range (1,n+1):
    if x%n==0:
        div=div+1
        print(x)


