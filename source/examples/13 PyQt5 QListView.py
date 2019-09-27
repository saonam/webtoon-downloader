from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

app = QApplication([])
model = QListWidget()
model.addItem(QListWidgetItem("Lolz"))
model.addItem(QListWidgetItem("Lolz"))
model.addItem(QListWidgetItem("Lolz"))
model.addItem("lool")
model.show()
app.exec_()
