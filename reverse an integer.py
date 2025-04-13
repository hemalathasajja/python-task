#write a program to reverse an integer value 54321 python
#here we are using M A D Technique % + // i.e modulus,addition,division

number = int(input("enter number: "))
reverse = 0
temp = number
while temp != 0:
    last_digit = temp % 10
    reverse = reverse * 10 + last_digit
    temp = temp // 10

print("Reverse of Number : ", number, " is : ", reverse )
