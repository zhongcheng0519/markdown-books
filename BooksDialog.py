# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BooksDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(781, 571)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidgetEnvironments = QTableWidget(Dialog)
        if (self.tableWidgetEnvironments.columnCount() < 2):
            self.tableWidgetEnvironments.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetEnvironments.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetEnvironments.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidgetEnvironments.setObjectName(u"tableWidgetEnvironments")

        self.verticalLayout.addWidget(self.tableWidgetEnvironments)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonAddEnv = QPushButton(Dialog)
        self.pushButtonAddEnv.setObjectName(u"pushButtonAddEnv")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAddEnv.sizePolicy().hasHeightForWidth())
        self.pushButtonAddEnv.setSizePolicy(sizePolicy)
        self.pushButtonAddEnv.setMinimumSize(QSize(32, 0))
        self.pushButtonAddEnv.setMaximumSize(QSize(32, 16777215))

        self.horizontalLayout.addWidget(self.pushButtonAddEnv)

        self.pushButtonDelEnv = QPushButton(Dialog)
        self.pushButtonDelEnv.setObjectName(u"pushButtonDelEnv")
        sizePolicy.setHeightForWidth(self.pushButtonDelEnv.sizePolicy().hasHeightForWidth())
        self.pushButtonDelEnv.setSizePolicy(sizePolicy)
        self.pushButtonDelEnv.setMinimumSize(QSize(32, 0))
        self.pushButtonDelEnv.setMaximumSize(QSize(32, 16777215))

        self.horizontalLayout.addWidget(self.pushButtonDelEnv)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableWidgetBooks = QTableWidget(Dialog)
        if (self.tableWidgetBooks.columnCount() < 2):
            self.tableWidgetBooks.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidgetBooks.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidgetBooks.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.tableWidgetBooks.setObjectName(u"tableWidgetBooks")

        self.verticalLayout.addWidget(self.tableWidgetBooks)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonAddBook = QPushButton(Dialog)
        self.pushButtonAddBook.setObjectName(u"pushButtonAddBook")
        sizePolicy.setHeightForWidth(self.pushButtonAddBook.sizePolicy().hasHeightForWidth())
        self.pushButtonAddBook.setSizePolicy(sizePolicy)
        self.pushButtonAddBook.setMinimumSize(QSize(32, 0))
        self.pushButtonAddBook.setMaximumSize(QSize(32, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButtonAddBook)

        self.pushButtonDelBook = QPushButton(Dialog)
        self.pushButtonDelBook.setObjectName(u"pushButtonDelBook")
        sizePolicy.setHeightForWidth(self.pushButtonDelBook.sizePolicy().hasHeightForWidth())
        self.pushButtonDelBook.setSizePolicy(sizePolicy)
        self.pushButtonDelBook.setMinimumSize(QSize(32, 0))
        self.pushButtonDelBook.setMaximumSize(QSize(32, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButtonDelBook)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Books", None))
        ___qtablewidgetitem = self.tableWidgetEnvironments.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Environment", None));
        ___qtablewidgetitem1 = self.tableWidgetEnvironments.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Value", None));
        self.pushButtonAddEnv.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.pushButtonDelEnv.setText(QCoreApplication.translate("Dialog", u"-", None))
        ___qtablewidgetitem2 = self.tableWidgetBooks.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Book Title", None));
        ___qtablewidgetitem3 = self.tableWidgetBooks.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Path", None));
        self.pushButtonAddBook.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.pushButtonDelBook.setText(QCoreApplication.translate("Dialog", u"-", None))
    # retranslateUi

