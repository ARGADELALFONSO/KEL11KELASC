import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from ui import VendingMachineUI
from logic import VendingMachineLogic

class VendingMachineApp(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.logic = VendingMachineLogic()
        self.buyer_ui = VendingMachineUI(self.logic)
        self.addWidget(self.buyer_ui)

    def refresh_app(self):
        """Menghapus dan memuat ulang UI"""
        self.removeWidget(self.buyer_ui)  # Hapus widget lama
        self.buyer_ui = VendingMachineUI(self.logic)  # Buat ulang UI dengan data terbaru
        self.addWidget(self.buyer_ui)  # Tambahkan widget baru
        self.setCurrentWidget(self.buyer_ui)  # Tampilkan widget baru

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VendingMachineApp()
    window.show()
    sys.exit(app.exec_())
