# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kayit.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_kayitPage(object):
    def setupUi(self, kayitPage):
        kayitPage.setObjectName("kayitPage")
        kayitPage.resize(400, 300)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        kayitPage.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Window/image/icon-window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        kayitPage.setWindowIcon(icon)
        self.label_2 = QtWidgets.QLabel(kayitPage)
        self.label_2.setGeometry(QtCore.QRect(130, 60, 110, 37))
        self.label_2.setMinimumSize(QtCore.QSize(110, 0))
        self.label_2.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTabletTracking(False)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setIndent(-1)
        self.label_2.setObjectName("label_2")
        self.btnKayit = QtWidgets.QPushButton(kayitPage)
        self.btnKayit.setGeometry(QtCore.QRect(211, 220, 81, 23))
        self.btnKayit.setObjectName("btnKayit")
        self.layoutWidget = QtWidgets.QWidget(kayitPage)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 100, 219, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.userName = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.userName.setFont(font)
        self.userName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.userName.setObjectName("userName")
        self.verticalLayout.addWidget(self.userName)
        self.sifre = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.sifre.setFont(font)
        self.sifre.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sifre.setObjectName("sifre")
        self.verticalLayout.addWidget(self.sifre)
        self.sifreAgain = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.sifreAgain.setFont(font)
        self.sifreAgain.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sifreAgain.setObjectName("sifreAgain")
        self.verticalLayout.addWidget(self.sifreAgain)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.leUser = QtWidgets.QLineEdit(self.layoutWidget)
        self.leUser.setObjectName("leUser")
        self.verticalLayout_2.addWidget(self.leUser)
        self.lePass = QtWidgets.QLineEdit(self.layoutWidget)
        self.lePass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lePass.setObjectName("lePass")
        self.verticalLayout_2.addWidget(self.lePass)
        self.lePassAgain = QtWidgets.QLineEdit(self.layoutWidget)
        self.lePassAgain.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lePassAgain.setObjectName("lePassAgain")
        self.verticalLayout_2.addWidget(self.lePassAgain)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(kayitPage)
        QtCore.QMetaObject.connectSlotsByName(kayitPage)

    def retranslateUi(self, kayitPage):
        _translate = QtCore.QCoreApplication.translate
        kayitPage.setWindowTitle(_translate("kayitPage", "Kayıt Sayfası"))
        self.label_2.setText(_translate("kayitPage", " KAYIT SAYFASI "))
        self.btnKayit.setText(_translate("kayitPage", "Kayıt Ol"))
        self.userName.setText(_translate("kayitPage", "Kullanıcı Adı"))
        self.sifre.setText(_translate("kayitPage", "Şifre"))
        self.sifreAgain.setText(_translate("kayitPage", "Şifre Yeniden"))
import icons_rc