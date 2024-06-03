from PyQt5 import uic

with open("girisui.py", "w", encoding="utf-8") as fout:
    uic.compileUi("giris.ui", fout)