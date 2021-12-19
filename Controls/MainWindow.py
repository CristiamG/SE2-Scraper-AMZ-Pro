import os
import time
from PySide2.QtWidgets import QWidget, QFileDialog, QTableWidgetItem, QTableView, QTableWidget, QAbstractItemView
from Interface.MainWindow import MainWindow
from logic.ScrapFuntions import DataFile, GetUrl, KWUrls, Scraping, UrlsByASIN, DataFrameCreator

class controls (QWidget,MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.ComboBox()
        self.ScrapearPushButton.clicked.connect(self.ComboBox)        
        self.AttachFilePushButton.clicked.connect(self.AttachFileASIN)
        #self.ExcelExportPushButton.clicked.connect(self.ExportFuntion)
                  
                
    def ComboBox(self):
        self.SearchSelectorComboBox.addItems(["","Scrapear por Archivo","Escrapear por ASIN","Escrapear por palabra clave"])
        UserOption=self.SearchSelectorComboBox.currentText()
        self.ProgressBar.setValue(6)
                        
        if UserOption=='Escrapear por ASIN':
            self.ProgressBarProces(16)           
            ASIN=self.InputTextLineEdit.text()
            self.ProgressBarProces(21)
            Urls=UrlsByASIN(ASIN)
            self.ProgressBarProces(31)
            FileData=Scraping(Urls)
            self.ProgressBarProces(61)
            self.PrintDataTable(FileData)
            self.ProgressBarProces(76)
            self.ExcelExportPushButton.clicked.connect(lambda: self.ExportFuntion(FileData))
            self.ProgressBarProces(101)

        elif UserOption=="Scrapear por Archivo":
            self.ProgressBarProces(15)
            self.AttachFilePushButton.clicked.connect(self.AttachFileASIN)
            LocalFile=self.InputTextLineEdit.text()
            self.ProgressBarProces(21)
            urls=DataFile(LocalFile)
            self.ProgressBarProces(31)
            FileData=Scraping(urls)
            self.ProgressBarProces(61)
            self.PrintDataTable(FileData)
            self.ProgressBarProces(76)
            self.ExcelExportPushButton.clicked.connect(lambda: self.ExportFuntion(FileData))
            self.ProgressBarProces(101)
            

        elif UserOption=="Escrapear por palabra clave":
            self.ProgressBarProces(15)
            kw=self.InputTextLineEdit.text()
            self.ProgressBarProces(20)
            urls=KWUrls(kw)
            self.ProgressBarProces(30)
            FileData=Scraping(urls) 
            self.PrintDataTable(FileData)
            self.ProgressBarProces(76)
            self.ExcelExportPushButton.clicked.connect(lambda: self.ExportFuntion(FileData))
            self.ProgressBarProces(101)
                     
    def AttachFileASIN (self):
        FilePath=QFileDialog.getOpenFileName()[0]
        self.InputTextLineEdit.setText(FilePath) 
        self.ProgressBarProces(10)
    
    def PrintDataTable(self,FileData):
        self.tableView.setRowCount(len(FileData))
        self.tableView.setColumnCount(len(FileData[0]))
        self.tableView.setHorizontalHeaderLabels(FileData[0])
        RowNumber=0
        for row in FileData[1:]:
            RowNumber+=1
            for i in row:
                ColumnNumber=row.index(i)


                self.tableView.setItem(RowNumber,ColumnNumber,QTableWidgetItem(str(i)))

    def ProgressBarProces (self,Num=100):
        for i in range(Num):
            time.sleep(0.01)
            self.ProgressBar.setValue(i)

    #file_name='hola.xlsx'
    def ExportFuntion(self,FileData):
        ExportFile=QFileDialog.getSaveFileName()[0]
        #ExportFile=self.InputTextLineEdit.setText(ExportFile1)
        #default_fileName=os.path.join('c:/')
        """ExportFile1, _ = QFileDialog.getSaveFileName(
        self, "Save data file", 'c:/', "Excel Files (*.xlsx)")
        
        ExportFile=os.path.join(ExportFile1)
        ExportFile=self.InputTextLineEdit.setText(ExportFile)"""
        DataFrameCreator(FileData,ExportFile)