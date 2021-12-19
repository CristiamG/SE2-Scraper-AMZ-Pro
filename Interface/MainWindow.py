from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(829, 481)
        icon = QIcon()
        icon.addFile(u"./Icons/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ProgressBar = QProgressBar(MainWindow)
        self.ProgressBar.setObjectName(u"ProgressBar")
        self.ProgressBar.setValue(24)

        self.gridLayout.addWidget(self.ProgressBar, 2, 0, 1, 4)

        self.SearchSelectorComboBox = QComboBox(MainWindow)
        self.SearchSelectorComboBox.setObjectName(u"SearchSelectorComboBox")

        self.gridLayout.addWidget(self.SearchSelectorComboBox, 0, 0, 1, 1)

        self.ScrapearPushButton = QPushButton(MainWindow)
        self.ScrapearPushButton.setObjectName(u"ScrapearPushButton")

        self.gridLayout.addWidget(self.ScrapearPushButton, 0, 5, 1, 1)

        self.ExcelExportPushButton = QPushButton(MainWindow)
        self.ExcelExportPushButton.setObjectName(u"ExcelExportPushButton")

        self.gridLayout.addWidget(self.ExcelExportPushButton, 2, 4, 1, 2)

        self.InputTextLineEdit = QLineEdit(MainWindow)
        self.InputTextLineEdit.setObjectName(u"InputTextLineEdit")

        self.gridLayout.addWidget(self.InputTextLineEdit, 0, 1, 1, 2)

        self.AttachFilePushButton = QPushButton(MainWindow)
        self.AttachFilePushButton.setObjectName(u"AttachFilePushButton")

        self.gridLayout.addWidget(self.AttachFilePushButton, 0, 3, 1, 2)

        self.tableView = QTableWidget(MainWindow)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 6)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SE2 Code AMZ Scraper", None))
        self.ScrapearPushButton.setText(QCoreApplication.translate("MainWindow", u"SCRAPEAR", None))
        self.ExcelExportPushButton.setText(QCoreApplication.translate("MainWindow", u"EXPORTAR DATOS", None))
        self.AttachFilePushButton.setText(QCoreApplication.translate("MainWindow", u"ADJUNTAR", None))