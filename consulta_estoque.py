# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consulta_estoque.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sql
from opcoes_filtro import Opcoes_filtro
from PyQt5 import QtCore, QtGui, QtWidgets

class Consulta_estoque(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(968, 554)
        Form.setMinimumSize(QtCore.QSize(968, 554))
        Form.setMaximumSize(QtCore.QSize(968, 554))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/technician.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#busca{\n"
"    background-image: url(:/img/user.svg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: left;\n"
"    background-color: rgb(137, 184, 214);\n"
"}\n"
"#Form{\n"
"    image: url(:/img/tecnico.jpg);\n"
"}\n"
"\n"
"QWidget{    \n"
"    background-color: rgb(188, 230, 254, 100);\n"
"}\n"
"\n"
"#filtro, #limite{\n"
"    background-color: rgb(137, 184, 214);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 66))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/img/search.svg"))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.widget_3)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.busca = QtWidgets.QLineEdit(self.groupBox)
        self.busca.setAlignment(QtCore.Qt.AlignCenter)
        self.busca.setClearButtonEnabled(True)
        self.busca.setObjectName("busca")
        self.horizontalLayout_2.addWidget(self.busca)
        self.filtro = QtWidgets.QComboBox(self.groupBox)
        self.filtro.setObjectName("filtro")
        self.filtro.addItem("")
        self.filtro.addItem("")
        self.filtro.addItem("")
        self.filtro.addItem("")
        self.horizontalLayout_2.addWidget(self.filtro)
        self.limite = QtWidgets.QSpinBox(self.groupBox)
        self.limite.setMaximumSize(QtCore.QSize(102, 16777215))
        self.limite.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.limite.setMaximum(1000)
        self.limite.setProperty("value", 100)
        self.limite.setDisplayIntegerBase(10)
        self.limite.setObjectName("limite")
        self.horizontalLayout_2.addWidget(self.limite)
        self.verticalLayout.addWidget(self.groupBox)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabela = QtWidgets.QTableWidget(self.groupBox_2)
        self.tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabela.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabela.setShowGrid(False)
        self.tabela.setObjectName("tabela")
        self.tabela.setColumnCount(5)
        self.tabela.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(4, item)
        self.tabela.horizontalHeader().setDefaultSectionSize(183)
        self.tabela.horizontalHeader().setMinimumSectionSize(39)
        self.horizontalLayout_3.addWidget(self.tabela)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cancelar = QtWidgets.QPushButton(self.widget_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelar.setIcon(icon1)
        self.cancelar.setIconSize(QtCore.QSize(37, 27))
        self.cancelar.setObjectName("cancelar")
        self.horizontalLayout_4.addWidget(self.cancelar)
        self.opcoes = QtWidgets.QPushButton(self.widget_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/gear-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.opcoes.setIcon(icon2)
        self.opcoes.setIconSize(QtCore.QSize(37, 27))
        self.opcoes.setObjectName("opcoes")
        self.horizontalLayout_4.addWidget(self.opcoes)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CONSULTA ESTOQUE - ASSISTENCIA TECNICA"))
        self.label.setText(_translate("Form", "CONSULTA ESTOQUE"))
        self.busca.setPlaceholderText(_translate("Form", "DIGITE SUA BUSCA AQUI"))
        self.filtro.setItemText(0, _translate("Form", "SELECIONE FILTRO"))
        self.filtro.setItemText(1, _translate("Form", "NOME"))
        self.filtro.setItemText(2, _translate("Form", "CÓDIGO"))
        self.filtro.setItemText(3, _translate("Form", "DESCRIÇÃO"))
        self.limite.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">DEFINE UM LIMITE PARA NÃO SOBRECARREGAR O SERVIDOR</span></p></body></html>"))
        self.limite.setSuffix(_translate("Form", " LIMITE"))
        self.tabela.setSortingEnabled(True)
        item = self.tabela.horizontalHeaderItem(0)
        item.setText(_translate("Form", "CÓDIGO"))
        item = self.tabela.horizontalHeaderItem(1)
        item.setText(_translate("Form", "PRODUTO"))
        item = self.tabela.horizontalHeaderItem(2)
        item.setText(_translate("Form", "QUANTIDADE"))
        item = self.tabela.horizontalHeaderItem(3)
        item.setText(_translate("Form", "QUANTIDADE MINIMA"))
        item = self.tabela.horizontalHeaderItem(4)
        item.setText(_translate("Form", "PREÇO"))
        self.cancelar.setText(_translate("Form", "CANCELAR"))
        self.opcoes.setText(_translate("Form", "OPÇÕES"))
        self.carregar_janela(Form)

    Janela = None
    produto_selecionado = False
    def carregar_janela(self, Form):
        self.Janela = Form
        self.cancelar.clicked.connect(self.Janela.close)
        self.busca.textChanged.connect(self.eventos_busca)
        self.tabela.horizontalHeader().setSectionsMovable(True)
        self.filtro.currentTextChanged.connect(self.mudar_filtro)
        self.tabela.doubleClicked.connect(self.alterar_produto)
        self.opcoes.clicked.connect(self.abrir_opcaoes_filtro)
        self.carregar_tabela()
        self.adiciona_completar_busca()


    opcao_filtro = 1
    def abrir_opcaoes_filtro(self):
        Form = QtWidgets.QDialog()
        ui = Opcoes_filtro()
        ui.setupUi(Form, self.opcao_filtro, "ESTOQUE", self.pegar_dados_tabela(), True)
        Form.exec()
        if(ui.opcao_escolhida != False):
            self.opcao_filtro = ui.opcao_escolhida
            self.carregar_tabela(self.filtro.currentIndex())
        self.busca.setFocus(True)


    def pegar_dados_tabela(self):
        tabela = []
        for lin in range(self.tabela.rowCount()):
            linha = []
            for col in range(5):
                try: linha.append(self.tabela.item(lin, col).text())
                except: linha.append(str(self.tabela.cellWidget(lin, col).value()) + " R$")
            tabela.append(linha)
        return tabela


    def alterar_produto(self):
        try:
            linha = self.tabela.selectedItems()
            self.produto_selecionado = linha[0].text()
            self.Janela.close()
        except: pass


    def mudar_filtro(self):
        self.busca.clear()
        self.busca.setFocus(True)
        if(self.filtro.currentIndex() == 0):
            self.carregar_tabela()
            self.busca.setPlaceholderText("DIGITE SUA BUSCA AQUI (NOME DO FORNECEDOR)")

        elif(self.filtro.currentIndex() == 1):
            self.busca.setInputMask("")
            self.busca.textChanged.connect(self.eventos_busca)
            self.busca.setPlaceholderText("DIGITE SUA BUSCA AQUI (NOME DO FORNECEDOR)")

        elif(self.filtro.currentIndex() == 2):
            # self.busca.setInputMask("999999999999999999999999999999999999999999999999")
            self.busca.setPlaceholderText("DIGITE SUA BUSCA AQUI (CÓDIGO DO FORNECEDOR)")

        elif(self.filtro.currentIndex() == 3):
            self.busca.setInputMask("")
            self.busca.textChanged.connect(self.eventos_busca)
            self.busca.setPlaceholderText("DIGITE SUA BUSCA AQUI (CNPJ/CPF DO FORNECEDOR)")


    def eventos_busca(self):
        self.defini_maisculo()
        indx = self.filtro.currentIndex()
        if(self.filtro.currentIndex() == 0):
            self.filtro.setCurrentIndex(1)
            self.carregar_tabela(1)

        elif(self.filtro.currentIndex() == 1):
            self.carregar_tabela(indx)

        elif(self.filtro.currentIndex() == 2):
            self.carregar_tabela(indx)

        elif(self.filtro.currentIndex() == 3):
            self.carregar_tabela(indx)

    def defini_maisculo(self): self.busca.setText(self.busca.text().upper())

    habilitar_completar = True
    def carregar_tabela(self, opcao=0):
        SQL = sql.SQL()
        busca = self.busca.text()
        lim = self.limite.value()

        opcao = SQL.pegar_estoque() if(opcao == 0) else SQL.pegar_estoque_nome(busca, lim) \
        if(opcao == 1) else SQL.pegar_estoque_codigo(busca, lim)\
        if(opcao == 2) else SQL.pegar_estoque_descricao(busca, lim)

        self.tabela.setRowCount(0)
        for dados in opcao: self.ad_tabela(dados)
        self.habilitar_completar = False


    nome_completar = []
    def adiciona_completar_busca(self):
        self.busca.setCompleter(QtWidgets.QCompleter(self.nome_completar ,self.busca))


    unidade = ['PC', 'CX', 'PCT', 'UN']
    def ad_tabela(self, dados):
        lin = self.tabela.rowCount()
        self.tabela.insertRow(lin)
        cores = {'amarelo':QtGui.QColor(255,255,0), 'vermelho':QtGui.QColor(255,0,0), 'branco':QtGui.QColor(255, 255, 255)}
        for col, usu in enumerate(dados):
            item = QtWidgets.QTableWidgetItem()

            usu = str(usu) + ' '+ str(self.unidade[dados[-1]]) if(col == 2) else usu
            usu = str(usu) + ' '+ str(self.unidade[dados[-1]]) if(col == 3) else usu
            usu = self.moeda(usu, (dados[2], dados[3])) if(col == 4) else usu
            if(col != 4): item.setText(str(usu))

            item.setBackground(cores['vermelho'] if(dados[2] == 0) else cores['amarelo'] if(dados[2] <= dados[3]) \
                               else cores['branco'])


            if(col != 4): self.tabela.setItem(lin, col, item)
            else: self.tabela.setCellWidget(lin, col, usu)

            if(col == 1 and self.habilitar_completar): self.nome_completar.append(usu)


    def moeda(self, valor, cor):
        moeda = QtWidgets.QDoubleSpinBox()
        moeda.setGroupSeparatorShown(True)
        moeda.setEnabled(False)
        moeda.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        moeda.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        moeda.setSuffix(" R$")
        moeda.setMaximum(9999.99)
        moeda.setValue(valor)
        moeda.setMaximumSize(200, 100)
        cores = [(255,0,0), (255,255,0), (255,255,255)]
        moeda.setStyleSheet("background-color: rgb({}, {}, {});\nborder: None;\n"\
                            "color: rgb(0, 0, 0);".format(*cores[0] if(cor[0] == 0) else cores[1] if(cor[0] <= cor[1]) else cores[2]))
        return moeda

import recursos

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Consulta_estoque()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
