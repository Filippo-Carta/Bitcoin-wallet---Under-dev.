import os
from cryptography.fernet import Fernet
import wallets
from bip_utils import (
    Bip39MnemonicGenerator,
    Bip39WordsNum,
)
import time

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()
print('\n WELCOME TO YOUR HARDWARE KEY WALLET \n')
print('CREATE WALLET [1]           OPEN WALLET [2] \n')

todo = input("OPTION >>  ")
try:
    if todo == "1":
        cls()
        if wallets.full == True:
            print('For security reasons you can\'t have more than 2 wallets stored')
            print(wallets.list)
            print('Press CTRL+C to exit...')
            time.sleep(999999999)
        print('\n             CREATING WALLET')
        wordnum = input("\n How many BIP39 words do you want? (12 / 24) >> ")
        
        if wordnum == "24":
            mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)

            cls()
            walname = str(input("Wallet name (Special characters not allowed) >> "))
            nb_passphrase = str(mnemonic)

            cls()
            ok = str(input('Im going to show you your passphrase. y/n >> '))
            if ok == "y":
                cls()
                print("\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print(nb_passphrase)
                print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                skip = input('\n\nThis is the only time you can see this, write it on a paper sheet. press [ENTER] to skip >> ')
                if skip == "":
                    cls()
                    def conf():
                        
                        conf_pssph = str(input("\n\nEnter passphrase (no dots, no capitals) >>"))
                        if conf_pssph == nb_passphrase:
                            cls()
                            print("\nSet Password\n")
                            setpass = str(input("Set a password (min. length 15) (make sure no one is watching) >> "))  
                            cls()
                            retype = str(input('Retype password >>'))

                            if setpass == retype and len(setpass) >= 15:

                                cls()
                                script_dir = os.path.dirname(os.path.abspath(__file__))

                                with open(os.path.join(script_dir, "wallets.py"), "a") as f:
                                    try:

                                        if (wallets.list[0]):

                                            f.write(f"\nlist2 = list1.append(\'{walname}\')\n")
                                            f.write(f'{walname} = ' + '{\n')
                                            f.write(f'\'wal\' : "{nb_passphrase}",\n')
                                            f.write('\n full = True')
                                            f.close()
                                            print('Writing it to file... wait...')
                                            time.sleep(3)
                                            f.close()
                                            print(f'Successfully created wallet {walname}')   
                                            

                                    except IndexError:
                                        
                                        f.write(f"\nlist1 = list.append(\'{walname}\')\n")
                                        f.write(f'{walname} = ' + '{\n')
                                        f.write(f'\'wal\' : "{nb_passphrase}",\n')
                                        f.write('\n}')
                                        f.close()
                                        print('Writing it to file... wait...')
                                        time.sleep(3)
                                        f.close()
                                        print(f'Successfully created wallet {walname}')           
                            else:
                                cls()
                                print("Try again. Exiting ...")
                        else:
                            cls()
                            print("WRONG. try again")
                            conf()

                    conf()
                else:
                    print("Exiting...")
            else:
                print("Exiting...")
        elif wordnum == '12':
            mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_12)

            cls()
            walname = str(input("Wallet name (Special characters not allowed) >> "))
            nb_passphrase = str(mnemonic)

            cls()
            ok = str(input('Im going to show you your passphrase. y/n >> '))
            if ok == "y":
                cls()
                print("\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print(nb_passphrase)
                print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                skip = input('\n\nThis is the only time you can see this, write it on a paper sheet. press [ENTER] to skip >> ')
                if skip == "":
                    cls()
                    def conf():
                        
                        conf_pssph = str(input("\n\nEnter passphrase (no dots, no capitals) >>"))
                        if conf_pssph == nb_passphrase:
                            cls()
                            print("\nSet Password\n")
            
                            def setpassword():
                                setpass = str(input("Set a password (min. length 15) (make sure no one is watching) >> "))  
                                cls()
                                retype = str(input('Retype password >>'))

                                if setpass == retype and len(setpass) >= 15:

                                    cls()
    
                                    script_dir = os.path.dirname(os.path.abspath(__file__))

                                    with open(os.path.join(script_dir, "wallets.py"), "a") as f:
                                        try:

                                            if (wallets.list[0]):

                                                f.write(f"\nlist2 = list1.append(\'{walname}\')\n")
                                                f.write(f'{walname} = ' + '{\n')
                                                f.write(f'\'wal\' : "{nb_passphrase}",\n')
                                                f.write(f"\'password\' : \'{setpass}\'")
                                                f.write('\n}')
                                                f.write('\n full = True')
                                                f.close()
                                                print('Writing it to file... wait...')
                                                time.sleep(3)
                                                f.close()
                                                print(f'Successfully created wallet {walname}')   
                                                

                                        except IndexError:
                                            
                                            f.write(f"\nlist1 = list.append(\'{walname}\')\n")
                                            f.write(f'{walname} = ' + '{\n')
                                            f.write(f'\'wal\' : "{nb_passphrase}",\n')
                                            f.write(f"\'password\' : \'{setpass}\'")
                                            f.write('\n}')
                                            f.close()
                                            print('Writing it to file... wait...')
                                            time.sleep(3)
                                            f.close()
                                            print(f'Successfully created wallet {walname}')     
                                                            
                                else:
                                    cls()
                                    print("Try again.")
                                    setpassword()
                            setpassword()
                        else:
                            cls()
                            print("WRONG. try again")
                            conf()
                    conf()
                else:
                    print("Exiting...")
            else:
                print("Exiting...")  
        else:
            print("This is not a valid passphrase number. Exiting...")
        
    elif todo == "2":
        guess = str(input("Enter your password >> "))
        if guess == wallets.qerthgth:
            pass     




    else:
        cls()
        print('Check your answer. Exiting...')
except KeyboardInterrupt:
    print("Exiting...")