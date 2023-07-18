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

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encode_text(text, shift):
    encoded_text = ""
    for char in text:
        cur_index = alphabet.index(char)
        new_index = 0
        if cur_index + shift < 26:
            new_index = cur_index + shift
        else:
            new_index = (cur_index + shift) - 25
        encoded_text += alphabet[new_index]
    return print(f"{encoded_text}")


def decode_text(text, shift):
    return print("decode")


if direction == "encode":
    encode_text(text, shift)
elif direction == "decode":
    decode_text(text, shift)
else:
    print("Wrong Direction")
