#-------------------------------------------------
# NPM   : 5220411359
# NAMA  : REGITA CAHYA ARRAHMA
# SISTEM PENERIMAAN KARYAWAN BARU YG ENTERTAIMENT
#-------------------------------------------------

import os
import koneksi as rca
import random as ama
import datetime
now=datetime.datetime.now()

import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="regita_cahya",
    passwd="1412123",
    database="penerimaan_karyawan"
)

def rca_sigin():
    os.system("cls")
    print("-".center(46, "-"))
    print(" Sig In ".center(46, "-"))
    print("-".center(46, "-"))
    email=str(input('\nEmail    : '))
    password=str(input('Password : '))
    #menambahkan info sig in ke database tabel login
    sql = "INSERT INTO login VALUES (%s,%s)"
    val = (email,password)
    cursor = rca.konek.cursor()
    cursor.execute(sql,val)
    rca.konek.commit()
    print('\n----------------------------------------------')
    print(' Berhasil Sig in '.center(46, "-"))
    print('----------------------------------------------\n')
    rca_menu()

def rca_login():
    os.system("cls")
    print("-".center(46, "-"))
    print(" Log In ".center(46, "-"))
    print("-".center(46, "-"))
    email=str(input('\nEmail    : '))
    password=str(input('Password : '))
    #login dengan memanggil database dari tabel login
    cursor = rca.konek.cursor()
    sql = "SELECT * FROM login WHERE email LIKE %s OR password LIKE %s"
    val = (email,password)
    cursor.execute(sql, val)
    hasil = cursor.fetchall()

    if cursor.rowcount < 1:
        print('\n----------------------------------------------')
        print(' Email dan password tidak tersedia '.center(46, "-"))
        print(' Silahkan coba lagi! '.center(46, "-"))
        print('----------------------------------------------\n')
        os.system('pause')
        rca_login()
    else: 
        print('\n----------------------------------------------')
        print(' Berhasil Log In '.center(46, "-"))
        print('----------------------------------------------\n')
        rca_menu()

def rca_daftar():
    os.system("cls")
    print("-".center(108, "-"))
    print(' PENERIMAAN KARYAWAN BARU TAHUN 2023 '.center(108, "-"))
    print(' YG ENTERTAIMENT '.center(108, "-"))
    print(' Jl. Mapo-gu, Hapjeongdong, No. 397-5, Kroya '.center(108, "-"))
    print('------------------------------------------------------------------------------------------------------------\n')
    print("-".center(108, "-"))
    print(' Daftar Menjadi Karyawan Baru YG Entertaiment '.center(108, "-"))
    print("-".center(108, "-"))
    print('\nIsi Data Dengan Benar Dengan Teliti\n')
    no_dftr=int(input('\nNo Pendaftaran      : '))
    nama=str(input('Nama Lengkap        : '))
    nik=int(input('NIK                 : '))
    jenis_k=str(input('Jenis Kelamin [P/L] : '))
    ttl=str(input('Tanggal Lahir       : '))
    agama=str(input('Agama               : '))
    alamat=str(input('Alamat              : '))
    no_hp=int(input('No HP               : '))
    email=str(input('Email               : '))
    lulus=str(input('Lulusan             : '))
    ahli=str(input('Keahlian            : '))
    print('\nData Yang Anda Masukkan Tidak Bisa Diubah Lagi')
    #menambahkan data pendaftaran ke database tabel daftar_karyawan_baru
    sql = "INSERT INTO daftar_karyawan_baru VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (no_dftr,nama,nik,jenis_k,ttl,agama,alamat,no_hp,email,lulus,ahli)
    cursor = rca.konek.cursor()
    cursor.execute(sql,val)
    rca.konek.commit()
    print('\n------------------------------------------------------------------------------------------------------------')
    print(' Berhasil Mengisi Data '.center(108, "-"))
    print("-".center(108, "-"))
    rca_menu()

