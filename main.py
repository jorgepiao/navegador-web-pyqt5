import sys
import os
import json
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                            QPushButton, QLabel, QLineEdit, QTabBar,
                            QFrame,QStackedLayout)
from PyQt5.QtGui import QIcon, QWindow, QImage
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


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
        self.tabbar.tabBarClicked.connect(self.CambiarTab)

        self.tabbar.setCurrentIndex(0)

        #- seguimiento de pestañas
        self.cuentaTab = 0 #tabCount
        self.tabs = []

        #- crear barra de direcciones
        self.Toolbar = QWidget()
        self.ToolbarLayout = QHBoxLayout()
        self.addressbar = BarraDirecciones()

        self.Toolbar.setLayout(self.ToolbarLayout)
        self.ToolbarLayout.addWidget(self.addressbar)

        #- boton nueva pestaña
        self.botonAgregarTab = QPushButton('+') # AddTabButton
        self.botonAgregarTab.clicked.connect(self.AgregarTab)

        self.ToolbarLayout.addWidget(self.botonAgregarTab)
        
        #- establecer vista principal
        self.contenedor = QWidget() # container
        self.contenedor.layout = QStackedLayout()
        self.contenedor.setLayout(self.contenedor.layout)

        self.layout.addWidget(self.tabbar)
        self.layout.addWidget(self.Toolbar)
        self.layout.addWidget(self.contenedor)

        self.setLayout(self.layout)

        self.AgregarTab()

        self.show()


    def CerrarTab(self, i): # CloseTab()
        self.tabbar.removeTab(i)


    def AgregarTab(self): # AddTab
        i = self.cuentaTab

        self.tabs.append(QWidget())
        self.tabs[i].layout = QVBoxLayout()
        self.tabs[i].setObjectName('pestaña' + str(i))
        
        #- abrir webview
        self.tabs[i].content = QWebEngineView()
        self.tabs[i].content.load(QUrl.fromUserInput('http://google.com'))

        #- agregar webview al diseño de pestañas (layout)
        self.tabs[i].layout.addWidget(self.tabs[i].content)

        #- establecer pestaña top de [] al diseño (layout)
        self.tabs[i].setLayout(self.tabs[i].layout)

        #- agregar pestaña al top al widget apilado
        self.contenedor.layout.addWidget(self.tabs[i])
        self.contenedor.layout.setCurrentWidget(self.tabs[i])

        #- establecer la pestaña al tope de la pantalla
        self.tabbar.addTab('Nueva pestaña')
        self.tabbar.setTabData(i, 'tab' + str(i))
        self.tabbar.setCurrentIndex(i)

        self.cuentaTab += 1


    def CambiarTab(self, i):
        tab_dato = self.tabbar.tabData(i)
        print('tab:', tab_dato)

        tab_contenido = self.findChild(QWidget, tab_dato)
        self.contenedor.layout.setCurrentWidget(tab_contenido)
        # self.contenedor.layout.setCurrentWidget(self.tabs[i])



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()

    sys.exit(app.exec_())



