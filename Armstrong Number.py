num = int(input("Enter the number to check if it is an armstrong number: "))

sum=0
temp=num
while temp > 0:
    digit = temp % 10
    sum += digit**3
    temp//=10

if num==sum:
   print(num," is an armstrong number!")
else:
   print(num," isn't an armstrong number...")