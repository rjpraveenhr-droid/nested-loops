#take two input from user
a = int(input("enter a lower range: ")) #10
b = int(input("enter a upper range: ")) #100

print("Prime numbers between", a, "and", b, "are:")
#iterate loop from lower limit to upper limit
for num in range(a, b + 1):
    # all prine numbers are greater than 1
    if num > 1:
        for i in range(2, num):#7 : 1 and 7: 2 to 6
            if (num % i) == 0:
                break
        else:
            print(num,"is a prime number")