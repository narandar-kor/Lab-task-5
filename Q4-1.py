number = (10,15,20,25,30,35,40)

Even = 0
Odd = 0

for i in number:
    if i%2==0:
        Even += 1
    else:
        Odd += 1

print("Even number's is : ",Even)
print("Odd number's is : ",Odd)