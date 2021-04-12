# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SUPORTE05\Documents\Meus Programas\apps\ASSISTENCIA TECNICA\UI\login.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import sql
from main import Assistencia
from PyQt5 import QtCore, QtGui, QtWidgets

class Login(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(380, 495)
        Form.setMinimumSize(QtCore.QSize(380, 495))
        Form.setMaximumSize(QtCore.QSize(380, 495))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/technician.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#fundo{\n"
"    background-image: url(:/img/login.jpg);\n"
"}\n"
"\n"
"#usuario{    \n"
"    background-image: url(:/img/user.svg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: left;\n"
"}\n"
"\n"
"#senha{\n"
"    background-image: url(:/img/key.svg);    \n"
"    background-repeat: no-repeat;\n"
"    background-position: left;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fundo = QtWidgets.QWidget(Form)
        self.fundo.setObjectName("fundo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fundo)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.fechar = QtWidgets.QLabel(self.fundo)
        self.fechar.setMaximumSize(QtCore.QSize(32, 32))
        self.fechar.setText("")
        self.fechar.setPixmap(QtGui.QPixmap(":/img/fechar.svg"))
        self.fechar.setAlignment(QtCore.Qt.AlignCenter)
        self.fechar.setObjectName("fechar")
        self.horizontalLayout_4.addWidget(self.fechar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.label_3 = QtWidgets.QLabel(self.fundo)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/img/login.svg"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.frame = QtWidgets.QFrame(self.fundo)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.usuario = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.usuario.setFont(font)
        self.usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.usuario.setClearButtonEnabled(False)
        self.usuario.setObjectName("usuario")
        self.horizontalLayout_2.addWidget(self.usuario)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.senha = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.senha.setFont(font)
        self.senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senha.setAlignment(QtCore.Qt.AlignCenter)
        self.senha.setObjectName("senha")
        self.horizontalLayout_3.addWidget(self.senha)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.fundo)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.entrar = QtWidgets.QToolButton(self.frame_2)
        self.entrar.setText("")
        self.entrar.setIcon(icon)
        self.entrar.setIconSize(QtCore.QSize(80, 72))
        self.entrar.setAutoRaise(True)
        self.entrar.setObjectName("entrar")
        self.horizontalLayout.addWidget(self.entrar)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.fundo)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LOGIN - SISTEMA MANUNTEÇÃO"))
        self.fechar.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">FECHAR A JANELA</span></p></body></html>"))
        self.usuario.setPlaceholderText(_translate("Form", "USUÁRIO"))
        self.senha.setPlaceholderText(_translate("Form", "SENHA"))
        self.entrar.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">ACESSE O SISTEMA</span></p></body></html>"))
        self.entrar.setShortcut(_translate("Form", "Return, Enter"))
        self.carregar_janela(Form)

    Janela = None
    def carregar_janela(self, Form):
        self.Janela = Form
        self.propriedades_janela(Form)
        self.entrar.clicked.connect(self.entrar_sistema)


    def entrar_sistema(self):
        try:
            for campo in [self.usuario, self.senha]:
                if(campo.text() == ''): campo.setFocus(True); return False

            if(not sql.SQL().pegar_usuario_senha({'usuario': self.usuario.text(), 'senha': int(self.senha.text())})):
                QtWidgets.QMessageBox.warning(None, "LOGIN - SISTEMA MANUNTEÇÃO", "<b>USUÁRIO E SENHA ESTÃO INCORRETOS</b>")
                self.senha.clear()
                return False
            self.acessar_sistema()
        except Exception as erro: QtWidgets.QMessageBox.information(None, "LOGIN - SISTEMA MANUNTEÇÃO", "NÃO É POSSIVEL ACESSAR O SISTEMA!")


    def acessar_sistema(self):
        self.Janela.close()
        self.Form = QtWidgets.QMainWindow()
        self.ui = Assistencia()
        self.ui.setupUi(self.Form)
        self.Form.show()


    def propriedades_janela(self, Form):
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.fundo.mousePressEvent = self.fundo_click
        self.fundo.mouseMoveEvent = self.fundo_move
        self.fechar.mousePressEvent = self.fechar_janela

    def fechar_janela(self, event): self.Janela.close()

    def fundo_click(self, event):
        self.oldPos = event.globalPos()

    def fundo_move(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        self.Janela.move(self.Janela.x() + delta.x(), self.Janela.y() + delta.y())
        self.oldPos = event.globalPos()

import recursos


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Login()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
