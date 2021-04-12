# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SUPORTE05\Documents\Meus Programas\apps\ASSISTENCIA TECNICA\UI\main.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import re
import sql
from time import sleep
from estoque import Estoque
from usuarios import Usuarios
from tecnicos import Tecnicos
from clientes import Clientes
from produtos import Produtos
from usuarios import Usuarios
from servicos import Servicos
from orcamentos import Orcamentos
from categorias import Categorias
from fornecedores import Fornecedores
from PyQt5 import QtCore, QtGui, QtWidgets
from meus_dados import Meus_dados
from mensangens_sistema import Mensagens_sistema
from clasula_contratos import clasula_contratos
from seleciona_logo import Seleciona_logo



class Assistencia(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1180, 732)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/technician.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QToolTip {\n"
"    border: 2px solid darkkhaki;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"    opacity: 200;    \n"
"    color: rgb(1, 92, 146);\n"
"    background-color: rgb(188, 230, 254);    \n"
"    border-color: rgb(1, 92, 146);\n"
"}\n"
"\n"
"#principal{    \n"
"    background-image: url(:/img/hardware-e1535121140229.jpg);\n"
"}\n"
"\n"
"QWidget{        \n"
"    background-color: rgb(188, 230, 254, 150);\n"
"}\n"
"\n"
"#ferramentas{    \n"
"    background-color: qlineargradient(spread:pad, x1:0.778, y1:1, x2:1, y2:0, stop:0 rgba(1, 92, 146, 255), stop:1 rgba(188, 230, 254, 200));\n"
"    border: 1px;\n"
"    border-color: rgb(188, 230, 254);\n"
"}\n"
"\n"
"#ferramentas QToolButton{\n"
"    color: rgb(255, 255, 255);\n"
"    font: 10pt \"Franklin Gothic Heavy\";    \n"
"}\n"
"\n"
"#ferramentas QGroupBox{\n"
"    border:0px;\n"
"}\n"
"\n"
"QToolButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    margin: 0px 50px 0px 50px;    \n"
"    padding: 0px 100px 0px 100px;    \n"
"}\n"
"\n"
"QToolButton:hover:pressed{\n"
"    background-color: rgb(84, 167, 216);\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"    background-color: rgb(1, 92, 146);\n"
"}\n"
"\n"
"#grupo_operacao, #grupo_usuario{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"#grupo_painel{    \n"
"    background-color: rgb(188, 230, 254, 150);\n"
"}\n"
"\n"
"#grupo_painel, #servicos, #grupo_produtos, QMenu, QMenuBar, QScrollArea{\n"
"    border: 1px;\n"
"    border-color: rgb(1, 92, 146);\n"
"    font: 87 10pt \"Arial Black\";    \n"
"    color: rgb(1, 92, 146);\n"
"}\n"
"\n"
"#servicos, #produtos{\n"
"    background-color: rgb(68, 154, 202, 100);\n"
"}\n"
"\n"
"#grupo_operacao{             \n"
"    color: rgb(1, 92, 146);\n"
"    font: 87 12pt \"Arial Black\";\n"
"}\n"
"\n"
"#grupo_tabela{\n"
"    border: 1px;\n"
"    border-radius: 8px;        \n"
"    background-color: rgba(1, 92, 146, 0);\n"
"}\n"
"#tabela::item:hover {    \n"
"    background-color: rgb(255, 255, 127);\n"
"}\n"
"\n"
"#busca{\n"
"    border-radius: 5px;        \n"
"    background-color: rgb(68, 154, 202, 150);\n"
"    margin:0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"#bt_busca, #in_busca{\n"
"    background-color: rgb(68, 154, 202);    \n"
"    color: rgb(188, 230, 254);\n"
"    border: 0px;\n"
"    height: 50px;\n"
"    margin:0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"#bt_busca:hover:pressed{\n"
"    background-color: rgb(84, 167, 216);\n"
"}\n"
"\n"
"#bt_busca:hover{\n"
"    background-color: rgb(1, 92, 146);\n"
"}\n"
"\n"
"Line{\n"
"    background-color: rgb(68, 154, 202);\n"
"}\n"
"\n"
"#tabela{\n"
"    background-color: rgb(68, 154, 202, 200);\n"
"    border: 1px;\n"
"}\n"
"\n"
"#tabela::item:selected{\n"
"    background-color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"#tabela:item{    \n"
"    background-color: rgb(136, 204, 245);\n"
"}\n"
"\n"
"#tabela::indicator:unchecked {\n"
"    background-color: rgb(68, 154, 202);\n"
"}\n"
"\n"
"#titulo{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.principal = QtWidgets.QWidget(MainWindow)
        self.principal.setObjectName("principal")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.principal)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_2 = QtWidgets.QFrame(self.principal)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(327, 0))
        self.frame.setMaximumSize(QtCore.QSize(330, 16777215))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(9, 4, 9, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ferramentas = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ferramentas.sizePolicy().hasHeightForWidth())
        self.ferramentas.setSizePolicy(sizePolicy)
        self.ferramentas.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ferramentas.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ferramentas.setTitle("")
        self.ferramentas.setAlignment(QtCore.Qt.AlignCenter)
        self.ferramentas.setFlat(False)
        self.ferramentas.setCheckable(False)
        self.ferramentas.setObjectName("ferramentas")
        self._2 = QtWidgets.QVBoxLayout(self.ferramentas)
        self._2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self._2.setContentsMargins(0, 0, 0, 0)
        self._2.setSpacing(6)
        self._2.setObjectName("_2")
        self.grupo_usuario = QtWidgets.QGroupBox(self.ferramentas)
        self.grupo_usuario.setMaximumSize(QtCore.QSize(16777215, 100))
        self.grupo_usuario.setAutoFillBackground(False)
        self.grupo_usuario.setTitle("")
        self.grupo_usuario.setFlat(False)
        self.grupo_usuario.setCheckable(False)
        self.grupo_usuario.setObjectName("grupo_usuario")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.grupo_usuario)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.usuarios = QtWidgets.QToolButton(self.grupo_usuario)
        self.usuarios.setAcceptDrops(False)
        self.usuarios.setAutoFillBackground(False)
        self.usuarios.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/man.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.usuarios.setIcon(icon1)
        self.usuarios.setIconSize(QtCore.QSize(75, 63))
        self.usuarios.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.usuarios.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.usuarios.setAutoRaise(True)
        self.usuarios.setObjectName("usuarios")
        self.verticalLayout_3.addWidget(self.usuarios)
        self._2.addWidget(self.grupo_usuario)
        self.line = QtWidgets.QFrame(self.ferramentas)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self._2.addWidget(self.line)
        self.clientes = QtWidgets.QToolButton(self.ferramentas)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/consultation.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clientes.setIcon(icon2)
        self.clientes.setIconSize(QtCore.QSize(48, 48))
        self.clientes.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.clientes.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.clientes.setAutoRaise(True)
        self.clientes.setArrowType(QtCore.Qt.NoArrow)
        self.clientes.setObjectName("clientes")
        self._2.addWidget(self.clientes)
        self.produtos = QtWidgets.QToolButton(self.ferramentas)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/box.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.produtos.setIcon(icon3)
        self.produtos.setIconSize(QtCore.QSize(48, 48))
        self.produtos.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.produtos.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.produtos.setAutoRaise(True)
        self.produtos.setArrowType(QtCore.Qt.NoArrow)
        self.produtos.setObjectName("produtos")
        self._2.addWidget(self.produtos)
        self.tecnicos = QtWidgets.QToolButton(self.ferramentas)
        self.tecnicos.setStyleSheet("")
        self.tecnicos.setIcon(icon)
        self.tecnicos.setIconSize(QtCore.QSize(48, 48))
        self.tecnicos.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.tecnicos.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.tecnicos.setAutoRaise(True)
        self.tecnicos.setArrowType(QtCore.Qt.NoArrow)
        self.tecnicos.setObjectName("tecnicos")
        self._2.addWidget(self.tecnicos)
        self.ordem_servicos = QtWidgets.QToolButton(self.ferramentas)
        self.ordem_servicos.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/design.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ordem_servicos.setIcon(icon4)
        self.ordem_servicos.setIconSize(QtCore.QSize(48, 48))
        self.ordem_servicos.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.ordem_servicos.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.ordem_servicos.setAutoRaise(True)
        self.ordem_servicos.setArrowType(QtCore.Qt.NoArrow)
        self.ordem_servicos.setObjectName("ordem_servicos")
        self._2.addWidget(self.ordem_servicos)
        self.fornecedores = QtWidgets.QToolButton(self.ferramentas)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/operator.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fornecedores.setIcon(icon5)
        self.fornecedores.setIconSize(QtCore.QSize(48, 48))
        self.fornecedores.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.fornecedores.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.fornecedores.setAutoRaise(True)
        self.fornecedores.setArrowType(QtCore.Qt.NoArrow)
        self.fornecedores.setObjectName("fornecedores")
        self._2.addWidget(self.fornecedores)
        self.line_2 = QtWidgets.QFrame(self.ferramentas)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self._2.addWidget(self.line_2)
        self.grupo_operacao = QtWidgets.QGroupBox(self.ferramentas)
        self.grupo_operacao.setMaximumSize(QtCore.QSize(16777215, 71))
        self.grupo_operacao.setAlignment(QtCore.Qt.AlignCenter)
        self.grupo_operacao.setObjectName("grupo_operacao")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.grupo_operacao)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sair = QtWidgets.QToolButton(self.grupo_operacao)
        self.sair.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/shutdown.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sair.setIcon(icon6)
        self.sair.setIconSize(QtCore.QSize(36, 36))
        self.sair.setAutoRaise(True)
        self.sair.setObjectName("sair")
        self.horizontalLayout_2.addWidget(self.sair)
        self._2.addWidget(self.grupo_operacao)
        self.verticalLayout.addWidget(self.ferramentas)
        self.horizontalLayout_3.addWidget(self.frame)
        self.grupo_painel = QtWidgets.QGroupBox(self.frame_2)
        self.grupo_painel.setMinimumSize(QtCore.QSize(800, 0))
        self.grupo_painel.setTitle("")
        self.grupo_painel.setObjectName("grupo_painel")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.grupo_painel)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.grupo_produtos = QtWidgets.QGroupBox(self.grupo_painel)
        self.grupo_produtos.setTitle("")
        self.grupo_produtos.setFlat(False)
        self.grupo_produtos.setObjectName("grupo_produtos")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.grupo_produtos)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.busca = QtWidgets.QGroupBox(self.grupo_produtos)
        self.busca.setTitle("")
        self.busca.setObjectName("busca")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.busca)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.in_busca = QtWidgets.QLineEdit(self.busca)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.in_busca.setFont(font)
        self.in_busca.setAlignment(QtCore.Qt.AlignCenter)
        self.in_busca.setClearButtonEnabled(True)
        self.in_busca.setObjectName("in_busca")
        self.horizontalLayout_4.addWidget(self.in_busca)
        self.line_3 = QtWidgets.QFrame(self.busca)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_4.addWidget(self.line_3)
        spacerItem = QtWidgets.QSpacerItem(6, 2, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.bt_busca = QtWidgets.QToolButton(self.busca)
        self.bt_busca.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/find-my-friend.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_busca.setIcon(icon7)
        self.bt_busca.setIconSize(QtCore.QSize(40, 40))
        self.bt_busca.setObjectName("bt_busca")
        self.horizontalLayout_4.addWidget(self.bt_busca)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.busca)
        self.grupo_tabela = QtWidgets.QGroupBox(self.grupo_produtos)
        self.grupo_tabela.setTitle("")
        self.grupo_tabela.setObjectName("grupo_tabela")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.grupo_tabela)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.scrollArea = QtWidgets.QScrollArea(self.grupo_tabela)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 755, 474))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabela = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tabela.setObjectName("tabela")
        self.tabela.setColumnCount(0)
        self.tabela.setRowCount(0)
        self.verticalLayout_5.addWidget(self.tabela)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_6.addWidget(self.scrollArea)
        self.verticalLayout_2.addWidget(self.grupo_tabela)
        self.verticalLayout_4.addWidget(self.grupo_produtos)
        spacerItem1 = QtWidgets.QSpacerItem(72, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_3.addWidget(self.grupo_painel)
        self.verticalLayout_6.addWidget(self.frame_2)
        self.barra_status = QtWidgets.QFrame(self.principal)
        self.barra_status.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_status.setObjectName("barra_status")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.barra_status)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.minimizar = QtWidgets.QPushButton(self.barra_status)
        self.minimizar.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/img/minimizi.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizar.setIcon(icon8)
        self.minimizar.setFlat(True)
        self.minimizar.setObjectName("minimizar")
        self.horizontalLayout.addWidget(self.minimizar)
        self.restaurar = QtWidgets.QPushButton(self.barra_status)
        self.restaurar.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/img/maximize.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restaurar.setIcon(icon9)
        self.restaurar.setFlat(True)
        self.restaurar.setObjectName("restaurar")
        self.horizontalLayout.addWidget(self.restaurar)
        self.fechar_b = QtWidgets.QPushButton(self.barra_status)
        self.fechar_b.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/img/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fechar_b.setIcon(icon10)
        self.fechar_b.setFlat(True)
        self.fechar_b.setObjectName("fechar_b")
        self.horizontalLayout.addWidget(self.fechar_b)
        self.titulo = QtWidgets.QLabel(self.barra_status)
        self.titulo.setMaximumSize(QtCore.QSize(16777215, 900))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.titulo.setFont(font)
        self.titulo.setScaledContents(False)
        self.titulo.setWordWrap(False)
        self.titulo.setOpenExternalLinks(False)
        self.titulo.setObjectName("titulo")
        self.horizontalLayout.addWidget(self.titulo)
        spacerItem2 = QtWidgets.QSpacerItem(19, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.negativo = QtWidgets.QLabel(self.barra_status)
        self.negativo.setMaximumSize(QtCore.QSize(20, 20))
        self.negativo.setText("")
        self.negativo.setTextFormat(QtCore.Qt.PlainText)
        self.negativo.setPixmap(QtGui.QPixmap(":/img/green-led-on.png"))
        self.negativo.setAlignment(QtCore.Qt.AlignCenter)
        self.negativo.setObjectName("negativo")
        self.horizontalLayout.addWidget(self.negativo)
        self.positivo = QtWidgets.QLabel(self.barra_status)
        self.positivo.setMaximumSize(QtCore.QSize(20, 20))
        self.positivo.setText("")
        self.positivo.setTextFormat(QtCore.Qt.PlainText)
        self.positivo.setPixmap(QtGui.QPixmap(":/img/led-red-on.png"))
        self.positivo.setAlignment(QtCore.Qt.AlignCenter)
        self.positivo.setObjectName("positivo")
        self.horizontalLayout.addWidget(self.positivo)
        self.data_hora = QtWidgets.QDateTimeEdit(self.barra_status)
        self.data_hora.setEnabled(True)
        self.data_hora.setReadOnly(True)
        self.data_hora.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.data_hora.setAccelerated(False)
        self.data_hora.setProperty("showGroupSeparator", False)
        self.data_hora.setObjectName("data_hora")
        self.horizontalLayout.addWidget(self.data_hora)
        self.verticalLayout_6.addWidget(self.barra_status)
        MainWindow.setCentralWidget(self.principal)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1180, 24))
        self.menubar.setObjectName("menubar")
        self.menuCADASTROS = QtWidgets.QMenu(self.menubar)
        self.menuCADASTROS.setObjectName("menuCADASTROS")
        self.menuEQUIPAMENTOS = QtWidgets.QMenu(self.menubar)
        self.menuEQUIPAMENTOS.setObjectName("menuEQUIPAMENTOS")
        self.menuSERVI_OS_OR_AMENTO = QtWidgets.QMenu(self.menubar)
        self.menuSERVI_OS_OR_AMENTO.setObjectName("menuSERVI_OS_OR_AMENTO")
        self.menuSOBRE = QtWidgets.QMenu(self.menubar)
        self.menuSOBRE.setObjectName("menuSOBRE")
        self.menuESTOQUE = QtWidgets.QMenu(self.menubar)
        self.menuESTOQUE.setObjectName("menuESTOQUE")
        MainWindow.setMenuBar(self.menubar)
        self.cadastro_cliente = QtWidgets.QAction(MainWindow)
        self.cadastro_cliente.setIcon(icon2)
        self.cadastro_cliente.setObjectName("cadastro_cliente")
        self.actionPRODUTOS = QtWidgets.QAction(MainWindow)
        self.actionPRODUTOS.setObjectName("actionPRODUTOS")
        self.cadastro_tecnico = QtWidgets.QAction(MainWindow)
        self.cadastro_tecnico.setIcon(icon)
        self.cadastro_tecnico.setObjectName("cadastro_tecnico")
        self.cadastro_fornecedor = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/img/service.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cadastro_fornecedor.setIcon(icon11)
        self.cadastro_fornecedor.setObjectName("cadastro_fornecedor")
        self.cadastrar_produto = QtWidgets.QAction(MainWindow)
        self.cadastrar_produto.setIcon(icon3)
        self.cadastrar_produto.setObjectName("cadastrar_produto")
        self.cadastro_software = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/img/code.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cadastro_software.setIcon(icon12)
        self.cadastro_software.setObjectName("cadastro_software")
        self.gerar_ordem_servico = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/img/plan.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gerar_ordem_servico.setIcon(icon13)
        self.gerar_ordem_servico.setObjectName("gerar_ordem_servico")
        self.termos_responsabilidade = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/img/gdpr.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.termos_responsabilidade.setIcon(icon14)
        self.termos_responsabilidade.setObjectName("termos_responsabilidade")
        self.ajuda = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/img/horse-about-to-attack-side-view.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ajuda.setIcon(icon15)
        self.ajuda.setObjectName("ajuda")
        self.tipo_servico = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/img/folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tipo_servico.setIcon(icon16)
        self.tipo_servico.setObjectName("tipo_servico")
        self.cadastro_usuarios = QtWidgets.QAction(MainWindow)
        self.cadastro_usuarios.setIcon(icon1)
        self.cadastro_usuarios.setObjectName("cadastro_usuarios")
        self.entrada_estoque = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/img/stock-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.entrada_estoque.setIcon(icon17)
        self.entrada_estoque.setObjectName("entrada_estoque")
        self.configuracoes = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/img/gear-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.configuracoes.setIcon(icon18)
        self.configuracoes.setObjectName("configuracoes")
        self.categorias = QtWidgets.QAction(MainWindow)
        self.categorias.setIcon(icon4)
        self.categorias.setObjectName("categorias")
        self.cadastro_servicos = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/img/customer-support.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cadastro_servicos.setIcon(icon19)
        self.cadastro_servicos.setObjectName("cadastro_servicos")
        self.gerenciar_estoque = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/img/warehouse.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gerenciar_estoque.setIcon(icon20)
        self.gerenciar_estoque.setObjectName("gerenciar_estoque")
        self.contrato_uso = QtWidgets.QAction(MainWindow)
        self.contrato_uso.setIcon(icon13)
        self.contrato_uso.setObjectName("contrato_uso")
        self.meus_dados = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/img/login.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.meus_dados.setIcon(icon21)
        self.meus_dados.setObjectName("meus_dados")
        self.mensagens_sistema = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/img/letter.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mensagens_sistema.setIcon(icon22)
        self.mensagens_sistema.setObjectName("mensagens_sistema")
        self.alterar_logo = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/img/logo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alterar_logo.setIcon(icon23)
        self.alterar_logo.setObjectName("alterar_logo")
        self.menuCADASTROS.addAction(self.cadastro_cliente)
        self.menuCADASTROS.addAction(self.cadastro_tecnico)
        self.menuCADASTROS.addAction(self.cadastro_fornecedor)
        self.menuCADASTROS.addAction(self.cadastro_usuarios)
        self.menuEQUIPAMENTOS.addAction(self.cadastrar_produto)
        self.menuEQUIPAMENTOS.addAction(self.cadastro_servicos)
        self.menuEQUIPAMENTOS.addAction(self.categorias)
        self.menuSERVI_OS_OR_AMENTO.addAction(self.gerar_ordem_servico)
        self.menuSERVI_OS_OR_AMENTO.addAction(self.termos_responsabilidade)
        self.menuSOBRE.addAction(self.ajuda)
        self.menuSOBRE.addAction(self.configuracoes)
        self.menuSOBRE.addAction(self.contrato_uso)
        self.menuSOBRE.addAction(self.meus_dados)
        self.menuSOBRE.addAction(self.mensagens_sistema)
        self.menuSOBRE.addAction(self.alterar_logo)
        self.menuESTOQUE.addAction(self.gerenciar_estoque)
        self.menubar.addAction(self.menuCADASTROS.menuAction())
        self.menubar.addAction(self.menuEQUIPAMENTOS.menuAction())
        self.menubar.addAction(self.menuESTOQUE.menuAction())
        self.menubar.addAction(self.menuSERVI_OS_OR_AMENTO.menuAction())
        self.menubar.addAction(self.menuSOBRE.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ASSISTENCIA TECNICA DE MANUNTEÇÃO"))
        self.usuarios.setToolTip(_translate("MainWindow", "<html><head/><body><p>GERENCIE OS USUÁRIOS DO SISTEMA</p></body></html>"))
        self.clientes.setToolTip(_translate("MainWindow", "<html><head/><body><p>GERENCIE OS CLIENTES DO SISTEMA</p></body></html>"))
        self.clientes.setText(_translate("MainWindow", "CLIENTES"))
        self.produtos.setToolTip(_translate("MainWindow", "<html><head/><body><p>GERENCIE OS PRODUTOS DO SISTEMA</p></body></html>"))
        self.produtos.setText(_translate("MainWindow", "EQUIPAMENTOS"))
        self.tecnicos.setToolTip(_translate("MainWindow", "<html><head/><body><p>GERENCIE OS TENICOS DO SISTEMA</p></body></html>"))
        self.tecnicos.setText(_translate("MainWindow", "TECNICOS"))
        self.ordem_servicos.setToolTip(_translate("MainWindow", "<html><head/><body><p>GERENCIE AS ORDENS DE SERVIÇOS</p><p><br/></p></body></html>"))
        self.ordem_servicos.setText(_translate("MainWindow", "ORDEM SERVIÇOS"))
        self.fornecedores.setToolTip(_translate("MainWindow", "<html><head/><body><p>GERENCIE OS FORNECEDORES DO SISTEMA</p></body></html>"))
        self.fornecedores.setText(_translate("MainWindow", "FORNECEDORES"))
        self.grupo_operacao.setTitle(_translate("MainWindow", "OPERAÇÃOES"))
        self.sair.setToolTip(_translate("MainWindow", "<html><head/><body><p>SAIA DO SISTEMA</p></body></html>"))
        self.in_busca.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">FAÇA BUSCA POR CLIENTES, SERVIÇOS OU PRODUTOS!</span></p></body></html>"))
        self.in_busca.setPlaceholderText(_translate("MainWindow", "CLIENTES ... SERVIÇOS ... PRODUTOS..."))
        self.bt_busca.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">FAÇA BUSCA POR CLIENTES, SERVIÇOS OU PRODUTOS!</span></p></body></html>"))
        self.minimizar.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">ESCONDE A APLICAÇÃO</span></p></body></html>"))
        self.restaurar.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">RESTAURA A APLICAÇÃO</span></p></body></html>"))
        self.fechar_b.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">FECHA A APLICAÇÃO</span></p></body></html>"))
        self.titulo.setText(_translate("MainWindow", "ASSISTENCIA TECNICA DE MANUNTEÇÃO - GREGHONO@GMAIL.COM"))
        self.data_hora.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy HH:mm:ss"))
        self.menuCADASTROS.setTitle(_translate("MainWindow", "CADASTROS"))
        self.menuEQUIPAMENTOS.setTitle(_translate("MainWindow", "PRODUTOS/SERVIÇOS"))
        self.menuSERVI_OS_OR_AMENTO.setTitle(_translate("MainWindow", "SERVIÇOS/ORÇAMENTO"))
        self.menuSOBRE.setTitle(_translate("MainWindow", "SOBRE"))
        self.menuESTOQUE.setTitle(_translate("MainWindow", "ESTOQUE"))
        self.cadastro_cliente.setText(_translate("MainWindow", "CLIENTES"))
        self.actionPRODUTOS.setText(_translate("MainWindow", "PRODUTOS"))
        self.cadastro_tecnico.setText(_translate("MainWindow", "TECNICOS"))
        self.cadastro_fornecedor.setText(_translate("MainWindow", "FORNECEDORES"))
        self.cadastrar_produto.setText(_translate("MainWindow", "CADASTRO EQUIPAMENTOS"))
        self.cadastro_software.setText(_translate("MainWindow", "CADASTROS SOFTWARES"))
        self.gerar_ordem_servico.setText(_translate("MainWindow", "GERAR ORDEM SERVIÇOS"))
        self.termos_responsabilidade.setText(_translate("MainWindow", "TERMOS CONTRATOS"))
        self.ajuda.setText(_translate("MainWindow", "AJUDA"))
        self.tipo_servico.setText(_translate("MainWindow", "TIPO SERVIÇOS"))
        self.cadastro_usuarios.setText(_translate("MainWindow", "USUÁRIOS"))
        self.entrada_estoque.setText(_translate("MainWindow", "ENTRADAS"))
        self.configuracoes.setText(_translate("MainWindow", "CONFIGURAÇÕES"))
        self.categorias.setText(_translate("MainWindow", "CATEGORIAS"))
        self.cadastro_servicos.setText(_translate("MainWindow", "CADASTRO SERVIÇOS"))
        self.gerenciar_estoque.setText(_translate("MainWindow", "GERENCIAR ESTOQUE"))
        self.contrato_uso.setText(_translate("MainWindow", "CONTRATO DE USO"))
        self.meus_dados.setText(_translate("MainWindow", "MEUS DADOS"))
        self.mensagens_sistema.setText(_translate("MainWindow", "MENSAGENS DO SISTEMA"))
        self.alterar_logo.setText(_translate("MainWindow", "ALTERAR LOGO"))
        self.carregar_janela(MainWindow)

    Janela = None
    def carregar_janela(self, MainWindow):
        self.Janela = MainWindow
        self.carregar_variaveis()
        self.carregar_data_hora()
        self.eventos()
        self.propriedades_janela(MainWindow)
        self.pegar_propriedades_sistema()


    def pegar_propriedades_sistema(self):
        self.contador = 0
        self.rolatem_mensagem = QtCore.QTimer()
        vencimento = sql.SQL().pegar_vencimento_cliente()[0][0].split('-')

        vencimento = vencimento[2] +"/"+ vencimento[1] +"/"+ vencimento[0]
        self.mensagem = re.sub('\n', '', sql.SQL().pegar_mensagem_padrao()[0][0]).upper() + " ||| LICENÇA VALE ATÉ ({}) ||| ".format(vencimento)
        self.rolatem_mensagem.timeout.connect(self.rolar_mensagem)
        self.rolatem_mensagem.start(500)


    def rolar_mensagem(self):
        if(len(self.mensagem) != self.contador): self.contador += 1
        else: self.contador = 0
        self.titulo.setText(self.mensagem[self.contador:] + self.mensagem[:self.contador])
        self.Janela.setWindowTitle(self.mensagem[self.contador:] + self.mensagem[:self.contador])


    def propriedades_janela(self, Janela):
        self.Janela.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Janela.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.fechar_b.clicked.connect(self.Janela.close)
        self.minimizar.clicked.connect(self.Janela.showMinimized)
        self.restaurar.clicked.connect(self.maxi_janela)
        self.Janela.mouseDoubleClickEvent = self.mouseDoubleClickEvent
        self.Janela.mousePressEvent = self.mousePressEvent
        self.Janela.mouseMoveEvent = self.mouseMoveEvent


    def eventos(self):
        self.sair.clicked.connect(self.fechar_sistema)
        self.usuarios.clicked.connect(self.cadastro_usuario)
        self.cadastro_usuarios.triggered.connect(self.cadastro_usuario)
        self.clientes.clicked.connect(self.cadastro_clientes)
        self.cadastro_cliente.triggered.connect(self.cadastro_clientes)
        self.produtos.clicked.connect(self.cadastro_produtos)
        self.cadastrar_produto.triggered.connect(self.cadastro_produtos)
        self.tecnicos.clicked.connect(self.cadastro_tecnicos)
        self.cadastro_tecnico.triggered.connect(self.cadastro_tecnicos)
        self.ordem_servicos.clicked.connect(self.cadastrar_ordem_servico)
        self.gerar_ordem_servico.triggered.connect(self.cadastrar_ordem_servico)
        self.fornecedores.clicked.connect(self.cadastrar_fornecedores)
        self.cadastro_fornecedor.triggered.connect(self.cadastrar_fornecedores)
        self.categorias.triggered.connect(self.cadastrar_categorias)
        self.termos_responsabilidade.triggered.connect(self.cadastrar_termos_responsabilidade)
        self.ajuda.triggered.connect(self.ajudar)
        self.configuracoes.triggered.connect(self.configuracao)
        self.cadastro_servicos.triggered.connect(self.cadastrar_servicos)
        self.gerenciar_estoque.triggered.connect(self.cadastrar_estoque)
        self.meus_dados.triggered.connect(self.abrir_meus_dados)
        self.titulo.mouseDoubleClickEvent = self.abrir_mensagens
        self.mensagens_sistema.triggered.connect(self.abrir_mensagens)
        self.contrato_uso.triggered.connect(self.abrir_contrato_uso)
        self.alterar_logo.triggered.connect(self.alterar_logo_empresa)


    def alterar_logo_empresa(self):
        self.Form = QtWidgets.QDialog()
        self.ui = Seleciona_logo()
        self.ui.setupUi(self.Form)
        self.Form.exec()

    def abrir_contrato_uso(self):
        self.Form = QtWidgets.QDialog()
        self.ui = clasula_contratos()
        self.ui.setupUi(self.Form)
        self.Form.exec()

    def abrir_mensagens(self, event):
        self.Form = QtWidgets.QDialog()
        self.ui = Mensagens_sistema()
        self.ui.setupUi(self.Form)
        self.Form.exec()


    def abrir_meus_dados(self):
        self.Form = QtWidgets.QDialog()
        self.ui = Meus_dados()
        self.ui.setupUi(self.Form)
        self.Form.exec()


    def cadastrar_estoque(self):
        self.Form = QtWidgets.QDialog()
        self.ui = Estoque()
        self.ui.setupUi(self.Form)
        self.Form.exec()


    def configuracao(self): print("CONTIGUÇÃOI")


    def ajudar(self): print("AJUDA")


    def cadastrar_termos_responsabilidade(self): print("cadastrar_termos_responsabilidade")


    def cadastrar_servicos(self):
        self.Form = QtWidgets.QDialog()
        self.ui = Servicos()
        self.ui.setupUi(self.Form)
        self.Form.exec()

    def cadastrar_categorias(self):
        self.Form = QtWidgets.QDialog()
        self.ui = Categorias()
        self.ui.setupUi(self.Form)
        self.Form.exec()


    def cadastrar_fornecedores(self):
        self.Form = QtWidgets.QDialog()
        self.ui = Fornecedores()
        self.ui.setupUi(self.Form)
        self.Form.exec()

    def cadastro_usuario(self):
        self.Form = QtWidgets.QDialog()
        self.ui = Usuarios()
        self.ui.setupUi(self.Form)
        self.Form.exec()

    def cadastro_clientes(self):
        self.Form = QtWidgets.QDialog()
        self.ui = Clientes()
        self.ui.setupUi(self.Form)
        self.Form.exec()


    def cadastro_produtos(self):
        self.Form = QtWidgets.QDialog()
        self.ui = Produtos()
        self.ui.setupUi(self.Form)
        self.Form.exec()


    def cadastro_tecnicos(self):
        self.Form = QtWidgets.QDialog()
        self.ui = Tecnicos()
        self.ui.setupUi(self.Form)
        self.Form.exec()


    def cadastrar_ordem_servico(self):
        self.Form = QtWidgets.QDialog()
        self.ui = Orcamentos()
        self.ui.setupUi(self.Form)
        self.Form.exec()


    def carregar_variaveis(self):
        self.titulo_t = "SISTEMA MANNUNTEÇÃO"


    def fechar_sistema(self):
        msg = QtWidgets.QMessageBox.question(None, self.titulo_t, "DESEJA SAIR DO SISTEMA?")
        if(msg == QtWidgets.QMessageBox.Yes): self.Janela.close()


    def carregar_data_hora(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.carregar_data_hora)
        self.timer.start(1000)
        time = QtCore.QDateTime.currentDateTime()
        self.data_hora.setDateTime(time)
        if(int(time.toString("s")) % 2 == 0):
            self.positivo.setPixmap(QtGui.QPixmap(":/img/green-led-on.png"))
            self.negativo.setPixmap(QtGui.QPixmap(":/img/led-red-on.png"))
        else:
            self.positivo.setPixmap(QtGui.QPixmap(":/img/led-red-on.png"))
            self.negativo.setPixmap(QtGui.QPixmap(":/img/green-led-on.png"))


    def mouseDoubleClickEvent(self, event):  self.maxi_janela()


    def mousePressEvent(self, event): self.oldPos = event.globalPos()


    def closeEvent(self, event): self.close()


    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint (event.globalPos() - self.oldPos)
        self.Janela.move(self.Janela.x() + delta.x(), self.Janela.y() + delta.y())
        self.oldPos = event.globalPos()


    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.Janela.close()
        if e.key() == QtCore.Qt.Key_F11:
            if self.Janela.isMaximized():
                self.Janela.showNormal()
                self.max_c = True
            else:
                self.showMaximized()


    max_c = True
    def maxi_janela(self):
        if(self.max_c):
            self.Janela.showMaximized()
            self.max_c = False
        else:
            self.Janela.showNormal()
            self.max_c = True


import recursos


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Assistencia()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
