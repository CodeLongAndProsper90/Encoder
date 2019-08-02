import random
from time import sleep
from colorama import Fore, Back, Style
from os import system, name
secure_mode = False
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')
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
                        encrypted = (ALPHABET.index(character) + int(sheet[position])) % 26
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
    if secure_mode == False:
        dat = open("." + encoded + ".edat", "r")
        odat = open("." + encoded + ".odat", "r")
        e = 0
        s = 0
        data = dat.read()
        data.rstrip()
        odata = odat.read()
        odata.rstrip()
        try:
            otp = open(data, "r")
            e = 1
        except:
            print("Verify Failed. 01, OTP does not exist in the current context.")
            pass
        da = int(otp.readline()) - int(odata)
        if e == 1:
            if da == 0:
                return True
        else:
            return False

def menu():
        choices = ['1', '2', '3', '4', '5']
        choice = '0'
        while True:
                while choice not in choices:
                        print('\nWhat would you like to do?')
                        print('1. Generate one-time pads')
                        print('2. Encrypt a message')
                        print('3. Decrypt a message')
                        print('4. Quit the program')
                        print('5. Verify Encryption')
                        print('6. Enter Secure mode')
                        choice = input('Please type 1, 2, 3, 4, 5 or 6 and press Enter ')
                        if choice == '1':
                                sheets = int(input('How many one-time pads would you like to generate? '))
                                length = int(input('What will be your maximum message length? '))
                                generate_otp(sheets, length)
                        elif choice == '2':
                                filename = input('Type in the filename of the OTP you want to use ')
                               
                                ofile = filename

                                sheet = load_sheet(filename)
                                plaintext = get_plaintext()
                                if '//' in plaintext:
                                    print('Nope/')
                                ciphertext = encrypt(plaintext, sheet)
                                filename = input('What will be the name of the encrypted file? ')
                                if '//' in filename:
                                    print("Nope.")
                                data = filename + ".edat" #make the file extension for verication

                                save_file(filename, ciphertext) #save the encrypted file

                                datafile = open("." + data,  "w") 
                                otp_file = open(ofile, "r")
                                datafile.write(ofile) #put the opt filename in the file
                                if secure_mode == True:
                                    datafile.truncate(0)
                                    datafile.write("//sm")
                                datafile.close() # stop handling
                                datafile = open("." + filename + ".odat","w")
                                datafile.write(otp_file.readline())
                                if secure_mode == True:
                                    datafile.truncate()
                                    datafile.write('//sm')
                                #exit the files
                                datafile.close()
                                otp_file.close()
                        elif choice == '3':
                                filename = input('Type in the filename of the OTP you want to use ')
                                sheet = load_sheet(filename)
                                filename = input('Type in the name of the file to be decrypted ')
                                ciphertext = load_file(filename)
                                plaintext = decrypt(ciphertext, sheet)
                                print('The message reads:')
                                print('')
                                print(plaintext)
                                if secure_mode == True:
                                    sleep(2.50)
                                    clear()
                                if secure_mode == False:
                                    verify(filename)
                        elif choice == '4':
                          exit()
                        elif choice == '5':
                            filename = input('What is the file to verify? ')
                            if verify(filename) ==  True:
                                sleep(1)
                                print(Fore.GREEN + "\nVerify passed"+Style.RESET_ALL)
                            else:
                                sleep(1)
                                print(Fore.RED + "\nVerify Failed."+Style.RESET_ALL)
                        elif choice == '6':
                            cho = input("Do you want to continue into safe mode? [y/N]")
                            cho.lower()
                            if cho == 'y':
                                secure_mode = True
                            else:
                                pass
                        choice = '0'

menu()
