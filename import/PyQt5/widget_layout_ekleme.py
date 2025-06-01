from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QLabel, QHBoxLayout, QSplitter, QTextEdit,
    QListWidgetItem, QFileDialog, QComboBox, QMessageBox
)
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QTimer
from PyQt5.QtGui import QFont, QColor, QIcon, QPixmap


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Başlık Yazısı")
        self.setWindowIcon(QIcon("icon.ico"))
        self.UI()
    def UI(self):
        layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.label_yazisi = QLabel("Yazı")
        self.button = QPushButton("Buton")
        self.edit = QLineEdit()
        self.edit.setPlaceholderText("Arka yazı")