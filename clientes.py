# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SUPORTE05\Documents\Meus Programas\apps\ASSISTENCIA TECNICA\UI\clientes.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import sql
import pegar_cep
from PyQt5 import QtCore, QtGui, QtWidgets
from consulta_cliente import Consulta_cliente

class Clientes(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(810, 428)
        Form.setMinimumSize(QtCore.QSize(810, 428))
        Form.setMaximumSize(QtCore.QSize(810, 428))
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
"    background-image: url(:/img/cliente.jpg);\n"
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
"#label_14, #label_15, #label_16, #label_17{    \n"
"    background-color: rgba(255, 255, 255, 0);    \n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
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
        self.documento = QtWidgets.QLineEdit(self.groupBox)
        self.documento.setClearButtonEnabled(True)
        self.documento.setObjectName("documento")
        self.horizontalLayout_3.addWidget(self.documento)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cpf = QtWidgets.QRadioButton(self.groupBox)
        self.cpf.setChecked(True)
        self.cpf.setObjectName("cpf")
        self.horizontalLayout_6.addWidget(self.cpf)
        self.cnpj = QtWidgets.QRadioButton(self.groupBox)
        self.cnpj.setObjectName("cnpj")
        self.horizontalLayout_6.addWidget(self.cnpj)
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
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addWidget(self.groupBox)
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
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setContentsMargins(9, 18, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_12.addWidget(self.label_7)
        self.cidade = QtWidgets.QLineEdit(self.groupBox_2)
        self.cidade.setClearButtonEnabled(True)
        self.cidade.setObjectName("cidade")
        self.horizontalLayout_12.addWidget(self.cidade)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.cep = QtWidgets.QLineEdit(self.groupBox_2)
        self.cep.setClearButtonEnabled(True)
        self.cep.setObjectName("cep")
        self.horizontalLayout_10.addWidget(self.cep)
        self.bt_cep = QtWidgets.QPushButton(self.groupBox_2)
        self.bt_cep.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/usb.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_cep.setIcon(icon1)
        self.bt_cep.setObjectName("bt_cep")
        self.horizontalLayout_10.addWidget(self.bt_cep)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_19.addWidget(self.label_12)
        self.complemento = QtWidgets.QLineEdit(self.groupBox_2)
        self.complemento.setClearButtonEnabled(True)
        self.complemento.setObjectName("complemento")
        self.horizontalLayout_19.addWidget(self.complemento)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_20.addWidget(self.label_13)
        self.estado = QtWidgets.QComboBox(self.groupBox_2)
        self.estado.setMinimumSize(QtCore.QSize(122, 0))
        self.estado.setEditable(False)
        self.estado.setObjectName("estado")
        self.estado.addItem("")
        self.horizontalLayout_20.addWidget(self.estado)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_20)
        self.verticalLayout_3.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.rua = QtWidgets.QLineEdit(self.groupBox_2)
        self.rua.setClearButtonEnabled(True)
        self.rua.setObjectName("rua")
        self.horizontalLayout_8.addWidget(self.rua)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.numero = QtWidgets.QLineEdit(self.groupBox_2)
        self.numero.setClearButtonEnabled(True)
        self.numero.setObjectName("numero")
        self.horizontalLayout_9.addWidget(self.numero)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_11.addWidget(self.label_6)
        self.bairro = QtWidgets.QLineEdit(self.groupBox_2)
        self.bairro.setClearButtonEnabled(True)
        self.bairro.setObjectName("bairro")
        self.horizontalLayout_11.addWidget(self.bairro)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.horizontalLayout_21.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.principal)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.cadastrar = QtWidgets.QPushButton(self.groupBox_4)
        self.cadastrar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cadastrar.setIcon(icon2)
        self.cadastrar.setIconSize(QtCore.QSize(41, 52))
        self.cadastrar.setFlat(True)
        self.cadastrar.setObjectName("cadastrar")
        self.verticalLayout_7.addWidget(self.cadastrar)
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_7.addWidget(self.label_14)
        self.procurar = QtWidgets.QPushButton(self.groupBox_4)
        self.procurar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/find-my-friend.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.procurar.setIcon(icon3)
        self.procurar.setIconSize(QtCore.QSize(41, 52))
        self.procurar.setFlat(True)
        self.procurar.setObjectName("procurar")
        self.verticalLayout_7.addWidget(self.procurar)
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setEnabled(False)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_7.addWidget(self.label_15)
        self.excluir = QtWidgets.QPushButton(self.groupBox_4)
        self.excluir.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.excluir.setIcon(icon4)
        self.excluir.setIconSize(QtCore.QSize(41, 52))
        self.excluir.setFlat(True)
        self.excluir.setObjectName("excluir")
        self.verticalLayout_7.addWidget(self.excluir)
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_7.addWidget(self.label_16)
        self.sair = QtWidgets.QPushButton(self.groupBox_4)
        self.sair.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/cross.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sair.setIcon(icon5)
        self.sair.setIconSize(QtCore.QSize(41, 52))
        self.sair.setFlat(True)
        self.sair.setObjectName("sair")
        self.verticalLayout_7.addWidget(self.sair)
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_7.addWidget(self.label_17)
        self.verticalLayout_6.addWidget(self.groupBox_4)
        self.horizontalLayout_21.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.principal)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_21.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.principal)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CADASTRO CLIENTES - ASSISTENCIA TECNICA DE MANUNTEÇÃO"))
        self.groupBox.setTitle(_translate("Form", "DADOS"))
        self.label.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">CÓDIGO DO CLIENTE</span></p></body></html>"))
        self.label.setText(_translate("Form", "CÓDIGO"))
        self.codigo.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">CÓDIGO DO CLIENTE</span></p></body></html>"))
        self.label_2.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">DOCUMENTO DO CLIENTE</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "CPF/CNPJ"))
        self.documento.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">DOCUMENTO DO CLIENTE</span></p></body></html>"))
        self.documento.setInputMask(_translate("Form", "999.999.999-99"))
        self.cpf.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">DOCUMENTO CPF DO CLIENTE</span></p></body></html>"))
        self.cpf.setText(_translate("Form", "CPF"))
        self.cnpj.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">DOCUMENTO CNPJ DO CLIENTE</span></p></body></html>"))
        self.cnpj.setText(_translate("Form", "CNPJ"))
        self.label_3.setToolTip(_translate("Form", "<html><head/><body><p>NOME COMPLETO DO CLIENTE</p></body></html>"))
        self.label_3.setText(_translate("Form", "NOME"))
        self.nome.setToolTip(_translate("Form", "<html><head/><body><p>NOME COMPLETO DO CLIENTE</p></body></html>"))
        self.groupBox_3.setTitle(_translate("Form", "CONTATO"))
        self.label_9.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">CONTATO DO CLIENTE</span></p></body></html>"))
        self.label_9.setText(_translate("Form", "TELEFONE"))
        self.telefone.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">CONTATO DO CLIENTE</span></p></body></html>"))
        self.telefone.setInputMask(_translate("Form", "(999)99999-9999"))
        self.label_10.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">CONTATO DO CLIENTE</span></p></body></html>"))
        self.label_10.setText(_translate("Form", "WHASTAPP"))
        self.whatsapp.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">CONTATO DO CLIENTE</span></p></body></html>"))
        self.whatsapp.setInputMask(_translate("Form", "(999)99999-9999"))
        self.label_11.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">CONTATO DO CLIENTE</span></p></body></html>"))
        self.label_11.setText(_translate("Form", "E-MAIL"))
        self.email.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">CONTATO DO CLIENTE</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("Form", "ENDEREÇO"))
        self.label_7.setToolTip(_translate("Form", "<html><head/><body><p>ENDEREÇO DO CLIENTE</p></body></html>"))
        self.label_7.setText(_translate("Form", "CIDADE"))
        self.cidade.setToolTip(_translate("Form", "<html><head/><body><p>ENDEREÇO DO CLIENTE</p></body></html>"))
        self.label_8.setText(_translate("Form", "CEP"))
        self.cep.setInputMask(_translate("Form", "99.999.999"))
        self.bt_cep.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">PREENCHA O CEP E CLIQUE AQUI PARA PREENCHER O RESTANTE</span></p></body></html>"))
        self.label_12.setToolTip(_translate("Form", "<html><head/><body><p>ENDEREÇO DO CLIENTE</p></body></html>"))
        self.label_12.setText(_translate("Form", "COMPLEMENTO"))
        self.complemento.setToolTip(_translate("Form", "<html><head/><body><p>ENDEREÇO DO CLIENTE</p></body></html>"))
        self.label_13.setToolTip(_translate("Form", "<html><head/><body><p>ENDEREÇO DO CLIENTE</p></body></html>"))
        self.label_13.setText(_translate("Form", "ESTADO"))
        self.estado.setToolTip(_translate("Form", "<html><head/><body><p>ENDEREÇO DO CLIENTE</p></body></html>"))
        self.estado.setItemText(0, _translate("Form", "SÃO PAULO"))
        self.label_4.setToolTip(_translate("Form", "<html><head/><body><p>ENDEREÇO DO CLIENTE</p></body></html>"))
        self.label_4.setText(_translate("Form", "RUA"))
        self.rua.setToolTip(_translate("Form", "<html><head/><body><p>ENDEREÇO DO CLIENTE</p></body></html>"))
        self.label_5.setToolTip(_translate("Form", "<html><head/><body><p>ENDEREÇO DO CLIENTE</p></body></html>"))
        self.label_5.setText(_translate("Form", "Nº"))
        self.numero.setToolTip(_translate("Form", "<html><head/><body><p>ENDEREÇO DO CLIENTE</p></body></html>"))
        self.label_6.setToolTip(_translate("Form", "<html><head/><body><p>ENDEREÇO DO CLIENTE</p></body></html>"))
        self.label_6.setText(_translate("Form", "BAIRRO"))
        self.bairro.setToolTip(_translate("Form", "<html><head/><body><p>ENDEREÇO DO CLIENTE</p></body></html>"))
        self.label_14.setText(_translate("Form", "CADASTRAR"))
        self.label_15.setText(_translate("Form", "PROCURAR"))
        self.label_16.setText(_translate("Form", "EXCLUIR"))
        self.label_17.setText(_translate("Form", "SAIR"))
        self.Janela = Form
        self.carregar_eventos()


    def carregar_eventos(self):
        self.sair.clicked.connect(self.Janela.close)
        self.cadastrar.clicked.connect(self.cadastra)
        self.cpf.clicked.connect(self.mudar_mascara)
        self.cnpj.clicked.connect(self.mudar_mascara)
        self.bt_cep.clicked.connect(self.preenche_cep)
        self.codigo.setText(str(sql.SQL().pegar_codigo_cliente() + 1))
        self.estado.clear()
        self.estados = ["Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal",
                        "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará", "Paraíba",
                        "Paraná" ,"Pernambuco" ,"Piauí" ,"Rio de Janeiro", "Rio Grande do Norte" ,"Rio Grande do Sul" ,"Rondônia" ,"Roraima",
                        "Santa Catarina", "Sergipe", "Tocantins", "São Paulo"]

        self.siglas = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE',
                       'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SE', 'TO', 'SP']

        for estado in self.estados: self.estado.addItem(estado)
        self.estado.setCurrentIndex(26)
        self.procurar.clicked.connect(self.abrir_consulta_categoria)
        self.maisculos()

    def maisculos(self):
         self.nome.textChanged.connect(self.nome_maisculo)
         self.email.textChanged.connect(self.email_maisculo)
         self.cidade.textChanged.connect(self.cidade_maisculo)
         self.complemento.textChanged.connect(self.complemento_maisculo)
         self.numero.textChanged.connect(self.numero_maisculo)
         self.bairro.textChanged.connect(self.bairro_maisculo)
         self.rua.textChanged.connect(self.rua_maisculo)

    def nome_maisculo(self): self.nome.setText(self.nome.text().upper())
    def email_maisculo(self): self.email.setText(self.email.text().upper())
    def cidade_maisculo(self): self.cidade.setText(self.cidade.text().upper())
    def complemento_maisculo(self): self.complemento.setText(self.complemento.text().upper())
    def numero_maisculo(self): self.numero.setText(self.numero.text().upper())
    def bairro_maisculo(self): self.bairro.setText(self.bairro.text().upper())
    def rua_maisculo(self): self.rua.setText(self.rua.text().upper())


    def abrir_consulta_categoria(self):
        Form = QtWidgets.QDialog()
        ui = Consulta_cliente()
        ui.setupUi(Form)
        Form.exec_()
        if(ui.clientes_selecionado != False):
            self.carregar_cliente(ui.clientes_selecionado)


    def carregar_cliente(self, cliente):
        dados = sql.SQL().pegar_cliente_todos(cliente)[0]
        self.codigo.setText(str(dados[0]))
        self.nome.setText(str(dados[1]))
        self.telefone.setText(str(dados[2]))
        self.whatsapp.setText(str(dados[3]))
        self.email.setText(str(dados[4]))
        self.documento.setText(str(dados[5]))
        self.cnpj.setChecked(True if(dados[6] == 1) else False)
        self.cep.setText(str(dados[7]))
        self.rua.setText(str(dados[8]))
        self.estado.setCurrentIndex(self.pegar_estado(dados[9]))
        self.numero.setText(str(dados[10]))
        self.cidade.setText(str(dados[11]))
        self.bairro.setText(str(dados[12]))
        self.complemento.setText(str(dados[13]))
        self.label_14.setText("ALTERAR")
        self.cadastrar.disconnect()
        self.cadastrar.clicked.connect(self.alterar_cliente)
        self.excluir.disconnect()
        self.excluir.clicked.connect(self.desativar_cliente)


    def desativar_cliente(self):
        msg = QtWidgets.QMessageBox.question(None, "CADASTRO CATEGORIAS - ASSISTENCIA TECNICA DE MANUNTEÇÃO",\
                                             "DESEJA DESATIVAR O CLIENTE <b>{}?</b>".format(self.nome.text()))
        if(msg == QtWidgets.QMessageBox.Yes):
            if(sql.SQL().desativar_cliente({"codigo": self.codigo.text()})):
                QtWidgets.QMessageBox.information(None, "CADASTRO CATEGORIAS - ASSISTENCIA TECNICA DE MANUNTEÇÃO",\
                                                  "<b>CLIENTE {} DESATIVADO COM SUCESSO!</b>".format(self.nome.text()))
                self.Janela.close()


    def alterar_cliente(self):
        msg = QtWidgets.QMessageBox.question(None, "CADASTRO CLIENTES - ASSISTENCIA TECNICA DE MANUNTEÇÃO",\
                                             "<b>DESEJA ALTERAR O CLIENTE {}?</b>".format(self.nome.text()))
        if(msg == QtWidgets.QMessageBox.Yes):
            SQL = {"cpf": self.documento.text(),
                   "nome": self.nome.text(),
                   "telefone": self.telefone.text(),
                   "whastapp": self.whatsapp.text(),
                   "email": self.email.text(),
                   "tipo_documento": 0 if(self.cpf.isChecked()) else 1,
                   "cidade": self.cidade.text(),
                   "cep": self.cep.text(),
                   "complemento": self.complemento.text(),
                   "estado": self.estado.currentText(),
                   "rua": self.rua.text(),
                   "numero": self.numero.text(),
                   "bairro": self.bairro.text(),
                   "codigo": self.codigo.text()}
            if(sql.SQL().alterar_cliente(SQL)):
                QtWidgets.QMessageBox.information(None, "CADASTRO CATEGORIAS - ASSISTENCIA TECNICA DE MANUNTEÇÃO",\
                                                  "<b>ALTERADO O CLIENTE {} COM SUCESSO!</b>".format(self.nome.text()))
                self.Janela.close()


    def pegar_estado(self, estado):
        for estados in range(0, self.estado.count()):
            if(self.estado.itemText(estados).upper() == estado): return estados


    def preenche_cep(self):
        PROXIES = {'https': 'https://192.168.0.254:10082/',
                    'http': 'http://192.168.0.254:10082/'}

        cep = pegar_cep.CEP(self.cep.text(), PROXIES)
        cep = cep.pegar_endereco()
        if(cep != False):
            self.bairro.setText(str(cep["bairro"]))
            self.rua.setText(str(cep["rua"]))
            self.cidade.setText(str(cep["cidade"]))
            self.estado.setCurrentIndex(self.siglas.index(cep["estado"]))
            self.numero.setFocus(True)


    def verifica_preenchimento(self):
        lista = [self.cpf, self.telefone, self.whatsapp, self.nome, self.bairro,
                 self.numero, self.email, self.documento, self.cidade, self.cep, self.rua]

        for cont, entrada in enumerate(lista):
            if(entrada.text() == "" or entrada.text() == ".." or entrada.text() == "()-"\
                or entrada.text() == "../-"):
                entrada.setFocus(True)
                return False
        return True


    def cadastra(self):
        if(self.verifica_preenchimento()):
            SQL = {"cpf": self.documento.text(),
                   "nome": self.nome.text(),
                   "telefone": self.telefone.text(),
                   "whastapp": self.whatsapp.text(),
                   "email": self.email.text(),
                   "tipo_documento": 0 if(self.cpf.isChecked()) else 1,
                   "cidade": self.cidade.text(),
                   "cep": self.cep.text(),
                   "complemento": self.complemento.text(),
                   "estado": self.estado.currentText(),
                   "rua": self.rua.text(),
                   "numero": self.numero.text(),
                   "bairro": self.bairro.text()}
            if(sql.SQL().inserir_clientes(SQL)):  self.limpar_campos()

    mascara = ""
    def mudar_mascara(self):
        if(self.cpf.isChecked()): self.documento.setInputMask("999.999.999-99"); self.mascara = "..-"
        if(self.cnpj.isChecked()): self.documento.setInputMask("99.999.999/9999-99"); self.mascara = "../-"
        self.documento.setFocus(True)


    def limpar_campos(self):
        QtWidgets.QMessageBox.information(None, "CADASTRO CLIENTES - SISTEMA ASSISTENCIA TECNICA",
        "CADASTRO REALISADO COM SUCESSO DO CLIENTE (<b>{}</b>)!"
        .format(self.nome.text()))
        lista =  [self.telefone, self.whatsapp, self.nome, self.bairro,
                 self.numero, self.email, self.documento, self.cidade, self.cep, self.rua]
        [campo.clear() for campo in lista]
        self.codigo.setText(str(int(self.codigo.text()) + 1))


import recursos


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Clientes()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
