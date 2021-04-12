# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SUPORTE05\Documents\Meus Programas\apps\ASSISTENCIA TECNICA\UI\seleciona_logo.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import os
import sql
import tempfile
from PyQt5 import QtCore, QtGui, QtWidgets


class Seleciona_logo(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(852, 766)
        Form.setMinimumSize(QtCore.QSize(852, 766))
        Form.setMaximumSize(QtCore.QSize(852, 766))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/technician.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#Form{    \n"
"    background-color: rgb(1, 92, 146);\n"
"    \n"
"    background-image: url(:/img/login.jpg);\n"
"}\n"
"\n"
"QWidget{    \n"
"    background-color: rgb(68, 154, 202, 100);\n"
"}\n"
"\n"
"QLabel, QToolButton{    \n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QToolTip {\n"
"    border: 2px solid darkkhaki;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"    opacity: 200;    \n"
"    color: rgb(1, 92, 146);\n"
"    background-color: rgb(188, 230, 254);    \n"
"    border-color: rgb(1, 92, 146);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.caminho = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.caminho.setFont(font)
        self.caminho.setAlignment(QtCore.Qt.AlignCenter)
        self.caminho.setObjectName("caminho")
        self.horizontalLayout.addWidget(self.caminho)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/img/logo.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.procurar = QtWidgets.QToolButton(self.widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.procurar.setIcon(icon1)
        self.procurar.setIconSize(QtCore.QSize(43, 41))
        self.procurar.setAutoRaise(True)
        self.procurar.setObjectName("procurar")
        self.horizontalLayout_4.addWidget(self.procurar)
        self.verticalLayout.addWidget(self.widget)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.confirmar = QtWidgets.QToolButton(self.frame_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/confirm.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.confirmar.setIcon(icon2)
        self.confirmar.setIconSize(QtCore.QSize(55, 54))
        self.confirmar.setAutoRaise(True)
        self.confirmar.setObjectName("confirmar")
        self.horizontalLayout_2.addWidget(self.confirmar)
        self.cancelar = QtWidgets.QToolButton(self.frame_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/cross.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelar.setIcon(icon3)
        self.cancelar.setIconSize(QtCore.QSize(55, 54))
        self.cancelar.setAutoRaise(True)
        self.cancelar.setObjectName("cancelar")
        self.horizontalLayout_2.addWidget(self.cancelar)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LOGO - ASSISTENCIA TECNICA"))
        self.caminho.setText(_translate("Form", "SELECIONE UMA IMAGEM PARA SAIR NOS RELATÓRIOS\nTAMANHO RECOMENDANDODE (120x100)px"))
        self.label_2.setText(_translate("Form", "CAMINHO DO ARQUIVO SELECIONADO"))
        self.procurar.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">CLIQUE AQUI PARA ALTERAR A IMAGEM.</span></p></body></html>"))
        self.procurar.setText(_translate("Form", "..."))
        self.confirmar.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">CONFIRMA A SELEÇÃO DA IMAGEM</span></p></body></html>"))
        self.confirmar.setText(_translate("Form", "SAIR"))
        self.cancelar.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">CANCELA OPERAÇÃO</span></p></body></html>"))
        self.cancelar.setText(_translate("Form", "ALTERAR"))
        self.carregar_janela(Form)


    Janela = None
    def carregar_janela(self, Form):
        self.Janela = Form
        self.Janela.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.cancelar.clicked.connect(self.Janela.close)
        self.procurar.clicked.connect(self.procurar_img)
        self.confirmar.clicked.connect(self.alterar_img)
        self.pegar_img()


    def pegar_img(self):
        try:
            img = sql.SQL().pegar_meus_dados_logo()[0][0]
            with open(tempfile.gettempdir() + r'\img.jpg', "wb") as arq: arq.write(img)
            if(isinstance(img, bytes)): self.label.setPixmap(QtGui.QPixmap(tempfile.gettempdir() + r'\img.jpg'))
        except Exception as erro: print("ERRO EM CARREEGAR IMAGEM({})".format(erro))


    def alterar_img(self):
        if(self.label_2.text() != "CAMINHO DO ARQUIVO SELECIONADO"):
            msg = QtWidgets.QMessageBox.question(None, "LOGO - ASSISTENCIA TECNICA", 'DESEJA ALTERAR O LOGO ?')
            if(msg == QtWidgets.QMessageBox.Yes):
                if(sql.SQL().inserir_meus_dados_logo(self.label_2.text())):
                    QtWidgets.QMessageBox.information(None, "LOGO - ASSISTENCIA TECNICA", "IMAGEM ALTERADA COM SUCESSO!")
                    self.Janela.close()
                    return True
                QtWidgets.QMessageBox.information(None, "LOGO - ASSISTENCIA TECNICA", "NÃO FOI POSSIVEL SALVER A IMAGEM DO CAMINHO:<b>{}</b>!".format(self.label_2.text()))


    def procurar_img(self):
        file = self.abrir_img()
        if(file != ""):
            self.label_2.setText(file)
            self.label.setPixmap(QtGui.QPixmap(file))


    def abrir_img(self):
        """ CHAMA DIALOGO PARA IMPRIMIR RELATORIO """
        caminho = os.path.expanduser("~/")
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,
        "SELECIONE O ARQUIVO DE LOGO", caminho+"image.png","*.png")
        return fileName


import recursos


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Seleciona_logo()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
