import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    your_text = ""
    if encode_or_decode == "decode":  #<--- if the user chooses decode, make the shift negative so it moves backwards
        shift_amount *= -1

    for letter in original_text: #<-- loop through every letter in the message

        if letter not in alphabet:# if the character is not in the alphabet (like space, number, symbol), just add it to the output without changing it.
            your_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount  #<--- find the position of the letter in the alphabet after the shift value is set.
            shifted_position %= len(alphabet)   #<--- keeps the position within the alphabet range, example- if z is encoded with shift 1,(26+1=27), it becomes a (26+1=27 , 27%26=1).
            your_text += alphabet[shifted_position]   #<--- add the new shifted letter to the output text
    print(f"Here is the {encode_or_decode}d result: {your_text}")


should_continue = True

while should_continue:  #<--- this is the main loop, it is there to let the user decide when he/she wants to quit, so it keeps on repeating.

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    should_restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if should_restart == "no":  #<--- if user says "no" then the program ends
        should_continue = False
        print("Thank You, and Goodbye")