import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from urllib.request import urlopen


class imgLable(QLabel):
    def __init__(self):
        super(imgLable, self).__init__()
        self.setFrameStyle(QFrame.Box)
        # bigEditor.setMaximumSize(300,300)
        self.setMinimumSize(160, 160)
        self.setMargin(5)
        # self.setPixmap(pixmap)
        self.setAlignment(Qt.AlignCenter)
        self.setScaledContents(True)


class myWidget(QDialog):
    def __init__(self):
        super(myWidget, self).__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('pic clould')
        self.createMenu()
        self.createUploadLayout()
        self.createImgLayout()
        self.resize(400,600)


        layout = QVBoxLayout()
        layout.setMenuBar(self.menuBar)
        # layout.setColumnStretch(1, 20)
        # layout.setColumnMinimumWidth(1, 250)
        layout.addWidget(self.uploadGroup)
        layout.addWidget(self.gridGroupBox)

        self.setLayout(layout)

    def createUploadLayout(self):
        self.uploadGroup = QWidget()
        layout = QHBoxLayout()
        self.openFileNameEdit = QLineEdit()
        self.openFileNameEdit.setMinimumWidth(400)
        self.openFileNameButton = QPushButton("Upload")
        self.openFileNameButton.clicked.connect(self.showFileDialog)

        layout.addWidget(self.openFileNameButton)
        layout.addWidget(self.openFileNameEdit)
        self.uploadGroup.setMaximumHeight(80)
        self.uploadGroup.setLayout(layout)

    def createImgLayout(self):
        self.gridGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.setSpacing(20)
        # url = "https://git-scm.com/images/logo@2x.png"
        # imgData = urlopen(url).read()
        pixmap = QPixmap()
        # pixmap.loadFromData(imgData)
        pixmap.load('open.png')
        # bigEditor.setPixmap(pixmap)
        for i in range(3):
            for j in range(3):
                bigEditor = imgLable()
                bigEditor.setPixmap(pixmap)
                layout.addWidget(bigEditor,j,i)
        self.gridGroupBox.setLayout(layout)

    def showFileDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname:
            print(fname[0])
            self.openFileNameEdit.setText(fname[0])

    def createMenu(self):
        self.menuBar = QMenuBar()

        self.fileMenu = QMenu("&File", self)
        self.exitAction = self.fileMenu.addAction("E&xit")

        self.configMenu = QMenu("&Config",self)

        self.menuBar.addMenu(self.fileMenu)
        self.menuBar.addMenu(self.configMenu)

        self.exitAction.triggered.connect(self.close)

    # def closeEvent(self, QCloseEvent):
    #     reply = QMessageBox.question(
    #         self,
    #         'info',
    #         'Are you sure exit?',
    #         QMessageBox.Yes,
    #         QMessageBox.No
    #     )
    #     if reply == QMessageBox.Yes:
    #         QCloseEvent.accept()
    #     else:
    #         QCloseEvent.ignore()




if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    mywidget = myWidget()
    sys.exit(mywidget.exec_())


