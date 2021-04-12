# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SUPORTE05\Documents\Meus Programas\apps\ASSISTENCIA TECNICA\UI\orcamentos.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import sql
from produtos import Produtos
from buscao_servicos import Busca_servico
from buscao_produtos import Busca_produto
from PyQt5 import QtCore, QtGui, QtWidgets


class Orcamentos(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1249, 625)
        Form.setMinimumSize(QtCore.QSize(1249, 625))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/technician.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QToolTip {\n"
"    border: 2px solid darkkhaki;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"    opacity: 200;    \n"
"    color: rgb(1, 92, 146);\n"
"    background-color: rgb(188, 230, 254);    \n"
"    border-color: rgb(1, 92, 146);\n"
"}\n"
"\n"
"#tabela_saida{    \n"
"    background-color: rgb(255, 200, 189);\n"
"}\n"
"\n"
"#tabela_entrada{    \n"
"    background-color: rgb(233, 255, 229);\n"
"}\n"
"\n"
"#principal{\n"
"    background-image: url(:/img/ordem.jpg);\n"
"}\n"
"\n"
"QFrame, QGroupBox{\n"
"    border: 1px;    \n"
"    border-color: rgb(188, 230, 254);\n"
"    color: rgb(1, 92, 146);\n"
"    font: 10pt \"Franklin Gothic Heavy\";    \n"
"}\n"
"\n"
"QWidget{        \n"
"    background-color: rgb(188, 230, 254, 200);\n"
"}\n"
"\n"
"QToolButton{\n"
"    color: rgb(255, 255, 255);\n"
"    font: 10pt \"Franklin Gothic Heavy\";    \n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    margin: 0% 50% 0% 50%;    \n"
"    padding:0% 50% 0% 50%;    \n"
"}\n"
"\n"
"QToolButton:hover:pressed{\n"
"    background-color: rgb(84, 167, 216);\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"    background-color: rgb(1, 92, 146);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit, QComboBox{                \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(84, 167, 216);\n"
"}\n"
"\n"
"QLineEdit:hover, QComboBox:hover{                \n"
"    background-color: rgb(1, 92, 146);\n"
"}\n"
"\n"
"QRadioButton{\n"
"    color: rgb(1, 92, 146);    \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QRadioButton::indicator:indeterminate:pressed{      \n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"#valores_situacao *{    \n"
"    font: 16pt \"MS Shell Dlg 2\";    \n"
"}\n"
"\n"
"#valores_situacao QComboBox{        \n"
"    font: 87 16pt \"Arial Black\";\n"
"}\n"
"\n"
"#valores_situacao QLabel{        \n"
"    font: 75 15pt \"Arial Black\";    \n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"#valor_total{    \n"
"    color: rgb(255, 0, 0);    \n"
"    font: 75 20pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLabel{\n"
"    background-color: rgba(255, 255, 255, 0);    \n"
"}\n"
"\n"
"#label_9{    \n"
"    font: 20pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"    background-color: rgb(68, 154, 202, 200);\n"
"    border: 1px;\n"
"}\n"
"\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"QTableWidget:item{    \n"
"    background-color: rgb(136, 204, 245);\n"
"}\n"
"\n"
"QTableWidget::indicator:unchecked {\n"
"    background-color: rgb(68, 154, 202);\n"
"}\n"
"\n"
"#frame_3{\n"
"    margin: 0% 0% 0% 0%;    \n"
"    padding:0% 0% 0% 0%;\n"
"}\n"
"\n"
"#descricao_produto{\n"
"    color: rgb(1, 92, 146);\n"
"}\n"
"\n"
"#label_10, #label_8, #label_11{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#valor_servicos, #valor_pecas{    \n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.principal = QtWidgets.QFrame(Form)
        self.principal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.principal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.principal.setObjectName("principal")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.principal)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.frame = QtWidgets.QFrame(self.principal)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_11.addWidget(self.label_7)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.groupBox_6 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.data_hora = QtWidgets.QDateTimeEdit(self.groupBox_6)
        self.data_hora.setEnabled(False)
        self.data_hora.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.data_hora.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.data_hora.setProperty("showGroupSeparator", False)
        self.data_hora.setObjectName("data_hora")
        self.horizontalLayout_13.addWidget(self.data_hora)
        self.horizontalLayout_14.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.data_entrada = QtWidgets.QDateEdit(self.groupBox_7)
        self.data_entrada.setCalendarPopup(True)
        self.data_entrada.setObjectName("data_entrada")
        self.horizontalLayout_10.addWidget(self.data_entrada)
        self.horizontalLayout_14.addWidget(self.groupBox_7)
        self.verticalLayout_12.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.equipamento = QtWidgets.QComboBox(self.groupBox_5)
        self.equipamento.setEditable(True)
        self.equipamento.setObjectName("equipamento")
        self.equipamento.addItem("")
        self.horizontalLayout_8.addWidget(self.equipamento)
        self.add_equipamento = QtWidgets.QPushButton(self.groupBox_5)
        self.add_equipamento.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/add-round-button-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_equipamento.setIcon(icon1)
        self.add_equipamento.setIconSize(QtCore.QSize(32, 23))
        self.add_equipamento.setFlat(True)
        self.add_equipamento.setObjectName("add_equipamento")
        self.horizontalLayout_8.addWidget(self.add_equipamento)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_12.addWidget(self.groupBox_5)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.cliente = QtWidgets.QComboBox(self.groupBox_2)
        self.cliente.setEditable(True)
        self.cliente.setObjectName("cliente")
        self.cliente.addItem("")
        self.horizontalLayout_15.addWidget(self.cliente)
        self.add_equipamento_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.add_equipamento_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/find-my-friend.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_equipamento_2.setIcon(icon2)
        self.add_equipamento_2.setIconSize(QtCore.QSize(32, 32))
        self.add_equipamento_2.setFlat(True)
        self.add_equipamento_2.setObjectName("add_equipamento_2")
        self.horizontalLayout_15.addWidget(self.add_equipamento_2)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_12.addWidget(self.groupBox_2)
        self.verticalLayout_12.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_7.addLayout(self.verticalLayout_12)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_16.setContentsMargins(-1, 18, -1, -1)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.descricao_produto = QtWidgets.QTextEdit(self.groupBox_3)
        self.descricao_produto.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.descricao_produto.setObjectName("descricao_produto")
        self.verticalLayout_16.addWidget(self.descricao_produto)
        self.horizontalLayout_7.addWidget(self.groupBox_3)
        self.verticalLayout_11.addLayout(self.horizontalLayout_7)
        self.verticalLayout_5.addLayout(self.verticalLayout_11)
        spacerItem = QtWidgets.QSpacerItem(198, 35, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.groupBox_8 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_8.setMinimumSize(QtCore.QSize(500, 0))
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_13.setContentsMargins(9, 18, -1, -1)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.tabela_orcamento = QtWidgets.QTableWidget(self.groupBox_8)
        self.tabela_orcamento.setAutoScrollMargin(16)
        self.tabela_orcamento.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabela_orcamento.setDragEnabled(False)
        self.tabela_orcamento.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabela_orcamento.setObjectName("tabela_orcamento")
        self.tabela_orcamento.setColumnCount(6)
        self.tabela_orcamento.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/barcode.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.tabela_orcamento.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/box.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.tabela_orcamento.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/prod_servi.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon5)
        self.tabela_orcamento.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/count.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon6)
        self.tabela_orcamento.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/dollar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon7)
        self.tabela_orcamento.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon7)
        self.tabela_orcamento.setHorizontalHeaderItem(5, item)
        self.tabela_orcamento.horizontalHeader().setDefaultSectionSize(100)
        self.verticalLayout_13.addWidget(self.tabela_orcamento)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.add_produto = QtWidgets.QPushButton(self.groupBox_8)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/img/stock-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_produto.setIcon(icon8)
        self.add_produto.setIconSize(QtCore.QSize(24, 24))
        self.add_produto.setObjectName("add_produto")
        self.horizontalLayout_18.addWidget(self.add_produto)
        self.add_servico = QtWidgets.QPushButton(self.groupBox_8)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/img/service.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_servico.setIcon(icon9)
        self.add_servico.setIconSize(QtCore.QSize(24, 24))
        self.add_servico.setObjectName("add_servico")
        self.horizontalLayout_18.addWidget(self.add_servico)
        self.exc_linha = QtWidgets.QPushButton(self.groupBox_8)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/img/remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exc_linha.setIcon(icon10)
        self.exc_linha.setIconSize(QtCore.QSize(24, 24))
        self.exc_linha.setObjectName("exc_linha")
        self.horizontalLayout_18.addWidget(self.exc_linha)
        self.verticalLayout_13.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_17.addWidget(self.groupBox_8)
        self.groupBox_9 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_9.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_9.setMaximumSize(QtCore.QSize(400, 16777215))
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_14.setContentsMargins(-1, 18, -1, -1)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_9)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(29, 34))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.tabela_entrada = QtWidgets.QTableWidget(self.tab)
        self.tabela_entrada.setAutoScrollMargin(20)
        self.tabela_entrada.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabela_entrada.setTabKeyNavigation(True)
        self.tabela_entrada.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tabela_entrada.setObjectName("tabela_entrada")
        self.tabela_entrada.setColumnCount(2)
        self.tabela_entrada.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_entrada.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_entrada.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_entrada.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_entrada.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_entrada.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/img/attach.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon11)
        self.tabela_entrada.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/img/cogwheels.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon12)
        self.tabela_entrada.setHorizontalHeaderItem(1, item)
        self.tabela_entrada.horizontalHeader().setDefaultSectionSize(130)
        self.horizontalLayout_19.addWidget(self.tabela_entrada)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/img/sign-in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon13, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.tabela_saida = QtWidgets.QTableWidget(self.tab_2)
        self.tabela_saida.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabela_saida.setTabKeyNavigation(True)
        self.tabela_saida.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tabela_saida.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabela_saida.setObjectName("tabela_saida")
        self.tabela_saida.setColumnCount(2)
        self.tabela_saida.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_saida.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_saida.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_saida.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_saida.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_saida.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon11)
        self.tabela_saida.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon12)
        self.tabela_saida.setHorizontalHeaderItem(1, item)
        self.tabela_saida.horizontalHeader().setDefaultSectionSize(130)
        self.verticalLayout_15.addWidget(self.tabela_saida)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/img/sign-out-option.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon14, "")
        self.verticalLayout_14.addWidget(self.tabWidget)
        self.horizontalLayout_17.addWidget(self.groupBox_9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_17)
        self.valores_situacao = QtWidgets.QGroupBox(self.frame)
        self.valores_situacao.setTitle("")
        self.valores_situacao.setObjectName("valores_situacao")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.valores_situacao)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.valores_situacao)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.tecnico = QtWidgets.QComboBox(self.valores_situacao)
        self.tecnico.setObjectName("tecnico")
        self.tecnico.addItem("")
        self.verticalLayout_9.addWidget(self.tecnico)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.valores_situacao)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.valor_servicos = QtWidgets.QDoubleSpinBox(self.valores_situacao)
        self.valor_servicos.setEnabled(False)
        self.valor_servicos.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.valor_servicos.setWrapping(False)
        self.valor_servicos.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.valor_servicos.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.valor_servicos.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.valor_servicos.setProperty("showGroupSeparator", True)
        self.valor_servicos.setMaximum(999999999.99)
        self.valor_servicos.setObjectName("valor_servicos")
        self.horizontalLayout_4.addWidget(self.valor_servicos)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.valores_situacao)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.valor_pecas = QtWidgets.QDoubleSpinBox(self.valores_situacao)
        self.valor_pecas.setEnabled(False)
        self.valor_pecas.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.valor_pecas.setWrapping(False)
        self.valor_pecas.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.valor_pecas.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.valor_pecas.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.valor_pecas.setProperty("showGroupSeparator", True)
        self.valor_pecas.setMaximum(999999999.99)
        self.valor_pecas.setObjectName("valor_pecas")
        self.horizontalLayout_5.addWidget(self.valor_pecas)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_10.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.valores_situacao)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.situacao = QtWidgets.QComboBox(self.valores_situacao)
        self.situacao.setObjectName("situacao")
        self.situacao.addItem("")
        self.situacao.addItem("")
        self.situacao.addItem("")
        self.situacao.addItem("")
        self.situacao.addItem("")
        self.situacao.addItem("")
        self.situacao.addItem("")
        self.situacao.addItem("")
        self.situacao.addItem("")
        self.situacao.addItem("")
        self.verticalLayout_4.addWidget(self.situacao)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.valores_situacao)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.desconto = QtWidgets.QDoubleSpinBox(self.valores_situacao)
        self.desconto.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.desconto.setWrapping(False)
        self.desconto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.desconto.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.desconto.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.desconto.setProperty("showGroupSeparator", True)
        self.desconto.setMaximum(999999999.99)
        self.desconto.setObjectName("desconto")
        self.horizontalLayout_3.addWidget(self.desconto)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.valores_situacao)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.valor_total = QtWidgets.QDoubleSpinBox(self.valores_situacao)
        self.valor_total.setEnabled(False)
        self.valor_total.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.valor_total.setWrapping(False)
        self.valor_total.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.valor_total.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.valor_total.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.valor_total.setProperty("showGroupSeparator", True)
        self.valor_total.setMaximum(999999999.99)
        self.valor_total.setObjectName("valor_total")
        self.horizontalLayout_2.addWidget(self.valor_total)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_8.addLayout(self.verticalLayout_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.verticalLayout_5.addWidget(self.valores_situacao)
        self.horizontalLayout_21.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.principal)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setContentsMargins(9, -1, 9, -1)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_3 = QtWidgets.QFrame(self.groupBox_4)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_18.addWidget(self.label_9)
        self.codigo = QtWidgets.QLCDNumber(self.frame_3)
        self.codigo.setMaximumSize(QtCore.QSize(200, 16777215))
        self.codigo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.codigo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.codigo.setLineWidth(1)
        self.codigo.setMidLineWidth(0)
        self.codigo.setSmallDecimalPoint(False)
        self.codigo.setDigitCount(10)
        self.codigo.setObjectName("codigo")
        self.verticalLayout_18.addWidget(self.codigo)
        self.verticalLayout_17.addWidget(self.frame_3)
        spacerItem1 = QtWidgets.QSpacerItem(0, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_17.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.verticalLayout_17)
        self.imprimir = QtWidgets.QPushButton(self.groupBox_4)
        self.imprimir.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/img/excel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.imprimir.setIcon(icon15)
        self.imprimir.setIconSize(QtCore.QSize(55, 62))
        self.imprimir.setFlat(True)
        self.imprimir.setObjectName("imprimir")
        self.verticalLayout_6.addWidget(self.imprimir)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.checklist = QtWidgets.QPushButton(self.groupBox_4)
        self.checklist.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/img/test.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checklist.setIcon(icon16)
        self.checklist.setIconSize(QtCore.QSize(55, 62))
        self.checklist.setFlat(True)
        self.checklist.setObjectName("checklist")
        self.verticalLayout_6.addWidget(self.checklist)
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.termos = QtWidgets.QPushButton(self.groupBox_4)
        self.termos.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/img/plan.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.termos.setIcon(icon17)
        self.termos.setIconSize(QtCore.QSize(55, 62))
        self.termos.setFlat(True)
        self.termos.setObjectName("termos")
        self.verticalLayout_6.addWidget(self.termos)
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 134))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.finalizar = QtWidgets.QPushButton(self.groupBox)
        self.finalizar.setEnabled(False)
        self.finalizar.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/img/payment-terminal.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.finalizar.setIcon(icon18)
        self.finalizar.setIconSize(QtCore.QSize(45, 46))
        self.finalizar.setFlat(True)
        self.finalizar.setObjectName("finalizar")
        self.horizontalLayout.addWidget(self.finalizar)
        self.sair = QtWidgets.QPushButton(self.groupBox)
        self.sair.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/img/cross.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sair.setIcon(icon19)
        self.sair.setIconSize(QtCore.QSize(45, 46))
        self.sair.setFlat(True)
        self.sair.setObjectName("sair")
        self.horizontalLayout.addWidget(self.sair)
        self.cadastrar = QtWidgets.QPushButton(self.groupBox)
        self.cadastrar.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/img/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cadastrar.setIcon(icon20)
        self.cadastrar.setIconSize(QtCore.QSize(45, 46))
        self.cadastrar.setFlat(True)
        self.cadastrar.setObjectName("cadastrar")
        self.horizontalLayout.addWidget(self.cadastrar)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.horizontalLayout_21.addWidget(self.frame_2)
        self.verticalLayout_7.addWidget(self.principal)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ORDEM SERVIÇOS - ASSISTENCIA TECNICA DE MANUNTEÇÃO"))
        self.label_7.setText(_translate("Form", "DESCRIÇÃO DO SERVIÇO/ATENDIMENTO"))
        self.groupBox_6.setToolTip(_translate("Form", "<html><head/><body><p>DATA E HORA ATUAL</p></body></html>"))
        self.groupBox_6.setTitle(_translate("Form", "DATA/HORA"))
        self.data_hora.setToolTip(_translate("Form", "<html><head/><body><p>DATA E HORA ATUAL</p></body></html>"))
        self.groupBox_7.setTitle(_translate("Form", "DATA/HORA --- DEVOLUÇÃO"))
        self.groupBox_5.setTitle(_translate("Form", "EQUIPAMENTO"))
        self.equipamento.setItemText(0, _translate("Form", "SELECIONE EQUIPAMENTO"))
        self.groupBox_2.setTitle(_translate("Form", "CLIENTE"))
        self.cliente.setItemText(0, _translate("Form", "SELECIONE CLIENTE"))
        self.groupBox_3.setToolTip(_translate("Form", "<html><head/><body><p>DESCREVA OS PROBLEMAS QUE O PRODUTO DE ENTRADA TEM</p></body></html>"))
        self.groupBox_3.setTitle(_translate("Form", "DESCRIÇÃO DO EQUIPAMENTO"))
        self.descricao_produto.setToolTip(_translate("Form", "<html><head/><body><p>DESCREVA OS PROBLEMAS QUE O PRODUTO DE ENTRADA TEM</p></body></html>"))
        self.descricao_produto.setPlaceholderText(_translate("Form", "DESCREVA O SERVIÇO OU PRODUTO. O QUE VAI SER FEITO NO MESMO"))
        self.groupBox_8.setToolTip(_translate("Form", "<html><head/><body><p>TABELA DE ORÇAMENTO</p></body></html>"))
        self.groupBox_8.setTitle(_translate("Form", "PRODUTOS/SERVIÇOS"))
        self.tabela_orcamento.setToolTip(_translate("Form", "<html><head/><body><p>TABELA DE ORÇAMENTO</p></body></html>"))
        item = self.tabela_orcamento.horizontalHeaderItem(0)
        item.setText(_translate("Form", "CÓDIGO"))
        item.setToolTip(_translate("Form", "CÓDIGO DO ORÇAMENTO"))
        item = self.tabela_orcamento.horizontalHeaderItem(1)
        item.setText(_translate("Form", "SERVIÇO/PRODUTO"))
        item.setToolTip(_translate("Form", "SERVIÇO/PRODUTO DO ORÇAMENTO"))
        item = self.tabela_orcamento.horizontalHeaderItem(2)
        item.setText(_translate("Form", "TIPO"))
        item.setToolTip(_translate("Form", "O TIPO PODE SER: PRODUTO/SERVIÇO"))
        item = self.tabela_orcamento.horizontalHeaderItem(3)
        item.setText(_translate("Form", "UNIDADE"))
        item.setToolTip(_translate("Form", "QUANTIDADE SELECIONADA DO PRODUTO"))
        item = self.tabela_orcamento.horizontalHeaderItem(4)
        item.setText(_translate("Form", "VALOR(UNIDADE)"))
        item.setToolTip(_translate("Form", "CUSTO POR UNIDADE(R$)"))
        item = self.tabela_orcamento.horizontalHeaderItem(5)
        item.setText(_translate("Form", "TOTAL(R$)"))
        item.setToolTip(_translate("Form", "TOTAL PARA ESSA LINHA"))
        self.add_produto.setToolTip(_translate("Form", "<html><head/><body><p>ADICIONE PRODUTOS NO ORÇAMENTO(EQUIPAMENTOS VENDIDOS)</p></body></html>"))
        self.add_produto.setText(_translate("Form", "PRODUTO"))
        self.add_servico.setToolTip(_translate("Form", "<html><head/><body><p>ADICIONE SERVIÇOS NO ORÇAMENTO(SERVIÇOS REALIZADO PELO TECNICO)</p></body></html>"))
        self.add_servico.setText(_translate("Form", "SERVIÇO"))
        self.exc_linha.setToolTip(_translate("Form", "<html><head/><body><p>SELECIONE UM ITEM E FAÇA A REMOÇÃO DA LISTA DO ORÇAMENTO</p></body></html>"))
        self.exc_linha.setText(_translate("Form", "EXCLUIR"))
        self.groupBox_9.setTitle(_translate("Form", "ANEXOS"))
        self.tabWidget.setToolTip(_translate("Form", "<html><head/><body><p>TIRE FOTOS DO ESTADO DO PRODUTO QUANDO ELE ENTROU</p></body></html>"))
        self.tabela_entrada.setToolTip(_translate("Form", "<html><head/><body><p>TIRE FOTOS DO ESTADO DO PRODUTO QUANDO ELE ENTROU</p></body></html>"))
        item = self.tabela_entrada.verticalHeaderItem(0)
        item.setText(_translate("Form", "ANEXO_1"))
        item = self.tabela_entrada.verticalHeaderItem(1)
        item.setText(_translate("Form", "ANEXO_2"))
        item = self.tabela_entrada.verticalHeaderItem(2)
        item.setText(_translate("Form", "ANEXO_3"))
        item = self.tabela_entrada.verticalHeaderItem(3)
        item.setText(_translate("Form", "ANEXO_4"))
        item = self.tabela_entrada.verticalHeaderItem(4)
        item.setText(_translate("Form", "ANEXO_5"))
        item = self.tabela_entrada.horizontalHeaderItem(0)
        item.setText(_translate("Form", "FOTO"))
        item = self.tabela_entrada.horizontalHeaderItem(1)
        item.setText(_translate("Form", "OPERAÇÕES"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "ENTRADA"))
        self.tabela_saida.setToolTip(_translate("Form", "<html><head/><body><p>TIRE FOTOS DO ESTADO DO PRODUTO EM SEU NOVO ESTADO</p></body></html>"))
        item = self.tabela_saida.verticalHeaderItem(0)
        item.setText(_translate("Form", "ANEXO_1"))
        item = self.tabela_saida.verticalHeaderItem(1)
        item.setText(_translate("Form", "ANEXO_2"))
        item = self.tabela_saida.verticalHeaderItem(2)
        item.setText(_translate("Form", "ANEXO_3"))
        item = self.tabela_saida.verticalHeaderItem(3)
        item.setText(_translate("Form", "ANEXO_4"))
        item = self.tabela_saida.verticalHeaderItem(4)
        item.setText(_translate("Form", "ANEXO_5"))
        item = self.tabela_saida.horizontalHeaderItem(0)
        item.setText(_translate("Form", "FOTO"))
        item = self.tabela_saida.horizontalHeaderItem(1)
        item.setText(_translate("Form", "OPERAÇÕES"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "SAÍDA"))
        self.label_5.setText(_translate("Form", "TECNICO"))
        self.tecnico.setItemText(0, _translate("Form", "SELECIONE TECNICO"))
        self.label_3.setText(_translate("Form", "VALOR SERVIÇOS"))
        self.valor_servicos.setSuffix(_translate("Form", " R$"))
        self.label_4.setText(_translate("Form", "VALOR PEÇAS"))
        self.valor_pecas.setSuffix(_translate("Form", " R$"))
        self.label_6.setText(_translate("Form", "SITUAÇÃO"))
        self.situacao.setItemText(0, _translate("Form", "SELECIONE SITUAÇÃO"))
        self.situacao.setItemText(1, _translate("Form", "ABANDONADO PELO CLIENTE"))
        self.situacao.setItemText(2, _translate("Form", "ENTREGA PENDENTE"))
        self.situacao.setItemText(3, _translate("Form", "RETIRADA CLIENTE"))
        self.situacao.setItemText(4, _translate("Form", "PENDENTE (PEÇAS)"))
        self.situacao.setItemText(5, _translate("Form", "SAÍDA ENTREGA"))
        self.situacao.setItemText(6, _translate("Form", "NADA CONSTA"))
        self.situacao.setItemText(7, _translate("Form", "NA BANCADA"))
        self.situacao.setItemText(8, _translate("Form", "ENTREGA OK"))
        self.situacao.setItemText(9, _translate("Form", "RETORNO"))
        self.label_2.setText(_translate("Form", "DESCONTOS(-)"))
        self.desconto.setSuffix(_translate("Form", " R$"))
        self.label.setText(_translate("Form", "VALOR TOTAL"))
        self.valor_total.setSuffix(_translate("Form", " R$"))
        self.label_9.setText(_translate("Form", "N. O.S."))
        self.label_8.setToolTip(_translate("Form", "<html><head/><body><p>FAÇA IMPRESSÃO OU EXPORTE PARA EXCEL</p></body></html>"))
        self.label_8.setText(_translate("Form", "IMPRIMIR"))
        self.label_10.setToolTip(_translate("Form", "<html><head/><body><p>FAÇA IMPRESSÃO DO CHECK LIST</p></body></html>"))
        self.label_10.setText(_translate("Form", "CHECKLIST"))
        self.label_11.setToolTip(_translate("Form", "<html><head/><body><p>SELECIONE UM TEMO DE GARANTIA. CASO NÃO SELECIONE OUTRO SERÁ IMPRESSO O PADRÃO</p></body></html>"))
        self.label_11.setText(_translate("Form", "TERMOS"))
        self.groupBox.setTitle(_translate("Form", "OPERAÇÕES"))
        self.Janela = Form
        self.carregar_janela()


    def carregar_janela(self):
        self.carregar_eventos()


    def carregar_eventos(self):
        self.sair.clicked.connect(self.Janela.close)
        self.add_produto.clicked.connect(self.adicionar_produto)
        self.add_servico.clicked.connect(self.adicionar_servico)
        self.exc_linha.setDisabled(True)
        self.codigo.display(str(sql.SQL().pegar_codigo_orcamentos() + 1))
        self.data_entrada.setDateTime(QtCore.QDateTime.currentDateTime())
        self.data_hora.setDateTime(QtCore.QDateTime.currentDateTime())
        self.tabela_orcamento.setSortingEnabled(True)
        self.carregar_equipamentos()
        self.carregar_clientes()
        self.carregar_tecnicos()
        self.carregar_tabela_anexo_entrada()
        self.carregar_tabela_anexo_saida()
        self.desconto.valueChanged.connect(self.calcula_total)
        self.tabela_orcamento.horizontalHeader().setSectionsMovable(True)
        self.tabela_orcamento.clicked.connect(self.habilita_exclui_linha)
        self.exc_linha.clicked.connect(self.exclui_linha)
        self.cadastrar.clicked.connect(self.cadastra)
        self.add_equipamento.clicked.connect(self.cadastrar_produto)
        self.limpar_variaveis()


    def cadastra(self):
        if(self.verificar_campos()):
            msg = QtWidgets.QMessageBox.question(None, "ORCAMENTOS - SISTEMA MANNUNTEÇÃO",
                                              "DESEJA CRIAR O ORÇAMENTO <b>{}</b> PARA ESSE PRAZO <b>{}</b>?".format(int(self.codigo.value()), self.data_entrada.text()))
            if(msg == QtWidgets.QMessageBox.Yes):
                SQL = {"eqt_ent_oct":self.equipamento.currentText().split("(")[1].split(")")[0],
                       "data_entrada": self.data_hora.text(),
                       "data_saida": self.data_entrada.text(),
                       "cliente_oct": self.cliente.currentText().split("(")[1].split(")")[0],
                       "descricao_oct": self.descricao_produto.toPlainText(),
                       "tecnico_oct": self.tecnico.currentText().split("(")[1].split(")")[0],
                       "valor_oct": self.valor_servicos.value(),
                       "valor_peca": self.valor_pecas.value(),
                       "valor_desconto_oct": self.desconto.value(),
                       "total_servico": self.valor_total.value(),
                       "situacao_oct": self.situacao.currentIndex()}
                self.conexao = sql.SQL().inserir_orcamento(SQL, False)
                if(self.atualizar_produtos_sql()): sql.SQL().fechar_conexao(self.conexao)

                QtWidgets.QMessageBox.information(None, "ORCAMENTOS - SISTEMA MANNUNTEÇÃO",
                                                  "CADASTRADOR ORÇAMENTO <b>{}</b> PARA O CLIENTE <b>{}</b> COM SUCESSO!".format(int(self.codigo.value()), self.cliente.currentText()))
                [campo.setCurrentIndex(0) for campo in [self.cliente, self.equipamento, self.tecnico, self.situacao]]
                [campo.setValue(0) for campo in [self.valor_total, self.valor_pecas, self.desconto, self.valor_servicos]]
                self.descricao_produto.clear()
                self.limpar_variaveis()
                self.tabela_orcamento.setRowCount(0)


    def atualizar_produtos_sql(self):
        prod_alt = {}
        for produto in self.produtos:
            prod_alt["quantidade"] = int(sql.SQL().pegar_estoque_codigo_tabela(produto["codigo"])[0][3]) - produto["quantidade"]
            prod_alt["codigo"] = produto["codigo"]
            sql.SQL().alterar_produto_estoque_quantidade(prod_alt, False, self.conexao)
            sql.SQL().inserir_orcamento_produtos({'orcamento': int(self.codigo.value()), 'produto': produto["codigo"], 'quantidade': produto["quantidade"]}, self.conexao)

        for servico in self.servicos:
            sql.SQL().inserir_orcamento_servicos({'orcamento': int(self.codigo.value()), 'servico': servico['codigo'], 'quantidade': servico['quantidade']}, self.conexao)
        return True


    def limpar_variaveis(self):
        #limpeza de variaveis
        self.servicos.clear()
        self.produtos.clear()


    def verificar_campos(self):
        lista = [self.cliente, self.equipamento, self.tecnico, self.situacao]
        for campo in lista:
            if(campo.currentIndex() == 0):
                QtWidgets.QMessageBox.information(None, "ORCAMENTOS - SISTEMA MANNUNTEÇÃO", "PREENCHA O CAMPO SELECIONADO!")
                campo.setFocus(True)
                return False

        if(self.descricao_produto.toPlainText() == ''):
            QtWidgets.QMessageBox.information(None, "ORCAMENTOS - SISTEMA MANNUNTEÇÃO", "<b>PREENCHA UMA DESCRIÇAO  DO ORÇAMENTO</b>")
            self.descricao_produto.setFocus(True)
            return False

        if(self.valor_total.value() == 0):
            QtWidgets.QMessageBox.information(None, "ORCAMENTOS - SISTEMA MANNUNTEÇÃO", "<b>SEU ORÇAMENTO DEVE TER ALGUM PRODUTO OU SERVIÇO!</b>")
            return False

        return True


    def exclui_linha(self):
        try:
            linha_i = self.tabela_orcamento.selectedItems()
            if(linha_i[2].text() == "SERVIÇOS"):
                self.valor_servicos.setValue(self.valor_servicos.value() - float(linha_i[5].text().split(" ")[0]))
                self.servicos.pop(self.retorna_indice_lista(self.servicos, linha_i[1].text()))
            else:
                self.valor_pecas.setValue(self.valor_pecas.value() - float(linha_i[5].text().split(" ")[0]))
                self.produtos.pop(self.retorna_indice_lista(self.produtos, linha_i[1].text()))

            self.tabela_orcamento.removeRow(self.tabela_orcamento.currentRow())
            self.exc_linha.setEnabled(False)
            self.calcula_total()
        except Exception as erro:  print("ERRO EM REMOVER ({})".format(erro))


    def retorna_indice_lista(self, lista, bsq):
        for contagem, linha in enumerate(lista):
            if(linha["desc"] == str(bsq)): return contagem


    def habilita_exclui_linha(self):
        self.exc_linha.setEnabled(True)


    def adicionar_servico(self):
        self.Form = QtWidgets.QDialog()
        self.ui = Busca_servico()
        self.ui.setupUi(self.Form, self.servicos)
        self.Form.exec()
        if(self.ui.servico != False):
            self.adicionar_servico_tabela(self.ui.servico)

    servicos = []
    def adicionar_servico_tabela(self, servico):
        self.tabela_orcamento.insertRow(self.tabela_orcamento.rowCount())
        linha = self.tabela_orcamento.rowCount()
        self.servicos.append({'codigo': servico['codigo'], 'desc': servico['servico'], "quantidade": servico['quantidade']})
        self.tabela_orcamento.setItem(linha - 1, 0, QtWidgets.QTableWidgetItem(str(linha)))
        self.tabela_orcamento.setItem(linha - 1, 1, QtWidgets.QTableWidgetItem(servico["servico"]))
        self.tabela_orcamento.setItem(linha - 1, 2, QtWidgets.QTableWidgetItem('SERVIÇOS'))
        self.tabela_orcamento.setItem(linha - 1, 3, QtWidgets.QTableWidgetItem(servico["unidade"]))
        self.tabela_orcamento.setItem(linha - 1, 4, QtWidgets.QTableWidgetItem(str(servico["quantidade"]) + ' HORAS'))
        self.tabela_orcamento.setItem(linha - 1, 5, QtWidgets.QTableWidgetItem(str(servico["preco"]) + " R$"))
        self.atualizar_servicos()


    def atualizar_servicos(self):
        valor_total = 0.00
        try:
            for linha in range(self.tabela_orcamento.rowCount()):
                if(self.tabela_orcamento.item(linha, 2).text() == "SERVIÇOS"):
                    valor_total += float(self.tabela_orcamento.item(linha, 5).text().split(" ")[0])
            self.valor_servicos.setValue(valor_total)
            self.calcula_total()
        except Exception as erro: print("ERRO EM ADICIONAR SERVIÇOS({})".format(erro))


    def calcula_total(self):
        total = self.valor_pecas.value() + self.valor_servicos.value() - self.desconto.value()
        self.valor_total.setValue(total)


    def adicionar_produto(self):
        self.Form = QtWidgets.QDialog()
        self.ui = Busca_produto()
        self.ui.setupUi(self.Form, self.produtos)
        self.Form.exec()
        if(self.ui.produto != False):
            self.adicionar_produto_tabela(self.ui.produto)


    def cadastrar_produto(self):
        self.Form = QtWidgets.QDialog()
        self.ui = Produtos()
        self.ui.setupUi(self.Form)
        self.Form.exec()
        self.equipamento.clear()
        self.equipamento.addItem("SELECIONE EQUIPAMENTO")
        self.carregar_equipamentos()


    produtos = []
    def adicionar_produto_tabela(self, produto):
        self.tabela_orcamento.insertRow(self.tabela_orcamento.rowCount())
        linha = self.tabela_orcamento.rowCount()
        self.produtos.append({'codigo': produto['codigo'], 'desc': produto['produto'], 'quantidade':produto['quantidade']})
        self.tabela_orcamento.setItem(linha - 1, 0, QtWidgets.QTableWidgetItem(str(linha)))
        self.tabela_orcamento.setItem(linha - 1, 1, QtWidgets.QTableWidgetItem(produto["produto"]))
        self.tabela_orcamento.setItem(linha - 1, 2, QtWidgets.QTableWidgetItem('PRODUTOS'))
        self.tabela_orcamento.setItem(linha - 1, 3, QtWidgets.QTableWidgetItem('{} - {}'.format(produto["quantidade"], produto["unidade"])))
        self.tabela_orcamento.setItem(linha - 1, 4, QtWidgets.QTableWidgetItem(produto["preco"]))
        total_produto = round(float(produto["quantidade"]) * float(produto["preco"].split(" ")[0]), 2)
        self.tabela_orcamento.setItem(linha - 1, 5, QtWidgets.QTableWidgetItem(str(total_produto) + " R$"))
        self.atualizar_pecas()


    def atualizar_pecas(self):
        valor_total = 0.00
        try:
            for linha in range(self.tabela_orcamento.rowCount()):
                if(self.tabela_orcamento.item(linha, 2).text() == "PRODUTOS"):
                    valor_total += float(self.tabela_orcamento.item(linha, 5).text().split(" ")[0])
            self.valor_pecas.setValue(valor_total)
            self.calcula_total()
        except Exception as erro: print("ERRO EM ADICIONAR PRODUTO({})".format(erro))


    def carregar_equipamentos(self):
        for equi in sql.SQL().pegar_produtos(): self.equipamento.addItem("{}({})".format(equi[1], equi[0]))


    def carregar_clientes(self):
        for cli in sql.SQL().pegar_clientes(): self.cliente.addItem("{}({})".format(cli[3], cli[0]))


    def carregar_tecnicos(self):
        for cli in sql.SQL().pegar_tecnicos(): self.tecnico.addItem("{}({})".format(cli[2], cli[0]))


    def carregar_tabela_anexo_entrada(self):
        self.tabela_entrada.setCellWidget(0, 1, self.defini_botao_anexo(0, 'ANEXAR'))
        self.tabela_entrada.setCellWidget(1, 1, self.defini_botao_anexo(1, 'ANEXAR'))
        self.tabela_entrada.setCellWidget(2, 1, self.defini_botao_anexo(2, 'ANEXAR'))
        self.tabela_entrada.setCellWidget(3, 1, self.defini_botao_anexo(3, 'ANEXAR'))
        self.tabela_entrada.setCellWidget(4, 1, self.defini_botao_anexo(4, 'ANEXAR'))


    def carregar_tabela_anexo_saida(self):
        self.tabela_saida.setCellWidget(0, 1, self.defini_botao_anexo(0, 'VER ANEXO'))
        self.tabela_saida.setCellWidget(1, 1, self.defini_botao_anexo(1, 'VER ANEXO'))
        self.tabela_saida.setCellWidget(2, 1, self.defini_botao_anexo(2, 'VER ANEXO'))
        self.tabela_saida.setCellWidget(3, 1, self.defini_botao_anexo(3, 'VER ANEXO'))
        self.tabela_saida.setCellWidget(4, 1, self.defini_botao_anexo(4, 'VER ANEXO'))


    def defini_botao_anexo(self, numero, text):
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/img/attach.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        bt = QtWidgets.QPushButton()
        bt.setIcon(icon11)
        bt.setText("{}({})".format(text, numero + 1))
        return bt


import recursos


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Orcamentos()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
