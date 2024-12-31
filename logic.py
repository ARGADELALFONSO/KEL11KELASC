import csv
from datetime import datetime

class VendingMachineLogic:
    def __init__(self, inventory_file="inventory.csv", transactions_file="transactions.csv"):
        self.inventory_file = inventory_file
        self.transactions_file = transactions_file
        self.load_inventory()
        self.cart = []

    def load_inventory(self):
        """Memuat data produk dari CSV"""
        self.inventory = []
        try:
            with open(self.inventory_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.inventory.append({
                        'Nama': row['Nama'],
                        'Harga': int(row['Harga']),
                        'Stok': int(row['Stok'])
                    })
        except FileNotFoundError:
            print("File inventory tidak ditemukan.")
        except Exception as e:
            print(f"Error saat memuat inventory: {e}")

    def save_inventory(self):
        """Menyimpan inventory ke file CSV"""
        with open(self.inventory_file, 'w', newline='') as file:
            fieldnames = ['Nama', 'Harga', 'Stok']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.inventory)

    def add_to_cart(self, product_name, price):
        """Menambahkan produk ke keranjang atau menambah jumlah jika sudah ada"""
        for item in self.cart:
            if item['Nama'] == product_name:
                item['Jumlah'] += 1
                return item

        for product in self.inventory:
            if product['Nama'] == product_name and product['Stok'] > 0:
                self.cart.append({
                    'Nama': product_name,
                    'Harga': price,
                    'Jumlah': 1
                })
                product['Stok'] -= 1
                return self.cart[-1]
        return None


    def remove_from_cart(self, product_name):
        """Menghapus produk dari keranjang"""
        for item in self.cart:
            if item['Nama'] == product_name:
                self.cart.remove(item)
                for product in self.inventory:
                    if product['Nama'] == product_name:
                        product['Stok'] += item['Jumlah']
                break

    def calculate_total(self):
        """Menghitung total harga keranjang"""
        return sum(item['Harga'] * item['Jumlah'] for item in self.cart)

    def record_transaction(self, total_price, paid_amount, change, payment_method):
        """Mencatat transaksi ke dalam file CSV"""
        transaction_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.transactions_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                ', '.join([item['Nama'] for item in self.cart]),
                total_price, paid_amount, change, payment_method, transaction_date
            ])

    def clear_cart(self):
        """Menghapus semua barang dari keranjang"""
        self.cart = []


    def update_product_stock(self, name, new_stock):
        """Mengupdate stok produk"""
        for product in self.inventory:
            if product['Nama'] == name:
                product['Stok'] = new_stock
                self.save_inventory()  # Simpan ke file setelah update stok
                return True
        return False
    def add_product(self, name, price, stock):
        """Menambah produk baru ke dalam inventory"""
        new_product = {'Nama': name, 'Harga': price, 'Stok': stock}
        self.inventory.append(new_product)
        self.save_inventory()  # Simpan ke file setelah menambah produk
    def update_product_price(self, name, new_price):
        """Mengupdate harga produk"""
        for product in self.inventory:
            if product['Nama'] == name:
                product['Harga'] = new_price
                self.save_inventory()  # Simpan ke file setelah update harga
                return  True
        return False

