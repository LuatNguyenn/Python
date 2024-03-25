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
import operator


def convert(text, shift, op):
    newIndex = 0
    encodeArr = []
    encodedString = ""
    for i in range(0, len((text).lower())):
        currentIndex = alphabet.index(text[i])
        newIndex = eval(str(currentIndex) + op + str(shift))
        encodeArr.append(alphabet[int(newIndex)])
    for y in encodeArr:
        encodedString += y
    return encodedString


def main():
    continueFlag = True
    while continueFlag:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        if direction == "encode":
            encodeStr = convert(text, shift, "+")
            print(f"Here is the encoded result: {encodeStr}")
        elif direction == "decode":
            decodeStr = convert(text, shift, "-")
            print(decodeStr)
        print("Type yes if continue and no to close")
        ans = input()
        if ans == "yes":
            continueFlag = True
            encodeArr = []
        else:
            continueFlag = False


# print('CLosed')
main()


# def decode(text, shift):
#     newIndex = 0
#     decodeArr = []
#     decodedString = ""
#     for i in range(0, len((text).lower())):
#         currentIndex = alphabet.index(text[i])
#         newIndex = currentIndex - shift
#         decodeArr.append(alphabet[newIndex])
#     for y in decodeArr:
#         decodedString += y
#     return decodedString
