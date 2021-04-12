# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SUPORTE05\Documents\Meus Programas\apps\ASSISTENCIA TECNICA\UI\atualizar_estoque.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Atualizar_estoque(object):
    def setupUi(self, Form, dados):
        Form.setObjectName("Form")
        Form.resize(547, 314)
        Form.setMinimumSize(QtCore.QSize(547, 314))
        Form.setMaximumSize(QtCore.QSize(547, 314))
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
        self.grupo = QtWidgets.QGroupBox(self.groupBox)
        self.grupo.setAlignment(QtCore.Qt.AlignCenter)
        self.grupo.setObjectName("grupo")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.grupo)
        self.horizontalLayout_3.setContentsMargins(-1, 25, 9, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabela = QtWidgets.QTableWidget(self.grupo)
        self.tabela.setIconSize(QtCore.QSize(0, 0))
        self.tabela.setShowGrid(True)
        self.tabela.setColumnCount(1)
        self.tabela.setObjectName("tabela")
        self.tabela.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/add-round-button-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.tabela.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/dollar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        item.setBackground(QtGui.QColor(213, 239, 255))
        self.tabela.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/box.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.tabela.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(0, item)
        self.tabela.horizontalHeader().setCascadingSectionResizes(False)
        self.tabela.horizontalHeader().setDefaultSectionSize(226)
        self.tabela.horizontalHeader().setMinimumSectionSize(0)
        self.tabela.verticalHeader().setDefaultSectionSize(30)
        self.tabela.verticalHeader().setMinimumSectionSize(10)
        self.horizontalLayout_3.addWidget(self.tabela)
        self.verticalLayout.addWidget(self.grupo)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.frame_2 = QtWidgets.QFrame(self.principal)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.atualiza_antigo = QtWidgets.QPushButton(self.frame_2)
        self.atualiza_antigo.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/package.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.atualiza_antigo.setIcon(icon5)
        self.atualiza_antigo.setIconSize(QtCore.QSize(45, 40))
        self.atualiza_antigo.setDefault(False)
        self.atualiza_antigo.setFlat(True)
        self.atualiza_antigo.setObjectName("atualiza_antigo")
        self.horizontalLayout.addWidget(self.atualiza_antigo)
        self.atualiza_novo = QtWidgets.QPushButton(self.frame_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/update-arrows.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.atualiza_novo.setIcon(icon4)
        self.atualiza_novo.setIconSize(QtCore.QSize(45, 40))
        self.atualiza_novo.setDefault(False)
        self.atualiza_novo.setFlat(True)
        self.atualiza_novo.setObjectName("atualiza_novo")
        self.horizontalLayout.addWidget(self.atualiza_novo)

        self.sair = QtWidgets.QPushButton(self.frame_2)
        self.sair.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/cross.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sair.setIcon(icon6)
        self.sair.setIconSize(QtCore.QSize(45, 40))
        self.sair.setDefault(False)
        self.sair.setFlat(True)
        self.sair.setObjectName("sair")
        self.horizontalLayout.addWidget(self.sair)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.verticalLayout_7.addWidget(self.principal)

        self.retranslateUi(Form, dados)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form, dados):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "INVENTÁRIO ESTOQUE - ASSISTENCIA TECNICA DE MANUNTEÇÃO"))
        self.grupo.setTitle(_translate("Form", "PRODUTO()"))
        item = self.tabela.verticalHeaderItem(0)
        item.setText(_translate("Form", "PREÇO ANTERIOR"))
        item = self.tabela.verticalHeaderItem(1)
        item.setText(_translate("Form", "PREÇO MÉDIO"))
        item = self.tabela.verticalHeaderItem(2)
        item.setText(_translate("Form", "QUANTIDADE ATUALIZADA"))
        self.atualiza_novo.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">ATUALIZA ESOQUE COM O PREÇO DE MÉDIA</span></p></body></html>"))
        self.atualiza_novo.setText(_translate("Form", "USAR PREÇO MÉDIO"))
        self.atualiza_antigo.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">SALVA O ESTOQUE COM O PREÇO ANTERIOR E A NOVA QUANTIDADE</span></p></body></html>"))
        self.atualiza_antigo.setText(_translate("Form", "USAR PREÇO ANTERIOR"))
        self.Janela = Form
        self.carregar_eventos(dados)

    def carregar_eventos(self, dados):
        self.sair.clicked.connect(self.fechar)
        self.atualiza_novo.clicked.connect(lambda:self.atualiza(1))
        self.atualiza_antigo.clicked.connect(lambda:self.atualiza(0))
        self.carregar_tabela(dados)


    def fechar(self):
        self.produto = False
        self.Janela.close()


    produto = {}
    def atualiza(self, opcao_atualiza):
        self.produto = {"preco": self.tabela.cellWidget(opcao_atualiza, 0).value(),
                        "quantidade": self.tabela.cellWidget(2, 0).value()}
        self.Janela.close()


    def carregar_tabela(self, dados):
        self.tabela.setCellWidget(0, 0, self.defini_preco(dados['preco_antigo']))
        self.tabela.setCellWidget(1, 0, self.defini_preco(dados['preco']))
        self.tabela.setCellWidget(2, 0, self.defini_quantidade(dados['quantidade']))


    def defini_preco(self, dados):
        preco = QtWidgets.QDoubleSpinBox()
        preco.setSuffix(" R$")
        preco.setGroupSeparatorShown(True)
        preco.setMinimum(1)
        preco.setMaximum(9999)
        preco.setValue(dados)
        preco.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        preco.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        return preco

    def defini_quantidade(self, dados):
        quantidade = QtWidgets.QSpinBox()
        quantidade.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        quantidade.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        quantidade.setMinimum(1)
        quantidade.setMaximum(999)
        quantidade.setValue(dados)
        return quantidade


import recursos


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Atualizar_estoque()
    dados = {"produto":'cpu',"quantidade":10,"preco":25.45, "preco_antigo":400.00}
    ui.setupUi(Form, dados)
    Form.show()
    sys.exit(app.exec_())

    sys.exit(app.exec_())
