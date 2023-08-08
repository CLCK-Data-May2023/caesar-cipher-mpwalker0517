# add your code here
shift = input("Please enter the number of places to shift: ")
while not shift.isdecimal():
    print("You need to enter a number between 1 and 25")
    break



shift = int(shift)

if shift <= 25:
    ""
else:
    print("You need to enter a number between 0 and 25!")

message = input("Please enter a sentence: ").lower()

abc = "abcdefghijklmnopqrstuvwxyz"
cipher = ' '

for char in message:
    if char in abc:
        index = abc.find(char)
        index = index + shift
        if index > 25:
            index -= 26
        char = abc[index]
    cipher += char


print("The encrypted senctence is:", cipher) 
