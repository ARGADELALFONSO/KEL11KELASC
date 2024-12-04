## Kelas      : C
## Kelompok   : 11
## Anggota    :
-  I0324097 RADITYA YEFTA SYALLOM
-  I0324112 ARGA DEL ALFONSO N.
-  I0324117 MUHAMMAD ABAKHTA QABIL GILBRAN


## Deskripsi
Buat simulasi mesin penjual otomatis di desktop di mana pengguna dapat memilih barang, membayar, dan menerima kembalian. Tambahkan juga stok barang yang bisa habis. Tujuan: Memahami konsep perulangan, logika percabangan, pengelolaan variabel dan kondisi, serta kalkulasi sederhana

## Fitur
- Menampilkan Daftar Barang               : menampilkan daftar barang yang tersedia di vending machine, lengkap dengan harga dan stok yang masih ada.
- Fitur Pemilihan Barang                  : memasukkan nama barang yang ingin dibeli. Program akan memeriksa apakah barang tersedia atau stoknya habis.
- Input Uang                              : meminta pengguna untuk memasukkan jumlah uang sesuai harga barang yang dipilih.
- Menu Pembayaran                         : pembeli dapat memilih menu pembayaran pada produk bisa cash maupun ewallet yang tersedia
- Kembalian                               : jika pembeli membayar cash dan memiliki kembalian maka jumlah kembalian akan muncul
- Pembaruan Stok dan Penyimpanan ke Excel : setelah transaksi selesai, stok barang yang dibeli akan otomatis dikurangi, dan perubahan ini disimpan langsung ke file Excel.
- Melanjutkan atau Mengakhiri Pembelian   : setelah setiap pembelian, pengguna akan diberikan opsi untuk melanjutkan membeli barang lain atau mengakhiri transaksi.
- Admin                                   : di fitur admin ini sebagai admin dapat melihat seperti riwayat transaksi dengan login akun dan password

## Cara Menggunakan 
1. Persiapkan File Excel dan Program Python:
   - Pastikan Anda sudah memiliki file Excel bernama Vending_Machine_Inventory_Contoh.xlsx yang berisi data barang, harga, dan stok.
   - Simpan file Excel ini di folder yang sama dengan file Python (vending_machine.py) atau sesuaikan path file di dalam kode jika file Excel berada di lokasi berbeda.

2. Buka Terminal atau Command Prompt:
   - Navigasikan ke folder tempat Anda menyimpan file Python dan Excel.
   - Jalankan program dengan perintah berikut:
     bash
     python vending_machine.py

3. Setelah program dijalankan, daftar barang akan otomatis muncul di layar. Setiap barang akan dilengkapi informasi harga per unit dan stok yang masih tersedia.
  *Contoh Tampilan di Console*:
  Daftar Barang di Mesin Penjual Otomatis:
  Aqua - Harga: Rp5000 | Stok: 10
  Chips - Harga: Rp7000 | Stok: 5
  Soda - Harga: Rp8000 | Stok: 8
  Coklat - Harga: Rp10000 | Stok: 3

4. *input Nama Barang*:
   - Setelah daftar barang ditampilkan, Anda akan diminta untuk memasukkan nama barang yang ingin dibeli.
   - Ketik nama barang (misalnya, "Aqua").

5. *Cek Ketersediaan Barang*:
   - Program akan memeriksa apakah barang yang Anda pilih tersedia dalam stok. 
   - Jika stok barang habis, program akan memberi tahu Anda dan kembali ke daftar barang untuk memilih barang lain.

   *Contoh Pesan Jika Stok Barang Habis*:
   
   Maaf, barang tidak tersedia atau stok habis.
   
6. *Input Jumlah Uang*:
   - Jika barang tersedia, Anda akan diminta memasukkan jumlah uang yang Anda miliki.
   - Ketik jumlah uang dan tekan Enter.

7. *Cek Kecukupan Uang*:
   - Program akan membandingkan jumlah uang yang Anda masukkan dengan harga barang.
   - Jika uang yang dimasukkan kurang dari harga barang, program akan menampilkan pesan “Uang tidak cukup” dan membatalkan transaksi serta Anda bisa memilih barang lain.

   *Contoh Pesan Jika Uang Tidak Cukup*:
   
   Uang tidak cukup. Transaksi dibatalkan.
   
8. Jika uang yang Anda masukkan lebih dari harga barang, program akan menghitung dan memberikan kembalian.
  
  *Contoh Pesan Kembalian*:
  
  Kembalian Anda: Rp2000

#### Mengurangi Stok dan Menyimpan Perubahan

9.  Setelah pembelian berhasil, program akan mengurangi stok barang yang dibeli.
10. Stok baru akan langsung diperbarui di file Excel, sehingga data barang dan stok selalu akurat.

  *Contoh Pesan Konfirmasi Pembelian*:
  
   Anda telah membeli Aqua. Terima kasih atas pembelian Anda!
  

#### Memilih untuk Melanjutkan atau Mengakhiri Pembelian

11. *Prompt Melanjutkan Pembelian*:
   - Setelah pembelian, program akan menanyakan apakah Anda ingin membeli barang lain.
   - Jika Anda mengetik y, program akan kembali menampilkan daftar barang untuk pembelian baru.
   - Jika Anda mengetik n, program akan menampilkan pesan penutup dan berhenti.

   *Contoh Prompt*:
   
   Apakah ingin membeli barang lain? (y/n): 
   
12. Jika Anda memilih untuk mengakhiri pembelian dengan mengetik n, program akan menampilkan pesan "Terima kasih telah menggunakan mesin penjual otomatis" dan selesai.

  *Pesan Penutup*:
  
  Terima kasih telah menggunakan mesin penjual otomatis.

Dengan mengikuti langkah-langkah di atas, Anda bisa menjalankan program vending machine ini untuk melakukan transaksi pembelian, menerima kembalian, dan memastikan stok selalu diperbarui di file Excel. Program ini akan terus berjalan hingga Anda memilih untuk berhenti.
