# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SUPORTE05\Documents\Meus Programas\apps\ASSISTENCIA TECNICA\UI\clasula_contratos.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import sql
from PyQt5 import QtCore, QtGui, QtWidgets


class clasula_contratos(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(697, 481)
        Form.setMinimumSize(QtCore.QSize(697, 481))
        Form.setMaximumSize(QtCore.QSize(697, 481))
        Form.setStyleSheet("QWidget{\n"
"    background-color: rgb(188, 230, 254, 150);\n"
"}\n"
"\n"
"#mensagem{\n"
"    background-color: rgb(68, 154, 202, 200);\n"
"}\n"
"\n"
"QFrame{    \n"
"    background-color: rgb(137, 184, 214, 250);\n"
"}\n"
"\n"
"QLabel, #cancelar{    \n"
"    background-color: rgb(137, 184, 214, 0);\n"
"}\n"
"\n"
"#Form{\n"
"    background-image: url(:/img/mensagens.jpeg);\n"
"}\n"
"\n"
"#codigo, #vencimento{    \n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(17)
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
        self.clasulas = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.clasulas.setFont(font)
        self.clasulas.setReadOnly(True)
        self.clasulas.setObjectName("clasulas")
        self.horizontalLayout_4.addWidget(self.clasulas)
        self.verticalLayout_2.addWidget(self.frame)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.codigo = QtWidgets.QLabel(self.widget_2)
        self.codigo.setMaximumSize(QtCore.QSize(37, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.codigo.setFont(font)
        self.codigo.setAlignment(QtCore.Qt.AlignCenter)
        self.codigo.setObjectName("codigo")
        self.horizontalLayout.addWidget(self.codigo)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.vencimento = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.vencimento.setFont(font)
        self.vencimento.setObjectName("vencimento")
        self.horizontalLayout.addWidget(self.vencimento)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.custo = QtWidgets.QDoubleSpinBox(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.custo.setFont(font)
        self.custo.setAlignment(QtCore.Qt.AlignCenter)
        self.custo.setReadOnly(True)
        self.custo.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.custo.setProperty("showGroupSeparator", True)
        self.custo.setObjectName("custo")
        self.horizontalLayout.addWidget(self.custo)
        self.verticalLayout_2.addWidget(self.widget_2)
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
        Form.setWindowTitle(_translate("Form", "CONTRATO DE USO - SISTEMA MANUNTEÇÃO"))
        self.label.setText(_translate("Form", "SEU CONTRATO DE USO"))
        self.label_3.setText(_translate("Form", "SEU CÓDIGO DE CLIENTE"))
        self.codigo.setText(_translate("Form", "0"))
        self.label_4.setText(_translate("Form", "VENCIMENTO"))
        self.vencimento.setText(_translate("Form", "01/01/2000"))
        self.label_2.setText(_translate("Form", "CUSTO DIÁRIO"))
        self.custo.setSuffix(_translate("Form", " R$"))
        self.cancelar.setText(_translate("Form", "CANCELAR"))
        self.cancelar.setShortcut(_translate("Form", "Esc"))
        self.carregar_janela(Form)

    Janela = None
    def carregar_janela(self, Form):
        self.Janela = Form
        self.cancelar.clicked.connect(self.Janela.close)
        self.clasulas.setPlainText(sql.SQL().pegar_clasula()[0])
        self.custo.setValue(sql.SQL().pegar_clasula()[1])
        self.codigo.setText(str(sql.SQL().pegar_meus_dados()[0][9]))
        data = sql.SQL().pegar_vencimento_cliente()[0][0].split("-")
        data = data[2] +'/'+ data[1] +'/'+ data[0]
        self.vencimento.setText(data)



import recursos


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = clasula_contratos()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
