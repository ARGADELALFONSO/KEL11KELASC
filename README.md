## Kelas      : C
## Kelompok   : 11
## Anggota    :
-  I0324097 RADITYA YEFTA SYALLOM
-  I0324112 ARGA DEL ALFONSO N.
-  I0324117 MUHAMMAD ABAKHTA QABIL GILBRAN


## Deskripsi
Ini adalah aplikasi mesin penjual otomatis berbasis PyQt5 yang memungkinkan pelanggan untuk melihat produk, menambahkannya ke keranjang, memproses pembelian, dan melihat riwayat transaksi. Aplikasi ini juga memiliki panel admin untuk mengelola stok produk, harga, dan menambahkan produk baru. Tujuan: Memahami konsep perulangan, logika percabangan, pengelolaan variabel dan kondisi, serta kalkulasi sederhana

## Fitur
## Fitur Pelanggan:
1.   Menelusuri Produk: Melihat daftar produk yang tersedia, termasuk harga dan stok.
2.   Menambah ke Keranjang: Menambah produk ke keranjang belanja dan mengatur jumlahnya.
3.   Memproses Pembelian: Membayar produk dalam keranjang, baik menggunakan uang tunai atau poin loyalitas.
4.   Melihat Riwayat Transaksi: Melihat riwayat transaksi masa lalu.

## Fitur Admin:
1.   Memperbarui Stok Produk: Mengubah stok produk yang ada.
2.   Memperbarui Harga Produk: Menyesuaikan harga produk yang ada.
3.   Menambahkan Produk Baru: Menambah produk baru ke dalam inventaris mesin penjual otomatis.
4.   Melihat Riwayat Transaksi: Admin dapat melihat riwayat transaksi lengkap, termasuk nama produk, total, metode 
     pembayaran, dan kembalian.

## Flow Chart Aplikasi Mesin Penjual Otomatis
![FlowChart drawio](https://github.com/user-attachments/assets/29a15681-b9a1-445c-a05b-074c110b93d8)

## Cara Menggunakan 
Struktur Umum Program
Import Library: Program ini mengimpor berbagai modul dari PyQt5 untuk membuat antarmuka pengguna, serta modul csv untuk membaca dan menulis data transaksi.

Kelas AdminLoginDialog: Kelas ini mengatur dialog untuk login admin. Pengguna diminta untuk memasukkan username dan password. Jika berhasil, dialog akan ditutup dan mengizinkan akses ke panel admin.

Kelas VendingMachineUI: Kelas utama yang mengatur antarmuka pengguna untuk mesin penjual otomatis. Kelas ini berisi berbagai elemen UI seperti tombol produk, tabel keranjang belanja, dan tombol untuk melakukan pembayaran.

Komponen Utama
Antarmuka Pengguna:

1.     Tombol Produk: Setiap produk dalam inventaris ditampilkan sebagai tombol. Ketika tombol ditekan, produk tersebut ditambahkan ke keranjang belanja.
2.     Tabel Keranjang Belanja: Menampilkan produk yang telah ditambahkan ke keranjang, jumlah, total harga, dan tombol untuk menghapus item dari keranjang.
3.     Total dan Pembayaran: Menampilkan total harga dari semua item di keranjang dan menyediakan input untuk memasukkan uang serta memilih metode pembayaran.

Fungsi Login Admin:

Ketika tombol "Login Admin" ditekan, dialog login admin muncul. Jika username dan password yang dimasukkan benar, panel admin akan terbuka.
Panel Admin:

Di panel admin, admin dapat menambah produk baru, mengedit stok produk, mengedit harga produk, dan melihat histori transaksi. Setiap fungsi ini membuka dialog baru untuk input data.
Pengelolaan Produk:

1.     Menambah Produk: Admin dapat menambahkan produk baru dengan memasukkan nama, harga, dan stok.
2.     Mengedit Stok dan Harga: Admin dapat mengubah stok dan harga produk yang sudah ada.
3.     Histori Transaksi: Admin dapat melihat histori transaksi yang disimpan dalam file CSV.
Keranjang Belanja:

Pengguna dapat menambahkan produk ke keranjang, melihat total harga, dan melakukan pembayaran. Setelah pembayaran, transaksi dicatat dan keranjang dibersihkan.
Proses Pembayaran:

Ketika pengguna melakukan pembayaran, program memeriksa apakah uang yang dimasukkan cukup. Jika cukup, transaksi dicatat, dan pengguna diberi tahu tentang kembalian.
Alur Kerja Program
- Inisialisasi: Program dimulai dengan inisialisasi kelas VendingMachineUI, yang mempersiapkan antarmuka pengguna dan mengupdate tombol produk berdasarkan inventaris.

Interaksi Pengguna:

Pengguna dapat memilih produk, menambahkannya ke keranjang, dan melakukan pembayaran.
Admin dapat login untuk mengelola produk dan melihat histori transaksi.
- Penyimpanan Data: Data transaksi disimpan dalam file CSV untuk referensi di masa mendatang.

- Refresh UI: Setelah setiap perubahan (seperti menambah produk atau mengedit stok), antarmuka pengguna diperbarui untuk mencerminkan perubahan tersebut.

Kesimpulan
Program ini adalah aplikasi mesin penjual otomatis yang interaktif, memungkinkan pengguna untuk membeli produk dan admin untuk mengelola inventaris. Dengan menggunakan PyQt5, program ini menyediakan antarmuka pengguna yang ramah dan fungsional, serta menyimpan data transaksi untuk keperluan administrasi.
  


