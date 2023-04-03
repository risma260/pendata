# Load Data ke Power BI

Nama : Indah Kharisma

NIM : 210411100147

Penambangan Data (B)

**Cara load data file csv ke excel** 

1. Download file iris.csv di github 
2. Pastikan di laptop sudah terinstall microsoft excel
3. Buka microsoft excel lalu pilih menu Data
4. Klik Dapatkan Data lalu pilih yang dari Text/CSV
5. Selanjutnya pilih file iris.csv yang sudah didownload ke dalam laptop tadi
6. Setelah tabel muncul, klik muat 
7. Lalu tabel csv akan termuat dalam file excel 
8. Terakhir klik save 

 

**Cara load data dari file csv ke power BI**

1. Download file iris.csv di github
2. Install power BI di laptop, lalu jalankan
3. Di bagian home, pilih Get Data
4. Lalu pilih Excel Workbook
5. Setelahnya akan disuruh memilih dimana file Iris.csv diletakkan dalam file 
6. Lalu setelah tabel muncul, klik load data 
7. Di bagian data, centang semua kolom 
8. Dibagian gambar grafik, klik view more agar tampilannya menjadi besar
9. Klik save file

 

**Cara load data file csv ke power BI lewat sql server**

1. Pertama-tama pastikan laptop sudah terinstall sql server, dengan mendownload di https://dev.mysql.com/downloads/file/?id=515908
2. buka xampp lalu hidupkan mysql dan apache
3. buka powerBI lalu klik get Data dan pilih MySQL database
4. isikan server (3306) dan database
5. lalu pilih “Use my current credentials” dan klik connect
6. Lalu setelah tabel muncul, klik load data 
7. Di bagian data, centang semua kolom 
8. Dibagian gambar grafik, klik view more agar tampilannya menjadi besar
9. Klik save file

 

**Cara load data file csv ke power BI lewat postgresql cloud (elephant)**

1. Pastikan laptop sudah terinstall aplikasi postgresql 
2. Buka website elephantsql.com
3. Lalu buat akun di elephant.com 
4. Setelah akun terbuat, pilih Create New Instance 
5. Buat nama “Pendatab” lalu untuk Plan pilih “Tiny Turtle (Free)”
6. Lalu untuk region and data center pilih “Amazon Web Services”, dan klik “AP-NorthEast-1(Tokyo)”
7. Setelahnya instance sudah berhasil dibuat
8. Selanjutnya buka postgresql lalu buat server baru dengan memasukkan nama server, username dan password di instance yang baru dibuat di elephant tadi
9. Lalu setelah server terbuat, cari nama database yang sesuai dengan instance yang dibuat tadi
10. Lalu import file iris.csv ke dalam tabel menggunakan query tool
11. Selanjutnya buka aplikasi power BI 
12. Pilih Get Data lalu cari postgreSQL database
13. Isikan Server dan database yang sudah terbuat di Instance elephant
14. Lalu isikan username dan password juga
15. Lalu klik connect 
16. Pilih table public.iris lalu klik load
17. Di bagian data, centang semua kolom 
18. Dibagian gambar grafik, klik view more agar tampilannya menjadi besar
19. Klik save file

 

**Cara load data file csv ke power BI lewat postgresql local**

1. Pastikan laptop sudah terinstall postgresql dan powerBI
2. Selanjutnya buka aplikasi power BI 
3. Pilih Get Data lalu cari postgreSQL database
4. Isikan Server “localhost:5432” dan database yang sudah dibuat di postgresql
5. Lalu isikan username “postgres” dan password 
6. Lalu klik connect
7. Pilih table public.iris lalu klik load
8. Di bagian data, centang semua kolom 
9. Dibagian gambar grafik, klik view more agar tampilannya menjadi besar
10. Klik save file