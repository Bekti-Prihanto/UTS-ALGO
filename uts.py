saldo = 0
sampah = 0
saldo_nasabah = 0
sampah_nasabah = 0
print('Selamat Datang di Bank Sampah')
print('Menu:')
print('1. Admin')
print('2. Nasabah')
print('Keluar')
menu = int(input('Masukkan menu yang anda pilih: '))
if menu == 1:
    #username "qwerty" pass "qwerty"
    username = input('Username:')
    password = input('Password:')
    if username == 'qwerty' and password == 'qwerty':
        print('1. Total Saldo: ')
        print('2. Total Sampah Terkumpul')
        admin = int(input('Masukkan Pilihan Anda:'))
        if admin == 1:
            print('Total saldo admin sebanyak %d'%saldo)
        elif admin == 2:
            print('Total sampah yang terkumpul %d'%sampah)
    else:
        print('username atau password anda salah')
elif menu == 2:
    print('1. Total saldo')
    print('2. Total sampah')
    nasabah = int(input('Masukkan Pilihan anda'))
    if nasabah == 1:
        print('Total saldo anda %d'%saldo_nasabah)
    elif nasabah == 2:
        print('Total sampah yang anda setorkan %d kg'%sampah_nasabah)
    else:
        print('Menu yang anda pilih tidak tersedia')
elif menu == 3:
    print('Terima Kasih')