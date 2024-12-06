from PyQt5.QtWidgets import (
    QWidget, QGridLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox, QScrollArea, QComboBox, QDialog, QFormLayout, QApplication
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
import csv

class AdminLoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login Admin")
        self.setFixedSize(300, 150)

        layout = QFormLayout()
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.check_login)

        layout.addRow("Username:", self.username_input)
        layout.addRow("Password:", self.password_input)
        layout.addWidget(login_button)
        self.setLayout(layout)

        self.login_successful = False

    def check_login(self):
        if self.username_input.text() == "admin" and self.password_input.text() == "123":
            self.login_successful = True
            self.accept()
        else:
            QMessageBox.warning(self, "Login Gagal", "Username atau password salah.")


class VendingMachineUI(QWidget):
    def __init__(self, logic):
        super().__init__()
        self.logic = logic
        self.init_ui()
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.update_product_buttons()
    def init_ui(self):

        self.setStyleSheet("""
        QWidget {
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #a1c4fd, stop:1 #c2e9fb);
        }
        QPushButton {
            background-color: #ff9800;
            font-size: 14px;
            color: white;
            border-radius: 5px;
            padding: 10px;
        }
        QPushButton:hover {
            background-color: #ffa726;
        }
        QLabel {
            color: #2c3e50;
            font-size: 16px;
            font-weight: bold;
        }
        QTableWidget {
            background-color: #ffffff;
            alternate-background-color: #f0f0f0;
        }
        """)

        # **Scroll Area untuk Produk**
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        product_container = QWidget()
        grid_layout = QGridLayout(product_container)
        grid_layout.setSpacing(10)

        for i, item in enumerate(self.logic.inventory):
            row, col = divmod(i, 3)
            product_button = QPushButton(f"{item['Nama']}\nRp {item['Harga']}\nStok: {item['Stok']}")
            product_button.setFixedSize(120, 100)
            product_button.clicked.connect(lambda checked, name=item['Nama'], price=item['Harga']: self.add_to_cart(name, price))
            grid_layout.addWidget(product_button, row, col)

        scroll_area.setWidget(product_container)

        # **Tabel Keranjang Belanja**
        self.cart_table = QTableWidget()
        self.cart_table.setColumnCount(4)
        self.cart_table.setHorizontalHeaderLabels(['Nama Produk', 'Jumlah', 'Total Harga', 'Hapus'])
        self.cart_table.setAlternatingRowColors(True)

        # **Layout Total dan Pembayaran**
        total_layout = QHBoxLayout()
        self.total_label = QLabel("Total: Rp 0")
        total_layout.addWidget(self.total_label)

        self.money_input = QLineEdit()
        self.money_input.setPlaceholderText("Masukkan uang")
        total_layout.addWidget(self.money_input)

        self.payment_combo = QComboBox()
        self.payment_combo.addItems(["Cash", "Dana", "Gopay", "OVO"])
        total_layout.addWidget(self.payment_combo)

        # Tombol Bayar
        buy_button = QPushButton("Bayar")
        buy_button.setFixedSize(150, 40)
        buy_button.setStyleSheet("background-color: #4caf50; color: white; font-size: 14px; border-radius: 8px;")
        buy_button.clicked.connect(self.process_purchase)
        total_layout.addWidget(buy_button)

        # Tombol Hapus Keranjang
        clear_button = QPushButton("Hapus Keranjang")
        clear_button.setFixedSize(150, 40)
        clear_button.setStyleSheet("background-color: #f44336; color: white; font-size: 14px; border-radius: 8px;")
        clear_button.clicked.connect(self.clear_cart)
        total_layout.addWidget(clear_button)

        # Tombol Login Admin
        admin_login_button = QPushButton("Login Admin")
        admin_login_button.setFixedSize(150, 40)
        admin_login_button.clicked.connect(self.admin_login)

        # Tombol Refresh
        refresh_button = QPushButton("Refresh")
        refresh_button.setFixedSize(150, 40)
        refresh_button.setStyleSheet("background-color: #2196f3; color: white; font-size: 14px; border-radius: 8px;")
        refresh_button.clicked.connect(self.refresh_app_wrapper)  # Memanggil refresh_app di parent

        # Layout Header (Label + Tombol Login Admin dan Refresh di kanan atas)
        header_layout = QHBoxLayout()

        # Mengatur style hanya untuk label "Vending Machine"
        header_label = QLabel("Vending Machine")
        header_label.setStyleSheet("background: none;")  # Menghapus background hanya pada label ini
        header_layout.addWidget(header_label)

        header_layout.addStretch()  # Memberikan ruang kosong antara label dan tombol
        header_layout.addWidget(refresh_button)  # Menambahkan tombol refresh
        header_layout.addWidget(admin_login_button)  # Menambahkan tombol login admin di kanan

        # **Layout Utama**
        main_layout = QVBoxLayout()
        main_layout.addLayout(header_layout)  # Menambahkan header_layout ke main_layout
        main_layout.addWidget(scroll_area)
        main_layout.addWidget(self.cart_table)
        main_layout.addLayout(total_layout)

        self.setLayout(main_layout)

        # exit
        exit_button = QPushButton("Keluar")
        exit_button.setFixedSize(150, 40)
        exit_button.setStyleSheet("background-color: #f44336; color: white; font-size: 14px; border-radius: 8px;")
        exit_button.clicked.connect(self.close_application)  # Menghubungkan tombol dengan fungsi close_application
        total_layout.addWidget(exit_button)

    def admin_login(self):
        """Membuka dialog login admin"""
        login_dialog = AdminLoginDialog(self)
        if login_dialog.exec_() and login_dialog.login_successful:
            self.open_admin_panel()

    def open_admin_panel(self):
        """Membuka panel admin untuk mengelola produk"""
        admin_panel = QDialog(self)
        admin_panel.setWindowTitle("Panel Admin")
        admin_panel.setFixedSize(400, 300)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Panel Admin - Kelola Produk"))

        add_button = QPushButton("Tambah Produk Baru")
        add_button.clicked.connect(self.add_product)
        layout.addWidget(add_button)

        edit_button = QPushButton("Edit Stok Produk")
        edit_button.clicked.connect(self.edit_product_stock)
        layout.addWidget(edit_button)

        # Menambahkan tombol Edit Harga Produk
        edit_price_button = QPushButton("Edit Harga Produk")
        edit_price_button.clicked.connect(self.edit_product_price)
        layout.addWidget(edit_price_button)


        # Tambahkan Tombol Kembali dan Histori Transaksi
        back_button = QPushButton("Kembali")
        back_button.clicked.connect(admin_panel.close)
        layout.addWidget(back_button)

        history_button = QPushButton("Histori Transaksi")
        history_button.clicked.connect(self.show_transaction_history)
        layout.addWidget(history_button)

        admin_panel.setLayout(layout)
        admin_panel.exec_()

    def show_transaction_history(self):
        # Membuka window histori transaksi
        history_dialog = QDialog(self)
        history_dialog.setWindowTitle("Histori Transaksi")
        history_dialog.setFixedSize(600, 400)

        layout = QVBoxLayout()

        # Membaca transaksi dari file CSV
        transactions = self.read_transactions_from_csv()

        history_table = QTableWidget()
        history_table.setColumnCount(5)
        history_table.setHorizontalHeaderLabels(["Nama", "Total", "Pembayaran", "Kembalian", "Metode"])
        history_table.setRowCount(len(transactions))

        # Custom table styling
        history_table.setStyleSheet("""
            QTableWidget {
                border: 1px solid #ccc;
                font-size: 14px;
                background-color: #f9f9f9;
                gridline-color: #ddd;
            }
            QTableWidget::item {
                padding: 10px;
            }
            QHeaderView::section {
                background-color: #4CAF50;
                color: white;
                padding: 5px;
                font-weight: bold;
            }
            QTableWidget QTableCornerButton::section {
                background-color: #4CAF50;
            }
        """)

        for i, transaction in enumerate(transactions):
            history_table.setItem(i, 0, QTableWidgetItem(transaction["Nama"]))
            history_table.setItem(i, 1, QTableWidgetItem(str(transaction["Total"])))
            history_table.setItem(i, 2, QTableWidgetItem(str(transaction["Pembayaran"])))
            history_table.setItem(i, 3, QTableWidgetItem(str(transaction["Kembalian"])))
            history_table.setItem(i, 4, QTableWidgetItem(transaction["Metode"]))

        layout.addWidget(history_table)
        back_button = QPushButton("Kembali")
        back_button.clicked.connect(history_dialog.reject)
        layout.addWidget(back_button)
        
        history_dialog.setLayout(layout)
        history_dialog.exec_()

    def read_transactions_from_csv(self):
        transactions = []
        try:
            with open('transactions.csv', mode='r') as file:
                reader = csv.reader(file)  # Gunakan csv.reader untuk file tanpa header
                for row in reader:
                    if len(row) == 5:  # Pastikan format CSV benar
                        transactions.append({
                            "Nama": row[0],
                            "Total": int(row[1]),
                            "Pembayaran": int(row[2]),
                            "Kembalian": int(row[3]),
                            "Metode": row[4]
                        })
        except Exception as e:
            print(f"Error membaca file transaksi: {e}")
        return transactions

    def refresh_app(self):
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()  # Hapus semua widget
        self.update_product_buttons() 

    def refresh_app_wrapper(self):
        parent = self.parentWidget()
        if parent:
            parent.refresh_app()


    def update_product_stock(self):
        """Metode untuk mengupdate stok produk dari UI"""
        update_dialog = QDialog(self)
        update_dialog.setWindowTitle("Update Stok Produk")
        update_dialog.setFixedSize(300, 200)

        layout = QFormLayout()
        product_input = QComboBox()
        product_input.addItems([item['Nama'] for item in self.logic.inventory])  # Menambahkan produk
        stock_input = QLineEdit()

        update_button = QPushButton("Update")
        update_button.clicked.connect(lambda: self.save_product_stock(update_dialog, product_input, stock_input))

        layout.addRow("Pilih Produk:", product_input)
        layout.addRow("Stok Baru:", stock_input)
        layout.addWidget(update_button)

        update_dialog.setLayout(layout)
        update_dialog.exec_()

    def save_product_stock(self, dialog, product_input, stock_input):
        """Menyimpan perubahan stok produk dan memperbarui UI"""
        try:
            product_name = product_input.currentText()
            new_stock = int(stock_input.text())
            if self.logic.update_product_stock(product_name, new_stock):  # Update stok di backend
                self.refresh_app()  # Refresh UI setelah update stok
                QMessageBox.information(self, "Sukses", f"Stok untuk {product_name} berhasil diperbarui.")
                dialog.accept()
            else:
                QMessageBox.warning(self, "Error", "Produk tidak ditemukan.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Masukkan data valid.")

    def update_product_price(self):
        """Metode untuk mengupdate harga produk dari UI"""
        update_dialog = QDialog(self)
        update_dialog.setWindowTitle("Update Harga Produk")
        update_dialog.setFixedSize(300, 200)

        layout = QFormLayout()
        product_input = QComboBox()
        product_input.addItems([item['Nama'] for item in self.logic.inventory])  # Menambahkan produk
        price_input = QLineEdit()

        update_button = QPushButton("Update")
        update_button.clicked.connect(lambda: self.save_product_price(update_dialog, product_input, price_input))

        layout.addRow("Pilih Produk:", product_input)
        layout.addRow("Harga Baru:", price_input)
        layout.addWidget(update_button)

        update_dialog.setLayout(layout)
        update_dialog.exec_()

    def save_product_price(self, dialog, product_input, price_input):
        """Menyimpan perubahan harga produk dan memperbarui UI"""
        try:
            product_name = product_input.currentText()
            new_price = int(price_input.text())
            if self.logic.update_product_price(product_name, new_price):  # Update harga di backend
                self.refresh_app()  # Refresh UI setelah update harga
                QMessageBox.information(self, "Sukses", f"Harga untuk {product_name} berhasil diperbarui.")
                dialog.accept()
            else:
                QMessageBox.warning(self, "Error", "Produk tidak ditemukan.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Masukkan data valid.")

    def add_product(self):
        """Menambahkan produk baru dan memperbarui UI"""
        add_dialog = QDialog(self)
        add_dialog.setWindowTitle("Tambah Produk Baru")
        add_dialog.setFixedSize(300, 200)

        layout = QFormLayout()
        name_input = QLineEdit()
        price_input = QLineEdit()
        stock_input = QLineEdit()

        add_button = QPushButton("Simpan")
        add_button.clicked.connect(lambda: self.save_new_product(add_dialog, name_input, price_input, stock_input))

        back_button = QPushButton("Kembali")
        back_button.clicked.connect(add_dialog.reject)
        
        layout.addRow("Nama Produk:", name_input)
        layout.addRow("Harga:", price_input)
        layout.addRow("Stok:", stock_input)
        layout.addWidget(add_button)
        layout.addWidget(back_button)

        add_dialog.setLayout(layout)
        add_dialog.exec_()

    def save_new_product(self, dialog, name_input, price_input, stock_input):
        """Menyimpan produk baru dan memperbarui tampilan produk"""
        try:
            name = name_input.text()
            price = int(price_input.text())
            stock = int(stock_input.text())
            self.logic.add_product(name, price, stock)
            self.refresh_app() # Tambah produk baru ke logic
            QMessageBox.information(self, "Sukses", f"Produk {name} berhasil ditambahkan.")
            dialog.accept()

            # Memperbarui tampilan produk
            self.update_product_buttons()
        except ValueError:
            QMessageBox.warning(self, "Error", "Masukkan harga dan stok valid.")

    def edit_product_stock(self):
        """Mengedit stok produk melalui panel admin"""
        edit_dialog = QDialog(self)
        edit_dialog.setWindowTitle("Edit Stok Produk")
        edit_dialog.setFixedSize(300, 200)

        layout = QFormLayout()
        product_input = QComboBox()
        for product in self.logic.inventory:
            product_input.addItem(product['Nama'])

        stock_input = QLineEdit()
        edit_button = QPushButton("Simpan")
        edit_button.clicked.connect(lambda: self.save_product_stock(edit_dialog, product_input, stock_input))

        back_button = QPushButton("Kembali")
        back_button.clicked.connect(edit_dialog.reject)
        
        layout.addRow("Pilih Produk:", product_input)
        layout.addRow("Stok Baru:", stock_input)
        layout.addWidget(edit_button)
        layout.addWidget(back_button)

        edit_dialog.setLayout(layout)
        edit_dialog.exec_()

    
    def edit_product_price(self):
        """Mengedit harga produk melalui panel admin"""
        edit_dialog = QDialog(self)
        edit_dialog.setWindowTitle("Edit Harga Produk")
        edit_dialog.setFixedSize(300, 200)

        layout = QFormLayout()
        product_input = QComboBox()
        for product in self.logic.inventory:
            product_input.addItem(product['Nama'])

        price_input = QLineEdit()
        edit_button = QPushButton("Simpan")
        edit_button.clicked.connect(lambda: self.save_product_price(edit_dialog, product_input, price_input))

        back_button = QPushButton("Kembali")
        back_button.clicked.connect(edit_dialog.reject)
        
        layout.addRow("Pilih Produk:", product_input)
        layout.addRow("Harga Baru:", price_input)
        layout.addWidget(edit_button)
        layout.addWidget(back_button)
        
        edit_dialog.setLayout(layout)
        edit_dialog.exec_()


    def add_to_cart(self, product_name, price):
        """Menambahkan produk ke keranjang"""
        self.logic.add_to_cart(product_name, price)
        self.update_cart_table()

    def update_product_buttons(self):
        """Memperbarui tampilan tombol produk di UI secara otomatis"""
        for i, item in enumerate(self.logic.inventory):
            # Hapus tombol lama
            button = self.findChild(QPushButton, f"product_button_{i}")
            if button:
                button.deleteLater()

            row, col = divmod(i, 3)  # Menentukan posisi grid
            # Membuat tombol baru dengan harga dan stok terbaru
            product_button = QPushButton(f"{item['Nama']}\nRp {item['Harga']}\nStok: {item['Stok']}")
            product_button.setFixedSize(120, 100)
            product_button.setObjectName(f"product_button_{i}")
            product_button.clicked.connect(lambda checked, name=item['Nama'], price=item['Harga']: self.add_to_cart(name, price))
            
            # Menambahkan tombol produk baru ke layout
            self.grid_layout.addWidget(product_button, row, col)

    def update_cart_table(self):
        """Memperbarui tabel keranjang"""
        self.cart_table.setRowCount(0)
        for item in self.logic.cart:
            row_position = self.cart_table.rowCount()
            self.cart_table.insertRow(row_position)
            self.cart_table.setItem(row_position, 0, QTableWidgetItem(item['Nama']))
            self.cart_table.setItem(row_position, 1, QTableWidgetItem(str(item['Jumlah'])))
            self.cart_table.setItem(row_position, 2, QTableWidgetItem(f"Rp {item['Harga'] * item['Jumlah']}"))
            
            delete_button = QPushButton("Hapus")
            delete_button.clicked.connect(lambda checked, name=item['Nama']: self.remove_item(name))  # Memanggil remove_item
            self.cart_table.setCellWidget(row_position, 3, delete_button)

        total = self.logic.calculate_total()
        self.total_label.setText(f"Total: Rp {total}")

    def remove_item(self, product_name):
        """Fungsi untuk menghapus item dari cart dan update tabel"""
        self.logic.remove_from_cart(product_name)
        self.update_cart_table()  # Memperbarui tampilan tabel setelah dihapus

    def process_purchase(self):
        """Memproses pembelian"""
        try:
            money = int(self.money_input.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Masukkan jumlah uang valid.")
            return

        total = self.logic.calculate_total()
        if money < total:
            QMessageBox.warning(self, "Error", f"Uang tidak cukup. Total: Rp {total}.")
        else:
            change = money - total
            payment_method = self.payment_combo.currentText()
            self.logic.record_transaction(total, money, change, payment_method)
            
            # Menampilkan pesan transaksi berhasil dengan tombol kustom
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Transaksi Berhasil")
            msg_box.setText(f"Transaksi berhasil. Kembalian: Rp {change}.")
            
            # Menambahkan tombol kustom
            ok_button = QPushButton("Selesai")  # Ganti teks tombol
            msg_box.addButton(ok_button, QMessageBox.AcceptRole)
            
            # Menampilkan dialog
            msg_box.exec_()
            self.clear_cart()

    def clear_cart(self):
        """Menghapus isi keranjang"""
        self.logic.clear_cart()
        self.update_cart_table()
        
    def close_application(self):
        """Menutup aplikasi"""
        QApplication.quit()
        