def decrypt (text,s):
        result = ""
        for i in range(len(text)):
                char = text[i]
                if(char.isupper()):
                    #Decrypt uppercase characters in plain text
                    result += chr((ord(char) - s-65)%26 + 65)
                else:
                    #Decrypt lowercase characters in plain text
                    result += chr((ord(char) - s-97) %26 + 97)
        return result
    
text = input("Enter your cipher : ")
s=int(input("Enter shift pattern : "))
print("Cipher : " + text)	
print("Shift pattern : " + str(s))
print("Plain text : " + decrypt(text,s))
