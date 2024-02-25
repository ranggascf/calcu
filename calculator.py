def tambah(a, b):
    tambah = float(a) + float (b)
    return tambah

def kurang(a, b):
    kurang = float (a) - float (b)
    return kurang

def kali(a, b):
    kali = float (a) * float (b)
    return kali

def bagi(a, b):
    bagi = float (a) / float (b)
    return bagi

while True:
    print('\n\n\t\t========== Calculator ==========\n\n')
    a = input('Enter a number 1: ')
    b = input('Enter a number 2: ')
    print('\n1. Addition\n2. Subtraction\n3. Multiplication\n.4 Division\n.5 Cancelled')
    C = input('\npilih 1-5: ')
    if C == '1':
        print('Result: ', tambah(a, b))
    elif C == '2':
        print('Result: ', kurang(a, b))
    elif C == '3':
        print('Result: ', kali(a, b))
    elif C == '4':
        print('Result: ', bagi(a, b))
    elif C == '5':
        break
    else:
        print("Unknown Operation.")