from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QApplication
from Controls.MainWindow import controls

if __name__=='__main__':
    app=QApplication()
    window=controls()
    window.show()

    app.exec_()

