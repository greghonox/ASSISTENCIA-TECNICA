# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SUPORTE05\Documents\Meus Programas\apps\ASSISTENCIA TECNICA\UI\busca_produto.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import sql
from PyQt5 import QtCore, QtGui, QtWidgets


class Busca_produto(object):
    def setupUi(self, Form, produtos_selecionados):
        Form.setObjectName("Form")
        Form.resize(693, 437)
        Form.setMinimumSize(QtCore.QSize(693, 437))
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
"QLineEdit, QComboBox{                \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(84, 167, 216);\n"
"}\n"
"\n"
"QLineEdit:hover, QComboBox:hover{                \n"
"    background-color: rgb(1, 92, 146);\n"
"}\n"
"\n"
"QLabel{\n"
"    background-color: rgba(255, 255, 255, 0);    \n"
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
"")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabela = QtWidgets.QTableWidget(self.frame)
        self.tabela.setAutoScrollMargin(16)
        self.tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabela.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabela.setObjectName("tabela")
        self.tabela.setColumnCount(6)
        self.tabela.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/barcode.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.tabela.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/box.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.tabela.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/dollar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.tabela.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/count.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.tabela.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/cogwheels.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon5)
        self.tabela.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/design.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon6)
        self.tabela.setHorizontalHeaderItem(5, item)
        self.tabela.horizontalHeader().setDefaultSectionSize(164)
        self.horizontalLayout.addWidget(self.tabela)
        self.verticalLayout_7.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.filtro = QtWidgets.QComboBox(self.frame_3)
        self.filtro.setObjectName("filtro")
        self.filtro.addItem(icon2, "")
        self.filtro.addItem(icon1, "")
        self.horizontalLayout_3.addWidget(self.filtro)
        self.descricao = QtWidgets.QLineEdit(self.frame_3)
        self.descricao.setText("")
        self.descricao.setClearButtonEnabled(True)
        self.descricao.setObjectName("descricao")
        self.horizontalLayout_3.addWidget(self.descricao)
        self.verticalLayout_7.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.quantidade = QtWidgets.QSpinBox(self.frame_4)
        self.quantidade.setObjectName("quantidade")
        self.horizontalLayout_4.addWidget(self.quantidade)
        self.verticalLayout_7.addWidget(self.frame_4)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.confirmar = QtWidgets.QPushButton(self.frame_2)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/confirm.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.confirmar.setIcon(icon7)
        self.confirmar.setIconSize(QtCore.QSize(32, 31))
        self.confirmar.setObjectName("confirmar")
        self.horizontalLayout_2.addWidget(self.confirmar)
        self.cancelar = QtWidgets.QPushButton(self.frame_2)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/img/cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelar.setIcon(icon8)
        self.cancelar.setIconSize(QtCore.QSize(32, 31))
        self.cancelar.setObjectName("cancelar")
        self.horizontalLayout_2.addWidget(self.cancelar)
        self.verticalLayout_7.addWidget(self.frame_2)

        self.retranslateUi(Form, produtos_selecionados)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.descricao, self.filtro)
        Form.setTabOrder(self.filtro, self.tabela)
        Form.setTabOrder(self.tabela, self.quantidade)
        Form.setTabOrder(self.quantidade, self.confirmar)
        Form.setTabOrder(self.confirmar, self.cancelar)

    def retranslateUi(self, Form, produtos_selecionados):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ENCONTRAR PRODUTO - ASSISTENCIA TECNICA DE MANUNTEÇÃO"))
        item = self.tabela.horizontalHeaderItem(0)
        item.setText(_translate("Form", "CÓDIGO"))
        item = self.tabela.horizontalHeaderItem(1)
        item.setText(_translate("Form", "DESCRIÇÃO"))
        item.setToolTip(_translate("Form", "DESCRIÇÃO QUE FOI ATRIBUIDA AO PRODUTO(NOME)"))
        item = self.tabela.horizontalHeaderItem(2)
        item.setText(_translate("Form", "PREÇO"))
        item.setToolTip(_translate("Form", "PREÇO DE CADA UNIDADE"))
        item = self.tabela.horizontalHeaderItem(3)
        item.setText(_translate("Form", "QUANTIDADE"))
        item.setToolTip(_translate("Form", "QUANTIDADE EXISTENTE NO ESTOQUE"))
        item = self.tabela.horizontalHeaderItem(4)
        item.setText(_translate("Form", "UNIDADE"))
        item.setToolTip(_translate("Form", "(PEÇA, UNIDADE, CAIXA....)"))
        item = self.tabela.horizontalHeaderItem(5)
        item.setText(_translate("Form", "CATEGORIA"))
        item.setToolTip(_translate("Form", "TIPO DE EQUIPAMENTO"))
        self.label.setText(_translate("Form", "Filtrar:"))
        self.filtro.setItemText(0, _translate("Form", "DESCRIÇÃO"))
        self.filtro.setItemText(1, _translate("Form", "CÓDIGO"))
        self.descricao.setPlaceholderText(_translate("Form", "DIGITE SUA BUSCA AQUI"))
        self.label_2.setText(_translate("Form", "QUANTIDADE"))
        self.confirmar.setText(_translate("Form", "CONFIRMA"))
        self.confirmar.setShortcut(_translate("Form", "Enter, Return"))
        self.cancelar.setText(_translate("Form", "CANCELAR"))
        self.carregar_janela(Form, produtos_selecionados)

    Janela = False
    produto = {}
    produtos_selecionados = []
    def carregar_janela(self, Form, produtos_selecionados):
        self.Janela = Form
        self.produtos_selecionados = produtos_selecionados
        self.cancelar.clicked.connect(self.fechar)
        self.quantidade.setDisabled(True)
        self.carregar_tabela()
        self.carregar_auto_completar()
        self.descricao.textChanged.connect(self.pesquisa)
        self.filtro.currentTextChanged.connect(self.mudar_tipo_busca)
        self.tabela.doubleClicked.connect(self.habilita_quantidade)
        self.confirmar.clicked.connect(self.selecionado_produto)
        self.tabela.setSortingEnabled(True)
        self.tabela.horizontalHeader().setSectionsMovable(True)


    def fechar(self):
        self.produto = False
        self.Janela.close()


    def selecionado_produto(self):
        try:
            self.produto["produto"] = self.tabela.selectedItems()[1].text()
            self.produto["codigo"] = self.tabela.selectedItems()[0].text()
            self.produto["preco"] = self.tabela.selectedItems()[2].text()
            self.produto["unidade"] = self.tabela.selectedItems()[4].text()
            self.produto["quantidade"] = self.quantidade.value()
            self.Janela.close()
        except: pass


    def habilita_quantidade(self):
        self.quantidade.setEnabled(True)
        self.quantidade.setValue(1)
        self.quantidade.setMinimum(1)
        self.quantidade.setMaximum(int(self.tabela.selectedItems()[3].text()))


    def mudar_tipo_busca(self):
        self.descricao.setFocus(True)
        if(self.filtro.currentIndex() == 1):
            self.descricao.setInputMask("9999999999999999999999999999999999")
        else:
            self.descricao.setInputMask("")


    def pesquisa(self):
        if(self.filtro.currentIndex() == 0):
            busca = sql.SQL().pegar_estoque_descricao_tabela(self.descricao.text())
        else:
            busca = sql.SQL().pegar_estoque_codigo_tabela(self.descricao.text())


        self.tabela.setRowCount(0)
        linha = 0
        for data in busca:
            if(not str(data[0]) in [servico["codigo"] for servico in self.produtos_selecionados]):
                self.tabela.insertRow(self.tabela.rowCount())
                for coluna, produto in enumerate(data):
                    produto = str(produto) + " R$" if(coluna == 2) else produto
                    if(coluna == 4): produto = self.unidade[produto - 1]
                    self.tabela.setItem(linha, coluna,  QtWidgets.QTableWidgetItem(str(produto)))
                linha += 1

    descricao_autocomplete = []
    habilita_autocomlete_descricao = True
    def carregar_tabela(self):
        self.unidade = ['PEÇAS(PC)', 'CAIXA(CX)', 'PACOTE(PCT)', 'UNIDADE(UN)']
        linha = 0
        for data in sql.SQL().pegar_produto_estoque_tabela():
            if(not str(data[0]) in [servico["codigo"] for servico in self.produtos_selecionados]):
                self.tabela.insertRow(self.tabela.rowCount())
                for coluna, produto in enumerate(data):
                    if(coluna == 1 and self.habilita_autocomlete_descricao): self.descricao_autocomplete.append(produto); self.descricao_autocomplete.append(produto.lower())
                    if(coluna == 4): produto = self.unidade[produto - 1]
                    produto = str(produto) + " R$" if(coluna == 2) else produto
                    self.tabela.setItem(linha, coluna,  QtWidgets.QTableWidgetItem(str(produto)))
                linha += 1
        self.habilita_autocomlete_descricao = False


    def carregar_auto_completar(self):
        self.completer = QtWidgets.QCompleter(self.descricao_autocomplete, self.descricao)
        self.descricao.setCompleter(self.completer)

import recursos


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Busca_produto()
    ui.setupUi(Form, '')
    Form.show()
    sys.exit(app.exec_())
