import string
import os

ASSETS_DIR = os.path.dirname(__file__)

def get_asset_path(filename: str) -> str:
    return os.path.join(ASSETS_DIR, filename)

def load_message(filename: str) -> str:

    path = get_asset_path(filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "[file missing]"

letters = string.ascii_letters[:26]

def crypting(message, choice, key):
    keyindex = 0
    key = key.lower()
    allofthem = []
    for letter in message:
        originalletter = letter
        letter = letter.lower()
        if ("z" >= letter >= "a"):
            if choice == "1":
                crypted = letters.index(letter) + letters.index(key[keyindex])
            else:
                crypted = letters.index(letter) - letters.index(key[keyindex])
            keyindex += 1
            if keyindex == len(key):
                keyindex = 0
            crypted %= 26
            letter = letters[crypted]
        if ("Z" >= originalletter >= "A"):
            letter = letter.capitalize()
        allofthem.append(letter)
    allofthem = "".join(allofthem)
    with open((os.path.join(ASSETS_DIR, "cryptedmessage.txt")), "w", encoding="utf-8") as file:
        file.write(allofthem)
    print(f"\n{load_message('cryptedmessage.txt')}\n")
            
message = load_message("message.txt")


crypting(message, input("1 = encrypt, 2 = decrypt: "), input("Enter a key:"))

