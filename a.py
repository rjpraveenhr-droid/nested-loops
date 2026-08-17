'''Write a program to check how many times a character is repeated in a word'''
#Take input of a word
string = input("please enter your own word : ")#Damian:6
#take input of a character
char = input("Please enter your own Character : ")#a
i = 0
count = 0
#loop will to find the occurence of character
while(i < len(string)): #string operation

    if(string[i] == char): #condition 1
        count = count + 1
    i = i + 1

    #Display the result 
    print("The total Number of times ", char, " has Occurred = " , count)