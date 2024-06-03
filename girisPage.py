from girisui import *
from kayitPage import *
from libraryPage import *
from PyQt5.QtWidgets import *
import sys
import sqlite3

class pageGiris(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_girisPage()
        self.ui.setupUi(self)
        
        #database configuration
        self.conn=sqlite3.Connection("kullanici.db") #veri tabanını açar
        self.curs=self.conn.cursor() #sql komutlarını kullanmak execute etmek için cursor nesnesi kullanılır
        
        #signal slot
        self.ui.btnGiris.clicked.connect(self.GIRIS)
        self.ui.btnKayit.clicked.connect(self.KAYIT)
        self.ui.cbRemember.stateChanged.connect(self.CHECK)
        
    def CHECK(self):
        if (self.ui.cbRemember.isChecked()):#Checkbox'in isaretlenip isaretlenmedigini kontrol eder
            self.ui.lePassword.setEchoMode(QLineEdit.Normal)#checkbox'in EchoMode'unu Normal yaparak sifrenin gorunmesini saglar
        else:
            self.ui.lePassword.setEchoMode(QLineEdit.Password)
        
    def KAYIT(self):
        self.pencereac = pageKayit()
        self.hide()#gorunen ekranin kapanmasini saglar
        self.pencereac.show()#kayit sayfanin acilmasini saglar
        
    
    def GIRIS(self):
        sqluser = "SELECT UserName, Password FROM kullanicilar"
        kullanici_verileri = list(self.curs.execute(sqluser))
       
        username = self.ui.leKullanciAdi.text()
        password = self.ui.lePassword.text()
       
        for user, pw in kullanici_verileri:
            if user == username and pw == password:
                # Başarılı giriş işlemi
                QMessageBox().information(self, "Bilgilendirme", "Giriş başarılı")
                #Sayfa acilma islemleri
                self.pencereac = pageLibrary()
                self.hide()
                self.pencereac.show()
                return
            #Bos degerler girilince bilgilindirme ekrani gelir
            elif username is "" or password is "":
                QMessageBox().information(self, "Bilgilendirme", "Kullanici adi ve Şifre giriniz!")
                return
        # Kullanıcı adı veya şifre hatalı
        QMessageBox().information(self, "Bilgilendirme", "Kullanıcı Adı veya Şifre hatalı")
    
    
        

if (__name__=="__main__"):
    app = QApplication(sys.argv) ##application oluşturuluyor
    window = pageGiris()
    window.show()
    sys.exit(app.exec_()) #pencereden çıkarken uygulama ile lgili tüm işlemler sonlandırılıyor