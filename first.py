# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os 
from os import name
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTextEdit,QAction, QFileDialog, QApplication, QPushButton, QWidget, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QColor, QRegExpValidator, QSyntaxHighlighter, QTextCharFormat
from minifying import *
from indentation import*
from error import *
from json_conv import *

class SyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent):
        super(SyntaxHighlighter, self).__init__(parent)
        self._highlight_lines = dict()

    def highlight_line(self, line, fmt):
        if isinstance(line, int) and line >= 0 and isinstance(fmt, QTextCharFormat):
            self._highlight_lines[line] = fmt
            tb = self.document().findBlockByLineNumber(line)
            self.rehighlightBlock(tb)

    def clear_highlight(self):
        self._highlight_lines = dict()
        self.rehighlight()

    def highlightBlock(self, text):
        line = self.currentBlock().blockNumber()
        fmt = self._highlight_lines.get(line)
        if fmt is not None:
            self.setFormat(0, len(text), fmt)

class Ui_MainWindow(object):
    def __init__(self):
        file_left = []
        file_right = []
        self.file = []
        self.text = []
        self.data2 =""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1113, 711)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1111, 151))
        font = QtGui.QFont()
        font.setFamily("Niagara Solid")
        font.setPointSize(20)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.push_browse = QtWidgets.QPushButton(self.frame)
        self.push_browse.setGeometry(QtCore.QRect(20, 20, 241, 51))
        self.push_browse.setObjectName("push_browse")
        self.push_save = QtWidgets.QPushButton(self.frame)
        self.push_save.setGeometry(QtCore.QRect(690, 90, 371, 51))
        self.push_save.setObjectName("push_save")
        self.push_compression = QtWidgets.QPushButton(self.frame)
        self.push_compression.setGeometry(QtCore.QRect(330, 90, 331, 51))
        self.push_compression.setObjectName("push_compression")
        self.push_json = QtWidgets.QPushButton(self.frame)
        self.push_json.setGeometry(QtCore.QRect(690, 20, 371, 51))
        self.push_json.setObjectName("push_json")
        self.push_minifying = QtWidgets.QPushButton(self.frame)
        self.push_minifying.setGeometry(QtCore.QRect(20, 90, 241, 51))
        self.push_minifying.setObjectName("push_minifying")
        self.push_adjust = QtWidgets.QPushButton(self.frame)
        self.push_adjust.setGeometry(QtCore.QRect(330, 20, 91, 51))
        self.push_adjust.setObjectName("push_adjust")
        self.push_indentation = QtWidgets.QPushButton(self.frame)
        self.push_indentation.setGeometry(QtCore.QRect(450, 20, 211, 51))
        self.push_indentation.setObjectName("push_indentation")
        self.textEdit_right = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_right.setGeometry(QtCore.QRect(560, 240, 541, 401))
        self.textEdit_right.setObjectName("textEdit_right")
        self.textEdit_left = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_left.setGeometry(QtCore.QRect(10, 240, 521, 401))
        self.textEdit_left.setObjectName("textEdit_left")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(770, 170, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Niagara Solid")
        font.setPointSize(29)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 170, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Niagara Solid")
        font.setPointSize(29)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(160, 160, 771, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1113, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    

        self._highlighter = SyntaxHighlighter(self.textEdit_left.document())
        self._highlighter_right = SyntaxHighlighter(self.textEdit_right.document())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.push_browse.setText(_translate("MainWindow", "Browse File"))
        self.push_save.setText(_translate("MainWindow", "Save Output"))
        self.push_compression.setText(_translate("MainWindow", "Compression"))
        self.push_json.setText(_translate("MainWindow", "XML TO JSON"))
        self.push_minifying.setText(_translate("MainWindow", "Minifying"))
        self.push_adjust.setText(_translate("MainWindow", "Fix Errors"))
        self.push_indentation.setText(_translate("MainWindow", "Fix Indentation"))
        self.label_2.setText(_translate("MainWindow", "Output"))
        self.label_3.setText(_translate("MainWindow", "Input"))

        self.push_browse.clicked.connect(self.click_browse)
        self.push_adjust.clicked.connect(self.click_check)
        self.push_compression.clicked.connect(self.click_compression)
        self.push_json.clicked.connect(self.click_json)
        self.push_minifying.clicked.connect(self.click_minifying)
        self.push_save.clicked.connect(self.click_save)
        self.push_indentation.clicked.connect(self.click_indentation)



    def click_browse(self):
        print("I am at Browse")
        ### Clear
        self.file_left = []
        self.file_right = []
        self.file = []
        self.textEdit_left.clear()
        self.textEdit_right.clear()
        ####
        

        fmt = QTextCharFormat()
        fmt.setBackground(QColor("white"))
      
        fname = QFileDialog.getOpenFileName()
        if fname[0]:
            f = open(fname[0], 'r')
            self.file = f
            with f:
                data = f.read()
                self.data2 = data
               # print(self.data2)
                self.textEdit_left.setText(data)

            f = open(self.file.name)
            for j,line in enumerate(f):
                self.text.append(deepcopy(line))


            list = errorDetect(self.text)
            print(list)
            self.errors = list
            self._highlighter.clear_highlight()
            fmt = QTextCharFormat()
            fmt.setBackground(QColor("yellow"))
            for i in range(len (list)):
                self._highlighter.highlight_line(list[i][0]-1, fmt)
            
    
    def click_indentation(self):
        print("I am at Indentation") 
        self._highlighter_right.clear_highlight()
        self.textEdit_right.clear()
        f = open(self.file.name)
        list1 , list2 ,list3 = indentation(f)
        print(list1)
        self.textEdit_right.setText(list1)
        

        
        


    def click_check(self):
        print("I am at Check")

        list =errorDetect(self.text)
        output = erorr_fix(self.text,list)
        self.textEdit_right.setText(output)
        self._highlighter_right.clear_highlight()
        fmt = QTextCharFormat()
        fmt.setBackground(QColor("yellow"))
        for i in range(len (list)):
            self._highlighter_right.highlight_line(list[i][0]-1, fmt)
        print(output)



        

        


    def click_minifying(self):
        print("I am at Minifying") 
        self._highlighter_right.clear_highlight()
        self.textEdit_right.clear()
        f = open(self.file.name)
        file1 ,list = minifying(f)
        self.textEdit_right.setText(file1)
        


    def click_save(self):
        print("I am at Save") 
        self.Save_Right()
        

    def click_compression(self):
        print("I am at Compp")
        f = open("test.xml","w")
        f.write(self.data2)
        f.close()
        os.startfile(r"C:\Users\Hp\Documents\DS\comp.exe")


    def click_json(self):
        print("I am at JSON")
        self.textEdit_right.clear()
        # print(self.file.name)
        # f = open(self.file.name)
        # data = []
        # with f:
        #     data = f.read()
        #     print(data)
        # listt = json_conv(data)
        # print(listt)
        fname = QFileDialog.getOpenFileName()
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                listt = json_conv(f)
                print(listt)
                self.textEdit_right.setText(listt   )


    def Save_Right(self):
        # S_File will get the directory path and extension.
        S__File = QtWidgets.QFileDialog.getSaveFileName(None,'SaveTextFile','/', "Text Files (*.txt)")

        # This will let you access the test in your QTextEdit
        Text = self.textEdit_right.toPlainText()

        # This will prevent you from an error if pressed cancel on file dialog.
        if S__File[0]: 
            # Finally this will Save your file to the path selected.
            with open(S__File[0], 'w') as file:
                file.write(Text) 
    
    
    
      



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())