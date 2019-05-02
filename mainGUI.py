# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kajet\Desktop\magisterka\magisterka_program\mainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from tutorial import Tutorial
import os
from shutil import move
from audio import audio_sample
from GMM_UBM import comparing_models, training_model


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(929, 557)
        font = QtGui.QFont()
        font.setPointSize(9)
        mainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_5 = QtWidgets.QFrame(self.tab)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.zPlikuBox = QtWidgets.QGroupBox(self.frame_5)
        self.zPlikuBox.setObjectName("zPlikuBox")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.zPlikuBox)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.szukajPliku = QtWidgets.QPushButton(self.zPlikuBox)
        self.szukajPliku.setMinimumSize(QtCore.QSize(0, 35))
        self.szukajPliku.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.szukajPliku.setFont(font)
        self.szukajPliku.setObjectName("szukajPliku")
        self.horizontalLayout_8.addWidget(self.szukajPliku)
        self.sciezka_line = QtWidgets.QLineEdit(self.zPlikuBox)
        self.sciezka_line.setObjectName("sciezka_line")
        self.horizontalLayout_8.addWidget(self.sciezka_line)
        self.horizontalLayout_5.addWidget(self.zPlikuBox)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.tab)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 110))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.nagrajBox = QtWidgets.QGroupBox(self.frame_6)
        self.nagrajBox.setMinimumSize(QtCore.QSize(0, 80))
        self.nagrajBox.setObjectName("nagrajBox")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.nagrajBox)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.line_3 = QtWidgets.QFrame(self.nagrajBox)
        self.line_3.setMinimumSize(QtCore.QSize(150, 0))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_7.addWidget(self.line_3)
        self.nagrajMowce = QtWidgets.QPushButton(self.nagrajBox)
        self.nagrajMowce.setMinimumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nagrajMowce.setFont(font)
        self.nagrajMowce.setObjectName("nagrajMowce")
        self.horizontalLayout_7.addWidget(self.nagrajMowce)
        self.line_4 = QtWidgets.QFrame(self.nagrajBox)
        self.line_4.setMinimumSize(QtCore.QSize(150, 0))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_7.addWidget(self.line_4)
        self.progressBar_2 = QtWidgets.QProgressBar(self.nagrajBox)
        self.progressBar_2.setMinimumSize(QtCore.QSize(350, 0))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.horizontalLayout_7.addWidget(self.progressBar_2)
        self.horizontalLayout_6.addWidget(self.nagrajBox)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.tab)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.odtworzMowce = QtWidgets.QPushButton(self.frame_9)
        self.odtworzMowce.setEnabled(False)
        self.odtworzMowce.setMinimumSize(QtCore.QSize(0, 0))
        self.odtworzMowce.setMaximumSize(QtCore.QSize(150, 40))
        self.odtworzMowce.setObjectName("odtworzMowce")
        self.horizontalLayout_10.addWidget(self.odtworzMowce)
        self.horizontalLayout_9.addWidget(self.frame_9)
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.nagrany_check = QtWidgets.QCheckBox(self.frame_8)
        self.nagrany_check.setEnabled(False)
        self.nagrany_check.setMinimumSize(QtCore.QSize(150, 30))
        self.nagrany_check.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nagrany_check.setObjectName("nagrany_check")
        self.verticalLayout_6.addWidget(self.nagrany_check)
        self.plik_check = QtWidgets.QCheckBox(self.frame_8)
        self.plik_check.setEnabled(False)
        self.plik_check.setMinimumSize(QtCore.QSize(150, 30))
        self.plik_check.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.plik_check.setObjectName("plik_check")
        self.verticalLayout_6.addWidget(self.plik_check)
        self.horizontalLayout_9.addWidget(self.frame_8)
        self.verticalLayout_5.addWidget(self.frame_7)
        self.frame_10 = QtWidgets.QFrame(self.tab)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.rozpoznajMowce = QtWidgets.QPushButton(self.frame_10)
        self.rozpoznajMowce.setEnabled(False)
        self.rozpoznajMowce.setMinimumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rozpoznajMowce.setFont(font)
        self.rozpoznajMowce.setObjectName("rozpoznajMowce")
        self.horizontalLayout_11.addWidget(self.rozpoznajMowce)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.textEdit = QtWidgets.QTextEdit(self.frame_10)
        self.textEdit.setEnabled(True)
        self.textEdit.setMinimumSize(QtCore.QSize(550, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_11.addWidget(self.textEdit)
        self.verticalLayout_5.addWidget(self.frame_10)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.tab_2)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.instrukcja = QtWidgets.QPushButton(self.frame_4)
        self.instrukcja.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.instrukcja.setFont(font)
        self.instrukcja.setFlat(True)
        self.instrukcja.setObjectName("instrukcja")
        self.horizontalLayout_2.addWidget(self.instrukcja)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame = QtWidgets.QFrame(self.tab_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.imie_box = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.imie_box.setFont(font)
        self.imie_box.setFlat(False)
        self.imie_box.setObjectName("imie_box")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.imie_box)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.imie_line = QtWidgets.QLineEdit(self.imie_box)
        self.imie_line.setMinimumSize(QtCore.QSize(0, 30))
        self.imie_line.setAutoFillBackground(False)
        self.imie_line.setText("")
        self.imie_line.setObjectName("imie_line")
        self.verticalLayout_4.addWidget(self.imie_line)
        self.verticalLayout_3.addWidget(self.imie_box)
        self.nazwisko_box = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.nazwisko_box.setFont(font)
        self.nazwisko_box.setFlat(False)
        self.nazwisko_box.setCheckable(False)
        self.nazwisko_box.setObjectName("nazwisko_box")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.nazwisko_box)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nazwisko_line = QtWidgets.QLineEdit(self.nazwisko_box)
        self.nazwisko_line.setMinimumSize(QtCore.QSize(0, 30))
        self.nazwisko_line.setText("")
        self.nazwisko_line.setObjectName("nazwisko_line")
        self.verticalLayout.addWidget(self.nazwisko_line)
        self.verticalLayout_3.addWidget(self.nazwisko_box)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setMinimumSize(QtCore.QSize(150, 0))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.wlaczNagrywanie = QtWidgets.QPushButton(self.frame_2)
        self.wlaczNagrywanie.setEnabled(True)
        self.wlaczNagrywanie.setMinimumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.wlaczNagrywanie.setFont(font)
        self.wlaczNagrywanie.setObjectName("wlaczNagrywanie")
        self.horizontalLayout_3.addWidget(self.wlaczNagrywanie)
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setMinimumSize(QtCore.QSize(150, 0))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar.setMinimumSize(QtCore.QSize(350, 0))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.tab_2)
        self.frame_3.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.odtworzNagranie = QtWidgets.QPushButton(self.frame_3)
        self.odtworzNagranie.setEnabled(False)
        self.odtworzNagranie.setMinimumSize(QtCore.QSize(150, 40))
        self.odtworzNagranie.setCheckable(False)
        self.odtworzNagranie.setDefault(False)
        self.odtworzNagranie.setObjectName("odtworzNagranie")
        self.horizontalLayout_4.addWidget(self.odtworzNagranie)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.zapiszNagranie = QtWidgets.QPushButton(self.frame_3)
        self.zapiszNagranie.setEnabled(False)
        self.zapiszNagranie.setMinimumSize(QtCore.QSize(150, 40))
        self.zapiszNagranie.setObjectName("zapiszNagranie")
        self.horizontalLayout_4.addWidget(self.zapiszNagranie)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.usunNagranie = QtWidgets.QPushButton(self.frame_3)
        self.usunNagranie.setEnabled(False)
        self.usunNagranie.setMinimumSize(QtCore.QSize(150, 40))
        self.usunNagranie.setObjectName("usunNagranie")
        self.horizontalLayout_4.addWidget(self.usunNagranie)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_11 = QtWidgets.QFrame(self.tab_2)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_11)
        self.textEdit_2.setMinimumSize(QtCore.QSize(0, 50))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_12.addWidget(self.textEdit_2)
        self.line_5 = QtWidgets.QFrame(self.frame_11)
        self.line_5.setMinimumSize(QtCore.QSize(40, 0))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_12.addWidget(self.line_5)
        self.liczba_nagran = QtWidgets.QLCDNumber(self.frame_11)
        self.liczba_nagran.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.liczba_nagran.setFont(font)
        self.liczba_nagran.setFrameShape(QtWidgets.QFrame.Box)
        self.liczba_nagran.setFrameShadow(QtWidgets.QFrame.Raised)
        self.liczba_nagran.setLineWidth(3)
        self.liczba_nagran.setDigitCount(1)
        self.liczba_nagran.setProperty("intValue", 5)
        self.liczba_nagran.setObjectName("liczba_nagran")
        self.horizontalLayout_12.addWidget(self.liczba_nagran)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem8)
        self.generujModel = QtWidgets.QPushButton(self.frame_11)
        self.generujModel.setEnabled(False)
        self.generujModel.setMinimumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.generujModel.setFont(font)
        self.generujModel.setObjectName("generujModel")
        self.horizontalLayout_12.addWidget(self.generujModel)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem9)
        self.verticalLayout_2.addWidget(self.frame_11)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(mainWindow)
        self.statusBar.setObjectName("statusBar")
        mainWindow.setStatusBar(self.statusBar)
        self.actionTab1 = QtWidgets.QAction(mainWindow)
        self.actionTab1.setObjectName("actionTab1")
        self.actionTab1_2 = QtWidgets.QAction(mainWindow)
        self.actionTab1_2.setObjectName("actionTab1_2")

        self.instrukcja.clicked.connect(self.openTutorial)
        self.wlaczNagrywanie.clicked.connect(self.startRecording)
        self.odtworzNagranie.clicked.connect(self.playRecording)
        self.zapiszNagranie.clicked.connect(self.saveRecording)
        self.usunNagranie.clicked.connect(self.deleteRecording)
        self.generujModel.clicked.connect(self.generateModel)

        self.szukajPliku.clicked.connect(self.searchFile)
        self.nagrajMowce.clicked.connect(self.recordSpeaker)
        self.odtworzMowce.clicked.connect(self.playSpeaker)
        self.rozpoznajMowce.clicked.connect(self.recognizeSpeaker)
        self.plik_check.stateChanged.connect(self.recordFromFile)
        self.nagrany_check.stateChanged.connect(self.recordFromRecord)

        self.timer_tab1 = QtCore.QTimer()
        self.timer_tab1.timeout.connect(self.updateProgressBar)
        self.timer_tab2 = QtCore.QTimer()
        self.timer_tab2.timeout.connect(self.updateProgressBar)

        self.record_time = 5
        self.step = 0
        self.recording_exist = False
        self.default_filename = 'file_to_test.wav'
        self.audio_directory = r'c:\Users\kajet\Desktop\magisterka\dane\Audio\Filtrowane\Uczace''\\'
        self.test_audio_directory = r'c:\Users\kajet\Desktop\magisterka\dane\Audio\Filtrowane\Testowe''\\'
        # self.test_audio_directory = r'c:\Users\kajet\Desktop\magisterka\dane\Grupy_testowe\wspolny_mikrofon_1_rodzina\dane_testowe_zgodne''\\'
        self.models_directory = r'C:\Users\kajet\Desktop\magisterka\dane\Modele\All''\\'
        # self.models_directory = r'c:\Users\kajet\Desktop\magisterka\dane\Grupy_testowe\wspolny_mikrofon_1_rodzina\modele''\\'

        self.UBM_directory = r'C:\Users\kajet\Desktop\magisterka\dane\Modele\UBM.gmm'

        # self.imie_line.setText('ja')
        # self.nazwisko_line.setText('ty')

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Narzędzie do nagrywanie"))
        self.zPlikuBox.setTitle(_translate("mainWindow", "Załaduj z pliku"))
        self.szukajPliku.setText(_translate("mainWindow", "..."))
        self.nagrajBox.setTitle(_translate("mainWindow", "Nagraj mówcę"))
        self.nagrajMowce.setText(_translate("mainWindow", "Włącz Nagrywanie"))
        self.odtworzMowce.setText(_translate("mainWindow", "Odtwórz Nagranie"))
        self.nagrany_check.setText(_translate("mainWindow", "Właśnie nagrany"))
        self.plik_check.setText(_translate("mainWindow", "Z pliku"))
        self.rozpoznajMowce.setText(_translate("mainWindow", "Rozpoznaj Mówcę"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "Rozpoznawanie mówcy"))
        self.instrukcja.setText(_translate("mainWindow", "Instrukcja"))
        self.imie_box.setTitle(_translate("mainWindow", "Podaj Imie"))
        self.imie_line.setPlaceholderText(_translate("mainWindow", "Imie"))
        self.nazwisko_box.setTitle(_translate("mainWindow", "Podaj Nazwisko"))
        self.nazwisko_line.setPlaceholderText(_translate("mainWindow", "Nazwisko"))
        self.wlaczNagrywanie.setText(_translate("mainWindow", "Włącz Nagrywanie"))
        self.odtworzNagranie.setText(_translate("mainWindow", "Odtwórz Nagranie"))
        self.zapiszNagranie.setText(_translate("mainWindow", "Zapisz Nagranie"))
        self.usunNagranie.setText(_translate("mainWindow", "Usuń Nagranie"))
        self.textEdit_2.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Potrzeba jeszcze nagrań w liczbie:</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">aby wygenerować model.</p></body></html>"))
        self.generujModel.setText(_translate("mainWindow", "Generuj Model"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "Generowanie modelu"))
        self.actionTab1.setText(_translate("mainWindow", "Tab1"))
        self.actionTab1_2.setText(_translate("mainWindow", "Tab1"))

    def updateProgressBar(self):
        if self.step >= 100:
            if self.timer_tab1.isActive():
                self.timer_tab1.stop()
            else:
                self.timer_tab2.stop()
                self.nagrany_check.setEnabled(True)
                self.recording_exist = True
            self.statusBar.showMessage('Nagrywanie zakończone')
            self.step = 0
            return

        self.step += 1
        if self.timer_tab1.isActive():
            self.progressBar.setValue(self.step)
        else:
            self.progressBar_2.setValue(self.step)

    def record(self, filename, timer):
        self.audio = AudioThread(filename, self.record_time)
        self.audio.start()
        timer.start((10 * self.record_time) - 4)

    def startRecording(self):
        if self.imie_line.text() not in ['', 'Nie podano imienia'] and self.nazwisko_line.text() not in ['',
                                                                                                         'Nie podano nazwiska']:
            self.nazwa_folderu = '_'.join([self.imie_line.text(), self.nazwisko_line.text()])
            self.nazwa_pliku = self.nazwa_folderu + '.wav'

            self.wlaczNagrywanie.setEnabled(False)
            self.imie_line.setReadOnly(True)
            self.nazwisko_line.setReadOnly(True)

            self.statusBar.showMessage('Nagrywanie w toku ...')
            self.record(self.nazwa_pliku, self.timer_tab1)

            self.odtworzNagranie.setEnabled(True)
            self.zapiszNagranie.setEnabled(True)
            self.usunNagranie.setEnabled(True)

        else:
            self.statusBar.showMessage('Nie podano danych')
            if self.imie_line.text() == '':
                self.imie_line.setText("Nie podano imienia")
            if self.nazwisko_line.text() == '':
                self.nazwisko_line.setText("Nie podano nazwiska")

    def play(self, filename):
        if os.path.isfile(filename):
            QtMultimedia.QSound.play(filename)
            self.statusBar.showMessage('Nagranie odtworzono')
        else:
            self.statusBar.showMessage('Nie ma takiego pliku')

    def playRecording(self):
        self.play(self.nazwa_pliku)

    def saveRecording(self):
        # print('skopiowano')
        dst = self.audio_directory + self.nazwa_folderu
        if not os.path.isdir(dst):
            os.mkdir(dst)

        wew_nazwa_pliku = self.nazwa_pliku.split('.')[0] + '_' + str(len(os.listdir(dst))) + '.wav'

        move(self.nazwa_pliku, dst + '\\' + wew_nazwa_pliku)

        no_F_dst = r'c:\Users\kajet\Desktop\magisterka\dane\Audio\Origin''\\' + self.nazwa_folderu
        if not os.path.isdir(no_F_dst):
            os.mkdir(no_F_dst)

        move('no_F_'+self.nazwa_pliku, no_F_dst + '\\' + wew_nazwa_pliku)

        self.liczba_nagran.display(self.liczba_nagran.intValue() - 1)

        if self.liczba_nagran.intValue() > 0:
            self.wlaczNagrywanie.setEnabled(True)
        else:
            self.generujModel.setEnabled(True)

        self.usunNagranie.setEnabled(False)
        self.zapiszNagranie.setEnabled(False)
        self.odtworzNagranie.setEnabled(False)
        self.statusBar.showMessage('Nagranie zapisano')

    def deleteRecording(self):
        # os.remove(os.getcwd() + '\\' + self.nazwa_pliku)
        os.remove(self.nazwa_pliku)
        self.usunNagranie.setEnabled(False)
        self.zapiszNagranie.setEnabled(False)
        self.odtworzNagranie.setEnabled(False)
        self.wlaczNagrywanie.setEnabled(True)
        self.statusBar.showMessage('Nagranie usunięto')

    def generateModel(self):
        training_model(self.audio_directory + self.nazwa_folderu + '\\', self.models_directory)
        self.liczba_nagran.display('5')
        self.statusBar.showMessage('Wygenerowano model')
        self.imie_line.setReadOnly(False)
        self.nazwisko_line.setReadOnly(False)
        self.wlaczNagrywanie.setEnabled(True)
        self.generujModel.setEnabled(False)

    def openTutorial(self):
        self.tutorial = Tutorial()

    def searchFile(self):
        self.fname = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, 'Open file', self.test_audio_directory)

        if self.fname[0]:
            self.sciezka_line.setText(self.fname[0])
            self.plik_check.setEnabled(True)
            self.file_to_test = self.sciezka_line.text()
        else:
            self.plik_check.setEnabled(False)
            self.plik_check.setChecked(False)

    def recordSpeaker(self):
        self.statusBar.showMessage('Nagrywanie w toku ...')
        self.file_to_test = self.default_filename
        self.record(self.file_to_test, self.timer_tab2)
        self.nagrajMowce.setText('Nagraj ponownie')

    def playSpeaker(self):
        self.play(self.file_to_test)

    def recordFromFile(self, state):
        if state == QtCore.Qt.Checked:
            self.nagrany_check.setEnabled(False)
            self.nagrany_check.setChecked(False)
            self.rozpoznajMowce.setEnabled(True)
            self.odtworzMowce.setEnabled(True)

            self.file_to_test = self.sciezka_line.text()
        else:
            self.rozpoznajMowce.setEnabled(False)
            self.odtworzMowce.setEnabled(False)
            if self.recording_exist:
                self.nagrany_check.setEnabled(True)

    def recordFromRecord(self, state):
        if state == QtCore.Qt.Checked:
            self.plik_check.setEnabled(False)
            self.plik_check.setChecked(False)
            self.rozpoznajMowce.setEnabled(True)
            self.odtworzMowce.setEnabled(True)
            self.file_to_test = self.default_filename
        else:
            self.rozpoznajMowce.setEnabled(False)
            self.odtworzMowce.setEnabled(False)
            if self.sciezka_line.text() != '':
                self.plik_check.setEnabled(True)

    def recognizeSpeaker(self):
        speaker = comparing_models(self.models_directory, self.UBM_directory, self.file_to_test)

        if speaker == 'UBM':
            self.textEdit.setText('Mówcy nie ma w bazie')
        else:
            self.textEdit.setText('Mówca rozpoznany jako: ' + speaker)


class AudioThread(QtCore.QThread):
    def __init__(self, nazwa_pliku, czas_nagrania):
        QtCore.QThread.__init__(self)

        self.nazwa_pliku = nazwa_pliku
        self.czas_nagrania = czas_nagrania

    def run(self):
        audio_sample(self.nazwa_pliku, self.czas_nagrania)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

