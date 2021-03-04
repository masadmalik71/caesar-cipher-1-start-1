alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
words = text.split()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#str = "Millie Bobby Brown is Enola Holmes"


def encode(text):
    character = []
    for letter in text:
        encrypt_index = alphabet.index(letter) + shift
        if encrypt_index/25 > 1:
            remainder = (encrypt_index%25) - 1
            character.append(alphabet[remainder])
        else:
            character.append(alphabet[encrypt_index])
            #encrypt_index = alphabet.index(letter) + shift - 25
            #print(remainder)
        
        wordy = ''.join(character)
    return wordy

def decode(text):
    character = []
    for letter in text:
        encrypt_index = alphabet.index(letter) - shift
        if encrypt_index/25 < -1:
            remainder = (encrypt_index%25) + 1
            character.append(alphabet[remainder])
        else:
            character.append(alphabet[encrypt_index])
        wordy = ''.join(character)
    return wordy

def sentance_maker(list1):
    characters = []
    for word in words:
        if direction == "encode" or direction == "e":
            characters.append(encode(word))
        elif direction == "decode" or direction == "d":
            characters.append(decode(word))
    str1 = ' '.join(characters)
    return str1

close = "yes"
close1 = "y"


while close == "yes" or  close1 == "y":

    print(sentance_maker(words))
    answer = input("You want to it again (Yes or No):\n").lower()
    if answer == "n":
        break
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    words = text.split()
    shift = int(input("Type the shift number:\n"))


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 