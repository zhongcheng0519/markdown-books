# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MarkdownBooks.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionEnvironment_E = QAction(MainWindow)
        self.actionEnvironment_E.setObjectName(u"actionEnvironment_E")
        self.actionBooks_B = QAction(MainWindow)
        self.actionBooks_B.setObjectName(u"actionBooks_B")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBoxTool = QComboBox(self.centralwidget)
        self.comboBoxTool.addItem("")
        self.comboBoxTool.addItem("")
        self.comboBoxTool.setObjectName(u"comboBoxTool")

        self.horizontalLayout.addWidget(self.comboBoxTool)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionBooks_B)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Markdown Books", None))
        self.actionEnvironment_E.setText(QCoreApplication.translate("MainWindow", u"Environment(&E)", None))
        self.actionBooks_B.setText(QCoreApplication.translate("MainWindow", u"Books(&B)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tool:", None))
        self.comboBoxTool.setItemText(0, QCoreApplication.translate("MainWindow", u"typora", None))
        self.comboBoxTool.setItemText(1, QCoreApplication.translate("MainWindow", u"Notable", None))

        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"Config(&C)", None))
    # retranslateUi

