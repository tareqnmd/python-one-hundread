alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


from caesar_art import logo

print(logo)


def encode_text(text, shift):
    update_text = ""
    for char in text:
        if char in alphabet:
            cur_index = alphabet.index(char)
            if (cur_index + shift) < 26:
                update_text += alphabet[cur_index + shift]
            else:
                update_text += alphabet[(cur_index + shift) - 26]
        else:
            update_text += char

    return print(f"The encoded text is {update_text}")


def decode_text(text, shift):
    update_text = ""
    for char in text:
        if char in alphabet:
            cur_index = alphabet.index(char)
            if (cur_index + shift) >= 0:
                update_text += alphabet[cur_index - shift]
            else:
                update_text += alphabet[26 - (cur_index + shift)]
        else:
            update_text += char

    return print(f"The decoded text is {update_text}")


def caesar(text, shift, direction):
    update_text = ""
    for char in text:
        if char in alphabet:
            cur_index = alphabet.index(char)
            if direction == "encode":
                if (cur_index + shift) < 26:
                    update_text += alphabet[cur_index + shift]
                else:
                    update_text += alphabet[(cur_index + shift) - 26]
            elif direction == "decode":
                if (cur_index + shift) >= 0:
                    update_text += alphabet[cur_index - shift]
                else:
                    update_text += alphabet[26 - (cur_index + shift)]
        else:
            update_text += char
    return print(f"The {direction} text is {update_text}")


caesar_continue = True

while caesar_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        # if direction == "encode":
        #     encode_text(text, shift)
        # elif direction == "decode":
        #     decode_text(text, shift)

        caesar(text, shift, direction)
        result = input("Type 'yes' if you want to go again.\n")
        if result != "yes":
            caesar_continue = False
    else:
        print("Wrong Direction")
