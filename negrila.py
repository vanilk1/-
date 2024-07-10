from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
lbl = QLabel("текст :D")
btn = QPushButton("Поидее кнопка")
main_loyaut = QVBoxLayout()
main_loyaut.addWidget(lbl)
main_loyaut.addWidget(btn)

window.setLayout(main_loyaut)
window.show()
app.exec()