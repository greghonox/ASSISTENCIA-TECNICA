# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SUPORTE05\Documents\Meus Programas\apps\ASSISTENCIA TECNICA\UI\produtos.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import sql
from categorias import Categorias
from fornecedores import Fornecedores
from PyQt5 import QtCore, QtGui, QtWidgets
from consulta_produtos import Consulta_produtos

class Produtos(object):
    def setupUi(self, Form, produto=False):
        Form.setObjectName("Form")
        Form.resize(790, 451)
        Form.setMinimumSize(QtCore.QSize(790, 451))
        Form.setMaximumSize(QtCore.QSize(790, 451))
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
"#principal{\n"
"image: url(:/img/hardware-e1535121140229.jpg);\n"
"}\n"
"\n"
"QFrame, QGroupBox{\n"
"    border: 1px;    \n"
"    border-color: rgb(188, 230, 254);\n"
"    color: rgb(1, 92, 146);\n"
"    font: 10pt \"Franklin Gothic Heavy\";    \n"
"\n"
"}\n"
"\n"
"QWidget{        \n"
"    background-color: rgb(188, 230, 254, 150);\n"
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
"background-color: rgb(84, 167, 216);\n"
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
"background-color: rgb(1, 92, 146);\n"
"}\n"
"\n"
"#descricao_completa{    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel{    \n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"#label_14,#label_15,#label_17,#label_16{    \n"
"    color: rgb(255, 255, 255);\n"
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
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(-1, 18, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.codigo = QtWidgets.QLineEdit(self.groupBox)
        self.codigo.setEnabled(False)
        self.codigo.setObjectName("codigo")
        self.horizontalLayout.addWidget(self.codigo)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.descricao = QtWidgets.QLineEdit(self.groupBox)
        self.descricao.setEnabled(True)
        self.descricao.setObjectName("descricao")
        self.horizontalLayout_2.addWidget(self.descricao)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.tipo_unidade = QtWidgets.QComboBox(self.groupBox)
        self.tipo_unidade.setObjectName("tipo_unidade")
        self.tipo_unidade.addItem("")
        self.tipo_unidade.addItem("")
        self.tipo_unidade.addItem("")
        self.tipo_unidade.addItem("")
        self.horizontalLayout_5.addWidget(self.tipo_unidade)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.fornecedor = QtWidgets.QComboBox(self.groupBox)
        self.fornecedor.setEditable(False)
        self.fornecedor.setObjectName("fornecedor")
        self.fornecedor.addItem("")
        self.horizontalLayout_3.addWidget(self.fornecedor)
        self.add_fornecedor = QtWidgets.QPushButton(self.groupBox)
        self.add_fornecedor.setMaximumSize(QtCore.QSize(47, 23))
        self.add_fornecedor.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/add-round-button-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_fornecedor.setIcon(icon1)
        self.add_fornecedor.setIconSize(QtCore.QSize(28, 19))
        self.add_fornecedor.setObjectName("add_fornecedor")
        self.horizontalLayout_3.addWidget(self.add_fornecedor)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setContentsMargins(-1, 18, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.categoria_equipamento = QtWidgets.QComboBox(self.groupBox_2)
        self.categoria_equipamento.setMinimumSize(QtCore.QSize(301, 0))
        self.categoria_equipamento.setEditable(True)
        self.categoria_equipamento.setObjectName("categoria_equipamento")
        self.categoria_equipamento.addItem("")
        self.horizontalLayout_7.addWidget(self.categoria_equipamento)
        self.add_categoria = QtWidgets.QPushButton(self.groupBox_2)
        self.add_categoria.setMaximumSize(QtCore.QSize(47, 23))
        self.add_categoria.setText("")
        self.add_categoria.setIcon(icon1)
        self.add_categoria.setIconSize(QtCore.QSize(28, 19))
        self.add_categoria.setObjectName("add_categoria")
        self.horizontalLayout_7.addWidget(self.add_categoria)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setContentsMargins(-1, 18, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.descricao_completa = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.descricao_completa.setObjectName("descricao_completa")
        self.verticalLayout_4.addWidget(self.descricao_completa)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_21.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.principal)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_21.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.principal)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.cadastrar = QtWidgets.QPushButton(self.groupBox_5)
        self.cadastrar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cadastrar.setIcon(icon2)
        self.cadastrar.setIconSize(QtCore.QSize(41, 52))
        self.cadastrar.setFlat(True)
        self.cadastrar.setObjectName("cadastrar")
        self.verticalLayout_9.addWidget(self.cadastrar)
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_9.addWidget(self.label_14)
        self.procurar = QtWidgets.QPushButton(self.groupBox_5)
        self.procurar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/find-my-friend.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.procurar.setIcon(icon3)
        self.procurar.setIconSize(QtCore.QSize(41, 52))
        self.procurar.setFlat(True)
        self.procurar.setObjectName("procurar")
        self.verticalLayout_9.addWidget(self.procurar)
        self.label_15 = QtWidgets.QLabel(self.groupBox_5)
        self.label_15.setEnabled(False)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_9.addWidget(self.label_15)
        self.excluir = QtWidgets.QPushButton(self.groupBox_5)
        self.excluir.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.excluir.setIcon(icon4)
        self.excluir.setIconSize(QtCore.QSize(41, 52))
        self.excluir.setFlat(True)
        self.excluir.setObjectName("excluir")
        self.verticalLayout_9.addWidget(self.excluir)
        self.label_16 = QtWidgets.QLabel(self.groupBox_5)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_9.addWidget(self.label_16)
        self.sair = QtWidgets.QPushButton(self.groupBox_5)
        self.sair.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/cross.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sair.setIcon(icon5)
        self.sair.setIconSize(QtCore.QSize(41, 52))
        self.sair.setFlat(True)
        self.sair.setObjectName("sair")
        self.verticalLayout_9.addWidget(self.sair)
        self.label_17 = QtWidgets.QLabel(self.groupBox_5)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_9.addWidget(self.label_17)
        self.verticalLayout_8.addWidget(self.groupBox_5)
        self.horizontalLayout_21.addWidget(self.frame_3)
        self.verticalLayout_7.addWidget(self.principal)

        self.retranslateUi(Form, produto)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form, produto):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CADASTRO EQUIPAMENTOS - ASSISTENCIA TECNICA DE MANUNTEÇÃO"))
        self.groupBox.setTitle(_translate("Form", "IDENTIFICAÇÃO"))
        self.label.setText(_translate("Form", "CÓDIGO"))
        self.label_2.setText(_translate("Form", "DESCRIÇÃO"))
        self.label_4.setText(_translate("Form", "UNIDADE"))
        self.tipo_unidade.setItemText(0, _translate("Form", "PEÇA(PC)"))
        self.tipo_unidade.setItemText(1, _translate("Form", "CAIXA(CX)"))
        self.tipo_unidade.setItemText(2, _translate("Form", "PACOTE(PCT)"))
        self.tipo_unidade.setItemText(3, _translate("Form", "UNIDADE(UN)"))
        self.label_3.setText(_translate("Form", "FORNECEDOR"))
        self.fornecedor.setItemText(0, _translate("Form", "FORNECEDOR"))
        self.groupBox_2.setTitle(_translate("Form", "CARACTERISTICAS"))
        self.label_5.setText(_translate("Form", "CATEGORIA"))
        self.categoria_equipamento.setItemText(0, _translate("Form", "EQUIPAMENTO"))
        self.groupBox_3.setTitle(_translate("Form", "DESCRIÇÃO COMPLETA"))
        self.descricao_completa.setPlaceholderText(_translate("Form", "DESCREVA UM RESUMO SOBRE ESSE PRODUTO"))
        self.label_14.setText(_translate("Form", "CADASTRAR"))
        self.label_15.setText(_translate("Form", "PROCURAR"))
        self.label_16.setText(_translate("Form", "EXCLUIR"))
        self.label_17.setText(_translate("Form", "SAIR"))
        self.Janela = Form
        self.carregar_janela(produto)


    def carregar_janela(self, produto):
        self.carregar_eventos()
        self.carregar_for()
        self.carregar_cat()
        self.descricao.textChanged.connect(self.descricao_maiscula)
        self.procurar.clicked.connect(self.abrir_consulta_categoria)
        if(produto == False):
            self.codigo.setText(str(sql.SQL().pegar_codigo_produtos() + 1))
        else:
            self.carregar_alteracao(produto)


    def carregar_alteracao(self, produto):
        dados = sql.SQL().pegar_produtos_codigo_tabela(produto)[0]
        self.codigo.setText(str(dados[0]))
        self.descricao.setText(str(dados[1]))
        self.tipo_unidade.setCurrentIndex(dados[2])

        try: self.fornecedor.setCurrentIndex(self.pegar_fornecedor(dados[3]))
        except: self.fornecedor_nao_encontrada(dados[3])

        try: self.categoria_equipamento.setCurrentIndex(self.pegar_categoria(dados[4]))
        except: self.categoria_nao_encontrada(dados[4])

        self.descricao_completa.setPlainText(str(dados[5]))
        self.cadastrar.disconnect()
        self.label_14.setText('ALTERAR')
        self.cadastrar.clicked.connect(self.alterar_produto)
        self.excluir.disconnect()
        self.excluir.clicked.connect(self.desativar_produto)


    def fornecedor_nao_encontrada(self, fornecedor):
        forn = sql.SQL().pegar_fornecedores_codigo(fornecedor)[0]
        self.fornecedor.setStyleSheet("background-color: rgb(255, 0, 0);\n")
        self.fornecedor.setToolTip("Á FORNECEDOR ANTERIOR({}({})) FOI DESATIVADA!".format(forn[1], forn[0]))
        self.fornecedor.setCurrentIndex(0)


    def categoria_nao_encontrada(self, categoria):
        cat = sql.SQL().pegar_categorias_servicos_codigo(categoria)[0]
        self.categoria_equipamento.setStyleSheet("background-color: rgb(255, 0, 0);\n")
        self.categoria_equipamento.setToolTip("Á CATEGORIA ANTERIOR({}({})) FOI DESATIVADA!".format(cat[1], cat[0]))
        self.categoria_equipamento.setCurrentIndex(0)


    def desativar_produto(self):
        msg = QtWidgets.QMessageBox.question(None, "CADASTRO EQUIPAMENTOS - ASSISTENCIA TECNICA DE MANUNTEÇÃO",
                                             "DESEJA DESATIVAR O PRODUTO <b>{}</b>?".format(self.descricao.text()))
        if(msg == QtWidgets.QMessageBox.Yes):
            if(sql.SQL().produto_desativar(self.codigo.text())):
                QtWidgets.QMessageBox.information(None, "CADASTRO EQUIPAMENTOS - ASSISTENCIA TECNICA DE MANUNTEÇÃO",
                                                     "PRODUTO <b>{}</b> DESATIVADO COM SUCESSO!".format(self.descricao.text()))
                self.Janela.close()


    def alterar_produto(self):
        msg = QtWidgets.QMessageBox.question(None, "CADASTRO EQUIPAMENTOS - ASSISTENCIA TECNICA DE MANUNTEÇÃO",
                                             "DESEJA ALTERAR O PRODUTO <b>{}</b>?".format(self.descricao.text()))
        if(msg == QtWidgets.QMessageBox.Yes):
            SQL = {"descricao": self.descricao.text(),
                   "unidade": self.tipo_unidade.currentIndex(),
                   "fornecedor": self.fornecedor.currentText().split("(")[1].split(")")[0],
                   "categoria_equipamento": self.categoria_equipamento.currentText().split("(")[1].split(")")[0],
                   "descricao_completa": self.descricao_completa.toPlainText(),
                   "codigo": self.codigo.text()}
            if(sql.SQL().produto_alterar(SQL)):
                QtWidgets.QMessageBox.information(None, "CADASTRO EQUIPAMENTOS - ASSISTENCIA TECNICA DE MANUNTEÇÃO",
                                                     "PRODUTO <b>{}</b> ALTERADO COM SUCESSO!".format(self.descricao.text()))
                self.Janela.close()


    def pegar_categoria(self, categoria):
        for cat in range(self.categoria_equipamento.count()):
            try:
                if(self.categoria_equipamento.itemText(cat).split('(')[1].split(')')[0] == str(categoria)): return cat
            except: pass


    def pegar_fornecedor(self, categoria):
        for cat in range(self.fornecedor.count()):
            try:
                if(self.fornecedor.itemText(cat).split('(')[1].split(')')[0] == str(categoria)): return cat
            except: pass


    def abrir_consulta_categoria(self):
        Form = QtWidgets.QDialog()
        ui = Consulta_produtos()
        ui.setupUi(Form)
        Form.exec_()
        if(ui.produto_selecionado != False):
            self.carregar_alteracao(ui.produto_selecionado)


    def descricao_maiscula(self): self.descricao.setText(self.descricao.text().upper())


    def carregar_for(self):
        self.fornecedor.clear()
        self.fornecedor.addItem("SELECIONE FORNECEDOR")
        for forn in sql.SQL().pegar_fornecedores():self.fornecedor.addItem("{}({})".format(forn[1], forn[0]))

    def carregar_cat(self):
        self.categoria_equipamento.clear()
        self.categoria_equipamento.addItem("SELECIONE CATEGORIA")
        for cate in sql.SQL().pegar_categorias_produtos():self.categoria_equipamento.addItem("{}({})".format(cate[1], cate[0]))


    def carregar_eventos(self):
        self.sair.clicked.connect(self.Janela.close)
        self.cadastrar.clicked.connect(self.cadastra)
        self.add_categoria.clicked.connect(self.cadastra_categoria)
        self.add_fornecedor.clicked.connect(self.cadastra_fornecedor)


    def cadastra_categoria(self):
        self.Form = QtWidgets.QDialog()
        self.ui = Categorias()
        self.ui.setupUi(self.Form)
        self.Form.exec()
        self.carregar_cat()


    def cadastra_fornecedor(self):
        self.Form = QtWidgets.QDialog()
        self.ui = Fornecedores()
        self.ui.setupUi(self.Form)
        self.Form.exec()
        self.carregar_for()


    def cadastra(self):
        if(self.verifica_preenchimento()):
            SQL = {"descricao": self.descricao.text(),
                    "unidade": self.tipo_unidade.currentIndex(),
                    "fornecedor": self.fornecedor.currentText().split("(")[1].split(")")[0],
                    "categoria_equipamento": self.categoria_equipamento.currentText().split("(")[1].split(")")[0],
                    "descricao_completa": self.descricao_completa.toPlainText()}
            sql.SQL().inserir_produtos(SQL)
            self.limpar_campos()


    def limpar_campos(self):
            QtWidgets.QMessageBox.information(None,"CADASTRO PRODUTO - SISTEMA MANUNTEÇÃO",
                                                   "PRODUTO <b>{}</b>".format(self.descricao.text()))
            [campo.clear() for campo in [self.descricao, self.descricao_completa]]
            [campo.setCurrentIndex(0) for campo in [self.fornecedor, self.categoria_equipamento]]
            self.codigo.setText(str(int(self.codigo.text()) + 1))


    def verifica_preenchimento(self):
        if(self.descricao.text() == ""): self.descricao.setFocus(True); return
        if(self.descricao_completa.toPlainText() == ""): self.descricao_completa.setFocus(True); return
        lista = [self.fornecedor, self.categoria_equipamento]
        for campo in lista:
            if(campo.currentIndex() == 0):
                QtWidgets.QMessageBox.information(None, "CADASTRO PRODUTO - SISTEMA MANUNTEÇÃO", "CAMPO NÃO FOI SELECIONADO!")
                campo.setFocus(True)
                return False
        return True


import recursos


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Produtos()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
