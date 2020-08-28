import sys
import os
import json

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                            QPushButton, QLabel, QLineEdit, QTabBar,
                            QFrame,QStackedLayout)
from PyQt5.QtGui import QIcon, QWindow, QImage
from PyQt5.QtCore import *


class BarraDirecciones(QLineEdit): # AddressBar()
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, e):
        self.selectAll()


class App(QFrame):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Navegador Web')
        self.CrearApp()
        self.setBaseSize(1366, 768)

    def CrearApp(self): # CreateApp()
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)

        #- crear pestañas
        self.tabbar = QTabBar(movable=True, tabsClosable=True)
        self.tabbar.tabCloseRequested.connect(self.CerrarTab)

        self.tabbar.addTab('Pestaña 1')
        self.tabbar.addTab('Pestaña 2')

        self.tabbar.setCurrentIndex(0)

        #- crear barra de direcciones
        self.Toolbar = QWidget()
        self.ToolbarLayout = QHBoxLayout()
        self.addressbar = BarraDirecciones()

        self.Toolbar.setLayout(self.ToolbarLayout)
        self.ToolbarLayout.addWidget(self.addressbar)

        self.layout.addWidget(self.tabbar)
        self.layout.addWidget(self.Toolbar)
        self.setLayout(self.layout)

        self.show()


    def CerrarTab(self, i): # CloseTab()
        self.tabbar.removeTab(i)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()

    sys.exit(app.exec_())



