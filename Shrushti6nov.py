i=1
while i<6:
    print(i)
    i+=1


n=-1
while n>0:
    print("lather")
    print("rinse")
print("Dry off")


while True:
    line=input('@')
    if line[0]=='#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')


i=1
sum=0
while  i<11:
    sum+=i
    i+=1
    print('sum=',sum)
print(sum)


