# add your code here
shift = 5

shift = int(shift)

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


print("The encrypted sentence is: ",cipher)
