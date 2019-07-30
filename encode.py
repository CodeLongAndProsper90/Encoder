import random
from time import sleep
from colorama import Fore, Back, Style


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def count_lines(filename):
  i=0
  f = open(filename, "r")
  for line in f:
    i=+1
  return i
def generate_otp(sheets, length):
        for sheet in range(sheets):
                with open("otp" + str(sheet) + ".txt","w") as f:
                        for i in range(length):
                                f.write(str(random.SystemRandom().randint(0,29))+"\n")


def load_sheet(filename):
        with open(filename, "r") as f:
                contents = f.read().splitlines()
        return contents


def get_plaintext():
        plaintext = input('Please type your message ')
        return plaintext.lower()


def load_file(filename):
        with open(filename, "r") as f:
                contents = f.read()
        return contents


def save_file(filename, data):
        with open(filename, 'w') as f:
                f.write(data)


def encrypt(plaintext, sheet):
        ciphertext = ''
        for position, character in enumerate(plaintext):
                if character not in ALPHABET:
                        ciphertext += character
                else:
                        encrypted = (ALPHABET.index(character) + int(sheet[position])) % 29
                        ciphertext += ALPHABET[encrypted]
        return ciphertext


def decrypt(ciphertext, sheet):
        plaintext = ''
        for position, character in enumerate(ciphertext):
                if character not in ALPHABET:
                        plaintext += character
                else:
                        decrypted = (ALPHABET.index(character) - int(sheet[position])) % 26
                        plaintext += ALPHABET[decrypted]
        return plaintext

def verify(encoded):
    dat = open(encoded, "r")
    datLines = []
    e = 0
    s = 0
    datLines = dat.readlines()
    try:
        otp = open(datLines[0], "r")
        e = 1
    except:
        e = 0
        pass
    if otp.readline() == datLines[1]:
       s = 1
    if e == 1:
        if s ==1:
            return True
    else:
        return False

def menu():
        choices = ['1', '2', '3', '4', '5']
        choice = '0'
        while True:
                while choice not in choices:
                        print('What would you like to do?')
                        print('1. Generate one-time pads')
                        print('2. Encrypt a message')
                        print('3. Decrypt a message')
                        print('4. Quit the program')
                        print('5. Verify Encryption')
                        choice = input('Please type 1, 2, 3 or 4 and press Enter ')
                        if choice == '1':
                                sheets = int(input('How many one-time pads would you like to generate? '))
                                length = int(input('What will be your maximum message length? '))
                                generate_otp(sheets, length)
                        elif choice == '2':
                                filename = input('Type in the filename of the OTP you want to use ')
                                ofile = filename
                                sheet = load_sheet(filename)
                                plaintext = get_plaintext()
                                ciphertext = encrypt(plaintext, sheet)
                                filename = input('What will be the name of the encrypted file? ')
                                data = filename + ".edat"
                                save_file(filename, ciphertext)
                                datafile = open(data,  "w")
                                fo = open(ofile, "r")
                                datafile.write(ofile + "\n" + fo.readline())
                                datafile.close()
                                fo.close()
                        elif choice == '3':
                                filename = input('Type in the filename of the OTP you want to use ')
                                sheet = load_sheet(filename)
                                filename = input('Type in the name of the file to be decrypted ')
                                ciphertext = load_file(filename)
                                plaintext = decrypt(ciphertext, sheet)
                                print('The message reads:')
                                print('')
                                print(plaintext)
                                verify(filename)
                        elif choice == '4':
                          exit()
                        elif choice == '5':
                            filename = input('What is the file to verify?')
                            verify(filename)
                        choice = '0'

menu()
