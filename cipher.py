# right shift 5
shift = 5
shift = int(shift)

#Receive message from input
message = input("Please enter a sentence: ").lower()


abc = "abcdefghijklmnopqrstuvwxyz"
encrypted_sentence = " "

#Encrypt sentence
for char in message:
    if char in abc:
        index = abc.find(char)
        index = index + shift
        if index > 25:
            index -= 26
        char = abc[index]
    encrypted_sentence += char


print('The encrypted sentence is: '+encrypted_sentence)
