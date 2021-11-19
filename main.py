import sys
from ui_main import Ui_MainWindow

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, SIGNAL,QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QObject, Slot, Signal, QThread)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


import pytesseract
from http.server import HTTPServer
import server
import os
import cv2
import numpy as np
from datetime import date
import socket
import time



#Klasörleme işlemi için tarih bulunması
tarih = date.today()
tarih= tarih.strftime("%d/%m/%y")
tarih = tarih.replace("/"," ")

#Sunucu için ip'nin bulunması
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("1.1.1.1", 80))
serverip = (s.getsockname()[0])
s.close()


# Global değişkenler
dosyadizini = os.getcwd()
goruntuislemedosyakonumu = None
islenecekgoruntuler = None
server_address_httpd = None
ipcameraadresi = None
uiverisi = None
url = 'http://192.168.1.101:8080/video' # 'IP WEBCAM' uygulaması üzerinden erişilebilecek olan yayın url'si. Arayüz üzerinden kontrol edilmektedir.
kitapadi = None
kayitadresi = None
konum = None

"""
Kitap Adı eğer ayarlanmamış (bir kitap adı değişkeni girilmiş ise örn: 'ArabaSevdası' , kaydedilen görüntüleri kitap adına ait klasörde depolar.
Arayüz üzerinde boş bırakılmış ise tarihe ait klasörü oluşturur ve kayıt işlemini o klasöre gerçekleştirir.
"""





