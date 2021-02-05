# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import numbers
import math

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from PyQt5.QtGui import QKeyEvent

#infix is used to store the infix expression
infix = []
#exp is to store entire expression to display the screen
exp = []
#postfix is to store postfix expression
postfix = []
#value is to store the numbers between operators
value = []
#stack is used to hold operators and operands during postfix conversion and evaluation respectively
stack = []


class expressionEvalution:

    def check_float(self, potential_float):
        try:
            float(potential_float)
            return True
        except:
            return False

    def preference(self, op):
        if op in ["(", ")"]:
            return 3
        elif op in ["*", "/"]:
            return 2
        else:
            return 1

    def checkOperator(self, op):
        if op == ")":
            preop = stack.pop()
            while preop != "(":
                postfix.append(preop)
                preop = stack.pop()
        else:
            pre1 = self.preference(op)
            val = stack.pop()
            pre2 = self.preference(val)
            while pre2 >= pre1:
                if val == "(":
                    stack.append(val)
                    break;
                else:
                    postfix.append(val)
                    val = stack.pop()
                    pre2 = self.preference(val)
            stack.append(val)

    def postfixEvalution(self, post):
        for i in post:
            if self.check_float(i):
                stack.append(i)
            else:
                val1 = float(stack.pop())
                val2 = float(stack.pop())
                # stack.append((eval(compile(val2 + i + val1,'<strinh>','eval'))))
                if i == "+":
                    stack.append(val2+val1)
                elif i == "-":
                    stack.append(val2-val1)
                elif i == "*":
                    stack.append(val2*val1)
                elif i == "/":
                    stack.append(val2/val1)
        return stack.pop()

    def infixToPostfix(self):
        infix.append(")")
        stack.append("(")
        for i in infix:
            if i == "(":
                stack.append(i)
            elif i == ")":
                self.checkOperator(i)
            elif i in ["+", "-", "*", "/"]:
                self.checkOperator(i)
                stack.append(i)
            else:
                postfix.append(i)
        stack.clear()
        self.result = self.postfixEvalution(postfix)
        infix.clear()
        postfix.clear()
        stack.clear()
        return self.result


