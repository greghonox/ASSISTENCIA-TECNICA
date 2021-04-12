# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SUPORTE05\Documents\Meus Programas\apps\ASSISTENCIA TECNICA\UI\estoque.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import sql
from produtos import Produtos
from PyQt5 import QtCore, QtGui, QtWidgets
from atualizar_estoque import Atualizar_estoque
from consulta_estoque import Consulta_estoque
from produtos import Produtos


class Estoque(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(947, 526)
        Form.setMinimumSize(QtCore.QSize(947, 526))
        Form.setMaximumSize(QtCore.QSize(947, 526))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/technician.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#principal{\n"
"    background-image: url(:/img/tecnico.jpg);\n"
"}\n"
"\n"
"QWidget{        \n"
"    background-color: rgb(188, 230, 254, 150);\n"
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
"QLabel{    \n"
"    background-color: rgba(255, 255, 255, 0);    \n"
"    color: rgb(1, 92, 146);\n"
"}\n"
"\n"
"#label_14,#label_15,#label_16, #label_17{    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#observacao{\n"
"color: rgb(1, 92, 146);\n"
"}\n"
"\n"
"QDateEdit, QSpinBox, QDoubleSpinBox{\n"
"color: rgb(1, 92, 146);\n"
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
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.produto = QtWidgets.QComboBox(self.groupBox)
        self.produto.setMinimumSize(QtCore.QSize(278, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.produto.setFont(font)
        self.produto.setEditable(True)
        self.produto.setObjectName("produto")
        self.produto.addItem("")
        self.horizontalLayout.addWidget(self.produto)
        self.add_produto = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_produto.sizePolicy().hasHeightForWidth())
        self.add_produto.setSizePolicy(sizePolicy)
        self.add_produto.setMaximumSize(QtCore.QSize(85, 16777215))
        self.add_produto.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/add-round-button-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_produto.setIcon(icon1)
        self.add_produto.setIconSize(QtCore.QSize(30, 29))
        self.add_produto.setFlat(True)
        self.add_produto.setObjectName("add_produto")
        self.horizontalLayout.addWidget(self.add_produto)
        self.edi_produto = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edi_produto.sizePolicy().hasHeightForWidth())
        self.edi_produto.setSizePolicy(sizePolicy)
        self.edi_produto.setMaximumSize(QtCore.QSize(85, 16777215))
        self.edi_produto.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/box.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edi_produto.setIcon(icon2)
        self.edi_produto.setIconSize(QtCore.QSize(38, 44))
        self.edi_produto.setFlat(True)
        self.edi_produto.setObjectName("edi_produto")
        self.horizontalLayout.addWidget(self.edi_produto)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.preco = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.preco.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.preco.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.preco.setProperty("showGroupSeparator", True)
        self.preco.setMaximum(9999.99)
        self.preco.setProperty("value", 1.0)
        self.preco.setObjectName("preco")
        self.horizontalLayout_2.addWidget(self.preco)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_32 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_3.addWidget(self.label_32)
        self.quantidade = QtWidgets.QSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.quantidade.setFont(font)
        self.quantidade.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.quantidade.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.quantidade.setMinimum(1)
        self.quantidade.setMaximum(999)
        self.quantidade.setObjectName("quantidade")
        self.horizontalLayout_3.addWidget(self.quantidade)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_31 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_4.addWidget(self.label_31)
        self.data_entrada = QtWidgets.QDateEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.data_entrada.setFont(font)
        self.data_entrada.setCalendarPopup(True)
        self.data_entrada.setObjectName("data_entrada")
        self.horizontalLayout_4.addWidget(self.data_entrada)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_33 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_8.addWidget(self.label_33)
        self.estoque_min = QtWidgets.QSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.estoque_min.setFont(font)
        self.estoque_min.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.estoque_min.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.estoque_min.setMinimum(0)
        self.estoque_min.setMaximum(9999)
        self.estoque_min.setProperty("value", 0)
        self.estoque_min.setObjectName("estoque_min")
        self.horizontalLayout_8.addWidget(self.estoque_min)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.observacao = QtWidgets.QPlainTextEdit(self.frame)
        self.observacao.setObjectName("observacao")
        self.verticalLayout_4.addWidget(self.observacao)
        self.horizontalLayout_21.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.principal)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame_2)
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cadastrar.setIcon(icon3)
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/find-my-friend.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.procurar.setIcon(icon4)
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.excluir.setIcon(icon5)
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/cross.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sair.setIcon(icon6)
        self.sair.setIconSize(QtCore.QSize(41, 52))
        self.sair.setFlat(True)
        self.sair.setObjectName("sair")
        self.verticalLayout_8.addWidget(self.sair)
        self.label_17 = QtWidgets.QLabel(self.groupBox_5)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_8.addWidget(self.label_17)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.horizontalLayout_21.addWidget(self.frame_2)
        self.verticalLayout_7.addWidget(self.principal)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CADASTRO ESTOQUE - ASSISTENCIA TECNICA DE MANUNTEÇÃO"))
        self.produto.setItemText(0, _translate("Form", "SELECIONE PRODUTO"))
        self.add_produto.setToolTip(_translate("Form", "<html><head/><body><p>Adicione novo produto!</p></body></html>"))
        self.edi_produto.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Edite</span> ou <span style=\" font-weight:600;\">visualize</span> esse produto!</p></body></html>"))
        self.label_2.setText(_translate("Form", "Preço"))
        self.preco.setSuffix(_translate("Form", "R$"))
        self.label_32.setToolTip(_translate("Form", "<html><head/><body><p>QUANTIDADE DE ENTRADA PARA O ESTOQUE</p></body></html>"))
        self.label_32.setText(_translate("Form", "Quantidade"))
        self.quantidade.setToolTip(_translate("Form", "<html><head/><body><p>QUANTIDADE DE ENTRADA PARA O ESTOQUE</p></body></html>"))
        self.label_31.setText(_translate("Form", "Data Entrada"))
        self.data_entrada.setToolTip(_translate("Form", "<html><head/><body><p>Informe o dia de <span style=\" font-weight:600;\">entrada do produto!</span></p><p><img src=\":/img/img/cuidado.svg\"/> A data <span style=\" font-weight:600;\">não pode ser maior que o dia de hoje!</span><img src=\":/img/img/cuidado.svg\"/></p></body></html>"))
        self.label_33.setToolTip(_translate("Form", "<html><head/><body><p><br/></p><p>QUANTIDADE DE MINIMA PARA RECEBER COMO ALERTA DE ESTOQUE BAIXO</p></body></html>"))
        self.label_33.setText(_translate("Form", "Estoque minimo"))
        self.estoque_min.setToolTip(_translate("Form", "<html><head/><body><p>QUANTIDADE DE MINIMA PARA RECEBER COMO ALERTA DE ESTOQUE BAIXO</p></body></html>"))
        self.observacao.setPlaceholderText(_translate("Form", "OBSERVAÇÕES DO PRODUTO"))
        self.label_14.setText(_translate("Form", "CADASTRAR"))
        self.label_15.setText(_translate("Form", "PROCURAR"))
        self.label_16.setText(_translate("Form", "EXCLUIR"))
        self.label_17.setText(_translate("Form", "SAIR"))
        self.Janela = Form
        self.carregar_eventos()

    def carregar_eventos(self):
        self.carregar_produtos()
        self.sair.clicked.connect(self.Janela.close)
        self.cadastrar.disconnect()
        self.cadastrar.clicked.connect(self.cadastra)
        self.add_produto.clicked.connect(self.cadastrar_produto)
        self.data_entrada.setDateTime(QtCore.QDateTime.currentDateTime())
        self.procurar.clicked.connect(self.abrir_consulta_categoria)
        self.produto.currentTextChanged.connect(self.selecao_produto)
        self.edi_produto.clicked.connect(self.editar_produto)


    def editar_produto(self):
        if(self.produto.currentIndex() != 0):
            self.Form = QtWidgets.QDialog()
            self.ui = Produtos()
            self.ui.setupUi(self.Form, self.produto.currentText().split("(")[1].split(")")[0])
            self.Form.exec()
            self.produto.clear()
            self.produto.addItem("SELECIONE PRODUTO")
            self.carregar_produtos()


    def exclui_produto(self):
        msg = QtWidgets.QMessageBox.question(None, "INSERÇÃO PRODUTO ESTOQUE - SISTEMA MANUNTEÇÃO",
        "DESEJA REMOVER PRODUTO <b>{}</b>?".format(self.produto.currentText()))
        if(msg == QtWidgets.QMessageBox.Yes and self.produto.currentIndex() != 0):
            sql.SQL().remover_produto_estoque(self.produto.currentText().split("(")[1].split(")")[0])
            QtWidgets.QMessageBox.information(None, "INSERÇÃO PRODUTO ESTOQUE - SISTEMA MANUNTEÇÃO",
            "PRODUTO <b>{}</b> COM SUCESSO!".format(self.produto.currentText()))
            self.Janela.close()


    def selecao_produto(self):
        try:  self.carregar_produto(self.produto.currentText().split("(")[1].split(")")[0], False)
        except: self.limpar_campos(False)


    def abrir_consulta_categoria(self):
        Form = QtWidgets.QDialog()
        ui = Consulta_estoque()
        ui.setupUi(Form)
        Form.exec_()
        if(ui.produto_selecionado):
            self.carregar_produto(ui.produto_selecionado)


    def carregar_produto(self, produto, bloquea_produto=True):
        dados = sql.SQL().pegar_estoque_codigo_tabela(produto)[0]
        self.produto.setCurrentIndex(self.pegar_ind_produto(dados[1]))
        self.quantidade.setValue(dados[2])
        self.estoque_min.setValue(dados[3])
        self.preco.setValue(dados[4])
        self.observacao.setPlainText(dados[6])

        self.data_entrada.setDate(QtCore.QDate.fromString(dados[7] ,"dd/MM/yyyy"))
        if(bloquea_produto):
            self.produto.setDisabled(bloquea_produto)
            self.label_14.setText("ALTERAR")
            self.cadastrar.disconnect()
            self.cadastrar.clicked.connect(self.alterar_produto)
            self.excluir.disconnect()
            self.excluir.clicked.connect(self.exclui_produto)


    def alterar_produto(self):
        msg = QtWidgets.QMessageBox.question(None, "CADASTRO ESTOQUE - ASSISTENCIA TECNICA DE MANUNTEÇÃO",\
                                             "<b>DESEJA ALTARAR O PRODUTO ?{}</b>".format(self.produto.currentText()))
        if(msg == QtWidgets.QMessageBox.Yes):
            SQL = {"produto": self.produto.currentText().split("(")[1].split(")")[0],
                   "preco": self.preco.value(),
                   "quantidade": self.quantidade.value(),
                   "data_entrega": self.data_entrada.date().toString("dd/MM/yyyy"),
                   "descricao": self.observacao.toPlainText(),
                   "estoque_min": self.estoque_min.value()}
            sql.SQL().alterar_produto_estoque(SQL)
            QtWidgets.QMessageBox.information(None, "CADASTRO ESTOQUE - ASSISTENCIA TECNICA DE MANUNTEÇÃO",\
                                              "PRODUTO <b>{}</b> ALTERADO COM SUCESSO!".format(self.produto.currentText()))
            self.Janela.close()


    def pegar_ind_produto(self, prod):
        for produto in range(1, self.produto.count()):
            try:
                if(self.produto.itemText(produto).split("(")[0] == prod): return produto
            except: pass


    def cadastra(self):
        if(self.produto.currentIndex() == 0):
            QtWidgets.QMessageBox.information(None, "CADASTRO DE ESTOQUE - SISTEMA MANUNTEÇÃO",
                                              "ESCOLHA O PRODUTO PARA FAZER A INSERÇÃO!")
        else:
            SQL = {"produto": self.produto.currentText().split("(")[1].split(")")[0],
                   "preco": self.preco.value(),
                   "quantidade": self.quantidade.value(),
                   "data_entrega": self.data_entrada.date().toString("dd/MM/yyyy"),
                   "descricao": self.observacao.toPlainText(),
                   "estoque_min": self.estoque_min.value()}
            if(not sql.SQL().pegar_estoque_existente(self.produto.currentText().split("(")[1].split(")")[0])):
                if(sql.SQL().inserir_estoque(SQL)):
                    QtWidgets.QMessageBox.information(None, "CADASTRO ESTOQUE - SISTEMA MANUNTEÇÃO",
                                                      "CADASTRO DO PRODUTO <b>{}</b> REALIZADA COM SUCESSO".format(self.produto.currentText()))
                    for campo in [self.preco, self.quantidade]: campo.setValue(1)
                    self.produto.setCurrentIndex(0)
                    self.observacao.clear()
            else:
                msg = QtWidgets.QMessageBox.question(None, "CADASTRO ESTOQUE - SISTEMA MANUNTEÇÃO",
                                                        "O PRODUTO <b>{}</b> JÁ EXISTE EM ESTOQUE COM PREÇO DEFINIDO,"\
                                                        " DESEJA INSERIR O PRODUTO COM O PREÇO NOVO?".format(self.produto.currentText()))
                if(msg == QtWidgets.QMessageBox.No):
                    QtWidgets.QMessageBox.information(None, "CADASTRO ESTOQUE - SISTEMA MANUNTEÇÃO",
                    "JÁ EXISTE O PRODUTO <b>{}</b> Vou demonstrar como vai ficar o seu estoque agora"
                    .format(self.produto.currentText()))

                    self.atualizar_estoque()
                else:
                    produto = sql.SQL().pegar_produto_estoque(self.produto.currentText().split("(")[1].split(")")[0])[0]

                    SQL = {"produto": self.produto.currentText().split("(")[1].split(")")[0],
                           "preco": self.preco.value(),
                           "quantidade": self.quantidade.value() + produto[1],
                           "data_entrega": self.data_entrada.date().toString("dd/MM/yyyy"),
                           "descricao": self.observacao.toPlainText(),
                           "estoque_min": self.estoque_min.value()}

                    sql.SQL().alterar_produto_estoque(SQL)
                self.msg_alteracao_produto_estoque()


    produto = {}
    def atualizar_estoque(self):
        produto = sql.SQL().pegar_produto_estoque(self.produto.currentText().split("(")[1].split(")")[0])[0]
        self.Form = QtWidgets.QDialog()
        self.ui = Atualizar_estoque()

        calculo = (produto[2] * produto[1] + self.preco.value()* self.quantidade.value()) / (produto[1] + self.quantidade.value())

        self.ui.setupUi(self.Form, {"produto": int(self.produto.currentText().split("(")[1].split(")")[0]),
                                    "quantidade": produto[1] + self.quantidade.value(),
                                    "preco_antigo": produto[2],
                                    "preco": calculo})
        self.Form.exec()
        if(self.ui.produto != False):
            SQL = {"produto": self.produto.currentText().split("(")[1].split(")")[0],
                   "preco": self.ui.produto["preco"],
                   "quantidade": self.ui.produto["quantidade"],
                   "data_entrega": self.data_entrada.date().toString("dd/MM/yyyy"),
                   "descricao": self.observacao.toPlainText(),
                   "estoque_min": self.estoque_min.value()}

            sql.SQL().alterar_produto_estoque(SQL)
            self.msg_alteracao_produto_estoque()


    def msg_alteracao_produto_estoque(self):
        QtWidgets.QMessageBox.information(None, "INSERÇÃO PRODUTO ESTOQUE - SISTEMA MANUNTEÇÃO",
        "FOI FEITO A ALTERAÇÃO DO PRODUTO <b>{}</b> COM SUCESSO!".format(self.produto.currentText()))
        self.limpar_campos()


    def limpar_campos(self, lim_produto=True):
        if(lim_produto): self.produto.setCurrentIndex(0)
        [campo.setValue(1) for campo in [self.preco, self.quantidade]]
        self.estoque_min.setValue(0)
        self.observacao.clear()


    def cadastrar_produto(self):
        self.Form = QtWidgets.QDialog()
        self.ui = Produtos()
        self.ui.setupUi(self.Form)
        self.Form.exec()
        self.produto.clear()
        self.produto.addItem("SELECIONE O PRODUTO")
        self.carregar_produtos()


    def carregar_produtos(self):
        for prod in sql.SQL().pegar_produtos(): self.produto.addItem(str("{}({})".format(prod[1], prod[0])))
        self.produto.setDisabled(False)
        self.cadastrar.disconnect()
        self.cadastrar.clicked.connect(self.cadastra)


import recursos


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Estoque()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
