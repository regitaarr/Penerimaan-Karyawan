import mysql.connector
from mysql.connector import Error
try:
    konek = mysql.connector.connect(host='localhost',
                                    database='penerimaan_karyawan',
                                    user='regita_cahya',
                                    password='1412123')
#cek jika terjadi kesalahan
except Error as e:
    print("Tidak bisa koneksi, terjadi kesalahan ", e)