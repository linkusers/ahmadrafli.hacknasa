import sys
from time import sleep


def HekelTeks(Hekel):
    Starter = '\n_____hacking ',Hekel.upper(),' started ,sabar ya ngab_____\n'

    for char in Starter: #typewriter effect
        sleep(1) #delay code to display
        sys.stdout.write(char)
        sys.stdout.flush()

    sleep(1) 
    print('\n__getting IP server__\n')
    sleep(1)
    print('__proceed to encrypted data__\n')
    sleep(1)
    
    BinaryTeks = '100110010101010100' * 30

    for char in BinaryTeks: 
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()

        sleep(0.01)
    print('\n','\n __bentar lagi bang__ \n')

    Pyramid = "_"
    for i in range (0,101,10):
        sleep(0.2)
        print(Pyramid,i,'%')
        Pyramid += '_'
    
    print('\n',Hekel.upper(),'udah di hack gan UwU\n')
    UlangiHiking()

def InputUser():
    ListTarget = ['NASA','CIA','FBI','GOOGLE','FB','KGB','UN']
    print('#'*5,'selamat datang di program hiking NASA,CIA,FBI,GOOGLE,FB,KGB,UN','#'*5)
    InputTarget = str(input('mau ngehek apa hari ini ? : '))

    if InputTarget.upper() in ListTarget:
        HekelTeks(InputTarget)
    else:
        print('salah ketik bang ulangi !')
        InputUser()


def UlangiHiking():
    InputUlangi = str(input('mau ngehek lagi (y/g) ?  :'))
    if InputUlangi == 'y':
        InputUser()
    elif InputUlangi == 'g':
        print('\ngudbye ^_^')
    else:
        UlangiHiking()
InputUser()
