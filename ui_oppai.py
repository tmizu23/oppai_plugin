# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_oppai.ui'
#
# Created: Fri Dec 20 13:53:51 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Oppai(object):
    def setupUi(self, Oppai):
        Oppai.setObjectName(_fromUtf8("Oppai"))
        Oppai.resize(390, 241)
        Oppai.setMaximumSize(QtCore.QSize(16777215, 241))
        Oppai.setAutoFillBackground(False)
        Oppai.setStyleSheet(_fromUtf8("background-color:rgb(245, 114, 255)"))
        self.buttonBox = QtGui.QDialogButtonBox(Oppai)
        self.buttonBox.setGeometry(QtCore.QRect(190, 200, 151, 32))
        self.buttonBox.setStyleSheet(_fromUtf8("background-color:rgb(255, 22, 183)"))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Open)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Oppai)
        self.label.setGeometry(QtCore.QRect(40, 10, 91, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.detailBox = QtGui.QCheckBox(Oppai)
        self.detailBox.setGeometry(QtCore.QRect(20, 200, 141, 31))
        self.detailBox.setObjectName(_fromUtf8("detailBox"))
        self.layoutWidget = QtGui.QWidget(Oppai)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 50, 91, 128))
        self.layoutWidget.setMaximumSize(QtCore.QSize(16777215, 128))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(22)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.aachanButton = QtGui.QRadioButton(self.layoutWidget)
        self.aachanButton.setMaximumSize(QtCore.QSize(16777215, 20))
        self.aachanButton.setChecked(True)
        self.aachanButton.setObjectName(_fromUtf8("aachanButton"))
        self.buttonGroup = QtGui.QButtonGroup(Oppai)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.aachanButton)
        self.verticalLayout.addWidget(self.aachanButton)
        self.nocchiButton = QtGui.QRadioButton(self.layoutWidget)
        self.nocchiButton.setMaximumSize(QtCore.QSize(16777215, 20))
        self.nocchiButton.setObjectName(_fromUtf8("nocchiButton"))
        self.buttonGroup.addButton(self.nocchiButton)
        self.verticalLayout.addWidget(self.nocchiButton)
        self.kashiyukaButton = QtGui.QRadioButton(self.layoutWidget)
        self.kashiyukaButton.setMaximumSize(QtCore.QSize(16777215, 20))
        self.kashiyukaButton.setObjectName(_fromUtf8("kashiyukaButton"))
        self.buttonGroup.addButton(self.kashiyukaButton)
        self.verticalLayout.addWidget(self.kashiyukaButton)
        self.tsubomiButton = QtGui.QRadioButton(self.layoutWidget)
        self.tsubomiButton.setMinimumSize(QtCore.QSize(0, 20))
        self.tsubomiButton.setMaximumSize(QtCore.QSize(16777215, 20))
        self.tsubomiButton.setObjectName(_fromUtf8("tsubomiButton"))
        self.buttonGroup.addButton(self.tsubomiButton)
        self.verticalLayout.addWidget(self.tsubomiButton)
        self.textBrowser = QtGui.QTextBrowser(Oppai)
        self.textBrowser.setGeometry(QtCore.QRect(160, 30, 201, 151))
        self.textBrowser.setStyleSheet(_fromUtf8("background-color:rgb(255, 210, 237)"))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(Oppai)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Oppai.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Oppai.reject)
        QtCore.QMetaObject.connectSlotsByName(Oppai)

    def retranslateUi(self, Oppai):
        Oppai.setWindowTitle(_translate("Oppai", "Oppai Plugin", None))
        self.label.setText(_translate("Oppai", "誰にしますか？", None))
        self.detailBox.setText(_translate("Oppai", "かわいい方がいい！", None))
        self.aachanButton.setText(_translate("Oppai", "あ～ちゃん", None))
        self.nocchiButton.setText(_translate("Oppai", "のっち", None))
        self.kashiyukaButton.setText(_translate("Oppai", "かしゆか", None))
        self.tsubomiButton.setText(_translate("Oppai", "つぼみ", None))

