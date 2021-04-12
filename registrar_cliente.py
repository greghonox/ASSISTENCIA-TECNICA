# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SUPORTE05\Documents\Meus Programas\apps\ASSISTENCIA TECNICA\UI\registrar_cliente.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import sql
import pegar_cep
import platform
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from login import Login

class Registrar_cliente(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(662, 568)
        Form.setMinimumSize(QtCore.QSize(662, 568))
        Form.setMaximumSize(QtCore.QSize(662, 568))
        Form.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/technician.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget{    \n"
"    background-color: rgb(220, 220, 220, 100);\n"
"}\n"
"\n"
"QFrame{\n"
"    background-color: rgb(220, 220, 220, 50);\n"
"    border-color: rgb(0, 0, 0);\n"
"    border: 2px solid darkkhaki;\n"
"    border-color: black;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QLabel, #frame_2, #frame_3, #frame_4{\n"
"    border: 0px;\n"
"}\n"
"\n"
"QLabel, QLineEdit{\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, #estado{\n"
"    color: rgb(255, 0, 0);\n"
"    font: 75 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"#titulo{    \n"
"    font: 75 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"#registro{\n"
"    color:rgb(85, 85, 255);\n"
"    background-color:rgb(0, 170, 255);\n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 40, 641, 511))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.titulo = QtWidgets.QLabel(self.frame_3)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.horizontalLayout_16.addWidget(self.titulo)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_17.addWidget(self.label_12)
        self.nome = QtWidgets.QLineEdit(self.frame_2)
        self.nome.setObjectName("nome")
        self.horizontalLayout_17.addWidget(self.nome)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.telefone = QtWidgets.QLineEdit(self.frame_2)
        self.telefone.setObjectName("telefone")
        self.horizontalLayout_3.addWidget(self.telefone)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.cep = QtWidgets.QLineEdit(self.frame_2)
        self.cep.setMaximumSize(QtCore.QSize(118, 16777215))
        self.cep.setObjectName("cep")
        self.horizontalLayout_8.addWidget(self.cep)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.estado = QtWidgets.QComboBox(self.frame_2)
        self.estado.setMinimumSize(QtCore.QSize(359, 0))
        self.estado.setObjectName("estado")
        self.horizontalLayout_4.addWidget(self.estado)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.cidade = QtWidgets.QLineEdit(self.frame_2)
        self.cidade.setObjectName("cidade")
        self.horizontalLayout_10.addWidget(self.cidade)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.bairro = QtWidgets.QLineEdit(self.frame_2)
        self.bairro.setObjectName("bairro")
        self.horizontalLayout_5.addWidget(self.bairro)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        self.rua = QtWidgets.QLineEdit(self.frame_2)
        self.rua.setObjectName("rua")
        self.horizontalLayout_11.addWidget(self.rua)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.numero = QtWidgets.QLineEdit(self.frame_2)
        self.numero.setObjectName("numero")
        self.horizontalLayout_7.addWidget(self.numero)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_18.addWidget(self.label_13)
        self.email = QtWidgets.QLineEdit(self.frame_2)
        self.email.setObjectName("email")
        self.horizontalLayout_18.addWidget(self.email)
        self.verticalLayout_2.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_19.addWidget(self.label_14)
        self.nome_fantasia = QtWidgets.QLineEdit(self.frame_2)
        self.nome_fantasia.setObjectName("nome_fantasia")
        self.horizontalLayout_19.addWidget(self.nome_fantasia)
        self.verticalLayout_2.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.registro = QtWidgets.QLCDNumber(self.frame_2)
        self.registro.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.registro.setFrameShape(QtWidgets.QFrame.Box)
        self.registro.setFrameShadow(QtWidgets.QFrame.Plain)
        self.registro.setSmallDecimalPoint(False)
        self.registro.setProperty("value", 12345.0)
        self.registro.setObjectName("registro")
        self.horizontalLayout_6.addWidget(self.registro)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.registrar = QtWidgets.QToolButton(self.frame_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/letter.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.registrar.setIcon(icon1)
        self.registrar.setIconSize(QtCore.QSize(51, 60))
        self.registrar.setCheckable(False)
        self.registrar.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.registrar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.registrar.setAutoRaise(True)
        self.registrar.setObjectName("registrar")
        self.horizontalLayout.addWidget(self.registrar)
        self.cancelar = QtWidgets.QToolButton(self.frame_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelar.setIcon(icon2)
        self.cancelar.setIconSize(QtCore.QSize(51, 60))
        self.cancelar.setCheckable(False)
        self.cancelar.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.cancelar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.cancelar.setAutoRaise(True)
        self.cancelar.setObjectName("cancelar")
        self.horizontalLayout.addWidget(self.cancelar)
        self.verticalLayout.addWidget(self.frame_4)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(-10, -10, 681, 581))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/img/depositphotos_190770396-stock-illustration-colorful-watercolor-spots-hand-drawn.jpg"))
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.frame.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "REGISTRO DE SISTEMA - 7 SISTEMAS"))
        self.titulo.setText(_translate("Form", "SOLICITAÇÃO DE REGISTRO PARA CLIENTE\n"
"PREENCHA O FORMULÁRIO PARA REALIZAR\n"
"A SOLICITAÇÃO DE REGISTRO"))
        self.label_12.setText(_translate("Form", "NOME COMPLETO"))
        self.label_2.setText(_translate("Form", "TELEFONE"))
        self.telefone.setInputMask(_translate("Form", "(999)99999-9999"))
        self.label_7.setText(_translate("Form", "CEP"))
        self.label_3.setText(_translate("Form", "ESTADO"))
        self.label_9.setText(_translate("Form", "CIDADE"))
        self.label_4.setText(_translate("Form", "BAIRRO"))
        self.label_10.setText(_translate("Form", "RUA"))
        self.label_6.setText(_translate("Form", "NUMERO"))
        self.label_13.setText(_translate("Form", "E-MAIL"))
        self.label_14.setText(_translate("Form", "NOME FANTASIA"))
        self.registrar.setText(_translate("Form", "REGISTRAR SISTEMA"))
        self.registrar.setShortcut(_translate("Form", "Return, Enter"))
        self.cancelar.setText(_translate("Form", "CANCELAR"))
        self.cancelar.setShortcut(_translate("Form", "Esc"))
        self.carregar_janela(Form)


    Janela = None
    def carregar_janela(self, Form):
        self.conexao = ('root', 'root', '192.168.0.75', 7077, 'assistencia_tecnica')
        self.Janela = Form
        self.propriedades_janela(Form)
        self.carregar_eventos()
        self.carrega_estado()
        # self.verificar_registro()


    def verificar_registro(self):
        try:
            registro = sql.SQL().pegar_registro()[0]
            self.con = sql.Gerencial_SQL(*self.conexao)

            try: self.data_servidor = [data for data in map(str, self.con.executar_cmd("SELECT CURDATE();", True))][0]
            except Exception as erro:
                if(registro[1] == 1 and int(sql.SQL().pegar_contagem()) != 10): pass
                else: self.encerrar_sistema_falta_conexao(); return False

            self.carregar_dados_anteriores()

            if(registro[1] == 0):
                if(self.con.verifica_licenca_cliente({'codigo': int(self.registro.value())}, 3)):
                    if(self.ainda_nao_ativo()): return True

                if(self.verifica_autorizado()):
                    sql.SQL().alterar_data_registro({'data_registro': QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd"), 'ativado': 1})
                    self.abrir_sistema(); return True
                else: self.licenca_expirada()

            elif(registro[1] == 1 and int(sql.SQL().pegar_contagem()) >= 10):
                if(self.verifica_autorizado()):
                    sql.SQL().atualiza_contagem_acesso(0)
                    self.abrir_sistema(); return True
                else: self.licenca_expirada(); return False

            elif(registro[1] == 1 and int(sql.SQL().pegar_contagem()) == 0):
                if(self.verifica_autorizado()): self.abrir_sistema(); return True
                else:  self.licenca_expirada(); return False

            elif(registro[1] == 1 and int(sql.SQL().pegar_contagem()) != 0): self.abrir_sistema(); return True

            elif(registro[1] == 3):  self.licenca_expirada()

        except Exception as erro: print("ERRO({})".format(erro)) ;return False


    def encerrar_sistema_falta_conexao(self):
        self.carregar_dados_anteriores()
        self.registrar.setEnabled(False)
        QtWidgets.QMessageBox.information(None, "FALHA AO CONECTAR SERVIDOR - 7 SISTEMAS", "NÃO FOI POSSIVEL CONECTAR AO SERVIDOR. "\
                                          "PEÇO A GENTILEZA QUE TENTE MAIS TARDE OU ENTRE EM CONTATO COM O SUPORTE TECNICO. "\
                                          "<b>WHASAPP OU TELEFONE (019)99250-9913</b>")


    def licenca_expirada(self):
        QtWidgets.QMessageBox.warning(None, "SOLICITAÇÃO DE REGISTRO - 7 SISTEMAS",
        "<b>PARECE QUE SUA LICENÇA EXPIROU OU AINDA NÃO FOI EFETUADA!</b>"\
        " ENTRE EM CONTATO COM PARA PODER REGULARIZAR!")
        self.registrar.setEnabled(False)
        # sql.SQL().atualiza_contagem_acesso(0)
        # sql.SQL().alterar_data_registro({'data_registro': QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd"), 'ativado': 0})


    def verifica_autorizado(self):
        try:
            if(self.con.verifica_licenca_cliente({'codigo': int(self.registro.value())}, 1)):
                if(self.con.verifica_licenca_cliente_data({"cliente": int(self.registro.value())})):
                    self.verifica_atualizacao() # ANTIGO
                    return True
            return False
        except: return False


    def abrir_sistema(self):
        self.con.gravar_registro({'usuario': self.codigo_cliente, 'operacao': 'ENTRADA SISTEMA', 'estado_anterior': '', 'estado_novo': '', 'tabela':''})
        self.Janela.close()
        self.abrir_login()
        sql.SQL().atualiza_contagem_acesso(int(sql.SQL().pegar_contagem())  + 1)


    def verifica_atualizacao(self):
        if(sql.SQL().verificar_atualizacao_tabelas(self.data_servidor)):
            self.atualizar_mensagem_banco_local()


    def atualizar_mensagem_banco_local(self):
        if(sql.SQL().verificar_atualizacao_tabelas(self.data_servidor)):
            con_ser = sql.Gerencial_SQL(*self.conexao)
            con = sql.SQL()

            mensagens = con_ser.pegar_mensagen_padrao(int(self.registro.value()))
            for msg in mensagens:
                con.inserir_mensagen_padroes(msg[2])
            con_ser.alterar_mensagem_vista(int(self.registro.value()))
            con.inserir_data_propriedate_tabelas(self.data_servidor, con_ser.pegar_data_vencimento_cliente({'cliente':int(self.registro.value())}))
            con.alterar_clasula(con_ser.pegar_clasula_contrato(), con_ser.pegar_custo_contrato())

            QtWidgets.QMessageBox.information(None, "SOLICITAÇÃO DE REGISTRO - 7 SISTEMAS", "EXISTE NOVAS MENSAGENS, FIQUE ATENTO!")


    def ainda_nao_ativo(self):
        msg = QtWidgets.QMessageBox.question(None, "SOLICITAÇÃO DE REGISTRO - 7 SISTEMAS",
                                          "<b>VOCÊ JÁ TENTOU REGISTRAR O SISTEMA ANTES. PRECISA AGUARDA O CONTATO NOSSO!</b>\n"
                                          "MAS SE VOCÊ DESEJA REVISTAR SEUS DADOS PARA ALTERAR É SÓ ACEITAR.\n VOCÊ QUER REVISAR SEU REGISTRO?")
        if(msg == QtWidgets.QMessageBox.Yes): return True
        sys.exit()
        return False


    def abrir_login(self):
        self.Form = QtWidgets.QDialog()
        self.ui = Login()
        self.ui.setupUi(self.Form)
        self.Form.exec()


    def carregar_dados_anteriores(self):
        dados = sql.SQL().pegar_meus_dados()[0]
        self.codigo_cliente = dados[9]
        self.registro.display(dados[9])
        self.nome_fantasia.setText(dados[10])
        self.nome.setText(dados[0])
        self.telefone.setText(dados[1])
        self.email.setText(dados[2])
        self.cep.setText(dados[3])
        self.rua.setText(dados[4])
        self.estado.setCurrentIndex(self.pegar_estado_ind(dados[5]))
        self.numero.setText(dados[6])
        self.cidade.setText(dados[7])
        self.registrar.disconnect()
        self.registrar.setText("ALTERAR REGISTRO")
        self.registrar.clicked.connect(self.alterar_registro)


    def alterar_registro(self):
        msg = QtWidgets.QMessageBox.question(None, "SOLICITAÇÃO DE REGISTRO - 7 SISTEMAS",
                                             "<b>DESEJA ALTERAR SEU REGISTRO SR {}</b>".format(self.nome.text()))
        if(msg == QtWidgets.QMessageBox.Yes):
            SQL = {"nome": self.nome.text(),
                   "telefone": self.telefone.text(),
                   "email": self.email.text(),
                   "cidade": self.cidade.text(),
                   "cep": self.cep.text(),
                   "estado": self.estado.currentText(),
                   "rua": self.rua.text(),
                   "numero": self.numero.text(),
                   "bairro": self.bairro.text(),
                   "senha": '123@123',
                   "complemento": "",
                   "situacao": 3,
                   "nome_fantasia": self.nome_fantasia.text(),
                   "codigo": int(self.registro.value())}
            sql.SQL().alterar_meus_dados(SQL)
            sql.SQL().alterar_data_registro({'data_registro': QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd"), 'ativado': 0})
            sql.Gerencial_SQL(*self.conexao).alterar_cliente(SQL)
            QtWidgets.QMessageBox.information(None, "SOLICITAÇÃO DE REGISTRO - 7 SISTEMAS",
                           "OBRIGADO <b>{}</b> POR SOLICITAR O REGISTRO DE USO DO SISTEMA"\
                            ". PEÇO QUE AGUARDE NOSSO RETORNO, SE PREFERIR PODE ENTRAR EM"\
                            " CONTATO COM <b>(19)999250-9913</b>".format(self.nome.text()))
            self.Janela.close()


    def pegar_estado_ind(self, estados):
        for cont, estado in enumerate(self.estados):
            if(any([estado == esta for esta in [estados, estados.upper()]])): return int(cont)
        return 26


    def carregar_eventos(self):
        self.cancelar.clicked.connect(self.Janela.close)
        self.cep.textChanged.connect(self.preenche_cep)
        self.nome.textChanged.connect(self.texto_maiusculo_nome)
        self.email.textChanged.connect(self.texto_maiusculo_email)
        self.registrar.clicked.connect(self.cadastra)
        self.registrar.setShortcut("Enter, Return")

    def texto_maiusculo_nome(self): self.nome.setText(self.nome.text().upper())

    def texto_maiusculo_email(self): self.email.setText(self.email.text().upper())


    def carrega_estado(self):
        self.estado.clear()
        self.estados = ["Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal",
                        "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará", "Paraíba",
                        "Paraná" ,"Pernambuco" ,"Piauí" ,"Rio de Janeiro", "Rio Grande do Norte" ,"Rio Grande do Sul" ,"Rondônia" ,"Roraima",
                        "Santa Catarina", "Sergipe", "Tocantins", "São Paulo"]

        self.siglas = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE',
                       'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SE', 'TO', 'SP']

        for estado in self.estados: self.estado.addItem(estado)
        self.estado.setCurrentIndex(26)


    def cadastra(self):
        if(self.verifica_preenchimento()):
            SQL = {"nome": self.nome.text(),
                   "telefone": self.telefone.text(),
                   "email": self.email.text(),
                   "cidade": self.cidade.text(),
                   "cep": self.cep.text(),
                   "estado": self.estado.currentText(),
                   "rua": self.rua.text(),
                   "numero": self.numero.text(),
                   "bairro": self.bairro.text(),
                   "senha": '123@123',
                   "complemento": "",
                   "situacao": 3,
                   "nome_fantasia": self.nome_fantasia.text(),
                   "computador": platform.node()}
            msg = QtWidgets.QMessageBox.question(None, "SOLICITAÇÃO DE REGISTRO - 7 SISTEMAS",
                                                 "CONFIRA OS DADOS ABAIXO! DESEJA SOLICITAR REGISTRO COM OS MESMOS?")
            if(msg == QtWidgets.QMessageBox.No):
                return False

            if(sql.Gerencial_SQL(*self.conexao).inserir_cliente(SQL)):
                self.registro.display(sql.Gerencial_SQL(*self.conexao).pegar_codigo_cliente())
                SQL["codigo"] = self.registro.value()
                sql.SQL().inserir_meus_dados(SQL)
                sql.SQL().inserir_data_registro({'data_registro': QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd"), 'ativado': 0})
                QtWidgets.QMessageBox.information(None, "SOLICITAÇÃO DE REGISTRO - 7 SISTEMAS",
                               "OBRIGADO <b>{}</b> POR SOLICITAR O REGISTRO DE USO DO SISTEMA"\
                                ". PEÇO QUE AGUARDE NOSSO RETORNO, SE PREFERIR PODE ENTRAR EM"\
                                " CONTATO COM <b>(19)999250-9913</b>".format(self.nome.text()))
                self.Janela.close()
            else: QtWidgets.QMessageBox(None, "SOLICITAÇÃO DE REGISTRO - 7 SISTEMAS", "OCORREU UM ERRO NA HORA DE REGISTRAR, TENTE MAIS TARDE OU ENTRE EM CONTATO COM "\
                                        "<b>WHATSAPP (19) 9950-9913</b> ou ligue para o mesmo numero.")


    def verifica_preenchimento(self):
        lista = [self.nome, self.telefone, self.cep, self.cidade,
                 self.bairro, self.rua, self.numero, self.email]
        for campo in lista:
            if(campo.text() == "" or campo.text() == "()-"):
                campo.setFocus(True)
                return False
        return True


    def preenche_cep(self):
        if(len(self.cep.text()) <= 7):
            return False
        PROXIES = {'https': 'https://192.168.0.254:10082/',
                    'http': 'http://192.168.0.254:10082/'}
        try:
            cep = pegar_cep.CEP(self.cep.text(), PROXIES)
            cep = cep.pegar_endereco()
            if(cep != False):
                self.bairro.setText(str(cep["bairro"]))
                self.rua.setText(str(cep["rua"]))
                self.cidade.setText(str(cep["cidade"]))
                self.estado.setCurrentIndex(self.siglas.index(cep["estado"]))
                self.numero.setFocus(True)
        except: pass


    def propriedades_janela(self, Janela):
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.frame.mousePressEvent = self.label_2_click
        self.frame.mouseMoveEvent = self.label_2_move


    def label_2_click(self, event):
        self.oldPos = event.globalPos()

    def label_2_move(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        self.Janela.move(self.Janela.x() + delta.x(), self.Janela.y() + delta.y())
        self.oldPos = event.globalPos()

import recursos


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Registrar_cliente()
    ui.setupUi(Form)
    Form.show()
    ui.verificar_registro()
    sys.exit(app.exec_())
