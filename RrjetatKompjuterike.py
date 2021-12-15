import sys
from time import sleep
from random import uniform

def power():
    try:
        n1 = int(input("Numri: "))
        n2 = int(input("Fuqia: "))
        rezultati = n1**n2
        print("Numri i fuqizuar: " + str(rezultati))
        if not n1 or n2:
            raise ValueError("Keni lene nje hapesire pa shenuar")
            """ Nuk osht kry hale """
    except ValueError:
        print("Programi pranon vetem numra")
    except ValueError as e:
        print(e)
def numberToBinary():
    try:
        number = int(input("Numri Decimal: "))
        if number == 0:
             return [0]
        bit = []
        while number:
            bit.append(number % 2)
            number >>= 1
            zgjidhja = bit[::-1]
            listToStr = ' '.join(map(str, zgjidhja))
        print("Numri ne binar: " + listToStr)
    except ValueError:
        print("Programi pranon vetem numra decimal")
        numberToBinary()

def ipToBinary():
    try:
        ipAddress = input("Ip adresa: ")
        ip = ipAddress.split(".")
        binaryIp = print('{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])))
    except ValueError:
        print("Vlere jo e pranueshme")
        ipToBinary()
    except IndexError:
        print("Sheno 4 vlera/shifra te ndara me pike(.)")
        ipToBinary()
print('''
    Zgjidhe funksionin

    1.Ngritja ne fuqi

    2.Shndrrimi i numrit ne Binar

    3.Shndrrimi i Ip adreses ne Binar

            ''')
zgjedhja = int(input("Shenoni zgjedhjen: "))
if zgjedhja == 1:
    power()
elif zgjedhja == 2:
    numberToBinary()
elif zgjedhja == 3:
    ipToBinary()
else:
    print("Beni nje zgjedhje")

while True:
    vazhdo = input("Vazhdo? Po ose Jo: ")
    if vazhdo == "po":
        print('''
    Zgjidhe funksionin

    1.Ngritja ne fuqi

    2.Shndrrimi i numrit ne Binar

    3.Shndrrimi i Ip adreses ne Binar

            ''')
        zgjedhja = int(input("Shenoni zgjedhjen: "))
        if zgjedhja == 1:
            power()
        elif zgjedhja == 2:
            numberToBinary()
        elif zgjedhja == 3:
            ipToBinary()
        elif str(zgjedhja) == "stop":
            break
        else:
            print("Beni nje zgjedhje")
    elif vazhdo == "jo":
        dil = "-------- Shihemi --------"
        for char in dil:
            print(char, end='')
            sys.stdout.flush()
            sleep((uniform(0, 0.3)))
       # for letter in dil:
        #    print(letter, end='')
        break
