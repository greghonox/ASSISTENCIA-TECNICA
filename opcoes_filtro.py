# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SUPORTE05\Documents\Meus Programas\apps\ASSISTENCIA TECNICA\UI\opcoes_filtro.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import os
import subprocess
from geracao_xls import Geracao_XLS
from PyQt5 import QtCore, QtGui, QtWidgets


class Opcoes_filtro(object):
    def setupUi(self, Form, opcao_filtro, titulo, dados_tabela, ocu_filtro=False):
        Form.setObjectName("Form")
        Form.resize(636, 153)
        Form.setMinimumSize(QtCore.QSize(636, 153))
        Form.setMaximumSize(QtCore.QSize(636, 153))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/technician.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#Form{\n"
"    background-color: rgb(1, 92, 146);\n"
"}\n"
"\n"
"QWidget{    \n"
"    background-color: rgb(137, 184, 214, 100);\n"
"}\n"
"\n"
"QLabel, QToolButton{\n"
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
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.imprimir = QtWidgets.QToolButton(self.widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/printer.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.imprimir.setIcon(icon1)
        self.imprimir.setIconSize(QtCore.QSize(100, 48))
        self.imprimir.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.imprimir.setAutoRaise(True)
        self.imprimir.setObjectName("imprimir")
        self.horizontalLayout_2.addWidget(self.imprimir)
        self.ver = QtWidgets.QToolButton(self.widget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/view.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ver.setIcon(icon2)
        self.ver.setIconSize(QtCore.QSize(100, 48))
        self.ver.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.ver.setAutoRaise(True)
        self.ver.setObjectName("ver")
        self.horizontalLayout_2.addWidget(self.ver)
        self.ver_tudo = QtWidgets.QToolButton(self.widget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/show.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ver_tudo.setIcon(icon3)
        self.ver_tudo.setIconSize(QtCore.QSize(100, 48))
        self.ver_tudo.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.ver_tudo.setAutoRaise(True)
        self.ver_tudo.setObjectName("ver_tudo")
        self.horizontalLayout_2.addWidget(self.ver_tudo)
        self.nao_ver = QtWidgets.QToolButton(self.widget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/hide.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nao_ver.setIcon(icon4)
        self.nao_ver.setIconSize(QtCore.QSize(100, 48))
        self.nao_ver.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.nao_ver.setAutoRaise(True)
        self.nao_ver.setObjectName("nao_ver")
        self.horizontalLayout_2.addWidget(self.nao_ver)
        self.cancelar = QtWidgets.QToolButton(self.widget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelar.setIcon(icon5)
        self.cancelar.setIconSize(QtCore.QSize(100, 48))
        self.cancelar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.cancelar.setAutoRaise(True)
        self.cancelar.setObjectName("cancelar")
        self.horizontalLayout_2.addWidget(self.cancelar)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form, opcao_filtro, titulo, dados_tabela, ocu_filtro)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form, opcao_filtro, titulo, dados_tabela, ocu_filtro):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "OPÇÕES DO RELATÓRIO DE {} - ASSISTENCIA TECNICA".format(titulo)))
        self.label.setText(_translate("Form", "OPÇÕES DO RELÁTORIO DE {}".format(titulo)))
        self.imprimir.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">REALIZE A IMPRESSÃO DO QUE ESTA LISTADO</span></p></body></html>"))
        self.imprimir.setText(_translate("Form", "IMPRIMIR"))
        self.ver.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">MODIFIQUE O FILTRO PARA NÃO MOSTRAR OS REGISTROS QUE FORAM EXCLUIDOS.</span></p></body></html>"))
        self.ver.setText(_translate("Form", "MOSTRAR ATIVOS"))
        self.ver_tudo.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">MODIFIQUE O FILTRO PARA MOSTRAR TODOS OS REGISTROS!</span></p></body></html>"))
        self.ver_tudo.setText(_translate("Form", "MOSTRAR TUDO"))
        self.nao_ver.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">MODIFIQUE O FILTRO PARA MOSTRAR OS REGISTROS QUE FORAM EXCLUIDOS.</span></p></body></html>"))
        self.nao_ver.setText(_translate("Form", "MOSTRAR DESATIVOS"))
        self.cancelar.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">SAIA DESSA TELA</span></p></body></html>"))
        self.cancelar.setText(_translate("Form", "CANCELAR"))
        self.carregar_janela(Form, opcao_filtro, dados_tabela, ocu_filtro)
        self.titulo = titulo

    Janela = None
    opcao_escolhida = False
    dados_tabela = []
    def carregar_janela(self, Form, opcao_filtro, dados_tabela, ocu_filtro):
        """
        2 - MOSTRAR OCULTO (ver)
        3 - VER TUDO (ver_tudo)
        1 - MOSTRAR ATIVOS(nao_ver)
        """
        self.Janela = Form
        self.cancelar.clicked.connect(self.Janela.close)
        self.ver.clicked.connect(lambda:self.escolha_feita(1))
        self.nao_ver.clicked.connect(lambda:self.escolha_feita(2))
        self.ver_tudo.clicked.connect(lambda:self.escolha_feita(3))

        if(ocu_filtro):
            [campo.setVisible(not ocu_filtro) for campo in [self.ver, self.ver_tudo, self.nao_ver]]
        self.imprimir.clicked.connect(self.imprimi)
        self.opcao_ja_escolhida(opcao_filtro)
        self.dados_tabela = dados_tabela

    def opcao_ja_escolhida(self, opcao):
        if(opcao == 3):
            self.ver_tudo.setDisabled(True)
        elif(opcao == 1):
            self.ver.setDisabled(True)
        elif(opcao == 2):
            self.nao_ver.setDisabled(True)


    def imprimi(self):
        """ CHAMA DIALOGO PARA IMPRIMIR RELATORIO """
        caminho = os.path.expanduser("~/")
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(None,
        "SELECIONE O ARQUIVO DE LOGO", caminho+"relatorio.xlsx")
        try:
            if(fileName != ""):
                Geracao_XLS(fileName, self.dados_tabela, self.titulo)
                QtWidgets.QMessageBox.information(None, self.label.text(), "GERADO O ARQUIVO <b>{}</b> PARA IMPRESSÃO COM SUCESSO!".format(fileName.upper()))
                msg = QtWidgets.QMessageBox.question(None, self.label.text(), "DESEJA VISUALIZAR O ARQUIVO PARA IMPRESSÃO?")
                if(msg == QtWidgets.QMessageBox.Yes):
                    subprocess.Popen(fileName, shell=True)
                self.Janela.close()
        except Exception as erro: QtWidgets.QMessageBox.warning(None, self.label.text(), "OCORREU UM ERRO(<b>{}</b>)".format(erro))



    def escolha_feita(self, opcao):
        self.opcao_escolhida = opcao
        self.Janela.close()


import recursos


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Opcoes_filtro()
#     ui.setupUi(Form, 0, 'teste', [], True)
#     Form.show()
#     sys.exit(app.exec_())
