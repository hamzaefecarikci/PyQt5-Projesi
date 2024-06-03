from libraryui import *
from PyQt5.QtWidgets import *
import sys
import sqlite3

class pageLibrary(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_library()
        self.ui.setupUi(self)
        self.currow=0
        
        #database configuration
        self.conn=sqlite3.Connection("kullanici.db") #veri tabanını açar
        self.curs=self.conn.cursor()  ##sql komutlarını kullanmak execute etmek için cursor nesnesi kullanılır
        
        #signal slot
        self.ui.btnNew.clicked.connect(self.YENI)
        self.ui.btnAdd.clicked.connect(self.EKLE)
        self.ui.tWMyGames.itemSelectionChanged.connect(self.itemSelectionChanged)
        self.ui.leSearch.textChanged.connect(self.ARA)
        self.ui.btnDelete.clicked.connect(self.SIL)
        self.ui.toolbtnright.clicked.connect(self.SONRAKI)
        self.ui.toolbtnleft.clicked.connect(self.ONCEKI)
        self.ui.btnUpdate.clicked.connect(self.DUZELT)
    
        #ekran acilince butun oyunlarin gozukmesini saglar
        self.sqlgenel="SELECT * FROM games"
        self.TableWidgettaGoster(self.sqlgenel)
        
    def YENI(self):
        #le editleri bos deger atar ve focuslanir
        self.ui.leGameName.setText("")
        self.ui.leCategory.setText("")
        self.ui.leGameName.setFocus(True)
        
    def EKLE(self):
        _gamename=self.ui.leGameName.text()
        _category = self.ui.leCategory.text()
        sql="INSERT INTO games (GameName,Category) VALUES (?,?)"
        parameter=[_gamename,_category]
        self.curs.execute(sql,parameter)
        self.conn.commit()
        QMessageBox().information(self,"Bilgilendirme","Kaydınız Eklendi")
        self.currow=self.ui.tWMyGames.rowCount()
        sqlgenel="SELECT * FROM games"
        self.TableWidgettaGoster(sqlgenel)
    
    def TableWidgettaGoster(self,sql):
        result = list(self.curs.execute(sql)) #veri çekiliyor ve list veri tipine çevrilir
        print(result)
        rowcount = len(result) #oyun sayısı elde edilir
        self.ui.tWMyGames.setRowCount(rowcount)
        for rowindex,rowdata in enumerate(result): #sorgudan dönen satırlar
            for colindex,coldata in enumerate(rowdata): #sorgudan elde edilen sütun verisi
                self.ui.tWMyGames.setItem(rowindex,colindex,QTableWidgetItem(str(coldata)))
        
        self.ui.tWMyGames.setCurrentCell(self.currow,0)
    
    def SONRAKI(self):
        self.currow += 1
        if (self.currow == self.ui.tWMyGames.rowCount()):
            self.currow=0
        self.ui.tWMyGames.setCurrentCell(self.currow,0)
    
    def ONCEKI(self):
        self.currow -= 1
        if (self.currow<0):
            self.currow = self.ui.tWMyGames.rowCount()-1
        self.ui.tWMyGames.setCurrentCell(self.currow,0)
        
    def TabletoForm(self):
        #tablodaki verilerin line editte gorunmesini saglar
        selectedrows = self.ui.tWMyGames.selectedItems()
        if selectedrows:
            self.ui.leGameName.setText(selectedrows[1].text())
            self.ui.leCategory.setText(selectedrows[2].text())
            
    def itemSelectionChanged(self):
        indeks=self.ui.tWMyGames.currentIndex()
        self.currow=indeks.row()
        self.TabletoForm()
        
    def SIL(self):
        selectedrow=self.ui.tWMyGames.selectedItems()
        if(selectedrow is None):
            QMessageBox().information("Uyari","Herhangi bir oyun seçmediniz!")
            pass
        else:
            response=QMessageBox().question(self,"Silme Onay","Seçili oyunu silmek istediğinize emin misin?",QMessageBox().Yes| QMessageBox().No)
            if (response==QMessageBox().Yes):
                silinecek=selectedrow[0].text()
                sql="DELETE FROM games WHERE Id=?"
                parameter=[silinecek]
                self.curs.execute(sql,parameter)
                self.conn.commit()
                self.TableWidgettaGoster(self.sqlgenel)

    def ARA(self):
        #aranan metni veri tabanindan ceker ve gosterilir
        sql="SELECT Id, GameName, Category FROM games WHERE GameName LIKE'%"+self.ui.leSearch.text()+"%'"
        self.TableWidgettaGoster(sql)
        
    def DUZELT(self):
        print("cuurow=",self.currow)
        duzeltsql="update games SET GameName=?, Category=? WHERE Id=?"
        selectedrow=self.ui.tWMyGames.selectedItems()
        gameId=selectedrow[0].text()
        parameter=[self.ui.leGameName.text(),self.ui.leCategory.text(),gameId]
        self.curs.execute(duzeltsql,parameter)
        self.conn.commit()
        self.TableWidgettaGoster(self.sqlgenel)

if (__name__=="__main__"):
    app = QApplication(sys.argv) ##application oluşturuluyor
    window = pageLibrary()
    window.show()
    sys.exit(app.exec_()) #pencereden çıkarken uygulama ile lgili tüm işlemler sonlandırılıyor