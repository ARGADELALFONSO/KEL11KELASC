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

## Cara Menggunakan 
1. Persiapkan File Excel dan Program Python:
   - Pastikan Anda sudah memiliki file Excel bernama Vending_Machine_Inventory_Contoh.csv yang berisi data barang, harga, dan stok.
   - Simpan file Excel ini di folder yang sama dengan file Python (vending_machine.py) atau sesuaikan path file di dalam kode jika file Excel berada di lokasi berbeda.

2. Buka Terminal atau Command Prompt:
   - Navigasikan ke folder tempat Anda menyimpan file Python dan Excel.
   - Jalankan program dengan perintah berikut:
     bash
     python vending_machine.py

3. Setelah program dijalankan, daftar barang akan otomatis muncul di layar. Setiap barang akan dilengkapi informasi harga per unit dan stok yang masih tersedia.
  *Contoh Tampilan di desktop*:
  Daftar Barang di Mesin Penjual Otomatis:
  Oreo - Harga: Rp10000 | Stok: 40
  Tango - Harga: Rp5000 | Stok: 50
  Kitkat - Harga: Rp12000 | Stok: 50
  Lays - Harga: Rp15000 | Stok: 20

4. *input Nama Barang*:
   - Setelah daftar barang ditampilkan, Anda akan diminta untuk memasukkan nama barang yang ingin dibeli.
   - Klik nama barang (misalnya, "Aqua").
   
5. *Input Jumlah Uang*:
   - Jika barang tersedia, Anda akan diminta memasukkan jumlah uang yang Anda miliki.
   - Ketik jumlah uang dan tekan Enter.
   - 

6. *Cek Kecukupan Uang*:
   - Program akan membandingkan jumlah uang yang Anda masukkan dengan harga barang.
   - Jika uang yang dimasukkan kurang dari harga barang, program akan menampilkan pesan “Uang tidak cukup” dan membatalkan transaksi serta Anda bisa memilih barang lain.

   *Contoh Pesan Jika Uang Tidak Cukup*:
   
   Uang tidak cukup. Transaksi dibatalkan.
   
7. Jika uang yang Anda masukkan lebih dari harga barang, program akan menghitung dan memberikan kembalian.
  
  *Contoh Pesan Kembalian*:
  
  Kembalian Anda: Rp2000

#### Mengurangi Stok dan Menyimpan Perubahan

8. Setelah pembelian berhasil, program akan mengurangi stok barang yang dibeli dengan cara refresh manual.
   
9. Stok baru akan langsung diperbarui di file Excel, sehingga data barang dan stok selalu akurat.

  *Contoh Pesan Konfirmasi Pembelian*:
  
   Anda telah membeli Aqua. Terima kasih atas pembelian Anda!
  


