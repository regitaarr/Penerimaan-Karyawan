# 🎭 YG Entertainment Employee Recruitment System

> *Where dreams meet reality in the entertainment industry! ✨*

## 📝 Overview

Hai programmer kece! 👋 Ini adalah sistem penerimaan karyawan baru untuk YG Entertainment yang dibuat dengan penuh cinta oleh **Regita Cahya Arrahma** (NPM: 5220411359). Sistem ini membantu calon karyawan untuk mendaftar, mengikuti tes, dan mendapatkan jadwal wawancara dengan cara yang mudah dan menyenangkan! 🎪

## 🌟 Features

### 🔐 Authentication System
- **Sign In**: Daftar akun baru untuk pertama kali
- **Log In**: Masuk dengan akun yang sudah ada
- Validasi otomatis dengan database MySQL

### 📋 Registration Process
- Form pendaftaran lengkap dengan validasi
- Data tersimpan aman di database
- Interface yang user-friendly dengan ASCII art yang cantik

### 🧠 Psychometric Test
- **Test Logika Aritmatika**: Tes kemampuan berpikir logis
- **Test Analog Verbal**: Tes kemampuan bahasa dan analogi
- **Test Matematika Dasar**: Tes kemampuan hitung dasar
- Sistem scoring otomatis (passing grade: 70/100)
- Pengumuman hasil langsung setelah tes

### 📅 Interview Scheduling
- Jadwal wawancara random untuk fairness
- Dress code instructions yang jelas
- Berbeda untuk kandidat putra dan putri

## 🛠️ Tech Stack

```python
# Core Technologies
- Python 3.x
- MySQL Database
- mysql-connector-python
```

## 📊 Database Schema

### Tables:
1. **login** - User authentication data
2. **daftar_karyawan_baru** - Registration information
3. **skor_test** - Test scores and results

## 🎯 How It Works

### 1. **User Registration Flow**
```
Sign In → Fill Personal Data → Take Psychometric Test → Get Interview Schedule
```

### 2. **Test System**
- 10 questions across 3 categories
- Each correct answer = 10 points
- Minimum 70 points to pass
- Immediate feedback after each question

### 3. **Smart Scheduling**
- Random interview slot assignment
- Gender-specific dress code instructions
- Professional presentation requirements

## 🚀 Installation & Setup

### Prerequisites
```bash
# Install required packages
pip install mysql-connector-python
```

### Database Configuration
```python
# Update database connection in main file
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    passwd="your_password",
    database="penerimaan_karyawan"
)
```

### Run the Application
```bash
python main.py
```

## 🎨 User Interface

Sistem ini menggunakan ASCII art yang aesthetic untuk menciptakan pengalaman yang menyenangkan:

```
------------------------------------------------------------------------------------------------------------
                              PENERIMAAN KARYAWAN BARU TAHUN 2023
                                        YG ENTERTAIMENT
                           Jl. Mapo-gu, Hapjeongdong, No. 397-5, Kroya
------------------------------------------------------------------------------------------------------------
```

## 🎭 Fun Facts

- 🎪 Alamat kantor terinspirasi dari lokasi asli YG Entertainment di Korea
- 🎨 Interface dibuat dengan love menggunakan ASCII art
- 🧠 Soal tes dirancang untuk mengukur kemampuan logika dan verbal
- 🎯 Sistem scoring yang fair dan transparan
- 💫 Random interview scheduling untuk keadilan

## 🤖 Code Structure

### Main Functions:
- `rca_sigin()` - User registration
- `rca_login()` - User authentication  
- `rca_daftar()` - Employee registration form
- `rca_test()` - Psychometric test system
- `rca_wawancara()` - Interview scheduling
- `rca_menu()` - Main navigation menu

### Key Features:
- **Input validation** untuk semua form
- **Database integration** yang seamless
- **Error handling** yang comprehensive
- **User-friendly feedback** di setiap step

## 🎪 Special Touches

- Menggunakan `random.choice()` untuk jadwal wawancara yang fair
- Real-time timestamp untuk tracking waktu tes
- Gender-specific instructions yang detail
- Professional presentation dengan ASCII borders

## 🔮 Future Enhancements

- [ ] Web-based interface dengan Flask/Django
- [ ] Email notifications untuk jadwal
- [ ] Advanced analytics dashboard
- [ ] Mobile app version
- [ ] Multi-language support

## 👥 About the Developer

**Regita Cahya Arrahma** - NPM: 5220411359
*Passionate programmer with a love for creating user-friendly applications* 💝

---

*Made with 💖 and lots of ☕ for YG Entertainment recruitment process*

> "Coding is not just about writing programs, it's about creating experiences!" ✨
