from kayitui import *
from girisPage import *
from PyQt5.QtWidgets import *
import sys
import sqlite3


class pageKayit(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_kayitPage()
        self.ui.setupUi(self)
        
        #database configuration
        self.conn=sqlite3.Connection("kullanici.db") #veri tabanını açar
        self.curs=self.conn.cursor()  ##sql komutlarını kullanmak execute etmek için cursor nesnesi kullanılır       
        
        #signal slot
        self.ui.btnKayit.clicked.connect(self.KAYITOL)
        
    def KAYITOL(self):
        userName = self.ui.leUser.text()
        
        pass1 = self.ui.lePass.text()
        pass2 = self.ui.lePassAgain.text()
        
        #Line editlerin bos olup olmadigi kontrol edilir.
        if((pass1 and pass2 and userName) is ""):
            QMessageBox().information(self,"Bilgilendirme","Eksik bir bilgi girdiniz")
        
        #parola ile tekrar girilen parolanin ayni olup olmadigi kontrol edilir.
        elif(pass1 == pass2):
            sql="INSERT INTO kullanicilar (UserName, Password) VALUES (?,?)"
            parameter=[userName,pass1]
            self.curs.execute(sql,parameter)
            self.conn.commit()
            
            QMessageBox().information(self,"Bilgilendirme","Kaydınız Eklendi")
            
            #Sayfa acilma islemleri
            self.hide()
            self.pencereac = pageGiris()
            self.pencereac.show()
        
            

if (__name__=="__main__"):
    app = QApplication(sys.argv) ##application oluşturuluyor
    window = pageKayit()
    window.show()
    sys.exit(app.exec_()) #pencereden çıkarken uygulama ile lgili tüm işlemler sonlandırılıyor