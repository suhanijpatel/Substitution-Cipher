import random

# A global constant defining the alphabet.
LCLETTERS = "abcdefghijklmnopqrstuvwxyz"

def isLegalKey( key ):
    # A key is legal if it has length 26 and contains all letters.
    # from LCLETTERS.
    return ( len(key) == 26 and all( [ ch in key for ch in LCLETTERS ] ) )

def makeRandomKey():
    # A legal random key is a permutation of LCLETTERS.
    lst = list( LCLETTERS )  # Turn string into list of letters
    random.shuffle( lst )    # Shuffle the list randomly
    return ''.join( lst )    # Assemble them back into a string

def caseChange( str , key, enc):
    result = ""
    for x in str :
        isUpper = 0
        if ord(x) < 91 :
            """check for case"""
            isUpper = 1
        if ord(x) < 91 and ord(x) > 64:
            x = x.lower()
            resultChar = ''
        if ord(x) > 96 and ord(x) < 123:
            if (enc == True) :
                """encrypt"""
                resultChar = key[ord(x)-97]
            else :
                resultChar = chr(key.find(x) + 97)

            if isUpper == 1 :
                resultChar = resultChar.upper()

            result+=resultChar

        else :
            result += x

    return result

# There may be some additional auxiliary functions defined here.
# I had several others, mainly used in encrypt and decrypt.

class SubstitutionCipher:
    def __init__ (self, key = makeRandomKey() ):
        """Create an instance of the cipher with stored key, which
        defaults to random."""
        if isLegalKey(key):
            self.__key = key
        else:
            print("Key entered is not legal")

    # Note that these are the required methods, but you may define
    # additional methods if you need them.  (I didn't need any.)

    def getKey( self ):
        """Getter for the stored key."""
        print("  Current cipher key: " + self.__key)

    def setKey( self, newKey ):
        """Setter for the stored key.  Check that it's a legal
        key."""
        if newKey == "random":
            self.__key = makeRandomKey()
            print("    New cipher key: " + self.__key)
        elif (isLegalKey(newKey)):
            self.__key = newKey
            print("    New cipher key: " + self.__key)
        elif newKey == "quit":
            command = ""
        else :
            print("    Illegal key entered. Try again!")
            command = input("  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ")
            self.setKey(command)

    def encryptText( self, plaintext ):
        """Return the plaintext encrypted with respect to the stored key."""
        print("    The encrypted text is: " + caseChange(plaintext, self.__key, True))

    def decryptText( self, ciphertext ):
        """Return the ciphertext decrypted with respect to the stored
        key."""
        print("    The decrypted text is: " + caseChange(ciphertext, self.__key, False))

def main( ):
    """ This implements the top level command loop.  It
    creates an instance of the SubstitutionCipher class and allows the user
    to invoke within a loop the following commands: getKey, changeKey,
    encrypt, decrypt, quit."""
    x = SubstitutionCipher()
    command = input("Enter a command (getKey, changeKey, encrypt, decrypt, quit): ")
    command = command.lower()
    while command != "quit":
        command = command.lower()
        if command == "getkey":
            x.getKey()
        elif command == "changekey":
            command = input("  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ")
            x.setKey(command)
        elif command == "encrypt":
            txt = input("  Enter a text to encrypt: ")
            x.encryptText(txt)
        elif command == "decrypt":
            txt = input("  Enter a text to decrypt: ")
            x.decryptText(txt)
        else:
            print("  Command not recognized. Try again!")
        command = input("Enter a command (getKey, changeKey, encrypt, decrypt, quit): ")
    print("Thanks for visiting!")

main()
