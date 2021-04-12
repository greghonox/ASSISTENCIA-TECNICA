# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SUPORTE05\Documents\Meus Programas\apps\ASSISTENCIA TECNICA\UI\mensagens_sistema.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import sql
from PyQt5 import QtCore, QtGui, QtWidgets


class Mensagens_sistema(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(697, 481)
        Form.setMinimumSize(QtCore.QSize(697, 481))
        Form.setMaximumSize(QtCore.QSize(697, 481))
        Form.setStyleSheet("QWidget{\n"
"    background-color: rgb(188, 230, 254, 150);\n"
"}\n"
"\n"
"#tabela, #mensagem{\n"
"    background-color: rgb(68, 154, 202, 200);\n"
"}\n"
"#tabela section{\n"
"background-color: rgb(98, 101, 255);\n"
"}\n"
"QFrame{    \n"
"    background-color: rgb(137, 184, 214, 250);\n"
"}\n"
"\n"
"#label, #cancelar{    \n"
"    background-color: rgb(137, 184, 214, 0);\n"
"}\n"
"\n"
"#Form{\n"
"    background-image: url(:/img/mensagens.jpeg);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mensagem = QtWidgets.QTextEdit(self.frame)
        self.mensagem.setReadOnly(True)
        self.mensagem.setObjectName("mensagem")
        self.horizontalLayout_4.addWidget(self.mensagem)
        self.tabela = QtWidgets.QTableWidget(self.frame)
        self.tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabela.setShowGrid(False)
        self.tabela.setObjectName("tabela")
        self.tabela.setColumnCount(2)
        self.tabela.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(1, item)
        self.tabela.horizontalHeader().setDefaultSectionSize(157)
        self.tabela.horizontalHeader().setMinimumSectionSize(39)
        self.tabela.verticalHeader().setDefaultSectionSize(30)
        self.tabela.verticalHeader().setMinimumSectionSize(30)
        self.tabela.verticalHeader().setSortIndicatorShown(False)
        self.tabela.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_4.addWidget(self.tabela)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cancelar = QtWidgets.QToolButton(self.frame_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelar.setIcon(icon)
        self.cancelar.setIconSize(QtCore.QSize(51, 60))
        self.cancelar.setCheckable(False)
        self.cancelar.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.cancelar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.cancelar.setAutoRaise(True)
        self.cancelar.setObjectName("cancelar")
        self.horizontalLayout_3.addWidget(self.cancelar)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MENSAGENS - SISTEMA MANUNTEÇÃO"))
        self.label.setText(_translate("Form", "MENSAGENS QUE FORAM ENVIADAS PARA VOCÊ."))
        self.tabela.setSortingEnabled(True)
        item = self.tabela.horizontalHeaderItem(0)
        item.setText(_translate("Form", "CONTAGEM"))
        item = self.tabela.horizontalHeaderItem(1)
        item.setText(_translate("Form", "MENSAGEM"))
        self.cancelar.setText(_translate("Form", "CANCELAR"))
        self.cancelar.setShortcut(_translate("Form", "Esc"))
        self.carregar_janela(Form)


    Janela = None
    def carregar_janela(self, Form):
        self.Janela = Form
        self.cancelar.clicked.connect(self.Janela.close)
        self.tabela.clicked.connect(self.mensagem_exibir)

        for col, dados in enumerate(sql.SQL().pegar_todas_mensagens()):
            self.tabela.insertRow(self.tabela.rowCount())
            for lin, mensagem in enumerate(dados):
                self.tabela.setItem(col, lin, QtWidgets.QTableWidgetItem(str(mensagem).upper()))

    def mensagem_exibir(self):
        linha = self.tabela.selectedItems()
        self.mensagem.setText(linha[1].text())


import recursos


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Mensagens_sistema()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
