'''
    GUI AD tools
    Compilation of stuff I use a lot
    Nothing fancy, more out of laziness
'''

### Modules
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

### Own imports
from otherFunctions import openFile, openUrl, returnIniSettings
from userFunctions import txt2lst, userInfo, groupInfo
from AD_Classes import UserName, UserGroup
from MainWindow import Ui_MainWindow
from DialogNotification import Ui_DialogNotification
from DialogSuccess import Ui_DialogSuccess

### Read INI file
mainSettings=returnIniSettings()

### Gui MainWindow
class runApplication(Ui_MainWindow):
    def __init__(self):
        self._translate = QtCore.QCoreApplication.translate
        self.run()
        self.Quit()
    def run(self):
        self.app=QApplication(sys.argv)
        self.window=QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.windowmods()
        self.menuactions()
        self.buttonactions()
        self.window.show()
        self.Quit()
    def menuactions(self):
        self.ui.actionExit.triggered.connect(self.Quit)
        self.ui.actionREADME.triggered.connect(lambda: openFile(mainSettings["fileREADME"]))
        self.ui.actionLICENSE.triggered.connect(lambda: openUrl(mainSettings["urlLicense"]))
        self.ui.actionVisitUs.triggered.connect(lambda: openUrl(mainSettings["urlMain"]))
    def buttonactions(self):
        # Uncomment next line to make the test button(s) visible
        # self.buttonactions_test()
        self.ui.pushButtonOpenLastFile.clicked.connect(self.buttonactions_openLastFile)
        self.ui.pushButtonUserInfo.clicked.connect(lambda: self.buttonactions_userInfo(self.ui.plainTextEditUserNames.toPlainText()))
    def buttonactions_test(self):
        # Test button(s)
        self.ui.pushButtonTest.show()
        self.ui.pushButtonTest.clicked.connect(lambda: self.diagSuc(title='Keyboard found',text='Press F1 to continue.\nThis is just a test :)',filename="README.txt"))    
    def buttonactions_openLastFile(self):
        try:
            if hasattr(self,'lastfile'):
                openFile(self.lastfile)
            else:
                openFile(mainSettings['resulttxtFile'])
        except FileNotFoundError:
            self.diagNot(title="File Error",text="Error: unable to open file.")
    def buttonactions_userInfo(self,text):
        self.lst=txt2lst(text)
        print(self.lst)
        self.userInfo=userInfo(lst=self.lst,request="info",resulttxtFile=mainSettings["resulttxtFile"])
        print(self.userInfo)
        
    def diagNot(self,title,text,width=mainSettings['DialogNotification_w'],height=mainSettings['DialogNotification_h']):
        self.diag_title=title
        self.diag_text=text
        self.diag_width=width
        self.diag_height=height
        self.d=DiagNot(title=self.diag_title,text=self.diag_text,width=self.diag_width,height=self.diag_height)
        self.d.show()
    def diagSuc(self,title,text,width=mainSettings['DialogSuccess_w'],height=mainSettings['DialogSuccess_h'],filename=mainSettings['resulttxtFile']):
        self.diag_title=title
        self.diag_text=text
        self.diag_width=width
        self.diag_height=height
        self.diag_filename=filename
        self.d=DiagSuc(title=self.diag_title,text=self.diag_text,width=self.diag_width,height=self.diag_height,filename=self.diag_filename)
        self.d.show()
    def windowmods(self):
        self.ui.pushButtonTest.hide() # only used to test
        self.window.setWindowTitle(mainSettings['MainWindow_title'])
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(mainSettings['icon']), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.setWindowIcon(self.icon)
        self.window.resize(int(mainSettings['MainWindow_w']), int(mainSettings['MainWindow_h']))
        self.text_usernames=mainSettings['defUser1'] + "\n" + mainSettings['defUser2'] + "\n" + mainSettings['defUser3'] + "\n"
        self.text_groupnames=mainSettings['defGroup1'] + "\n" + mainSettings['defGroup2'] + "\n" + mainSettings['defGroup3'] + "\n"
        self.ui.plainTextEditUserNames.setPlainText(self._translate("MainWindow", self.text_usernames))
        self.ui.plainTextEditGroupNames.setPlainText(self._translate("MainWindow", self.text_groupnames))
    def Quit(self):
        sys.exit(self.app.exec_())
        
### Gui DialogNotification
class DiagNot(Ui_DialogNotification):
    def __init__(self,title,text,width=mainSettings['DialogNotification_w'],height=mainSettings['DialogNotification_h']):
        self.title=title
        self.text=text
        self.width=width
        self.height=height
        self.run()
    def run(self):
        self.window=QDialog()
        self.ui=Ui_DialogNotification()
        self.ui.setupUi(self.window)
        self.buttonactions()
    def show(self):
        self.window.setWindowTitle(self.title)
        self.ui.labelText.setText(self.text)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(mainSettings['icon']), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.setWindowIcon(self.icon)
        self.resetsize(self.width,self.height)
        self.window.show()
    def resetsize(self,w,h):
        self.window.resize(int(w),int(h))
    def buttonactions(self):
        self.ui.pushButtonOK.clicked.connect(self.Quit)
    def Quit(self):
        self.window.hide()

### Gui DialogSuccess
class DiagSuc(Ui_DialogSuccess):
    def __init__(self,title,text,width=mainSettings['DialogSuccess_w'],height=mainSettings['DialogSuccess_h'],filename=mainSettings['resulttxtFile']):
        self.title=title
        self.text=text
        self.width=width
        self.height=height
        self.filename=filename
        self.run()
    def run(self):
        self.window=QDialog()
        self.ui=Ui_DialogSuccess()
        self.ui.setupUi(self.window)
        self.buttonactions()
    def show(self):
        self.window.setWindowTitle(self.title)
        self.ui.labelText.setText(self.text)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(mainSettings['icon']), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.setWindowIcon(self.icon)
        self.resetsize(self.width,self.height)
        self.window.show()
    def resetsize(self,w,h):
        self.window.resize(int(w),int(h))
    def buttonactions(self):
        self.ui.pushButtonOK.clicked.connect(self.Quit)
        self.ui.pushButtonOpenFile.clicked.connect(self.openFile)
    def openFile(self):
        # Extra so we can close the window afterwards
        openFile(self.filename)
        self.Quit()
    def Quit(self):
        self.window.hide()

### Run the window
if __name__ == "__main__":
    runApplication()



