from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class postMessage(QWidget):

    def __init__(self):
        super().__init__()
        self.stop = False  # your 'stop' variable
        self.initUI()

    def initUI(self):
        self.resize(1366, 804)
        self.baseImage = QLabel(self)
        self.baseImage.setGeometry(QRect(0, 0, 1366, 804))
        self.baseImage.setPixmap(QPixmap("baseIMG.png"))

        self.buttonPlaceholder = QLabel(self)
        self.buttonPlaceholder.setGeometry(QRect(1100, 710, 171, 61))
        self.buttonPlaceholder.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonPlaceholder.installEventFilter(self)
        self.animationLabel = QLabel(self)
        self.animationLabel.setGeometry(QRect(0, 0, 1366, 804))
        self.movie = QMovie('main.gif')
        self.animationLabel.setMovie(self.movie)


        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(QRect(50, 309, 1211, 351))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush = QBrush(QColor(130, 130, 130))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush = QBrush(QColor(105, 105, 105))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush = QBrush(QColor(130, 130, 130))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(105, 105, 105))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        brush = QBrush(QColor(130, 130, 130))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        brush = QBrush(QColor(105, 105, 105))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        self.textEdit.setPalette(palette)

        font = QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(25)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setLineWrapMode(QTextEdit.WidgetWidth)
        self.textEdit.installEventFilter(self)
        self.buttonPlaceholder.raise_()
        self.textEdit.setText('Start typing...')
        self.textEdit.clearFocus()
        self.textEdit.setDisabled(True)

        self.baseImage.setFocus()
        self.setWindowTitle('New Post - Anecdotal Application')
        self.show()
    def startError(self):
        self.animationLabel.show()
        self.movie.start()
        QTimer.singleShot(1500, self.stopError)
    def stopError(self):
        self.movie.stop()
        self.animationLabel.hide()

    def eventFilter(self, object, event):
        if event.type() == QEvent.MouseButtonPress:
            if object == self.buttonPlaceholder:
                if self.textEdit.toPlainText() in ["Start typing...",""] or self.textEdit.toPlainText().isspace():
                    if self.textEdit.toPlainText() != "Start typing...":
                        self.textEdit.clear()
                    self.startError()
                    self.baseImage.setPixmap(QPixmap('baseIMGERROR.png'))
                else:
                    self.baseImage.setPixmap(QPixmap('baseIMG.png'))
                    print(self.textEdit.toPlainText())
            elif object == self.textEdit:
                if self.textEdit.isEnabled() == False:
                    self.textEdit.setDisabled(False)
                    self.textEdit.clear()
                    self.textEdit.setFocus()
            return True
        else:
            return False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    runApp = postMessage()
    sys.exit(app.exec_())