class Ui_MainWindow(object):

    def __init__(self, a, b, c):
        self.sign = a

    def clicked(self,val):
        print(val)
        exp.append(val)
        self.line.setText(''.join(exp))
        value.append(val)

    def op_clicked(self,op):
        exp.append(op)
        infix.append(float(''.join(value)))
        infix.append(op)
        value.clear()
        self.line.setText(''.join(exp))

    def clearScreen(self):
        value.clear()
        exp.clear()
        infix.clear()
        self.line.setText(''.join(exp))

    def backClicked(self):
        if exp.pop().isdigit():
            self.line.setText(''.join(exp))
            value.pop()
        else:
            value.clear()
            infix.pop()
            value.append(infix.pop())
            self.line.setText(''.join(exp))


    def resultvalue(self):
        infix.append(float(''.join(value)))
        value.clear()
        exp.clear()
        result = expressionEvalution().infixToPostfix()
        if float(result).is_integer():
            result=int(result)
        self.line.setText(str(result))
        exp.append(str(result))
        value.append(str(result))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 380)
        MainWindow.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.line = QtWidgets.QLineEdit(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 20, 390, 61))
        self.line.setStyleSheet("color: rgb(255, 255, 255);\n""font: 75 16pt \"Tlwg Typist\";")
        self.line.setReadOnly(True)
        self.line.setObjectName("line")

        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(10, 110, 71, 51))
        self.seven.setStyleSheet("color: rgb(250, 250, 250);outline:none;")
        self.seven.setObjectName("seven")

        self.seven.clicked.connect(lambda :self.clicked("7"))

        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(90, 110, 71, 51))
        self.eight.setStyleSheet("color: rgb(250, 250, 250);outline:none;")
        self.eight.setObjectName("eight")

        self.eight.clicked.connect(lambda :self.clicked("8"))

        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(170, 110, 71, 51))
        self.nine.setStyleSheet("color: rgb(250, 250, 250);outline:none;")
        self.nine.setObjectName("nine")

        self.nine.clicked.connect(lambda :self.clicked("9"))

        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(10, 170, 71, 51))
        self.four.setStyleSheet("color: rgb(250, 250, 250);outline:none;")
        self.four.setObjectName("four")

        self.four.clicked.connect(lambda :self.clicked("4"))

        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(90, 170, 71, 51))
        self.five.setStyleSheet("color: rgb(250, 250, 250);outline:none;")
        self.five.setObjectName("five")

        self.five.clicked.connect(lambda :self.clicked("5"))

        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(170, 170, 71, 51))
        self.six.setStyleSheet("color: rgb(250, 250, 250);outline:none;")
        self.six.setObjectName("six")

        self.six.clicked.connect(lambda :self.clicked("6"))

        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(10, 230, 71, 51))
        self.one.setStyleSheet("color: rgb(250, 250, 250);outline:none;")
        self.one.setObjectName("one")

        self.one.clicked.connect(lambda :self.clicked("1"))

        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(90, 230, 71, 51))
        self.two.setStyleSheet("color: rgb(250, 250, 250);outline:none;")
        self.two.setObjectName("two")

        self.two.clicked.connect(lambda :self.clicked("2"))

        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(170, 230, 71, 51))
        self.three.setStyleSheet("color: rgb(250, 250, 250);outline:none;")
        self.three.setObjectName("three")

        self.three.clicked.connect(lambda :self.clicked("3"))

        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(10, 290, 151, 51))
        self.zero.setStyleSheet("color: rgb(250, 250, 250);outline:none;")
        self.zero.setObjectName("zero")

        self.zero.clicked.connect(lambda :self.clicked("0"))

        self.dot = QtWidgets.QPushButton(self.centralwidget)
        self.dot.setGeometry(QtCore.QRect(170, 290, 71, 51))
        self.dot.setStyleSheet("color: rgb(250, 250, 250);outline:none;")
        self.dot.setObjectName("dot")

        self.dot.clicked.connect(lambda :self.clicked("."))

        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(250, 110, 71, 51))
        self.clear.setStyleSheet("color: rgb(250, 250, 250);outline:none;")
        self.clear.setObjectName("clear")

        self.clear.clicked.connect(self.clearScreen)

        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(330, 110, 71, 51))
        self.back.setStyleSheet("color: rgb(250, 250, 250);outline:none;")
        self.back.setObjectName("back")

        self.back.clicked.connect(self.backClicked)

        self.divide = QtWidgets.QPushButton(self.centralwidget)
        self.divide.setGeometry(QtCore.QRect(250, 170, 71, 51))
        self.divide.setGeometry(QtCore.QRect(250, 170, 71, 51))
        self.divide.setStyleSheet("color: rgb(250, 250, 250);outline:none;")
        self.divide.setObjectName("divide")

        self.divide.clicked.connect(lambda :self.op_clicked("/"))

        self.sub = QtWidgets.QPushButton(self.centralwidget)
        self.sub.setGeometry(QtCore.QRect(330, 170, 71, 51))
        self.sub.setStyleSheet("color: rgb(250, 250, 250);outline:none;")
        self.sub.setObjectName("sub")

        self.sub.clicked.connect(lambda :self.op_clicked("-"))

        self.mul = QtWidgets.QPushButton(self.centralwidget)
        self.mul.setGeometry(QtCore.QRect(250, 230, 71, 51))
        self.mul.setStyleSheet("color: rgb(250, 250, 250);outline:none;")
        self.mul.setObjectName("mul")

        self.mul.clicked.connect(lambda :self.op_clicked("*"))

        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(330, 230, 71, 51))
        self.add.setStyleSheet("color: rgb(250, 250, 250);outline:none;")
        self.add.setObjectName("add")

        self.add.clicked.connect(lambda :self.op_clicked("+"))

        self.equal = QtWidgets.QPushButton(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(250, 290, 151, 51))
        self.equal.setStyleSheet("color: rgb(250, 250, 250);outline:none;")
        self.equal.setObjectName("equal")

        self.equal.clicked.connect(self.resultvalue)

        MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 22))
        # self.menubar.setStyleSheet("background-color: rgb(70, 70, 70);")
        # self.menubar.setStyleSheet("color: rgb(250, 250, 250);")
        # self.menubar.setObjectName("menubar")
        # self.menuFILE = QtWidgets.QMenu(self.menubar)
        # self.menuFILE.setObjectName("menuFILE")
        # self.menuFILE.setStyleSheet("border-color: rgb(10, 10, 10);")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        # self.actionNEW = QtWidgets.QAction(MainWindow)
        # self.actionNEW.setObjectName("actionNEW")
        # self.actionCLOSE = QtWidgets.QAction(MainWindow)
        # self.actionCLOSE.setObjectName("actionCLOSE")
        # self.menuFILE.addAction(self.actionNEW)
        # self.menuFILE.addAction(self.actionCLOSE)
        # self.menubar.addAction(self.menuFILE.menuAction())

        self.retranslateUi(MainWindow)
        # self.actionNEW.triggered.connect(self.line.clear)
        # self.actionCLOSE.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.four.setText(_translate("MainWindow", "4"))
        self.five.setText(_translate("MainWindow", "5"))
        self.six.setText(_translate("MainWindow", "6"))
        self.one.setText(_translate("MainWindow", "1"))
        self.two.setText(_translate("MainWindow", "2"))
        self.three.setText(_translate("MainWindow", "3"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.dot.setText(_translate("MainWindow", "."))
        self.clear.setText(_translate("MainWindow", "C"))
        self.back.setText(_translate("MainWindow", "<-"))
        self.divide.setText(_translate("MainWindow", "/"))
        self.sub.setText(_translate("MainWindow", "-"))
        self.mul.setText(_translate("MainWindow", "x"))
        self.add.setText(_translate("MainWindow", "+"))
        self.equal.setText(_translate("MainWindow", "="))
        # self.menuFILE.setTitle(_translate("MainWindow", "FILE"))
        # self.actionNEW.setText(_translate("MainWindow", "NEW"))
        # self.actionCLOSE.setText(_translate("MainWindow", "CLOSE"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, sign=" ", value2=" ", result=0):
        QMainWindow.__init__(self, parent=parent, a=sign, b=value2, c=result)
        self.setupUi(self)

    def keyPressEvent(self, event):
        try :
            if chr(event.key()).isdigit():
                Ui_MainWindow.clicked(self,chr(event.key()))
        except:
            print("Not a digit")
        else:
            if chr(event.key()) in["+","-","*","/"]:
                Ui_MainWindow.op_clicked(self,chr(event.key()))
        finally:
            if event.key() == QtCore.Qt.Key_Enter:
                Ui_MainWindow.resultvalue(self)
            elif event.key() == QtCore.Qt.Key_Back:
                Ui_MainWindow.backClicked(self)
            elif event.key() == QtCore.Qt.Key_Delete:
                Ui_MainWindow.clearScreen(self)



if __name__ == "__main__":
    import sys

    sign = " "
    value2 = " "
    convertValue = " "
    result = 0
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