def rca_test():
    os.system("cls")
    print('\n------------------------------------------------------------------------------------------------------------')
    print(' PENERIMAAN KARYAWAN BARU TAHUN 2023 '.center(108, "-"))
    print(' YG ENTERTAIMENT '.center(108, "-"))
    print(' Jl. Mapo-gu, Hapjeongdong, No. 397-5, Kroya '.center(108, "-"))
    print('------------------------------------------------------------------------------------------------------------\n')
    print("-".center(108, "-"))
    print(' Test Psikotes Bagi Calon Karyawan Baru '.center(108, "-"))
    print("-".center(108, "-"))
    no_dftr=int(input('\nNo Pendaftaran : '))
    nama=str(input('Nama Lengkap   : '))
    email=str(input('Email          : '))
    cursor = rca.konek.cursor()
    sql = "SELECT * FROM daftar_karyawan_baru WHERE no_daftar LIKE %s OR nama LIKE %s"
    val = (no_dftr,nama)
    cursor.execute(sql, val)
    hasil = cursor.fetchall()
    if cursor.rowcount < 1:
        print('\n------------------------------------------------------------------------------------------------------------')
        print(' Kamu Harus Isi Data Pendaftaran Terlebih Dahulu '.center(108, "-"))
        print('------------------------------------------------------------------------------------------------------------\n')
    else: 
        print('Waktu Dimulai  :',now)
        print('\n------------------------------------------------------------------------------------------------------------')
        #soal
        print('\nTest Logika Aritmatika')
        print('\nPetunjuk Mengerjakan Soal')
        print('Selesaikanlah deret-deret (seri-seri) ini dengan memilih salah satu jawaban yang tepat!')
        print('\n1. Suatu seri : 100-4-90-7-80')
        print('a. 8     b.9     c.10    d.11    e.12')
        jwb=str(input('\nJawaban : '))
        nilai1=None
        if jwb=='c' or 'C':
            print('Jawabanmu Benar')
            nilai1=10
        else: 
            print('Jawabanmu Salah')
            nilai1=0

        print('\n2. 5-7-10-12-15 seri selanjutnya ...')
        print('a. 12     b.10     c.8    d.6    e.4')
        jwb=str(input('\nJawaban : '))
        nilai2=None
        if jwb=='e' or jwb=='E': 
            print('Jawabanmu Benar')
            nilai2=10
        else: 
            print('Jawabanmu Salah')
            nilai2=0

        print('\nTest Analog Verbal')
        print('\nPetunjuk Mengerjakan Soal')
        print('Pilihlah satu jawaban yang mempunyai arti sama atau paling')
        print('dekat dengan arti kata yang dicetak dengan huruf kapital!')
        print('\n3. RELATIF = ...')
        print('a. Biasa     b. Ukuran    c. nisbi    d.Statis    e. Pasti')
        jwb=str(input('\nJawaban : '))
        nilai3=None
        if jwb=='a' or jwb=='A':
            print('Jawabanmu Benar')
            nilai3=10
        else: 
            print('Jawabanmu Salah')
            nilai3=0

        print('\n4. RENOVASI = ...')
        print('a. Pemagaran     b. Pemugaran    c. Pembongkaran    d.Peningkatan    e. Pemekaran')
        jwb=str(input('\nJawaban : '))
        nilai4=None
        if jwb=='b' or jwb=='B':
            print('Jawabanmu Benar')
            nilai4=10
        else: 
            print('Jawabanmu Salah')
            nilai4=0

        print('\n5. PRESTISE = ...')
        print('a. Unggul     b. Elite     c. Martabat    d.Berkah    e. Pilihan')
        jwb=str(input('\nJawaban : '))
        nilai5=None
        if jwb=='a' or jwb=='A':
            print('Jawabanmu Benar')
            nilai5=10
        else: 
            print('Jawabanmu Salah')
            nilai5=0

        print('\nPetunjuk Mengerjakan Soal')
        print('Pilihlah satu jawaban yang mempunyai lawan kata dengan huruf kapital!')
        print('\n6. PAKAR >< ...')
        print('a. Awam     b. Cendikia    c. Mahir    d.Spesialis    e. Acuh')
        jwb=str(input('\nJawaban : '))
        nilai6=None
        if jwb=='a' or jwb=='A':
            print('Jawabanmu Benar')
            nilai6=10
        else: 
            print('Jawabanmu Salah')
            nilai6=0

        print('\n7. INHEREN >< ...')
        print('a. Lepas     b. Batal    c. Melekat   d.Mundur   e. Sinergi')
        jwb=str(input('\nJawaban : '))
        nilai7=None
        if jwb=='a' or jwb=='A':
            print('Jawabanmu Benar')
            nilai7=10
        else: 
            print('Jawabanmu Salah')
            nilai7=0

        print('\nPetunjuk Mengerjakan Soal')
        print('Pilihlah satu jawaban yang mempunyai padanan kata yang tepat untuk dari soal!')
        print('\n8. September : Agustus = Mei : ........')
        print('a. Bulan     b. Musim    c. Juni    d. Juli    e. April')
        jwb=str(input('\nJawaban : '))
        nilai8=None
        if jwb=='e' or jwb=='E':
            print('Jawabanmu Benar')
            nilai8=10
        else: 
            print('Jawabanmu Salah')
            nilai8=0

        print('\n9. PADI : PETANI .... : .....')
        print('a. Matahari : Panas     b. Puisi : Penyair    c. Dokter : Obat')    
        print('d. Sawah : Sapi         e. Dukun : Jamu')
        jwb=str(input('\nJawaban : '))
        nilai9=None
        if jwb=='b' or jwb=='B':
            print('Jawabanmu Benar')
            nilai9=10
        else: 
            print('Jawabanmu Salah')
            nilai9=0

        print('\nTes Matematika Dasar')
        print('\n10. Berapakah jumlah 47 orang dan 11 orang ?')
        print('a. 48 orang     b. 57 orang   c. 58 orang    d. 68 orang    e. 79 orang')
        jwb=str(input('\nJawaban : '))
        nilai10=None
        if jwb=='c' or jwb=='C':
            print('Jawabanmu Benar')
            nilai10=10
        else: 
            print('Jawabanmu Salah')
            nilai10=0

        #skor hasil test
        nilai_total=nilai1+nilai2+nilai3+nilai4+nilai5+nilai6+nilai7+nilai8+nilai9+nilai10
        skor=nilai_total

        print('\n------------------------------------------------------------------------------------------------------------\n')
        print('Waktu Selesai :',now)
        print('\n------------------------------------------------------------------------------------------------------------\n')
        print("-".center(108, "-"))
        print(' Terimakasih Kamu Sudah Menyelesaikan Test Ini '.center(108, "-"))
        print("-".center(108, "-"))

        #menambah data test ke tabel nilai_test
        sql = "INSERT INTO skor_test VALUES (%s,%s,%s,%s)"
        val = (no_dftr,nama,email,skor)
        cursor = rca.konek.cursor()
        cursor.execute(sql,val)
        rca.konek.commit()
        os.system('pause')

        #melihat pengumuman
        os.system('cls')    
        print(' PENERIMAAN KARYAWAN BARU TAHUN 2023 '.center(108, "-"))
        print(' YG ENTERTAIMENT '.center(108, "-"))
        print(' Jl. Mapo-gu, Hapjeongdong, No. 397-5, Kroya '.center(108, "-"))
        print('------------------------------------------------------------------------------------------------------------')
        print('\n------------------------------------------------------------------------------------------------------------')
        print(' Pengumuman Penerimaan Karyawan Baru YG Entertaiment '.center(108, "-"))
        print("-".center(108, "-"))

        cursor = rca.konek.cursor()
        print('\nSilahkan Isi Data Dibawah Untuk Melihat Informasi Selanjutnya\n')
        keyword = input('No Pendaftaran : ')
        keyword = input('Nama           : ')
        sql = "SELECT * FROM skor_test WHERE no_daftar LIKE %s OR nama LIKE %s"
        val = ("%{}%".format(keyword), "%{}%".format(keyword))
        cursor.execute(sql, val)
        hasil = cursor.fetchall()

        if cursor.rowcount < 0:
            print("Tidak ada data")
        else:
            print("+-----------------+-------------------------+-----------------------+---------+")
            print("| No Pendaftaran  |          Nama           |         Email         |   Skor  |")
            print("+-----------------+-------------------------+-----------------------+---------+")
            no=0
            for x in hasil : 
                no+=1
                print("| {:3d}             |".format(x[0]),
                    "{:24s}|".format(x[1]),
                    "{:15s}       |".format(x[2]),
                    "{:^8d}|".format(x[3]))
            print("+-----------------+-------------------------+-----------------------+---------+")

        if skor >= 70 and skor <=100 :
            print('\n------------------------------------------------------------------------------------------------------------')
            print(' Selamat!!! Kamu Lulus Ke Tahap Berikutnya! '.center(108, "-"))
            print('------------------------------------------------------------------------------------------------------------\n') 
        else:
            print('\n------------------------------------------------------------------------------------------------------------') 
            print(' Maaf, Kamu Belum Bisa Menjadi Karyawan YG Entertaiment ;) '.center(108, "-"))
            print('------------------------------------------------------------------------------------------------------------\n') 
            rca_menu()

