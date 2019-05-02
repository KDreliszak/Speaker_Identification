import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QDesktopWidget
from PyQt5.QtGui import QFont


class Tutorial(QWidget):

    def __init__(self):
        super().__init__()
        self.width = 600
        self.height = 500

        self.title = 'Instrukcja'
        self.text = 'Miejsce na instrukcję'

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)

        self.resize(self.width, self.height)

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.font = QFont("Times", 10, QFont.Bold)

        self.textEdit = QTextEdit()
        self.textEdit.setFont(self.font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setText(self.text)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.textEdit)
        self.setLayout(self.layout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Tutorial()
    sys.exit(app.exec_())
