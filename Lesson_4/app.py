import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        layout = QGridLayout()

        layout.addWidget(Color("red"), 0, 3, 4, 1)
        layout.addWidget(Color("green"), 0, 0, 2, 2)    # this widget overlaps UNDER
        layout.addWidget(Color("orange"), 1, 1, 2, 2)   # this one (more recent additions have higher z-index)
        layout.addWidget(Color("blue"), 3, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()