import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtTest,QtCore
import lexico
from sintactico import Sintactico
from semantico import Semantico
class Ventana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('ventana.ui',self)
        self.pushButton.clicked.connect(self.procesar) 
        self.setWindowTitle('Nuevo archivo')
        self._tokens = list()

    def procesar(self):
        archivo = open('informacion.txt', 'w')
        archivo.write(self.textEdit.toPlainText())
        archivo.close()
        self.analizador=lexico.Lexico()
        self._tokens = self.analizador._tokens
        print(self._tokens)
        sintactico = Sintactico(len(self._tokens)-1)
        for token in self._tokens:
            sintactico.comparar(token[0],token[1])
        semantico = Semantico(sintactico.arbol)
        semantico.createTables()
        semantico.checkErrors()
          

app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
app.exec_()