class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ServerThread = ServerThread()
        self.YakalamaThread = YakalamaThread()
        self.GoruntuIslemeThread = GoruntuIslemeThread()
        self.OCRThread = OCRThread()
        self.fonksiyonlar()
        self.ui.stackedWidget.setCurrentIndex(0)



    def fonksiyonlar(self):

        icon = QIcon("./icon.png")
        self.setWindowIcon(icon)

        #Sayfalar
        self.ui.pushButton_ocrsayfasi.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_ocr))
        self.ui.pushButton_kaydetmesayfasi.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_capture))
        self.ui.pushButton_goruntuislemesayfasi.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_goruntuisleme))

        #Sinyaller
        self.ServerThread.serversinyali.connect(self.sunucubasladi)
        self.YakalamaThread.hatasinyali.connect(lambda: QMessageBox.critical(self, "Hata!", "IP Webcam uygulaması ile bağlantı sağlanamadı!\n"))
        self.GoruntuIslemeThread.tamamlandısinyali.connect(self.goruntuislendi)
        self.GoruntuIslemeThread.tamamentamamlandisinyali.connect(self.goruntuislemetamamlandi)

        self.OCRThread.tamamlandısinyali.connect(self.OCRgoruntuislendi)
        self.OCRThread.tamamentamamlandisinyali.connect(self.OCRgoruntuislemetamamlandi)

        #Buton Komutları
        self.ui.pushButton_capturebaslat.clicked.connect(self.goruntukaydetme)
        self.ui.checkBox_mobiluygulama.stateChanged.connect(self.sunucubaslat)
        self.ui.pushButton_dondur.clicked.connect(self.dondur)
        self.ui.pushButton_kaydet.clicked.connect(self.goruntuyukaydet)
        self.ui.pushButton_yardim.clicked.connect(self.yardim)
        self.ui.pushButton_capturedurdur.clicked.connect(self.goruntuyudurdur)
        self.ui.pushButton_dosyakonumusec.clicked.connect(self.dosyadizini)
        self.ui.pushButton_kayitkonumusec.clicked.connect(self.kayitdizini)
        self.ui.pushButton_goruntuislemesec.clicked.connect(self.goruntuislemedosyadizini)
        self.ui.pushButton_goruntuislemeayarlar.clicked.connect(self.goruntuislemeayarlar)
        self.ui.pushButton_goruntuislemebasla.clicked.connect(self.goruntuislemebaslat)
        self.ui.pushButton_ocrbasla.clicked.connect(self.ocrbasla)
        self.ui.pushButton_ocrdurdur.clicked.connect(self.ocrdurdur)


    def ocrbasla(self):
        global islenecekgoruntuler, kayitadresi, konum,dosyadizini
        os.chdir(dosyadizini)

        kayitadresi = self.ui.lineEdit_kayitkonumu.text()
        konum = self.ui.lineEdit_konum.text()
        konum = konum.replace("/", "\\")
        izinliuzantilar = self.ui.lineEdit_uzanti.text()
        try:
            izinliuzantilar = izinliuzantilar.split(",")


            islenecekgoruntuler = [fn for fn in os.listdir(konum) if any(fn.endswith(ext) for ext in izinliuzantilar)]
            if self.ui.checkBox_sadeceislenmisgoruntukullan.isChecked():
                islenecekgoruntuler = [s for s in islenecekgoruntuler if "_islenmis" in s]

        except:
            pass

        if len(islenecekgoruntuler) > 0 and len(kayitadresi) > 0:
            self.OCRThread.start()
        else:
            QMessageBox.critical(self, "Hata!", "Dosya yollarını doğru girdiğinizden emin olun!")

    def ocrdurdur(self):
        self.OCRThread.terminate()


    def goruntuislemebaslat(self):
        global islenecekgoruntuler, konum, dosyadizini
        os.chdir(dosyadizini)
        konum = self.ui.lineEdit_goruntuislemedosyakonumu.text()
        konum = konum.replace("/","\\")

        izinliuzantilar = ['jpg', 'jpeg', 'bmp', 'png']
        islenecekgoruntuler = [fn for fn in os.listdir(konum) if any(fn.endswith(ext) for ext in izinliuzantilar)]

        if len(islenecekgoruntuler) > 0:
            self.GoruntuIslemeThread.start()
        else:
            QMessageBox.critical(self, "Hata!", "İşlenecek görüntü bulunamadı!")

    def goruntuislendi(self, tamamlanmisgoruntuadi):
        self.ui.label_cikti.setText(f"İşlem sonucu: {tamamlanmisgoruntuadi} isimli görüntünün işlemesi tamamlandı")

    def goruntuislemetamamlandi(self):
        self.ui.label_cikti.setText("İşlem sonucu: Tüm görüntülerin işlemesi tamamlandı")
        QMessageBox.information(self, "Başarılı", "Tüm görüntülerin işlemesi tamamlandı")

    def OCRgoruntuislendi(self, tamamlanmisgoruntuadi):
        self.ui.label_cikti.setText(f"İşlem sonucu: {tamamlanmisgoruntuadi} isimli görüntünün işlemesi tamamlandı")

    def OCRgoruntuislemetamamlandi(self):
        self.ui.label_cikti.setText(f"İşlem sonucu: Tüm görüntülerin işlemesi tamamlandı")
        QMessageBox.information(self, "Başarılı", f"Sunucu http://{serverip}:8080/ adresinde başlatıldı!\n")

    def goruntuislemedurdur(self):
        self.GoruntuIslemeThread.terminate()

    def goruntuislemeayarlar(self):
        os.startfile("Ayarlar.txt")

    def goruntuislemedosyadizini(self):
        global goruntuislemedosyakonumu
        goruntuislemedosyakonumu = QtWidgets.QFileDialog.getExistingDirectory(self, 'Görüntülerin Bulunduğu Konumu Seçiniz')
        self.ui.lineEdit_goruntuislemedosyakonumu.setText(goruntuislemedosyakonumu)

    def dosyadizini(self):
        kayitdosyakonumu = QtWidgets.QFileDialog.getExistingDirectory(self, 'Görüntülerin Bulunduğu Konumu Seçiniz')
        self.ui.lineEdit_konum.setText(kayitdosyakonumu)

    def kayitdizini(self):
        kayitdosyakonumu = QtWidgets.QFileDialog.getExistingDirectory(self, 'Kayıt Konumunu Seçiniz')
        self.ui.lineEdit_kayitkonumu.setText(kayitdosyakonumu)

    def yardim(self):
        os.startfile("BeniOku.txt")

    def sunucubaslat(self):
        global port

        port = self.ui.lineEdit_port.text()
        if len(port) == 0:
            port = "8080"
        if self.ui.checkBox_mobiluygulama.isChecked():
            self.ServerThread.start()
        else:
            self.ServerThread.terminate()
            print("Sunucu durduruldu!")
            QMessageBox.information(self, "Başarılı", "Sunucu durduruldu!\n")

    def sunucubasladi(self):
        QMessageBox.information(self, "Başarılı", f"Sunucu http://{serverip}:8080/ adresinde başlatıldı!\n")

    def goruntukaydetme(self):
        global ipcameraadresi, port, kitapadi,dosyadizini

        ipcameraadresi = self.ui.lineEdit_ipcameraadresi.text()
        if len(ipcameraadresi)<3:
            ipcameraadresi = "192.168.1.101"
        ipcameraadresi = f"http://{ipcameraadresi}:8080/video"

        kitapadi = self.ui.lineEdit_kitapadi.text()

        # Dizin oluşturma ve değiştirme
        if len(kitapadi) > 0:
            try:
                os.chdir(f"{dosyadizini}\{kitapadi}")
            except:
                os.mkdir(f"{dosyadizini}\{kitapadi}")
                os.chdir(f"{dosyadizini}\{kitapadi}")
        else:
            try:
                os.chdir(f"{dosyadizini}\{tarih}")

            except:
                os.mkdir(f"{dosyadizini}\{tarih}")
                os.chdir(f"{dosyadizini}\{tarih}")

        f = open(f"{dosyadizini}\komut.txt", "w")
        f.write("done")
        f.close()
        self.YakalamaThread.start()

    def goruntuyudurdur(self):

        try:
            cv2.destroyAllWindows()
        except:
            pass
        self.YakalamaThread.terminate()

    def dondur(self):
        global uiverisi
        uiverisi = "dondur"

    def goruntuyukaydet(self):
        global uiverisi
        uiverisi = "kaydet"

