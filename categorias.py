# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SUPORTE05\Documents\Meus Programas\apps\ASSISTENCIA TECNICA\UI\categorias.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import sql
from PyQt5 import QtCore, QtGui, QtWidgets
from consulta_categorias import Consulta_categorias

class Categorias(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(468, 265)
        Form.setMinimumSize(QtCore.QSize(468, 265))
        Form.setMaximumSize(QtCore.QSize(468, 265))
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
"background-image: url(:/img/fundo.jpg);\n"
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
"QLineEdit{                \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(84, 167, 216);\n"
"}\n"
"\n"
"QLineEdit:hover, QComboBox:hover{                \n"
"background-color: rgb(1, 92, 146);\n"
"}\n"
"\n"
"QLabel{    \n"
"    background-color: rgb(255, 255, 255 ,0);\n"
"}\n"
"\n"
"QRadioButton{    \n"
"    color: rgb(68, 154, 202);\n"
"}")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.principal = QtWidgets.QFrame(Form)
        self.principal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.principal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.principal.setObjectName("principal")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.principal)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.principal)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.codigo = QtWidgets.QLineEdit(self.groupBox)
        self.codigo.setEnabled(False)
        self.codigo.setMaximumSize(QtCore.QSize(93, 16777215))
        self.codigo.setClearButtonEnabled(True)
        self.codigo.setObjectName("codigo")
        self.horizontalLayout_2.addWidget(self.codigo)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.nome = QtWidgets.QLineEdit(self.groupBox)
        self.nome.setClearButtonEnabled(True)
        self.nome.setObjectName("nome")
        self.horizontalLayout_5.addWidget(self.nome)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setContentsMargins(-1, 25, 9, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.servico = QtWidgets.QRadioButton(self.groupBox_2)
        self.servico.setObjectName("servico")
        self.horizontalLayout_3.addWidget(self.servico)
        self.produto = QtWidgets.QRadioButton(self.groupBox_2)
        self.produto.setChecked(True)
        self.produto.setAutoRepeat(False)
        self.produto.setObjectName("produto")
        self.horizontalLayout_3.addWidget(self.produto)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.frame_2 = QtWidgets.QFrame(self.principal)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cadastrar = QtWidgets.QPushButton(self.frame_2)
        self.cadastrar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cadastrar.setIcon(icon1)
        self.cadastrar.setIconSize(QtCore.QSize(45, 40))
        self.cadastrar.setDefault(False)
        self.cadastrar.setFlat(True)
        self.cadastrar.setObjectName("cadastrar")
        self.horizontalLayout.addWidget(self.cadastrar)
        self.procurar = QtWidgets.QPushButton(self.frame_2)
        self.procurar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/find-my-friend.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.procurar.setIcon(icon2)
        self.procurar.setIconSize(QtCore.QSize(45, 40))
        self.procurar.setDefault(False)
        self.procurar.setFlat(True)
        self.procurar.setObjectName("procurar")
        self.horizontalLayout.addWidget(self.procurar)
        self.excluir = QtWidgets.QPushButton(self.frame_2)
        self.excluir.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/eraser.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.excluir.setIcon(icon3)
        self.excluir.setIconSize(QtCore.QSize(45, 40))
        self.excluir.setDefault(False)
        self.excluir.setFlat(True)
        self.excluir.setObjectName("excluir")
        self.horizontalLayout.addWidget(self.excluir)
        self.sair = QtWidgets.QPushButton(self.frame_2)
        self.sair.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/cross.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sair.setIcon(icon4)
        self.sair.setIconSize(QtCore.QSize(45, 40))
        self.sair.setDefault(False)
        self.sair.setFlat(True)
        self.sair.setObjectName("sair")
        self.horizontalLayout.addWidget(self.sair)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.verticalLayout_7.addWidget(self.principal)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CADASTRO CATEGORIAS - ASSISTENCIA TECNICA DE MANUNTEÇÃO"))
        self.label.setToolTip(_translate("Form", "<html><head/><body><p>CÓDIGO DA CATEGORIA</p></body></html>"))
        self.label.setText(_translate("Form", "CÓDIGO"))
        self.codigo.setToolTip(_translate("Form", "<html><head/><body><p>CÓDIGO DA CATEGORIA</p></body></html>"))
        self.label_3.setToolTip(_translate("Form", "<html><head/><body><p>NOME DA CATEGÓRIA</p></body></html>"))
        self.label_3.setText(_translate("Form", "NOME"))
        self.nome.setToolTip(_translate("Form", "<html><head/><body><p>NOME DA CATEGÓRIA</p></body></html>"))
        self.groupBox_2.setTitle(_translate("Form", "TIPO CATEGORIA"))
        self.servico.setText(_translate("Form", "SERVIÇO"))
        self.produto.setText(_translate("Form", "PRODUTO"))
        self.Janela = Form
        self.carregar_eventos()

    def carregar_eventos(self):
        self.sair.clicked.connect(self.Janela.close)
        self.cadastrar.clicked.connect(self.cadastra)
        self.codigo.setText(str(sql.SQL().pegar_codigo_categorias() + 1))
        self.servico.clicked.connect(self.focar)
        self.produto.clicked.connect(self.focar)
        self.procurar.clicked.connect(self.abrir_consulta_categoria)


    def abrir_consulta_categoria(self):
        Form = QtWidgets.QDialog()
        ui = Consulta_categorias()
        ui.setupUi(Form)
        Form.exec_()
        if(ui.categoria_selecionado != False):
            self.carregar_categoria(ui.categoria_selecionado)


    def carregar_categoria(self, categoria):
        dados = sql.SQL().pegar_categorias_servicos_codigo(categoria)[0]
        self.codigo.setText(str(dados[0]))
        self.nome.setText(str(dados[1]))
        produto, servico = (False, True) if(dados[2] == 1) else (True, False)
        self.servico.setChecked(servico)
        self.produto.setChecked(produto)
        self.cadastrar.disconnect()
        self.cadastrar.clicked.connect(self.alterar_categoria)
        self.excluir.disconnect()
        self.excluir.clicked.connect(self.desativar_categoria)

    def desativar_categoria(self):
        msg = QtWidgets.QMessageBox.question(None, "CADASTRO CATEGORIAS - ASSISTENCIA TECNICA DE MANUNTEÇÃO",\
                                             "<b>DESEJA DESATIVAR A CATEGORIA {}?</b>".format(self.nome.text()))
        if(msg == QtWidgets.QMessageBox.Yes):
            if(sql.SQL().categoria_desativar({"codigo": self.codigo.text()})):
                QtWidgets.QMessageBox.information(None, "CADASTRO CATEGORIAS - ASSISTENCIA TECNICA DE MANUNTEÇÃO",\
                                                  "<b>CATEGORIA {} DESATIVADA COM SUCESSO!</b>".format(self.nome.text()))
                self.Janela.close()


    def alterar_categoria(self):
        msg = QtWidgets.QMessageBox.question(None, "CADASTRO CATEGORIAS - ASSISTENCIA TECNICA DE MANUNTEÇÃO",\
                                             "<b>DESEJA ALTERAR A CATEGORIA {}?</b>".format(self.nome.text()))
        if(msg == QtWidgets.QMessageBox.Yes):
            SQL = {"nome": self.nome.text(),
            "codigo": self.codigo.text(),
            "tipo_servicos": 0 if(self.produto.isChecked()) else 1}
            if(sql.SQL().categoria_alterar(SQL)):
                QtWidgets.QMessageBox.information(None, "CADASTRO CATEGORIAS - ASSISTENCIA TECNICA DE MANUNTEÇÃO",\
                                                  "<b>ALTERADO A CATEGORIA {} COM SUCESSO!</b>".format(self.nome.text()))
                self.Janela.close()


    def focar(self): self.nome.setFocus(True)


    def cadastra(self):
        if(self.nome.text() != ""):
            SQL = {"nome": self.nome.text(),
                   "tipo_servicos": 0 if(self.produto.isChecked()) else 1}
            sql.SQL().inserir_categorias(SQL)
            pr_sr = "PRODUTO" if(self.produto.isChecked()) else "SERVIÇO"
            QtWidgets.QMessageBox.information(None, "CADASTRO CATEGORIAS PRODUTOS/SERVIÇOS - SISTEMA ASSISTENCIA TECNICA",
                                             "CADASTRADO {} <b>{}</b> COM SUCESSO!".format(pr_sr, self.nome.text()))
            self.nome.clear()
            self.codigo.setText(str(int(self.codigo.text()) + 1))

import recursos


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Categorias()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