def rca_wawancara():
    os.system('')
    jadwal=['Rabu, 7 Februari 2023. Pukul 07.30 WIB','Rabu, 7 Februari 2023. Pukul 13.30 WIB',
            'Kamis, 8 Februari 2023. Pukul 07.30 WIB','Kamis, 8 Februari 2023. Pukul 13.30 WIB']
    print("-".center(108, "-"))
    print('\nBagi Kamu Yang Lulus, Silahkan Ikuti Tahap Selanjutnya\n')
    print("-".center(108, "-"))
    no_dftr=int(input('\nNo Pendaftaran      : '))
    nama=str(input('Nama Lengkap        : '))
    jenis_k=str(input('Jenis Kelamin [P/L] : '))
    #memastikan calon karyawan yang akan melakukan wawancara telah melakukan test sebelumnya 
    cursor = rca.konek.cursor()
    sql = "SELECT * FROM skor_test WHERE no_daftar LIKE %s OR nama LIKE %s"
    val = (no_dftr,nama)
    cursor.execute(sql, val)
    hasil = cursor.fetchall()
    if cursor.rowcount < 1:
        print('\n------------------------------------------------------------------------------------------------------------') 
        print(' Data Tidak Tersedia, Kamu Belum Melakukan Test '.center(108, "-"))
        print('------------------------------------------------------------------------------------------------------------\n') 
    else: 
        if jenis_k == 'P' or 'p':
            print('\n------------------------------------------------------------------------------------------------------------') 
            print(' PENERIMAAN KARYAWAN BARU TAHUN 2023 '.center(108, "-"))
            print(' YG ENTERTAIMENT '.center(108, "-"))
            print(' Jl. Mapo-gu, Hapjeongdong, No. 397-5, Kroya '.center(108, "-"))
            print("-".center(108, "-"))
            print('\n------------------------------------------------------------------------------------------------------------') 
            print(' INFORMASI JADWAL WAWANCARA '.center(108, "-"))
            print('------------------------------------------------------------------------------------------------------------\n') 
            print('No Pendaftaran   : ',no_dftr)
            print('Nama             : ',nama)
            print('Jadwal Wawancara : ',ama.choice(jadwal))
            print('\n------------------------------------------------------------------------------------------------------------\n') 
            print('Dimohon Untuk Datang Tepat Waktu Dengan Memakai Kemeja Putih Dan Celana/Rok Hitam, Bagi Yang Berhijab')
            print('Diwajibkan Menggunakan Hijab Warna Hitam Dan Membawa File Seperti Yang Telah Diinfokan Sebelumnya Di Brosur')
            print('\n------------------------------------------------------------------------------------------------------------\n') 
        elif jenis_k == "L" or 'l':
            print('\n------------------------------------------------------------------------------------------------------------') 
            print(' PENERIMAAN KARYAWAN BARU TAHUN 2023 '.center(108, "-"))
            print(' YG ENTERTAIMENT '.center(108, "-"))
            print(' Jl. Mapo-gu, Hapjeongdong, No. 397-5, Kroya '.center(108, "-"))
            print("-".center(108, "-"))
            print('\n------------------------------------------------------------------------------------------------------------') 
            print(' INFORMASI JADWAL WAWANCARA '.center(108, "-"))
            print('------------------------------------------------------------------------------------------------------------\n')
            print('No Pendaftaran   : ',no_dftr)
            print('Nama             : ',nama)
            print('Jadwal Wawancara : ',ama.choice(jadwal))
            print('\n------------------------------------------------------------------------------------------------------------') 
            print('Dimohon Untuk Datang Tepat Waktu Dengan Memakai Kemeja Putih Dan Celana/Rok Hitam, Bagi Yang Berhijab')
            print('Diwajibkan Menggunakan Hijab Warna Hitam Dan Membawa File Seperti Yang Telah Diinfokan Sebelumnya Di Brosur')
            print('\n------------------------------------------------------------------------------------------------------------\n') 
        else:
            rca_menu()

def rca_menu():

    print("-".center(46, "-"))
    print(" MENU ".center(46, "-"))
    print("-".center(46, "-"))
    print("1. Sig in")
    print('2. Log In')
    print("3. Pendaftaran")
    print("4. Test dan Pengumuman")
    print("5. Informasi Jadwal Wawancara")
    print("6. Keluar")
    print("-".center(46, "-"))
    pilihan= input("Pilih Menu : ")

    #clear screen      
    os.system("cls")
    if pilihan == "1":
        rca_sigin()
    elif pilihan == "2":
        rca_login()
    elif pilihan == "3":
        rca_daftar()
    elif pilihan == "4":
        rca_test()
    elif pilihan == "5":
        rca_wawancara()
    elif pilihan == "6":
        print("-".center(46, "-"))
        print(' KELUAR '.center(46, "-"))
        print("Terimakasih".center(46, "-"))
        print("-".center(46, "-"))
        exit()
    else: print("Menu salah!")

if __name__ == "__main__":
    while(True):
        rca_menu()