class ServerThread(QThread):
    serversinyali = Signal(str)


    def __init__(self, parent=None):
        QThread.__init__(self, parent)

    @Slot()
    def run(self):
        server_address_httpd = (serverip, 8080)
        httpd = HTTPServer(server_address_httpd, server.RequestHandler_httpd)
        print(f'Sunucu http://{serverip}:8080/ adresinde başlatıldı!\n')
        self.serversinyali.emit("Başarılı")


        httpd.serve_forever()

class YakalamaThread(QThread):
    hatasinyali = Signal(str)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)


    @Slot()
    def run(self):
        global ipcameraadresi,uiverisi,dosyadizini
        yakalama = cv2.VideoCapture(ipcameraadresi)
        ekraniayir = False
        sayac = 0
        while True:


            ret, goruntu = yakalama.read()

            if goruntu is not None:


                # Yeniden boyutlandırma
                boyutlandirma_yuzdesi = 50
                genislik = int(goruntu.shape[1] * boyutlandirma_yuzdesi / 100)
                yukseklik = int(goruntu.shape[0] * boyutlandirma_yuzdesi / 100)
                sonboyutlar = (genislik, yukseklik)

                goruntu = cv2.resize(goruntu, sonboyutlar, interpolation=cv2.INTER_AREA)
                orjinalgoruntu = goruntu.copy()  # Göstermek için görüntünün yedeklenmesi

                # Görüntüyü Döndürme
                goruntu = cv2.rotate(goruntu, cv2.cv2.ROTATE_90_CLOCKWISE)

                # Ekranı ikiye bölme
                if ekraniayir:
                    goruntu = cv2.rotate(goruntu, cv2.cv2.ROTATE_90_CLOCKWISE)
                    goruntu = cv2.rotate(goruntu, cv2.cv2.ROTATE_90_CLOCKWISE)
                    goruntu = cv2.rotate(goruntu, cv2.cv2.ROTATE_90_CLOCKWISE)
                    cv2.line(goruntu, (int(genislik / 2), 0), (int(genislik / 2), yukseklik), (0, 0, 255), 5)

                cv2.imshow('Yayin', goruntu)

                f = open(f"{dosyadizini}\komut.txt", "r")
                sunucuverisi = f.read()

                islem = cv2.waitKey(1)

                # Ekrandaki kaydetmek için 'q' tuşuna basılmalıdır. Eğer ekran ayrılmış durumda ise, sol ve sağ olmak üzere iki adet görüntü kaydedilecektir.
                if islem == ord("q") or sunucuverisi == "goruntukaydet" or uiverisi == "kaydet":
                    uiverisi = None

                    f = open(f"{dosyadizini}\komut.txt", "w")
                    f.write("done")
                    f.close()

                    sayac += 1
                    if ekraniayir:
                        solgoruntu = orjinalgoruntu[0: yukseklik, 0: int(genislik / 2)]
                        saggoruntu = orjinalgoruntu[0: yukseklik, int(genislik / 2): genislik]

                        cv2.imwrite(f'sayfa{sayac}.png', solgoruntu)
                        sayac += 1
                        cv2.imwrite(f'sayfa{sayac}.png', saggoruntu)

                        cv2.putText(goruntu, "Kaydedildi", (int(yukseklik / 2), int(genislik / 2)),
                                    cv2.FONT_HERSHEY_DUPLEX, 3,
                                    (0, 255, 0), 5, cv2.LINE_AA)
                    else:
                        cv2.imwrite(f'sayfa{sayac}.png', goruntu)
                        cv2.putText(goruntu, "Kaydedildi", (0, int(genislik / 2)), cv2.FONT_HERSHEY_DUPLEX, 3,
                                    (0, 255, 0), 5, cv2.LINE_AA)

                    cv2.imshow('Yayin', goruntu)
                    cv2.waitKey(300)
                    print("Kaydedildi")
                # Ekranı ikiye bölen çizgiyi çalıştırmak için 'w' tuşuna basılmalıdır, kapatmak için ise tekrar basılması yeterlidir.
                if islem == ord("w") or sunucuverisi == "dondur" or uiverisi == "dondur":
                    uiverisi = None
                    f = open(f"{dosyadizini}\komut.txt", "w")
                    f.write("done")
                    f.close()


                    if ekraniayir == False:
                        ekraniayir = True
                    else:
                        ekraniayir = False

                # Programı sonlandırmak için 's' tuşuna veya arayüzden 'Durdur' butonuna basılmalıdır.
                if islem == ord("s"):
                    cv2.destroyAllWindows()
                    break

            else:
                self.hatasinyali.emit("Hata")
                break

