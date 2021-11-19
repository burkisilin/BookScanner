# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PySide2 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 410)
        MainWindow.setMinimumSize(QtCore.QSize(458, 410))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_burakbayramoglu = QtWidgets.QLabel(self.centralwidget)
        self.label_burakbayramoglu.setMinimumSize(QtCore.QSize(323, 23))
        self.label_burakbayramoglu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_burakbayramoglu.setObjectName("label_burakbayramoglu")
        self.horizontalLayout_13.addWidget(self.label_burakbayramoglu)
        self.pushButton_yardim = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_yardim.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_yardim.setObjectName("pushButton_yardim")
        self.horizontalLayout_13.addWidget(self.pushButton_yardim)
        self.gridLayout_3.addLayout(self.horizontalLayout_13, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(440, 284))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton_kaydetmesayfasi = QtWidgets.QPushButton(self.frame)
        self.pushButton_kaydetmesayfasi.setMinimumSize(QtCore.QSize(115, 23))
        self.pushButton_kaydetmesayfasi.setMaximumSize(QtCore.QSize(98, 23))
        self.pushButton_kaydetmesayfasi.setObjectName("pushButton_kaydetmesayfasi")
        self.horizontalLayout_3.addWidget(self.pushButton_kaydetmesayfasi)
        self.pushButton_goruntuislemesayfasi = QtWidgets.QPushButton(self.frame)
        self.pushButton_goruntuislemesayfasi.setMinimumSize(QtCore.QSize(114, 23))
        self.pushButton_goruntuislemesayfasi.setMaximumSize(QtCore.QSize(114, 23))
        self.pushButton_goruntuislemesayfasi.setObjectName("pushButton_goruntuislemesayfasi")
        self.horizontalLayout_3.addWidget(self.pushButton_goruntuislemesayfasi)
        self.pushButton_ocrsayfasi = QtWidgets.QPushButton(self.frame)
        self.pushButton_ocrsayfasi.setMinimumSize(QtCore.QSize(120, 23))
        self.pushButton_ocrsayfasi.setMaximumSize(QtCore.QSize(114, 23))
        self.pushButton_ocrsayfasi.setObjectName("pushButton_ocrsayfasi")
        self.horizontalLayout_3.addWidget(self.pushButton_ocrsayfasi)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 245,240);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_capture = QtWidgets.QWidget()
        self.page_capture.setObjectName("page_capture")
        self.gridLayout = QtWidgets.QGridLayout(self.page_capture)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(228, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_goruntukaydetme = QtWidgets.QLabel(self.page_capture)
        self.label_goruntukaydetme.setAlignment(QtCore.Qt.AlignCenter)
        self.label_goruntukaydetme.setObjectName("label_goruntukaydetme")
        self.verticalLayout.addWidget(self.label_goruntukaydetme)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_ipcameraadresi = QtWidgets.QLabel(self.page_capture)
        self.label_ipcameraadresi.setObjectName("label_ipcameraadresi")
        self.horizontalLayout_2.addWidget(self.label_ipcameraadresi)
        self.lineEdit_ipcameraadresi = QtWidgets.QLineEdit(self.page_capture)
        self.lineEdit_ipcameraadresi.setMinimumSize(QtCore.QSize(133, 20))
        self.lineEdit_ipcameraadresi.setMaximumSize(QtCore.QSize(133, 20))
        self.lineEdit_ipcameraadresi.setObjectName("lineEdit_ipcameraadresi")
        self.horizontalLayout_2.addWidget(self.lineEdit_ipcameraadresi)
        self.lineEdit_port = QtWidgets.QLineEdit(self.page_capture)
        self.lineEdit_port.setMinimumSize(QtCore.QSize(41, 20))
        self.lineEdit_port.setMaximumSize(QtCore.QSize(41, 20))
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.horizontalLayout_2.addWidget(self.lineEdit_port)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_kitapadi = QtWidgets.QLabel(self.page_capture)
        self.label_kitapadi.setMinimumSize(QtCore.QSize(86, 20))
        self.label_kitapadi.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_kitapadi.setObjectName("label_kitapadi")
        self.horizontalLayout_12.addWidget(self.label_kitapadi)
        self.lineEdit_kitapadi = QtWidgets.QLineEdit(self.page_capture)
        self.lineEdit_kitapadi.setObjectName("lineEdit_kitapadi")
        self.horizontalLayout_12.addWidget(self.lineEdit_kitapadi)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.checkBox_mobiluygulama = QtWidgets.QCheckBox(self.page_capture)
        self.checkBox_mobiluygulama.setObjectName("checkBox_mobiluygulama")
        self.verticalLayout.addWidget(self.checkBox_mobiluygulama)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_dondur = QtWidgets.QPushButton(self.page_capture)
        self.pushButton_dondur.setObjectName("pushButton_dondur")
        self.horizontalLayout_11.addWidget(self.pushButton_dondur)
        self.pushButton_kaydet = QtWidgets.QPushButton(self.page_capture)
        self.pushButton_kaydet.setObjectName("pushButton_kaydet")
        self.horizontalLayout_11.addWidget(self.pushButton_kaydet)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_capturedurdur = QtWidgets.QPushButton(self.page_capture)
        self.pushButton_capturedurdur.setObjectName("pushButton_capturedurdur")
        self.horizontalLayout.addWidget(self.pushButton_capturedurdur)
        self.pushButton_capturebaslat = QtWidgets.QPushButton(self.page_capture)
        self.pushButton_capturebaslat.setObjectName("pushButton_capturebaslat")
        self.horizontalLayout.addWidget(self.pushButton_capturebaslat)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(226, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_capture)
        self.page_goruntuisleme = QtWidgets.QWidget()
        self.page_goruntuisleme.setObjectName("page_goruntuisleme")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_goruntuisleme)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem7)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.page_goruntuisleme)
        self.label.setEnabled(True)
        self.label.setMinimumSize(QtCore.QSize(297, 13))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_islemedosyaskonumu = QtWidgets.QLabel(self.page_goruntuisleme)
        self.label_islemedosyaskonumu.setObjectName("label_islemedosyaskonumu")
        self.horizontalLayout_14.addWidget(self.label_islemedosyaskonumu)
        self.lineEdit_goruntuislemedosyakonumu = QtWidgets.QLineEdit(self.page_goruntuisleme)
        self.lineEdit_goruntuislemedosyakonumu.setObjectName("lineEdit_goruntuislemedosyakonumu")
        self.horizontalLayout_14.addWidget(self.lineEdit_goruntuislemedosyakonumu)
        self.pushButton_goruntuislemesec = QtWidgets.QPushButton(self.page_goruntuisleme)
        self.pushButton_goruntuislemesec.setObjectName("pushButton_goruntuislemesec")
        self.horizontalLayout_14.addWidget(self.pushButton_goruntuislemesec)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem8)
        self.pushButton_goruntuislemedurdur = QtWidgets.QPushButton(self.page_goruntuisleme)
        self.pushButton_goruntuislemedurdur.setMinimumSize(QtCore.QSize(100, 23))
        self.pushButton_goruntuislemedurdur.setMaximumSize(QtCore.QSize(100, 23))
        self.pushButton_goruntuislemedurdur.setObjectName("pushButton_goruntuislemedurdur")
        self.horizontalLayout_10.addWidget(self.pushButton_goruntuislemedurdur)
        self.pushButton_goruntuislemebasla = QtWidgets.QPushButton(self.page_goruntuisleme)
        self.pushButton_goruntuislemebasla.setMinimumSize(QtCore.QSize(100, 23))
        self.pushButton_goruntuislemebasla.setMaximumSize(QtCore.QSize(100, 23))
        self.pushButton_goruntuislemebasla.setObjectName("pushButton_goruntuislemebasla")
        self.horizontalLayout_10.addWidget(self.pushButton_goruntuislemebasla)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem10)
        self.gridLayout_6.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem11)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem12)
        self.pushButton_goruntuislemeayarlar = QtWidgets.QPushButton(self.page_goruntuisleme)
        self.pushButton_goruntuislemeayarlar.setObjectName("pushButton_goruntuislemeayarlar")
        self.verticalLayout_6.addWidget(self.pushButton_goruntuislemeayarlar)
        self.horizontalLayout_15.addLayout(self.verticalLayout_6)
        self.gridLayout_6.addLayout(self.horizontalLayout_15, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_goruntuisleme)
        self.page_ocr = QtWidgets.QWidget()
        self.page_ocr.setObjectName("page_ocr")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_ocr)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem13)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem14)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_optikkaraktertanima_2 = QtWidgets.QLabel(self.page_ocr)
        self.label_optikkaraktertanima_2.setMinimumSize(QtCore.QSize(106, 16))
        self.label_optikkaraktertanima_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_optikkaraktertanima_2.setObjectName("label_optikkaraktertanima_2")
        self.verticalLayout_2.addWidget(self.label_optikkaraktertanima_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_konum = QtWidgets.QLabel(self.page_ocr)
        self.label_konum.setMinimumSize(QtCore.QSize(74, 20))
        self.label_konum.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_konum.setObjectName("label_konum")
        self.horizontalLayout_5.addWidget(self.label_konum)
        self.lineEdit_konum = QtWidgets.QLineEdit(self.page_ocr)
        self.lineEdit_konum.setMinimumSize(QtCore.QSize(133, 20))
        self.lineEdit_konum.setObjectName("lineEdit_konum")
        self.horizontalLayout_5.addWidget(self.lineEdit_konum)
        self.pushButton_dosyakonumusec = QtWidgets.QPushButton(self.page_ocr)
        self.pushButton_dosyakonumusec.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton_dosyakonumusec.setObjectName("pushButton_dosyakonumusec")
        self.horizontalLayout_5.addWidget(self.pushButton_dosyakonumusec)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_dosyauzantisi = QtWidgets.QLabel(self.page_ocr)
        self.label_dosyauzantisi.setMinimumSize(QtCore.QSize(74, 20))
        self.label_dosyauzantisi.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_dosyauzantisi.setObjectName("label_dosyauzantisi")
        self.horizontalLayout_6.addWidget(self.label_dosyauzantisi)
        self.lineEdit_uzanti = QtWidgets.QLineEdit(self.page_ocr)
        self.lineEdit_uzanti.setMinimumSize(QtCore.QSize(133, 20))
        self.lineEdit_uzanti.setObjectName("lineEdit_uzanti")
        self.horizontalLayout_6.addWidget(self.lineEdit_uzanti)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_ciktikonumu = QtWidgets.QLabel(self.page_ocr)
        self.label_ciktikonumu.setMinimumSize(QtCore.QSize(74, 20))
        self.label_ciktikonumu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_ciktikonumu.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_ciktikonumu.setObjectName("label_ciktikonumu")
        self.horizontalLayout_8.addWidget(self.label_ciktikonumu)
        self.lineEdit_kayitkonumu = QtWidgets.QLineEdit(self.page_ocr)
        self.lineEdit_kayitkonumu.setMinimumSize(QtCore.QSize(133, 20))
        self.lineEdit_kayitkonumu.setText("")
        self.lineEdit_kayitkonumu.setObjectName("lineEdit_kayitkonumu")
        self.horizontalLayout_8.addWidget(self.lineEdit_kayitkonumu)
        self.pushButton_kayitkonumusec = QtWidgets.QPushButton(self.page_ocr)
        self.pushButton_kayitkonumusec.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton_kayitkonumusec.setObjectName("pushButton_kayitkonumusec")
        self.horizontalLayout_8.addWidget(self.pushButton_kayitkonumusec)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.checkBox_sadeceislenmisgoruntukullan = QtWidgets.QCheckBox(self.page_ocr)
        self.checkBox_sadeceislenmisgoruntukullan.setObjectName("checkBox_sadeceislenmisgoruntukullan")
        self.verticalLayout_2.addWidget(self.checkBox_sadeceislenmisgoruntukullan)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_ocrdurdur = QtWidgets.QPushButton(self.page_ocr)
        self.pushButton_ocrdurdur.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton_ocrdurdur.setObjectName("pushButton_ocrdurdur")
        self.horizontalLayout_7.addWidget(self.pushButton_ocrdurdur)
        self.pushButton_ocrbasla = QtWidgets.QPushButton(self.page_ocr)
        self.pushButton_ocrbasla.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton_ocrbasla.setObjectName("pushButton_ocrbasla")
        self.horizontalLayout_7.addWidget(self.pushButton_ocrbasla)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem15)
        self.horizontalLayout_9.addLayout(self.verticalLayout_3)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem16)
        self.gridLayout_4.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_ocr)
        self.gridLayout_5.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.label_cikti = QtWidgets.QLabel(self.frame)
        self.label_cikti.setMinimumSize(QtCore.QSize(420, 13))
        self.label_cikti.setObjectName("label_cikti")
        self.gridLayout_5.addWidget(self.label_cikti, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Burak Scanner"))
        self.label_burakbayramoglu.setText(_translate("MainWindow", "Burak Bayramoğlu 171011009"))
        self.pushButton_yardim.setText(_translate("MainWindow", "Yardım"))
        self.pushButton_kaydetmesayfasi.setText(_translate("MainWindow", "Görüntü Kaydetme"))
        self.pushButton_goruntuislemesayfasi.setText(_translate("MainWindow", "Görüntü İşleme"))
        self.pushButton_ocrsayfasi.setText(_translate("MainWindow", "Optik Karakter Tanıma"))
        self.label_goruntukaydetme.setText(_translate("MainWindow", "Görüntü Kaydetme"))
        self.label_ipcameraadresi.setText(_translate("MainWindow", "IP Kamera Adresi:"))
        self.lineEdit_ipcameraadresi.setPlaceholderText(_translate("MainWindow", "IP Kamera Adresi"))
        self.lineEdit_port.setText(_translate("MainWindow", "8080"))
        self.lineEdit_port.setPlaceholderText(_translate("MainWindow", "Port"))
        self.label_kitapadi.setText(_translate("MainWindow", "Kitap Adı:"))
        self.lineEdit_kitapadi.setPlaceholderText(_translate("MainWindow", "Kitap veya Klasör Adı"))
        self.checkBox_mobiluygulama.setText(_translate("MainWindow", "Mobil Uygulamadan Yönetim"))
        self.pushButton_dondur.setText(_translate("MainWindow", "Döndür"))
        self.pushButton_kaydet.setText(_translate("MainWindow", "Gorüntüyü Kaydet"))
        self.pushButton_capturedurdur.setText(_translate("MainWindow", "Durdur"))
        self.pushButton_capturebaslat.setText(_translate("MainWindow", "Başlat"))
        self.label.setText(_translate("MainWindow", "Görüntü İşleme"))
        self.label_islemedosyaskonumu.setText(_translate("MainWindow", "Dosya Konumu:"))
        self.pushButton_goruntuislemesec.setText(_translate("MainWindow", "Seç"))
        self.pushButton_goruntuislemedurdur.setText(_translate("MainWindow", "Durdur"))
        self.pushButton_goruntuislemebasla.setText(_translate("MainWindow", "Başlat"))
        self.pushButton_goruntuislemeayarlar.setText(_translate("MainWindow", "Ayarlar"))
        self.label_optikkaraktertanima_2.setText(_translate("MainWindow", "Optik Karakter Tanıma"))
        self.label_konum.setText(_translate("MainWindow", "Dosya Konumu:"))
        self.lineEdit_konum.setPlaceholderText(_translate("MainWindow", "Arabasevdasi"))
        self.pushButton_dosyakonumusec.setText(_translate("MainWindow", "Seç"))
        self.label_dosyauzantisi.setText(_translate("MainWindow", "Dosya Uzantıları:"))
        self.lineEdit_uzanti.setText(_translate("MainWindow", "png,jpg,jpeg"))
        self.lineEdit_uzanti.setPlaceholderText(_translate("MainWindow", "png,jpg gibi"))
        self.label_ciktikonumu.setText(_translate("MainWindow", "Çıktı Konumu:"))
        self.lineEdit_kayitkonumu.setPlaceholderText(_translate("MainWindow", "Kayıt Adresi"))
        self.pushButton_kayitkonumusec.setText(_translate("MainWindow", "Seç"))
        self.checkBox_sadeceislenmisgoruntukullan.setText(_translate("MainWindow", "İçerisinde \"_islenmis\" içeren görüntüleri kullan"))
        self.pushButton_ocrdurdur.setText(_translate("MainWindow", "Durdur"))
        self.pushButton_ocrbasla.setText(_translate("MainWindow", "Başlat"))
        self.label_cikti.setText(_translate("MainWindow", "İşlem Sonucu:"))


