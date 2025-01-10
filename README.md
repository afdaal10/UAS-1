# Aplikasi Manajemen Data Sepatu

Aplikasi ini adalah program sederhana yang memungkinkan pengguna untuk menambahkan informasi tentang sepatu, termasuk merek, ukuran, dan harga, serta menampilkan daftar sepatu yang telah dimasukkan. Program ini ditulis dalam bahasa pemrograman Python dan terdiri dari beberapa kelas: `Shoe`, `Data`, `View`, dan `Process`.

## Struktur Kode

### 1. Kelas `Shoe`

Kelas ini merepresentasikan objek sepatu dengan atribut merek, ukuran, dan harga.

#### Atribut:
- **`brand`**: Merek sepatu (tipe data: string).
- **`size`**: Ukuran sepatu (tipe data: float).
- **`price`**: Harga sepatu (tipe data: float).

#### Metode:
- **`__init__(self, brand, size, price)`**: Konstruktor yang menginisialisasi objek sepatu dengan merek, ukuran, dan harga yang diberikan.

### 2. Kelas `Data`

Kelas ini bertanggung jawab untuk menyimpan dan mengelola daftar sepatu.

#### Atribut:
- **`shoes`**: Daftar untuk menyimpan objek sepatu (tipe data: list).

#### Metode:
- **`__init__(self)`**: Konstruktor yang menginisialisasi daftar kosong untuk menyimpan objek sepatu.
- **`add_shoe(self, shoe)`**: Menambahkan objek sepatu ke dalam daftar.
- **`get_all_shoes(self)`**: Mengembalikan semua objek sepatu yang telah ditambahkan.

### 3. Kelas `View`

Kelas ini mengelola tampilan data sepatu kepada pengguna.

#### Metode:
- **`display_shoes(shoes)`**: Metode statis yang menerima daftar objek sepatu dan mencetaknya dalam format tabel. Tabel terdiri dari tiga kolom: "Brand", "Size", dan "Price".

### 4. Kelas `Process`

Kelas ini berfungsi sebagai penghubung antara input pengguna dan tampilan data.

#### Atribut:
- **`data`**: Objek dari kelas `Data`.
- **`view`**: Objek dari kelas `View`.

#### Metode:
- **`__init__(self)`**: Konstruktor yang menginisialisasi objek dari kelas `Data` dan `View`.
- **`input_shoe(self)`**: Mengambil input dari pengguna untuk menambahkan informasi tentang sepatu. Metode ini juga melakukan validasi pada ukuran dan harga untuk memastikan keduanya positif.
- **`show_all_shoes(self)`**: Mengambil semua objek sepatu dari kelas `Data` dan memanggil metode `display_shoes` dari kelas `View`. Jika tidak ada sepatu yang ditambahkan, akan menampilkan pesan bahwa tidak ada data.

#
Berikut adalah link YouTube mengenai dokumentasi penjelasan program:
https://youtu.be/sJfkjD58kAM?si=6cJjug-QCvRS3UF6
