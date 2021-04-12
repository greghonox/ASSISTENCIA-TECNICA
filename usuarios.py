# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SUPORTE05\Documents\Meus Programas\apps\ASSISTENCIA TECNICA\UI\usuarios.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
from consulta_usuario import Consulta_usuarios
from PyQt5 import QtCore, QtGui, QtWidgets

import sql
class Usuarios(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(720, 412)
        Form.setMinimumSize(QtCore.QSize(720, 412))
        Form.setMaximumSize(QtCore.QSize(720, 412))
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
"image: url(:/img/usuario.jpg);\n"
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
"\n"
"QToolButton:hover:pressed{\n"
"    background-color: rgb(84, 167, 216);\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"    background-color: rgb(1, 92, 146);\n"
"}\n"
"\n"
"QCheckBox{\n"
"    color: rgb(1, 92, 146);    \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:pressed{      \n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QCheckBox:hover{\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"#label_5, #label_6, #label_7, #label_8 {    \n"
"    background-color: rgba(255, 255, 255, 0);    \n"
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
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.codigo = QtWidgets.QLineEdit(self.groupBox)
        self.codigo.setEnabled(False)
        self.codigo.setClearButtonEnabled(True)
        self.codigo.setObjectName("codigo")
        self.horizontalLayout_2.addWidget(self.codigo)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.cpf = QtWidgets.QLineEdit(self.groupBox)
        self.cpf.setClearButtonEnabled(True)
        self.cpf.setObjectName("cpf")
        self.horizontalLayout_3.addWidget(self.cpf)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.nome = QtWidgets.QLineEdit(self.groupBox)
        self.nome.setClearButtonEnabled(True)
        self.nome.setObjectName("nome")
        self.horizontalLayout_5.addWidget(self.nome)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.senha = QtWidgets.QLineEdit(self.groupBox)
        self.senha.setMaxLength(10)
        self.senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senha.setClearButtonEnabled(True)
        self.senha.setObjectName("senha")
        self.horizontalLayout_7.addWidget(self.senha)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setContentsMargins(-1, 18, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_15.addWidget(self.label_9)
        self.telefone = QtWidgets.QLineEdit(self.groupBox_3)
        self.telefone.setClearButtonEnabled(True)
        self.telefone.setObjectName("telefone")
        self.telefone.setInputMask("(999)99999-9999")
        self.horizontalLayout_15.addWidget(self.telefone)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_16.addWidget(self.label_10)
        self.whatsapp = QtWidgets.QLineEdit(self.groupBox_3)
        self.whatsapp.setClearButtonEnabled(True)
        self.whatsapp.setObjectName("whatsapp")
        self.whatsapp.setInputMask("(999)99999-9999")
        self.horizontalLayout_16.addWidget(self.whatsapp)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_16)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_17.addWidget(self.label_11)
        self.email = QtWidgets.QLineEdit(self.groupBox_3)
        self.email.setClearButtonEnabled(True)
        self.email.setObjectName("email")
        self.horizontalLayout_17.addWidget(self.email)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tecnico = QtWidgets.QCheckBox(self.groupBox_2)
        self.tecnico.setEnabled(True)
        self.tecnico.setCheckable(True)
        self.tecnico.setChecked(False)
        self.tecnico.setObjectName("tecnico")
        self.horizontalLayout.addWidget(self.tecnico)
        self.vendedor = QtWidgets.QCheckBox(self.groupBox_2)
        self.vendedor.setObjectName("vendedor")
        self.horizontalLayout.addWidget(self.vendedor)
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
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.cadastrar = QtWidgets.QPushButton(self.groupBox_4)
        self.cadastrar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cadastrar.setIcon(icon1)
        self.cadastrar.setIconSize(QtCore.QSize(41, 52))
        self.cadastrar.setFlat(True)
        self.cadastrar.setObjectName("cadastrar")
        self.verticalLayout_6.addWidget(self.cadastrar)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.procurar = QtWidgets.QPushButton(self.groupBox_4)
        self.procurar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/find-my-friend.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.procurar.setIcon(icon2)
        self.procurar.setIconSize(QtCore.QSize(41, 52))
        self.procurar.setFlat(True)
        self.procurar.setObjectName("procurar")
        self.verticalLayout_6.addWidget(self.procurar)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setEnabled(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.excluir = QtWidgets.QPushButton(self.groupBox_4)
        self.excluir.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.excluir.setIcon(icon3)
        self.excluir.setIconSize(QtCore.QSize(41, 52))
        self.excluir.setFlat(True)
        self.excluir.setObjectName("excluir")
        self.verticalLayout_6.addWidget(self.excluir)
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.sair = QtWidgets.QPushButton(self.groupBox_4)
        self.sair.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/cross.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sair.setIcon(icon4)
        self.sair.setIconSize(QtCore.QSize(41, 52))
        self.sair.setFlat(True)
        self.sair.setObjectName("sair")
        self.verticalLayout_6.addWidget(self.sair)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.horizontalLayout_21.addWidget(self.frame_2)
        self.verticalLayout_7.addWidget(self.principal)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CADASTRO USUARIOS - ASSISTENCIA TECNICA DE MANUNTEÇÃO"))
        self.groupBox.setTitle(_translate("Form", "DADOS"))
        self.label.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">CÓDIGO DO USUÁRIO</span></p></body></html>"))
        self.label.setText(_translate("Form", "CÓDIGO"))
        self.codigo.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">CÓDIGO DO USUÁRIO</span></p></body></html>"))
        self.label_2.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">DOCUMENTO CPF DO USUÁRIO</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "CPF"))
        self.cpf.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">DOCUMENTO CPF DO USUÁRIO</span></p></body></html>"))
        self.cpf.setInputMask(_translate("Form", "999.999.999-99"))
        self.label_3.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">NOME DO USUÁRIO NÃO PODE SER IGUAL A OUTRO</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "NOME"))
        self.nome.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">NOME DO USUÁRIO NÃO PODE SER IGUAL A OUTRO</span></p></body></html>"))
        self.label_4.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">SENHA LIVRE DE NO MÁXIMO 10 DIGITOS</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "SENHA"))
        self.senha.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">SENHA LIVRE DE NO MÁXIMO 10 DIGITOS</span></p></body></html>"))
        self.senha.setPlaceholderText(_translate("Form", "**************"))
        self.groupBox_3.setTitle(_translate("Form", "CONTATO"))
        self.label_9.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">CONTATO DO USUÁRIO</span></p></body></html>"))
        self.label_9.setText(_translate("Form", "TELEFONE"))
        self.telefone.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">CONTATO DO USUÁRIO</span></p></body></html>"))
        self.label_10.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">CONTATO DO USUÁRIO</span></p></body></html>"))
        self.label_10.setText(_translate("Form", "WHASTAPP"))
        self.whatsapp.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">CONTATO DO USUÁRIO</span></p></body></html>"))
        self.label_11.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">CONTATO DO USUÁRIO</span></p></body></html>"))
        self.label_11.setText(_translate("Form", "E-MAIL"))
        self.email.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">CONTATO DO USUÁRIO</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("Form", "TIPO USUÁRIO"))
        self.tecnico.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">SELECIONE O TIPO DE USUÁRIO</span></p></body></html>"))
        self.tecnico.setText(_translate("Form", "TECNICO"))
        self.vendedor.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">SELECIONE O TIPO DE USUÁRIO</span></p></body></html>"))
        self.vendedor.setText(_translate("Form", "VENDEDOR"))
        self.label_5.setText(_translate("Form", "CADASTRAR"))
        self.label_6.setText(_translate("Form", "PROCURAR"))
        self.label_7.setText(_translate("Form", "EXCLUIR"))
        self.label_8.setText(_translate("Form", "SAIR"))
        self.Janela = Form
        self.carregar_eventos()


    def carregar_eventos(self):
        self.sair.clicked.connect(self.Janela.close)
        self.cadastrar.clicked.connect(self.cadastra)
        self.codigo.setText(str(sql.SQL().pegar_codigo_usuario() + 1))

        self.procurar.clicked.connect(self.abrir_consulta_categoria)
        self.nome.textChanged.connect(self.nome_maisculo)
        self.email.textChanged.connect(self.email_maisculo)


    def nome_maisculo(self): self.nome.setText(self.nome.text().upper())
    def email_maisculo(self): self.email.setText(self.email.text().upper())


    def abrir_consulta_categoria(self):
        Form = QtWidgets.QDialog()
        ui = Consulta_usuarios()
        ui.setupUi(Form)
        Form.exec_()

        if(ui.usuario_selecionado != False):
            self.carregar_usuario(ui.usuario_selecionado)


    def carregar_usuario(self, usuario):
        dados = sql.SQL().pegar_usuario_todos(usuario)[0]
        self.codigo.setText(str(dados[0]))
        self.cpf.setText(str(dados[1]))
        self.nome.setText(str(dados[2]))
        self.senha.setText(str(dados[3]))
        self.telefone.setText(str(dados[4]))
        self.whatsapp.setText(str(dados[5]))
        self.email.setText(str(dados[6]))

        tec, ven = (False, False) if(dados[7] == 0) else (False, True) if(dados[7] == 1) else (True, False) if(dados[7] == 2) else (True, True)
        self.vendedor.setChecked(ven)
        self.tecnico.setChecked(tec)

        self.label_5.setText("ALTERAR")
        self.cadastrar.disconnect()
        self.cadastrar.clicked.connect(self.alterar_usuario)
        self.excluir.disconnect()
        self.excluir.clicked.connect(self.desativar_usuario)


    def pegar_estado(self, estado):
        for estados in range(0, self.estado.count()):
            if(self.estado.itemText(estados).upper() == estado): return estados


    def desativar_usuario(self):
        msg = QtWidgets.QMessageBox.question(None, "CADASTRO USUARIOS - ASSISTENCIA TECNICA DE MANUNTEÇÃO",\
                                                 "DESEJA DESATIVAR O USUARIO <b>{}?</b>".format(self.nome.text()))
        if(msg == QtWidgets.QMessageBox.Yes):
            if(sql.SQL().desativar_usuario({"codigo": self.codigo.text()})):
                QtWidgets.QMessageBox.information(None, "CADASTRO USUARIOS - ASSISTENCIA TECNICA DE MANUNTEÇÃO",\
                                                  "USUARIO <b>{}</b> DESATIVADO COM SUCESSO!".format(self.nome.text()))
                self.Janela.close()


    def alterar_usuario(self):
        msg = QtWidgets.QMessageBox.question(None, "CADASTRO USUARIOS - ASSISTENCIA TECNICA DE MANUNTEÇÃO",\
                                         "DESEJA ALTERAR O USUARIO <b>{}?</b>".format(self.nome.text()))
        if(msg == QtWidgets.QMessageBox.Yes):
            SQL = {"cpf": self.cpf.text(),
                   "nome": self.nome.text(),
                   "senha": self.senha.text(),
                   "telefone": self.telefone.text(),
                   "whastapp": self.whatsapp.text(),
                   "email": self.email.text(),
                   "codigo": self.codigo.text(),
                   "tipo_funcionario": 3 if(self.vendedor.isChecked() and self.tecnico.isChecked()) else \
                                       2 if(self.tecnico.isChecked()) else \
                                       1 if(self.vendedor.isChecked()) else 0}
            if(sql.SQL().alterar_usuario(SQL)):
                QtWidgets.QMessageBox.information(None, "CADASTRO USUARIOS - ASSISTENCIA TECNICA DE MANUNTEÇÃO",\
                                                  "ALTERADO O USUARIO <b>{}</b> COM SUCESSO!".format(self.nome.text()))
                self.Janela.close()


    def verifica_preenchimento(self):
        lista = [ self.cpf, self.telefone, self.whatsapp, self.nome, self.senha,
                 self.email]
        for cont, entrada in enumerate(lista):
            if(entrada.text() == "" or entrada.text() == "..-" or entrada.text() == "()-"):
                entrada.setFocus(True)
                return False
        return True


    def cadastra(self):
        if(self.verifica_preenchimento()):
            SQL = {"cpf": self.cpf.text(),
                   "nome": self.nome.text(),
                   "senha": self.senha.text(),
                   "telefone": self.telefone.text(),
                   "whastapp": self.whatsapp.text(),
                   "email": self.email.text(),
                   "tipo_funcionario": 3 if(self.vendedor.isChecked() and self.tecnico.isChecked()) else \
                                       2 if(self.tecnico.isChecked()) else \
                                       1 if(self.vendedor.isChecked()) else 0}
            if(sql.SQL().inserir_usuarios(SQL)):  self.limpar_campos()


    def limpar_campos(self):
        QtWidgets.QMessageBox.information(None, "CADASTRO USUARIO - SISTEMA ASSISTENCIA TECNICA",
        "CADASTRO REALISADO COM SUCESSO DO USUARIO (<b>{}</b>)!"
        .format(self.nome.text()))

        [campo.clear() for campo in [self.nome, self.cpf, self.senha, self.telefone, self.whatsapp, self.email]]
        [campo.setChecked(False) for campo in [self.tecnico, self.vendedor]]
        self.codigo.setText(str(int(self.codigo.text()) + 1))

import recursos

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Usuarios()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
