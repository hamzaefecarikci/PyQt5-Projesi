from PyQt5 import uic

with open("kayitui.py", "w", encoding="utf-8") as fout:
    uic.compileUi("kayit.ui", fout)