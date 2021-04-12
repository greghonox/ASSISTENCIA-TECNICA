# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SUPORTE05\Documents\Meus Programas\apps\ASSISTENCIA TECNICA\UI\servicos.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import sql
from categorias import Categorias
from PyQt5 import QtCore, QtGui, QtWidgets
from consulta_servicos import Consulta_servicos


class Servicos(object):
    def setupUi(self, Form):
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
"QLabel{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"#label_15,#label_16,#label_17, #label_14{    \n"
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
        self.tipo_unidade.setMinimumSize(QtCore.QSize(200, 0))
        self.tipo_unidade.setObjectName("tipo_unidade")
        self.tipo_unidade.addItem("")
        self.tipo_unidade.addItem("")
        self.tipo_unidade.addItem("")
        self.horizontalLayout_5.addWidget(self.tipo_unidade)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.valor_servico = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.valor_servico.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.valor_servico.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.valor_servico.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.valor_servico.setProperty("showGroupSeparator", True)
        self.valor_servico.setMaximum(999.99)
        self.valor_servico.setObjectName("valor_servico")
        self.horizontalLayout_5.addWidget(self.valor_servico)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/add-round-button-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.groupBox_5 = QtWidgets.QGroupBox(self.principal)
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.cadastrar = QtWidgets.QPushButton(self.groupBox_5)
        self.cadastrar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cadastrar.setIcon(icon2)
        self.cadastrar.setIconSize(QtCore.QSize(41, 52))
        self.cadastrar.setFlat(True)
        self.cadastrar.setObjectName("cadastrar")
        self.verticalLayout_8.addWidget(self.cadastrar)
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_8.addWidget(self.label_14)
        self.procurar = QtWidgets.QPushButton(self.groupBox_5)
        self.procurar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/find-my-friend.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.procurar.setIcon(icon3)
        self.procurar.setIconSize(QtCore.QSize(41, 52))
        self.procurar.setFlat(True)
        self.procurar.setObjectName("procurar")
        self.verticalLayout_8.addWidget(self.procurar)
        self.label_15 = QtWidgets.QLabel(self.groupBox_5)
        self.label_15.setEnabled(False)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_8.addWidget(self.label_15)
        self.excluir = QtWidgets.QPushButton(self.groupBox_5)
        self.excluir.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.excluir.setIcon(icon4)
        self.excluir.setIconSize(QtCore.QSize(41, 52))
        self.excluir.setFlat(True)
        self.excluir.setObjectName("excluir")
        self.verticalLayout_8.addWidget(self.excluir)
        self.label_16 = QtWidgets.QLabel(self.groupBox_5)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_8.addWidget(self.label_16)
        self.sair = QtWidgets.QPushButton(self.groupBox_5)
        self.sair.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/cross.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sair.setIcon(icon5)
        self.sair.setIconSize(QtCore.QSize(41, 52))
        self.sair.setFlat(True)
        self.sair.setObjectName("sair")
        self.verticalLayout_8.addWidget(self.sair)
        self.label_17 = QtWidgets.QLabel(self.groupBox_5)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_8.addWidget(self.label_17)
        self.horizontalLayout_21.addWidget(self.groupBox_5)
        self.verticalLayout_7.addWidget(self.principal)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CADASTRO SERVIÇOS - ASSISTENCIA TECNICA DE MANUNTEÇÃO"))
        self.groupBox.setTitle(_translate("Form", "IDENTIFICAÇÃO"))
        self.label.setText(_translate("Form", "CÓDIGO"))
        self.label_2.setText(_translate("Form", "DESCRIÇÃO"))
        self.label_4.setText(_translate("Form", "FORMA"))
        self.tipo_unidade.setItemText(0, _translate("Form", "FORMA COBRANÇA"))
        self.tipo_unidade.setItemText(1, _translate("Form", "HORA"))
        self.tipo_unidade.setItemText(2, _translate("Form", "SERVIÇO"))
        self.label_3.setText(_translate("Form", "VALOR"))
        self.valor_servico.setSuffix(_translate("Form", "R$"))
        self.groupBox_2.setTitle(_translate("Form", "CARACTERISTICAS"))
        self.label_5.setText(_translate("Form", "CATEGORIA"))
        self.categoria_equipamento.setItemText(0, _translate("Form", "SELECIONE O TIPO SERVIÇO"))
        self.groupBox_3.setTitle(_translate("Form", "DESCRIÇÃO COMPLETA"))
        self.descricao_completa.setPlaceholderText(_translate("Form", "DESCREVA UM RESUMO SOBRE ESSE SERVIÇO"))
        self.label_14.setText(_translate("Form", "CADASTRAR"))
        self.label_15.setText(_translate("Form", "PROCURAR"))
        self.label_16.setText(_translate("Form", "EXCLUIR"))
        self.label_17.setText(_translate("Form", "SAIR"))
        self.Janela = Form
        self.carregar_eventos()
        self.carregar_cat()

    def carregar_eventos(self):
        self.sair.clicked.connect(self.Janela.close)
        self.add_categoria.clicked.connect(self.cadastra_categoria)
        self.cadastrar.clicked.connect(self.cadatra)
        self.codigo.setText(str(sql.SQL().pegar_codigo_servicos() + 1))
        self.descricao.textChanged.connect(self.descricao_maiscula)
        self.procurar.clicked.connect(self.abrir_consulta_servicos)


    def abrir_consulta_servicos(self):
        Form = QtWidgets.QDialog()
        ui = Consulta_servicos()
        ui.setupUi(Form)
        Form.exec()
        if(ui.servico_selecionado != False):
            self.carregar_servicos(ui.servico_selecionado)


    def carregar_servicos(self, servico):
        dados = sql.SQL().pegar_servicos_tabela_codigo(servico)[0]
        self.codigo.setText(str(dados[0]))
        self.descricao.setText(str(dados[1]))
        self.tipo_unidade.setCurrentIndex(dados[2])

        try: self.categoria_equipamento.setCurrentIndex(self.pegar_categoria(dados[3]))
        except: self.categoria_nao_encontrada(dados[3])

        self.descricao_completa.setPlainText(dados[4])
        self.valor_servico.setValue(dados[5])
        self.label_14.setText('ALTERAR')
        self.cadastrar.disconnect()
        self.cadastrar.clicked.connect(self.alterar_servico)
        self.excluir.disconnect()
        self.excluir.clicked.connect(self.desativar_servicos)

    def categoria_nao_encontrada(self, categoria):
        cat = sql.SQL().pegar_categorias_servicos_codigo(categoria)[0]
        self.categoria_equipamento.setStyleSheet("background-color: rgb(255, 0, 0);\n")
        self.categoria_equipamento.setToolTip("Á CATEGORIA ANTERIOR({}({})) FOI DESATIVADA!".format(cat[1], cat[0]))
        self.categoria_equipamento.setCurrentIndex(0)


    def desativar_servicos(self):
        msg = QtWidgets.QMessageBox.question(None, "CADASTRO SERVIÇOS - ASSISTENCIA TECNICA DE MANUNTEÇÃO",\
                                             "<b>DESEJA REMOVER O SERVIÇO ?{}</b>".format(self.descricao.text()))
        if(msg == QtWidgets.QMessageBox.Yes):
            sql.SQL().desativar_servicos({'codigo': self.codigo.text()})
            QtWidgets.QMessageBox.information(None, "CADASTRO ESTOQUE - ASSISTENCIA TECNICA DE MANUNTEÇÃO",\
                                              "SERVIÇOS <b>{}</b> DESATIVADO COM SUCESSO!".format(self.descricao.text()))
            self.Janela.close()

    def pegar_categoria(self, cat):
        for indx in range(1, self.categoria_equipamento.count()):
            if(self.categoria_equipamento.itemText(indx).split("(")[1].split(")"[0])[0] == str(cat)): return indx


    def alterar_servico(self):
        if(self.verifica_preenchimento()):
            msg = QtWidgets.QMessageBox.question(None, "CADASTRO SERVIÇOS - ASSISTENCIA TECNICA DE MANUNTEÇÃO",\
                                                 "<b>DESEJA ALTARAR O SERVIÇO {}?</b>".format(self.descricao.text()))
            if(msg == QtWidgets.QMessageBox.Yes):
                SQL = {"descricao": self.descricao.text(),
                       "codigo": self.codigo.text(),
                       "descricao_completa": self.descricao_completa.toPlainText(),
                       "valor_servico": self.valor_servico.value(),
                       "forma_cobranca": self.tipo_unidade.currentIndex(),
                       "tipo_servico": self.categoria_equipamento.currentText().split("(")[1].split(")")[0],
                       "descricao_completa": self.descricao_completa.toPlainText()}
                sql.SQL().alterar_servicos(SQL)
                QtWidgets.QMessageBox.information(None, "CADASTRO ESTOQUE - ASSISTENCIA TECNICA DE MANUNTEÇÃO",\
                                                  "SERVIÇOS <b>{}</b> ALTERADO COM SUCESSO!".format(self.descricao.text()))
                self.Janela.close()



    def descricao_maiscula(self): self.descricao.setText(self.descricao.text().upper())


    def cadatra(self):
        if(self.verifica_preenchimento()):
            SQL = {"descricao": self.descricao.text(),
                   "descricao_completa": self.descricao_completa.toPlainText(),
                   "valor_servico": self.valor_servico.value(),
                   "forma_cobranca": self.tipo_unidade.currentIndex(),
                   "tipo_servico": self.categoria_equipamento.currentText().split("(")[1].split(")")[0],
                   "descricao_completa": self.descricao_completa.toPlainText()}
            if(sql.SQL().inserir_servicos(SQL)):
                self.limpar_dados()


    def limpar_dados(self):
        QtWidgets.QMessageBox.information(None, "CADASTRO DE SERVIÇOS - SISTEMA MANUNTEÇÃO",
                                          "SERVIÇO <b>{}</b> CADASTRADO COM SUCESSO!".format(self.descricao.text()))
        for campo in [self.tipo_unidade, self.categoria_equipamento]: campo.setCurrentIndex(0)
        for campo in [self.descricao, self.descricao_completa]: campo.clear()
        self.valor_servico.setValue(0.00)
        self.codigo.setText(str(int(self.codigo.text()) + 1))


    def verifica_preenchimento(self):
        for campo in [self.tipo_unidade, self.categoria_equipamento]:
            if(campo.currentIndex() == 0):
                QtWidgets.QMessageBox.information(None, "CADASTRO DE SERVIÇOS - SISTEMA MANUNTEÇÃO",
                                                  "PREENCHA OS CAMPOS VAZIOS")
                campo.setFocus(True)
                return
        if(self.descricao_completa.toPlainText() == ""): self.descricao_completa.setFocus(True); return
        if(self.descricao.text() == ""): self.descricao.setFocus(True); return
        if(self.valor_servico.value() == 0.0): self.valor_servico.setFocus(True)
        return True


    def cadastra_categoria(self):
        self.Form = QtWidgets.QDialog()
        self.ui = Categorias()
        self.ui.setupUi(self.Form)
        self.Form.exec()
        self.carregar_cat()


    def carregar_cat(self):
        self.categoria_equipamento.clear()
        self.categoria_equipamento.addItem("SELECIONE CATEGORIA")
        for cate in sql.SQL().pegar_categorias_servicos():self.categoria_equipamento.addItem("{}({})".format(cate[1], cate[0]))

import recursos


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Servicos()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
