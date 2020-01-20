import re

finalmsg=""
finalkey=0
deckey=26-finalkey
encrypted=[]
decrypted=[]
bruteDecrypted=[]

def msgip():
    global finalmsg
    msg=input("Enter the message [only lowercase]: ")
    if re.match("^[a-z ]*$", msg):
        finalmsg=msg
    else:
        print("Enter lowercase only")
        msg=''
        msgip()

def keyip():
    global finalkey
    key=eval(input("Enter the Key [1-26]: "))
    if -26 <= key <= 26:
        finalkey=key
    else:
        print("Enter correct key")
        key=0
        keyip()

def encrypt():
    s=''
    for ch in finalmsg:
        if ch==' ':
            encrypted.append(' ')
        else:
            encrypted.append(chr((ord(ch.upper()) - ord('A') + finalkey) % 26 + ord('A')))
    print("".join(encrypted))

def decrypt():
    for ch in encrypted:
        if ch==' ':
            decrypted.append(' ')
        else:
            decrypted.append(chr((ord(ch.lower()) - ord('a') - finalkey) % 26 + ord('a')))
            # decrypted.append((chr(ord(ch) + deckey)).lower())
    print("".join(decrypted))


msgip()
keyip()
encrypt()
decrypt()