class GoruntuIslemeThread(QThread):
    tamamlandısinyali = Signal(str)
    tamamentamamlandisinyali = Signal(str)
    global islenecekgoruntuler, konum
    def __init__(self, parent=None):
        QThread.__init__(self, parent)

    @Slot()
    def run(self):

        for i in islenecekgoruntuler:


            os.system(f'cmd /c "python sayfa_duzlestir.py "{konum}" "{konum}\{i}"')
            self.tamamlandısinyali.emit(i)

        self.tamamentamamlandisinyali.emit("Tamamlandi")

class OCRThread(QThread):
    tamamlandısinyali = Signal(str)
    tamamentamamlandisinyali = Signal(str)
    global islenecekgoruntuler, dosyadizini, kayitadresi, konum
    def __init__(self, parent=None):
        QThread.__init__(self, parent)

    @Slot()
    def run(self):

        os.chdir(konum)
        for i in islenecekgoruntuler:
            goruntu = cv2.imread(i)


            metin = pytesseract.image_to_string(goruntu, lang="tur")
            f = open(f"{kayitadresi}\{i}.txt", "w")
            f.write(metin)
            f.close()
            f = open(f"{kayitadresi}\hepsi.txt", "a")
            f.write(metin)
            f.close()
            self.tamamlandısinyali.emit(i)

        self.tamamentamamlandisinyali.emit("Tamamlandi")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


