def encrypt(text, s):
    result = ''

    # transverse the plain text

    for i in range(len(text)):
        char = text[i]

                        # Encrypt uppercase characters in plain text

        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():

                        # Encrypt lowercase characters in plain text

            result += chr((ord(char) + s - 97) % 26 + 97)
        elif ord(char) <= 64 and ord(char) >= 32:

                        # Encrypt common special characters

            result += chr((ord(char) + s - 32) % 33 + 32)
        else:

                        # Rest all symbols remain the same

            result += char
    return result


text = input('Enter your text : ')
s = int(input('Enter shift pattern : '))

print ('Plain text : ' + text)
print ('Shift pattern : ' + str(s))
print ('Cipher : ' + encrypt(text, s))	
		
