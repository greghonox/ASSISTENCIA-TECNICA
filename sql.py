import re
import sqlite3

class SQL:
    def __init__(self, contato='(019)99250-9913'):
        self.caminho = ""
        self.banco = r"db_manuntencao.db"
        self.caminho_absoluto = self.caminho + self.banco

        try: self.criar_bancodados(contato)
        except: pass


    def criar_bancodados(self, contato):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            conexao.execute("""CREATE TABLE "categorias" ("codigo"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    	                       "nome" TEXT, "tipo_servicos" INTEGER "situacao" INTEGER,);""")

            conexao.execute("""CREATE TABLE "gerencial" ("usuario"	TEXT, "senha" TEXT, "tentativa_registro" TEXT);""")

            conexao.execute("""CREATE TABLE "atualizacao" ("codigo" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, "atualizacao"	TEXT, "mensagem" TEXT);""")

            conexao.execute("""CREATE TABLE "registro" ("data_registro" TEXT, "ativado" INTEGER);""")

            conexao.execute("""CREATE TABLE "meus_dados" ("codigo" INTEGER,
                            "nome" TEXT, "nome_fantasia" TEXT, "telefone"	TEXT, "email"	TEXT,
                            "cep" TEXT, "rua" TEXT, "estado" TEXT, "numero"	TEXT, "bairro" TEXT,
    	                    "cidade" TEXT, "computador" TEXT, "logo" BLOB);""")

            conexao.execute("""CREATE TABLE "clientes" ("codigo" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                            "cnpj_cpf"	TEXT, "tipo_documento" INTEGER,"nome" TEXT,
    	                    "telefone"	TEXT, "whatsapp" TEXT, "email"	TEXT, "bairro" TEXT,
                            "cep" TEXT, "rua" TEXT, "estado" TEXT, "numero"	TEXT,
    	                    "cidade" TEXT, "complemento" TEXT, situacao INTEGER);""")

            conexao.execute("""CREATE TABLE "fornecedores" ("codigo" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                            "cnpj_cpf" TEXT, "tipo_documento" INTEGER,"nome"	TEXT,
                            "telefone" TEXT,"whatsapp" TEXT, "email" TEXT,"cidade" TEXT,
                            "cep" TEXT,"complemento" TEXT,"estado" TEXT,
                            "rua" TEXT,"numero" TEXT,"bairro" TEXT, situacao INTEGER);""")

            conexao.execute("""CREATE TABLE "servicos" ("codigo" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                            "descricao"	TEXT, "forma_cobranca" INTEGER, "descricao_completa" TEXT,
                            "valor" NUMERIC, "tipo_servico" INTEGER, "situacao" INTEGER);""")

            conexao.execute("""CREATE TABLE "tecnicos" (
                        	"codigo" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, "cpf"	INTEGER ,	"nome"	TEXT ,
                         	"telefone" TEXT ,"whatsapp" TEXT, "email" TEXT ,"cidade" TEXT ,
                          	"cep" TEXT , "bairro" TEXT, "numero" TEXT,	"estado" TEXT , "rua" TEXT ,
                            "complemento" TEXT , "tipo_tecnico" TEXT, "comissao" NUMERIC, situacao INTEGER);""")

            conexao.execute("""CREATE TABLE "usuarios" ("codigo" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,	"cpf" TEXT,
                            "nome"	INTEGER, "senha" INTEGER, "telefone" TEXT, "whastapp" TEXT, "email" TEXT,
                            "tipo_funcionario" INTEGER, situacao INTEGER);""")

            conexao.execute("""CREATE TABLE "equipamentos" ("codigo" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                            "descricao"	TEXT, "unidade"	INTEGER, "fornecedor" INTEGER,
                            "categoria_equipamento"	INTEGER, "descricao_completa" TEXT, "situacao" INTEGER,
                            FOREIGN KEY("categoria_equipamento") REFERENCES "categorias"("codigo"),
                            FOREIGN KEY("fornecedor") REFERENCES "fornecedores"("codigo"));""")

            conexao.execute("""CREATE TABLE "estoque" ("produto" INTEGER NOT NULL, "quantidade" INTEGER NOT NULL,
                        	"preco"	NUMERIC NOT NULL, "data_entrada" TEXT NOT NULL, "descricao" TEXT, "estoque_min" NUMERIC,
                        	FOREIGN KEY("produto") REFERENCES "equipamentos");""")

            conexao.execute("""CREATE TABLE "orcamentos"("codigo" INTEGER PRIMARY KEY AUTOINCREMENT, "data_entrada" TEXT,
                            "data_saida" TEXT, "eqt_ent_oct" INTEGER, "cliente_oct"	INTEGER, "descricao_oct" TEXT,
                            "tecnico_oct" INTEGER, "valor_oct" REAL, "valor_peca" REAL, "valor_desconto_oct" REAL,
                            "total_servico"	REAL, "situacao_oct" INTEGER,
                            FOREIGN KEY("cliente_oct") REFERENCES "clientes"("codigo"),
                            FOREIGN KEY("eqt_ent_oct") REFERENCES "equipamentos"("codigo"));""")

            conexao.execute("""CREATE TABLE "orcamento_produtos" ("orcamento" INTEGER, "produto" INTEGER, "quantidade" INTEGER,
                           FOREIGN KEY("produto") REFERENCES "equipamentos"("codigo"), FOREIGN KEY("orcamento") REFERENCES "orcamentos"("codigo"));""")

            conexao.execute("""CREATE TABLE "orcamento_servicos" ("orcamento" INTEGER, "servico" INTEGER, "quantidade" INTEGER,
                            FOREIGN KEY("orcamento") REFERENCES "orcamentos"("codigo"), FOREIGN KEY("servico") REFERENCES "servicos"("codigo"));""")

            conexao.execute("""CREATE TABLE "mensagens_sistema" ("codigo" INTEGER PRIMARY KEY AUTOINCREMENT, "mensagem_padrao" TEXT);""")

            conexao.execute("""CREATE TABLE "contrato_uso" ("clasulas_contrato" TEXT, "custo_diario" REAL);""")

            conexao.execute("""CREATE TABLE "propriedade_tabelas" ("data_atualizacao" TEXT, "tabela_atualizada" INTEGER, "contato" TEXT, "vencimento_licenca" TEXT, "contagem_acesso" TEXT);""")


            conexao.execute("""CREATE INDEX "categorias_indx" ON "categorias" ("nome" ASC);""")
            conexao.execute("""CREATE INDEX "clients_indxe" ON "clientes" ("nome" ASC);""")
            conexao.execute("""CREATE INDEX "equipamentos_indx" ON "equipamentos" ("descricao" ASC);""")
            conexao.execute("""CREATE INDEX "estoquess_indx" ON "estoque" ("produto" ASC);""")
            conexao.execute("""CREATE INDEX "fornecedores_indx" ON "fornecedores" ("nome" ASC);""")
            conexao.execute("""CREATE INDEX "servicos_indx" ON "servicos" ("descricao" ASC);""")
            conexao.execute("""CREATE INDEX "tenicos_indx" ON "tecnicos" ("nome" ASC);""")
            conexao.execute("""CREATE INDEX "usuarios_indx" ON "usuarios" ("nome" ASC);""")
            conexao.execute("""CREATE INDEX "orcamentos_indx" ON "orcamentos" ("data_entrada"	ASC);""")
            conexao.execute("""CREATE INDEX "orcamento_produtos_indx" ON "orcamento_produtos" ("produto" ASC);""")
            conexao.execute("""CREATE INDEX "orcamento_servicos_indx" ON "orcamento_produtos" ("servico" ASC);""")

            self.inserir_usuarios({"cpf": '333.333.333-988' ,"nome": 'admin' ,"senha": '123' ,"telefone": '(019)99250-9913',
            "whastapp": '(019)99250-9913' ,"email": 'admin@email.com.br' ,"tipo_funcionario": 0 })

            self.executar_cmd("""insert into contrato_uso(clasulas_contrato, custo_diario) values('{CONTRATO BASE}', '1.0'); """)
            self.executar_cmd("""insert into propriedade_tabelas(data_atualizacao, tabela_atualizada, contato, contagem_acesso) values(CURRENT_DATE, 1, '{}', '0'); """.format(contato))
            conexao.close()
        except Exception as erro: pass#print("ERRO EM CRIAR BANCO DE DADOS({})".format(erro))

######################################################################################################################################################################
################################################################################### USUARIOS
    def inserir_usuarios(self, dados):
        try:
            nome = self.limpar_dados(dados["nome"])
            email = self.limpar_dados(dados["email"])

            sql = """insert into usuarios(cpf, nome, senha, telefone, whastapp, email, tipo_funcionario, situacao) values('{}','{}','{}','{}','{}','{}','{}', '1')"""\
            .format(dados["cpf"], nome, dados["senha"], dados["telefone"], dados["whastapp"], email, dados["tipo_funcionario"])
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(sql)
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print(erro); return False


    def pegar_codigo_usuario(self):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo from usuarios order by codigo desc limit 1;" )
            return c.fetchall()[0][0]
        except Exception as erro: return 0


    def pegar_usuario_senha(self, dados):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select nome, senha from usuarios where nome='{}' and senha like '%{}%';".format(dados['usuario'], dados['senha']) )
            use, sen = [dados for dados in c.fetchall()[0]]
            return use == dados['usuario'].upper() and dados['senha'] == sen
        except Exception as erro:print(erro); return False

    def pegar_usuario(self, limite=100, opcao_filtro=0):
        try:
            filtro = ["where situacao='1'", "where situacao='0'", ""]
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo, nome, telefone, whastapp, email, situacao from usuarios {} limit '{}';".format(filtro[opcao_filtro -1], limite) )
            return c.fetchall()
        except Exception as erro:print(erro); return False


    def pegar_usuario_nome(self, nome, limite=100, opcao_filtro=0):
        try:
            filtro = ["situacao='1' and", "situacao='0' and", ""]
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo, nome, telefone, whastapp, email, situacao from usuarios where {} nome like '%{}%' limit '{}';".format(filtro[opcao_filtro -1], nome, limite) )
            return c.fetchall()
        except Exception as erro:print(erro); return False


    def pegar_usuario_codigo(self, codigo, limite=100):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo, nome, telefone, whastapp, email, situacao from usuarios where codigo = '{}' limit '{}';".format(codigo, limite) )
            return c.fetchall()
        except Exception as erro:print(erro); return False


    def pegar_usuario_todos(self, codigo, limite=100):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo, cpf, nome, senha, telefone, whastapp, email, tipo_funcionario, situacao from usuarios where codigo = '{}' limit '{}';".format(codigo, limite) )
            return c.fetchall()
        except Exception as erro:print(erro); return False


    def alterar_usuario(self, dados):
        try:
            nome = self.limpar_dados(dados["nome"])
            email = self.limpar_dados(dados["email"])

            sql = """update usuarios set cpf='{}', nome='{}', senha='{}', telefone='{}', whastapp='{}', email='{}', tipo_funcionario='{}', situacao='1' where codigo='{}';"""\
            .format(dados["cpf"], nome, dados["senha"], dados["telefone"], dados["whastapp"], email, dados["tipo_funcionario"], dados['codigo'])
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO EM INSERIR usuario {}".format(erro)); return False


    def desativar_usuario(self, dados):
        try:
            sql = """update usuarios set situacao='0' where codigo='{}';""".format(dados['codigo'])
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO EM INSERIR USUARIO {}".format(erro)); return False
######################################################################################################################################################################
################################################################################### MEUS DADOS
    def inserir_meus_dados(self, dados):
        try:
            nome = self.limpar_dados(dados["nome"])
            complemento = self.limpar_dados(dados["complemento"])
            bairro = self.limpar_dados(dados["bairro"])
            cidade = self.limpar_dados(dados["cidade"])
            numero = self.limpar_dados(dados["numero"])
            email = self.limpar_dados(dados["email"])
            rua = self.limpar_dados(dados["rua"])
            nome_fantasia = self.limpar_dados(dados["nome_fantasia"])

            sql = """insert into meus_dados(nome, nome_fantasia, telefone, email, cep,
            rua, estado, numero, cidade, bairro, computador, codigo) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');"""\
            .format(nome, nome_fantasia, dados["telefone"], email, dados["cep"], rua, dados["estado"], numero, cidade, dados['bairro'], dados["computador"], dados["codigo"])
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print(erro); return False


    def inserir_meus_dados_logo(self, logo):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute("update meus_dados set logo=?;", (self.pegar_img(logo),))
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print(erro); return False


    def pegar_img(self, img):
        with open(img, 'rb') as file: return file.read()


    def pegar_meus_dados_logo(self):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select logo from meus_dados;" )
            return c.fetchall()
        except: return False


    def alterar_meus_dados(self, dados):
        try:
            nome = self.limpar_dados(dados["nome"])
            complemento = self.limpar_dados(dados["complemento"])
            bairro = self.limpar_dados(dados["bairro"])
            cidade = self.limpar_dados(dados["cidade"])
            numero = self.limpar_dados(dados["numero"])
            email = self.limpar_dados(dados["email"])
            rua = self.limpar_dados(dados["rua"])
            nome_fantasia = self.limpar_dados(dados["nome_fantasia"])

            sql = """update meus_dados set nome='{}', nome_fantasia='{}', telefone='{}', email='{}', cep='{}',
            rua='{}', estado='{}', numero='{}', cidade='{}', bairro='{}';""".format(nome, nome_fantasia, dados["telefone"],
                                       email,dados["cep"], rua, dados["estado"], numero, cidade, dados['bairro'])
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(sql)
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print(erro); return False


    def pegar_meus_dados(self):
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.execute("select nome, telefone, email, cep, rua, estado, numero, cidade, bairro, codigo, nome_fantasia from meus_dados;" )
        return c.fetchall()

#### REGISTRANDO O SISTEMA
    def inserir_data_registro(self, dados):
        try:
            sql = """insert into registro(data_registro, ativado) values('{}', '{}');""".format(dados['data_registro'], dados['ativado'])
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as erro: print(erro); return False

    def alterar_data_registro(self, dados):
        try:
            sql = """update registro set data_registro='{}', ativado='{}';""".format(dados['data_registro'], dados['ativado'])
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as erro: print(erro); return False

    def pegar_registro(self):
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.execute("select * from registro" )
        return c.fetchall()
################################################################################### CLIENTES
    def inserir_clientes(self, dados):
        try:
            nome = self.limpar_dados(dados["nome"])
            complemento = self.limpar_dados(dados["complemento"])
            bairro = self.limpar_dados(dados["bairro"])
            cidade = self.limpar_dados(dados["cidade"])
            numero = self.limpar_dados(dados["numero"])
            email = self.limpar_dados(dados["email"])
            rua = self.limpar_dados(dados["rua"])

            sql = """insert into clientes(cnpj_cpf, tipo_documento, nome, telefone, whatsapp, email, cep,
            rua, estado, numero, cidade, bairro, situacao) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}', '1')"""\
            .format(dados["cpf"], dados["tipo_documento"], nome, dados["telefone"], dados["whastapp"], email,
            dados["cep"], rua, dados["estado"], numero, cidade, bairro)
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO EM INSERIR CLIENTE {}".format(erro)); return False


    def pegar_clientes(self, limite=100, opcao_filtro=0):
        filtro = ["where situacao='1'", "where situacao='0'", ""]
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.execute("select codigo, nome, telefone, whatsapp, email, cnpj_cpf, situacao from clientes {} order by codigo desc limit {};".format(filtro[opcao_filtro -1], limite))
        return c.fetchall()


    def pegar_codigo_cliente(self):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo from clientes order by codigo desc limit 1; " )
            return c.fetchall()[0][0]
        except: return 0


    def pegar_cliente_codigo(self, codigo, limite=100):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo, nome, telefone, whatsapp, email, cnpj_cpf, situacao from clientes where codigo = '{}' order by codigo desc limit '{}'; ".format(codigo, limite))
            return c.fetchall()
        except Exception as erro: print("ERRO EM PEGAR DADOS({})".format(erro)); return 0


    def pegar_cliente_nome(self, nome, limite=100, opcao_filtro=0):
        try:
            filtro = ["situacao='1' and", "situacao='0' and", ""]
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo, nome, telefone, whatsapp, email, cnpj_cpf, situacao from clientes where {} nome like '%{}%' limit '{}';".format(filtro[opcao_filtro -1], nome, limite) )
            return c.fetchall()
        except Exception as erro:print(erro); return False


    def pegar_cliente_documento(self, documento, limite=100, opcao_filtro=0):
        try:
            filtro = ["situacao='1' and", "situacao='0' and", ""]
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo, nome, telefone, whatsapp, email, cnpj_cpf, situacao from clientes where {} cnpj_cpf like '%{}%' limit '{}';".format(filtro[opcao_filtro -1], documento, limite) )
            return c.fetchall()
        except Exception as erro:print(erro); return False


    def pegar_cliente_todos(self, codigo, limite=100):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo, nome, telefone, whatsapp, email, cnpj_cpf, tipo_documento, cep, rua, estado, numero, cidade, bairro, complemento "\
                                " from clientes where codigo = '{}' order by codigo desc limit '{}'; ".format(codigo, limite))
            return c.fetchall()
        except Exception as erro: print("ERRO EM PEGAR DADOS({})".format(erro)); return 0


    def alterar_cliente(self, dados):
        try:
            nome = self.limpar_dados(dados["nome"])
            complemento = self.limpar_dados(dados["complemento"])
            bairro = self.limpar_dados(dados["bairro"])
            cidade = self.limpar_dados(dados["cidade"])
            numero = self.limpar_dados(dados["numero"])
            email = self.limpar_dados(dados["email"])
            rua = self.limpar_dados(dados["rua"])

            sql = """update clientes set cnpj_cpf='{}', tipo_documento='{}', nome='{}', telefone='{}', whatsapp='{}', email='{}', cep='{}',
            rua='{}', estado='{}', numero='{}', cidade='{}', bairro='{}', complemento='{}', situacao='1' where codigo='{}';"""\
            .format(dados["cpf"], dados["tipo_documento"], nome, dados["telefone"], dados["whastapp"], email,
            dados["cep"], rua, dados["estado"], numero, cidade, bairro, complemento, dados['codigo'])
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO EM INSERIR CLIENTE {}".format(erro)); return False


    def desativar_cliente(self, dados):
        try:
            sql = """update clientes set situacao='0' where codigo='{}';""".format(dados['codigo'])
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO EM INSERIR CLIENTE {}".format(erro)); return False
######################################################################################################################################################################
################################################################################### FORNECEDORES
    def inserir_fornecedores(self, dados):
        try:
            nome = self.limpar_dados(dados["nome"])
            complemento = self.limpar_dados(dados["complemento"])
            bairro = self.limpar_dados(dados["bairro"])
            cidade = self.limpar_dados(dados["cidade"])
            numero = self.limpar_dados(dados["numero"])
            email = self.limpar_dados(dados["email"])
            rua = self.limpar_dados(dados["rua"])

            sql = """insert into fornecedores(cnpj_cpf, tipo_documento, nome, telefone, whatsapp, email, cep,
            rua, estado, numero, cidade, situacao) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}', '1')"""\
            .format(dados["cpf"], dados["tipo_documento"], nome, dados["telefone"], dados["whastapp"], email,
            dados["cep"], rua, dados["estado"], numero, cidade)
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print(erro); return False


    def pegar_codigo_fornecedores(self):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo from fornecedores order by codigo desc limit 1; " )
            return c.fetchall()[0][0]
        except: return 0

    def pegar_fornecedores(self, limite=100, opcao_filtro=0):
        filtro = ["where situacao='1'", "where situacao='0'", ""]
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.execute("select codigo, nome, telefone, whatsapp, email, cnpj_cpf, situacao from fornecedores {} order by codigo desc limit '{}';".format(filtro[opcao_filtro -1], limite) )
        return c.fetchall()


    def pegar_fornecedores_codigo(self, codigo, limite=100):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo, nome, telefone, whatsapp, email, cnpj_cpf, situacao from fornecedores where codigo = '{}' order by codigo desc limit '{}'; ".format(codigo, limite))
            return c.fetchall()
        except Exception as erro: print("ERRO EM PEGAR DADOS({})".format(erro)); return 0


    def pegar_fornecedores_nome(self, nome, limite=100, opcao_filtro=0):
        try:
            filtro = ["situacao='1'", "situacao='0'", ""]
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo, nome, telefone, whatsapp, email, cnpj_cpf, situacao from fornecedores where {} and nome like '%{}%' limit '{}';".format(filtro[opcao_filtro -1], nome, limite) )
            return c.fetchall()
        except Exception as erro:print(erro); return False


    def pegar_fornecedores_documento(self, documento, limite=100, opcao_filtro=0):
        try:
            filtro = ["situacao='1' and", "situacao='0' and", ""]
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo, nome, telefone, whatsapp, email, cnpj_cpf, situacao from fornecedores where {} cnpj_cpf like '%{}%' limit '{}';".format(filtro[opcao_filtro -1], documento, limite) )
            return c.fetchall()
        except Exception as erro:print(erro); return False


    def pegar_fornecedor_todos(self, codigo, limite=100):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo, nome, telefone, whatsapp, email, cnpj_cpf, tipo_documento, cep, rua, estado, numero, cidade, bairro, complemento "\
                                " from fornecedores where codigo = '{}' order by codigo desc limit '{}'; ".format(codigo, limite))
            return c.fetchall()
        except Exception as erro: print("ERRO EM PEGAR DADOS({})".format(erro)); return 0


    def alterar_fornecedor(self, dados):
        try:
            nome = self.limpar_dados(dados["nome"])
            complemento = self.limpar_dados(dados["complemento"])
            bairro = self.limpar_dados(dados["bairro"])
            cidade = self.limpar_dados(dados["cidade"])
            numero = self.limpar_dados(dados["numero"])
            email = self.limpar_dados(dados["email"])
            rua = self.limpar_dados(dados["rua"])

            sql = """update fornecedores set cnpj_cpf='{}', tipo_documento='{}', nome='{}', telefone='{}', whatsapp='{}', email='{}', cep='{}',
            rua='{}', estado='{}', numero='{}', cidade='{}', bairro='{}', complemento='{}', situacao='1' where codigo='{}';"""\
            .format(dados["cpf"], dados["tipo_documento"], nome, dados["telefone"], dados["whastapp"], email,
            dados["cep"], rua, dados["estado"], numero, cidade, bairro, complemento, dados['codigo'])
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO EM INSERIR fornecedor {}".format(erro)); return False


    def desativar_fornecedor(self, dados):
        try:
            sql = """update fornecedores set situacao='0' where codigo='{}';""".format(dados['codigo'])
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO EM INSERIR fornecedor {}".format(erro)); return False
######################################################################################################################################################################
################################################################################### TECNICOS
    def inserir_tecnicos(self, dados):
        try:
            complemento = self.limpar_dados(dados["complemento"])
            bairro = self.limpar_dados(dados["bairro"])
            cidade = self.limpar_dados(dados["cidade"])
            numero = self.limpar_dados(dados["numero"])
            email = self.limpar_dados(dados["email"])
            nome = self.limpar_dados(dados["nome"])

            sql = """insert into tecnicos(cpf, nome, telefone, whatsapp, email, cep,
            rua, estado, complemento, tipo_tecnico, comissao, numero, bairro, cidade, situacao) values('{}','{}','{}','{}','{}',
            '{}','{}','{}','{}','{}','{}','{}','{}','{}', '1')"""\
            .format(dados["cpf"], nome, dados["telefone"], dados["whastapp"], email, dados["cep"],
            dados["rua"], dados["estado"], complemento, dados["tipo_tecnico"], dados["comissao"],
            numero, bairro, cidade)
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO:", erro); return False


    def pegar_tecnicos(self, limite=100, opcao_filtro=0):
        try:
            filtro = ["where situacao='1'", "where situacao='0'", ""]
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo, nome, telefone, whatsapp, email, cpf, situacao from tecnicos {} order by codigo desc limit '{}';".format(filtro[opcao_filtro -1], limite) )
            return c.fetchall()
        except Exception as erro: print("ERRO EM PEGAR DADOS({})".format(erro)); return 0


    def pegar_tecnicos_codigo(self, codigo, limite=100):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo, nome, telefone, whatsapp, email, cpf, situacao from tecnicos where codigo = '{}' order by codigo desc limit '{}'; ".format(codigo, limite))
            return c.fetchall()
        except Exception as erro: print("ERRO EM PEGAR DADOS({})".format(erro)); return 0


    def pegar_tecnicos_nome(self, nome, limite=100, opcao_filtro=0):
        try:
            filtro = ["situacao='1' and", "situacao='0' and", ""]
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo, nome, telefone, whatsapp, email, cpf, situacao from tecnicos where {} nome like '%{}%' limit '{}';".format(filtro[opcao_filtro -1], nome, limite) )
            return c.fetchall()
        except Exception as erro:print(erro); return False


    def pegar_tecnicos_documento(self, documento, limite=100, opcao_filtro=0):
        try:
            filtro = ["and situacao='1'", "and situacao='0'", ""]
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo, nome, telefone, whatsapp, email, cpf, situacao from tecnicos where cpf like '%{}%' {} limit '{}';".format(documento, filtro[opcao_filtro -1], limite) )
            return c.fetchall()
        except Exception as erro:print(erro); return False


    def pegar_codigo_tecnicos(self):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo from tecnicos order by codigo desc limit 1; " )
            return c.fetchall()[0][0]
        except: return 0


    def pegar_tecnico_todos(self, codigo, limite=100):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo, cpf, nome, telefone, whatsapp, email, cep,"
            "rua, estado, complemento, tipo_tecnico, comissao, numero, bairro, cidade, situacao "\
                                " from tecnicos where codigo = '{}' order by codigo desc limit '{}'; ".format(codigo, limite))
            return c.fetchall()
        except Exception as erro: print("ERRO EM PEGAR DADOS({})".format(erro)); return 0


    def alterar_tecnico(self, dados):
        try:
            nome = self.limpar_dados(dados["nome"])
            complemento = self.limpar_dados(dados["complemento"])
            bairro = self.limpar_dados(dados["bairro"])
            cidade = self.limpar_dados(dados["cidade"])
            numero = self.limpar_dados(dados["numero"])
            email = self.limpar_dados(dados["email"])
            rua = self.limpar_dados(dados["rua"])

            sql = """update tecnicos set cpf='{}', nome='{}', telefone='{}', whatsapp='{}', email='{}', cep='{}', rua='{}', estado='{}',
            complemento='{}', tipo_tecnico='{}', comissao='{}', numero='{}', bairro='{}', cidade='{}',
            situacao='1' where codigo='{}';"""\
            .format(dados["cpf"], nome, dados["telefone"], dados["whastapp"], email, dados["cep"],
            dados["rua"], dados["estado"], complemento, dados["tipo_tecnico"], dados["comissao"],
            numero, bairro, cidade, dados['codigo'])
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO EM INSERIR tecnico {}".format(erro)); return False


    def desativar_tecnico(self, dados):
        try:
            sql = """update tecnicos set situacao='0' where codigo='{}';""".format(dados['codigo'])
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO EM INSERIR tecnico {}".format(erro)); return False
######################################################################################################################################################################
################################################################################### CATEGORIA
    def inserir_categorias(self, dados):
        try:
            nome = self.limpar_dados(dados["nome"])

            sql = """insert into categorias(nome, tipo_servicos, situacao) values('{}','{}', '1')"""\
            .format(nome.upper(), dados["tipo_servicos"])
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO:", erro); return False


    def pegar_codigo_categorias(self):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo from categorias where situacao='1' order by codigo desc limit 1; " )
            return c.fetchall()[0][0]
        except: return 0


    def pegar_categorias(self, limit=100, opcao_filtro=0):
        filtro = ["where situacao='1'", "where situacao='0'", ""]
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.execute("select * from categorias {} limit {};".format(filtro[opcao_filtro - 1], limit))
        return c.fetchall()


    def pegar_categorias_produtos(self):
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.execute("select * from categorias where tipo_servicos = '0' and situacao='1';" )
        return c.fetchall()


    def pegar_categorias_servicos(self, limit=100):
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.execute("select codigo, nome, tipo_servicos, situacao  from categorias where tipo_servicos = '1' and situacao='1'  limit {};".format(limit))
        return c.fetchall()


    def pegar_categorias_servicos_nome(self, nome, limite=100, opcao_filtro=0):
        try:
            filtro = ["and situacao='1'", "and situacao='0'", ""]
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo, nome, tipo_servicos, situacao from categorias where nome like '%{}%' {} limit '{}';".format(nome, filtro[opcao_filtro - 1], limite) )
            return c.fetchall()
        except Exception as erro:print(erro); return False


    def pegar_categorias_servicos_codigo(self, codigo, limite=100):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo, nome, tipo_servicos, situacao from categorias where codigo = '{}' limit '{}';".format(codigo, limite) )
            return c.fetchall()
        except Exception as erro:print(erro); return False


    def categoria_alterar(self, dados):
        try:
            nome = self.limpar_dados(dados["nome"])

            sql = """update categorias set nome='{}', tipo_servicos='{}', situacao='1' where codigo='{}';""".format(nome.upper(), dados["tipo_servicos"], dados['codigo'])
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO EM ALTERAR CATEGORIA({})".format(erro)); return False

    def categoria_desativar(self, dados):
        try:
            sql = """update categorias set situacao='0' where codigo='{}';""".format(dados['codigo'])
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO EM ALTERAR CATEGORIA({})".format(erro)); return False
######################################################################################################################################################################
################################################################################### EQUIPAMENTOS
    def inserir_produtos(self, dados):
        try:
            descricao = self.limpar_dados(dados["descricao"])
            descricao_completa = self.limpar_dados(dados["descricao_completa"])

            sql = """insert into equipamentos(descricao, unidade, fornecedor, categoria_equipamento, descricao_completa, situacao) values('{}','{}','{}','{}','{}', '1')"""\
            .format(descricao, dados["unidade"], dados["fornecedor"], dados["categoria_equipamento"], descricao_completa)
            conexao = sqlite3.connect(self.caminho_absoluto)

            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO:", erro); return False


    def pegar_codigo_produtos(self):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo from equipamentos order by codigo desc limit 1; " )
            return c.fetchall()[0][0]
        except: return 0


    def pegar_produtos(self, limit=100, opcao_filtro=0):
        filtro = ["where eq.situacao='1'", "where eq.situacao='0'", ""]
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.execute("SELECT eq.codigo, eq.descricao, fr.nome, eq.unidade,"\
                            " ct.nome, eq.situacao FROM equipamentos as eq join fornecedores as "\
                            "fr on fr.codigo=eq.fornecedor join categorias as ct on"\
                            " ct.codigo=eq.categoria_equipamento {} order by eq.codigo desc limit '{}'; ".format(filtro[opcao_filtro -1], limit))
        return c.fetchall()


    def pegar_produtos_nome(self, nome, limit=100, opcao_filtro=0):
        try:
            filtro = ["and eq.situacao='1'", "and eq.situacao='0'", ""]
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("SELECT eq.codigo, eq.descricao, fr.nome, eq.unidade,"\
                                " ct.nome, eq.situacao FROM equipamentos as eq join fornecedores as "\
                                "fr on fr.codigo=eq.fornecedor join categorias as ct on"\
                                " ct.codigo=eq.categoria_equipamento  where eq.descricao like '%{}%' {} order by eq.codigo desc limit '{}'; ".format(nome, filtro[opcao_filtro -1], limit))
            return c.fetchall()
        except Exception as erro:print(erro); return False


    def pegar_produtos_descricao(self, nome, limit=100, opcao_filtro=0):
        try:
            filtro = ["and eq.situacao='1'", "and eq.situacao='0'", ""]
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("SELECT eq.codigo, eq.descricao, fr.nome, eq.unidade,"\
                                " ct.nome, eq.situacao FROM equipamentos as eq join fornecedores as "\
                                "fr on fr.codigo=eq.fornecedor join categorias as ct on"\
                                " ct.codigo=eq.categoria_equipamento  where eq.descricao_completa like '%{}%' {} order by eq.codigo desc limit '{}'; ".format(nome, filtro[opcao_filtro -1], limit))
            return c.fetchall()
        except Exception as erro:print(erro); return False


    def pegar_produtos_codigo(self, codigo, limit=100):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("SELECT eq.codigo, eq.descricao, fr.nome, eq.unidade,"\
                                " ct.nome, eq.situacao FROM equipamentos as eq join fornecedores as "\
                                "fr on fr.codigo=eq.fornecedor join categorias as ct on"\
                                " ct.codigo=eq.categoria_equipamento where eq.codigo='{}' limit '{}'; ".format(codigo, limit))
            return c.fetchall()
        except Exception as erro:print(erro); return False

    def pegar_produtos_codigo_tabela(self, codigo):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("SELECT * FROM equipamentos where codigo='{}'; ".format(codigo))
            return c.fetchall()
        except Exception as erro: print(erro); return False


    def produto_alterar(self, dados):
        try:
            descricao = self.limpar_dados(dados["descricao"])
            descricao_completa = self.limpar_dados(dados["descricao_completa"])

            sql = """update equipamentos set descricao='{}', unidade='{}', fornecedor='{}', categoria_equipamento='{}', descricao_completa='{}', situacao='1' where codigo='{}'; """\
            .format(descricao, dados["unidade"], dados["fornecedor"], dados["categoria_equipamento"], descricao_completa, dados['codigo'])
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO: ALTERAR PRODUTO({})".format(erro)); return False


    def produto_desativar(self, produto):
        try:
            sql = """update equipamentos set situacao='0' where codigo='{}'; """.format(produto)
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            self.remover_produto_estoque(produto)
            return True
        except Exception as erro: print("ERRO: DESATIVAR PRODUTO({})".format(erro)); return False
######################################################################################################################################################################
################################################################################### SERVIÇOS
    def inserir_servicos(self, dados):
        try:
            descricao = self.limpar_dados(dados["descricao"])
            descricao_completa = self.limpar_dados(dados["descricao_completa"])

            sql = """insert into servicos(descricao, forma_cobranca, valor, tipo_servico, descricao_completa, situacao) values('{}','{}','{}','{}','{}', '1');"""\
            .format(descricao, dados["forma_cobranca"], dados["valor_servico"], dados["tipo_servico"], dados["descricao_completa"])
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO:", erro); return False


    def pegar_servicos_tabela(self):
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.execute("select sv.codigo, sv.descricao, sv.forma_cobranca, ct.nome, sv.descricao_completa,  sv.valor, sv.situacao from servicos as sv"\
                            " join categorias as ct on sv.tipo_servico = ct.codigo order by sv.codigo asc; " )
        return c.fetchall()

    def pegar_servicos_tabela_codigo(self, codigo):
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.execute("select sv.codigo, sv.descricao, sv.forma_cobranca, sv.tipo_servico, sv.descricao_completa, sv.valor, sv.situacao from servicos as sv"\
                            " where sv.codigo = '{}' order by sv.codigo asc;".format(codigo))
        return c.fetchall()


    def pegar_servicos_tabela_descricao(self, descricao):
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.execute("select sv.codigo, sv.descricao, sv.forma_cobranca, ct.nome, sv.descricao_completa,  sv.valor, sv.situacao from servicos as sv"\
                            " join categorias as ct on sv.tipo_servico = ct.codigo  where sv.descricao like '%{}%' order by sv.codigo asc;".format(descricao))
        return c.fetchall()



    def pegar_servicos_tabela_observacao(self, descricao_completa):
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.execute("select sv.codigo, sv.descricao, sv.forma_cobranca, ct.nome, sv.valor, sv.descricao_completa, sv.situacao from servicos as sv"\
                            " join categorias as ct on sv.tipo_servico = ct.codigo  where sv.descricao_completa like '%{}%' order by sv.codigo asc;".format(descricao_completa))
        return c.fetchall()


    def pegar_codigo_servicos(self):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo from servicos order by codigo desc limit 1; " )
            return c.fetchall()[0][0]
        except: return 0


    def pegar_servicos(self, limit=100, opcao_filtro=0):
        try:
            filtro = ["where sv.situacao='1'", "where sv.situacao='0'", ""]
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select sv.codigo, sv.descricao, sv.forma_cobranca, "\
                                " ct.nome, sv.valor, sv.situacao from servicos as sv join categorias as ct on"\
                                " ct.codigo = sv.tipo_servico {} limit '{}';".format(filtro[opcao_filtro -1], limit))
            return c.fetchall()
        except Exception as erro:print(erro); return False


    def pegar_servicos_nome(self, nome, limit=100, opcao_filtro=0):
        try:
            filtro = ["and sv.situacao='1'", "and sv.situacao='0'", ""]
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select sv.codigo, sv.descricao, sv.forma_cobranca, "\
                                " ct.nome, sv.valor, sv.situacao from servicos as sv join categorias as ct on"\
                                " ct.codigo = sv.tipo_servico where sv.descricao like '%{}%' {} limit '{}';".format(nome, filtro[opcao_filtro -1], limit))
            return c.fetchall()
        except Exception as erro:print(erro); return False


    def pegar_servicos_descricao(self, nome, limit=100, opcao_filtro=0):
        try:
            filtro = ["and sv.situacao='1'", "and sv.situacao='0'", ""]
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select sv.codigo, sv.descricao, sv.forma_cobranca, "\
                                " ct.nome, sv.valor, sv.situacao from servicos as sv join categorias as ct on"\
                                " ct.codigo = sv.tipo_servico where sv.descricao_completa like '%{}%' {} limit '{}';".format(nome,  filtro[opcao_filtro -1], limit))
            return c.fetchall()
        except Exception as erro:print(erro); return False


    def pegar_servicos_codigo(self, codigo, limit=100):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select sv.codigo, sv.descricao, sv.forma_cobranca, "\
                                " ct.nome, sv.valor, sv.situacao from servicos as sv join categorias as ct on"\
                                " ct.codigo = sv.tipo_servico where sv.codigo = '{}' limit '{}';".format(codigo, limit))
            return c.fetchall()
        except Exception as erro:print(erro); return False


    def alterar_servicos(self, dados):
        try:
            descricao = self.limpar_dados(dados["descricao"])
            descricao_completa = self.limpar_dados(dados["descricao_completa"])

            sql = """update servicos set descricao='{}', forma_cobranca='{}', valor='{}', tipo_servico='{}', descricao_completa='{}', situacao='1' where codigo='{}';"""\
            .format(descricao, dados["forma_cobranca"], dados["valor_servico"], dados["tipo_servico"], dados["descricao_completa"], dados['codigo'])
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO:", erro); return False


    def desativar_servicos(self, dados):
        try:
            sql = """update servicos set situacao='0' where codigo='{}';""".format(dados['codigo'])
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO:", erro); return False
######################################################################################################################################################################
################################################################################### ESTOQUE
    def inserir_estoque(self, dados):
        try:
            descricao = self.limpar_dados(dados["descricao"])

            sql = """insert into estoque(produto, quantidade, preco, data_entrada, descricao, estoque_min) values('{}','{}','{}','{}','{}','{}');"""\
            .format(dados["produto"], dados["quantidade"], dados["preco"], dados["data_entrega"], descricao, dados['estoque_min'])
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO INSERIR SQL({}):".format(erro)); return False


    def pegar_estoque(self, limit=100):
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.execute("select eq.codigo, eq.descricao, et.quantidade, et.estoque_min, et.preco, eq.unidade "
        "from estoque as et join equipamentos as eq on eq.codigo = et.produto limit '{}';".format(limit))
        return c.fetchall()


    def pegar_produto_estoque(self, produto):
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.execute("select * from estoque where produto = '{}';".format(produto))
        return c.fetchall()


    def pegar_produto_estoque_nome(self):
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.execute("select eqp.descricao, et.produto from estoque as et inner join equipamentos as eqp on eqp.codigo = et.produto;")
        return c.fetchall()


    def pegar_produto_estoque_tabela(self):
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.execute("select et.produto, eqp.descricao, et.preco, et.quantidade, eqp.unidade, ctg.nome  from estoque"\
                            " as et inner join equipamentos as eqp on eqp.codigo = et.produto join categorias as ctg on ctg.codigo = eqp.categoria_equipamento"\
                            " order by produto asc;")
        return c.fetchall()


    def pegar_estoque_existente(self, produto):
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.execute("select * from estoque where produto = '{}';".format(produto))
        return 0 != len(c.fetchall())


    def pegar_estoque_codigo_tabela(self, produto):
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.execute("select eq.codigo, eq.descricao, et.quantidade, et.estoque_min, et.preco, eq.unidade,"\
                            " et.descricao, et.data_entrada from estoque as et join equipamentos as eq on eq.codigo = et.produto where et.produto='{}' ;".format(produto))
        return c.fetchall()


    def pegar_estoque_descricao_tabela(self, produto):
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.execute("select et.produto, eqp.descricao, et.preco, et.quantidade, eqp.unidade, ctg.nome  from estoque"\
                            " as et inner join equipamentos as eqp on eqp.codigo = et.produto  join categorias as ctg on ctg.codigo = eqp.categoria_equipamento"\
                            " where eqp.descricao like '%{}%' order by produto asc;".format(produto))
        return c.fetchall()


    def alterar_produto_estoque(self, dados):
        try:
            descricao = self.limpar_dados(dados["descricao"])
            if(descricao != ''):
                sql = """update estoque set quantidade='{}', preco='{}', data_entrada='{}', descricao='{}', estoque_min='{}' where produto = '{}';"""\
                .format(dados["quantidade"], dados["preco"], dados["data_entrega"], descricao, dados['estoque_min'], dados["produto"])
            else:
                sql = """update estoque set quantidade='{}', preco='{}', data_entrada='{}', estoque_min='{}' where produto = '{}';"""\
                .format(dados["quantidade"], dados["preco"], dados["data_entrega"], dados['estoque_min'], dados["produto"])

            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(str(sql).upper())
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO ALTERAR ESTOQUE SQL({}):".format(erro)); return False


    def alterar_produto_estoque_quantidade(self, dados, commit=True, conexao=False):
        try:
            sql = """update estoque set quantidade='{}' where produto = '{}';"""\
            .format(dados["quantidade"], dados["codigo"])

            if(conexao == False): conexao = sqlite3.connect(self.caminho_absoluto)

            c = conexao.cursor()
            c.execute(str(sql).upper())

            if(commit):
                conexao.commit()
                conexao.close()
                return True
            return conexao
        except Exception as erro: print("ERRO:", erro); return False


    def pegar_estoque_nome(self, nome, limit=100):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select eq.codigo, eq.descricao, et.quantidade, et.estoque_min, et.preco, eq.unidade "
            "from estoque as et join equipamentos as eq on eq.codigo = et.produto where eq.descricao like '%{}%'  limit '{}';".format(nome, limit))
            return c.fetchall()
        except Exception as erro:print(erro); return False


    def pegar_estoque_descricao(self, nome, limit=100):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select eq.codigo, eq.descricao, et.quantidade, et.estoque_min, et.preco, eq.unidade "
            "from estoque as et join equipamentos as eq on eq.codigo = et.produto where et.descricao like '%{}%' limit '{}';".format(nome, limit))
            return c.fetchall()
        except Exception as erro:print(erro); return False


    def pegar_estoque_codigo(self, codigo, limit=100):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select eq.codigo, eq.descricao, et.quantidade, et.estoque_min, et.preco, eq.unidade "
            "from estoque as et join equipamentos as eq on eq.codigo = et.produto where eq.codigo = '{}' limit '{}';".format(codigo, limit))
            return c.fetchall()
        except Exception as erro:print(erro); return False


    def remover_produto_estoque(self, produto):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute("delete from estoque where produto = '{}';".format(produto))
            conexao.commit()
            conexao.close()
        except Exception as erro: print("ERRO EM REMOVER PRODUTO({})".format(erro)); return False
######################################################################################################################################################################
################################################################################### ORCAMENTOS
    def inserir_orcamento(self, dados, commit=True, conexao=False):
        """
        COMMIT COMO FALSE VAI FAZER ELE RETORNA UM OBJETO SQLITE3.CONNECT PARA FECHAR A CONEXAO DEPOIS.
        CONEXAO E A CONEXÃO ANTERIOR JÁ ABERTA
        sql = {'eqt_ent_oct': '4', 'data_entrada': '12/07/2019 08:31', 'data_saida': '12/07/2019', 'cliente_oct': '2', 'descricao_oct': 'ertxdfghfdghdfg', 'tecnico_oct': '1', 'valor_oct': 0.0, 'valor_peca': 225.0, 'valor_desconto_oct': 0.0, 'total_servico': 225.0, 'situacao_oct': 9}
        cmd = SQL().inserir_orcamento(sql, False)
        cmd = SQL().inserir_orcamento(sql, False, cmd)
        cmd = SQL().inserir_orcamento(sql, False, cmd)
        SQL().fechar_conexao(cmd)
        """

        try:
            descricao = self.limpar_dados(dados["descricao_oct"])
            sql = """insert into orcamentos(data_entrada, data_saida, cliente_oct, descricao_oct, tecnico_oct, valor_oct,
            valor_peca, valor_desconto_oct, total_servico, situacao_oct, eqt_ent_oct) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}', '{}');"""\
            .format(dados['data_entrada'], dados['data_saida'], dados['cliente_oct'], descricao, dados['tecnico_oct'],dados['valor_oct'],
                    dados['valor_peca'], dados['valor_desconto_oct'], dados['total_servico'], dados['situacao_oct'], dados['eqt_ent_oct'])

            if(conexao == False): conexao = sqlite3.connect(self.caminho_absoluto)

            c = conexao.cursor()
            c.execute(str(sql).upper())
            if(commit):
                conexao.commit()
                conexao.close()
                return True
            return conexao
        except Exception as erro: print("ERRO:", erro); return False

    def pegar_codigo_orcamentos(self):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.execute("select codigo from orcamentos order by codigo desc limit 1; " )
            return c.fetchall()[0][0]
        except: return 0
######################################################################################################################################################################
################################################################################### ORCAÇEMENTOS SERVIÇOS
    def inserir_orcamento_servicos(self, dados, conexao):
        try:
            sql = """insert into orcamento_servicos(orcamento, servico, quantidade) values ('{}','{}','{}');"""\
            .format(dados["orcamento"], dados["servico"], dados["quantidade"])
            c = conexao.cursor()
            c.execute(sql)
            return conexao
        except Exception as erro: print(erro); return False
######################################################################################################################################################################
################################################################################### ORCAÇEMENTOS PRODUTOS
    def inserir_orcamento_produtos(self, dados, conexao):
        try:
            sql = """insert into orcamento_produtos(orcamento, produto, quantidade) values ('{}','{}','{}');"""\
            .format(dados["orcamento"], dados["produto"], dados["quantidade"])
            c = conexao.cursor()
            c.execute(sql)
            return conexao
        except Exception as erro: print(erro); return False
######################################################################################################################################################################
################################################################################### UTEIS
    def limpar_dados(self, dados):  return dados.replace("\"", "").replace("\'", "").upper()

    def fechar_conexao(self, conexao):
        conexao.commit()
        conexao.close()
        return True

    def executar_cmd(self, cmd, retorna=False):
        try:
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(cmd)
            conexao.commit()
            conexao.close()
            if(retorna):  return c.fetchall()
            return True
        except Exception as erro:  print("ERRO EXECUTAR COMANDO {}".format(erro)); return False
######################################################################################################################################################################
################################################################################### PROPRIEDADES MENSAGENS
    def verificar_atualizacao_tabelas(self, data):
        """
        VERIFICA SE A DATA LOCAL É IGUAL AO DO SERVIDOR
        """
        try:
            sql = "select data_atualizacao from propriedade_tabelas;"
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            return  c.execute(sql).fetchall()[0][0] != data
        except Exception as erro: print("ERRO EM VERIFICAR ATUALIZAÇÃO({})".format(erro)); return True
######################################################################################################################################################################
################################################################################### CONTRATO MENSAGENS
    def inserir_mensagen_padroes(self, msg):
        try:
            sql = "insert into mensagens_sistema(mensagem_padrao) values('{}');".format(msg)
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(sql)
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO EM INSERIR MENSAGEM({})".format(erro)); return False


    def alterar_clasula(self, clasula, custo_diario):
        try:
            sql = "update contrato_uso set clasulas_contrato='{}', custo_diario='{}';".format(clasula, custo_diario)
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(sql)
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO EM INSERIR MENSAGEM({})".format(erro)); return False


    def pegar_clasula(self):
        try:
            sql = "select * from contrato_uso;"
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            return c.execute(sql).fetchall()[0]
        except Exception as erro: print("ERRO EM PEGAR CLASULAS CONTRATOS({})".format(erro)); return False


    def inserir_data_propriedate_tabelas(self, data_atual, vencimento):
        try:
            sql = "update propriedade_tabelas set data_atualizacao='{}', contagem_acesso='0', tabela_atualizada='1', vencimento_licenca='{}';".format(data_atual, vencimento)
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(sql)
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO EM ATUALIZAR PROPRIEDADES({})".format(erro)); return False


    def atualiza_contagem_acesso(self, contagem):
        try:
            sql = "update propriedade_tabelas set contagem_acesso='{}';".format(contagem)
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            c.execute(sql)
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro: print("ERRO EM GRAVAR ACESSO({})".format(erro)); return False


    def pegar_contagem(self):
        try:
            sql = "select contagem_acesso from propriedade_tabelas;"
            conexao = sqlite3.connect(self.caminho_absoluto)
            c = conexao.cursor()
            return c.execute(sql).fetchall()[0][0]
        except Exception as erro: print("ERRO EM PEGAR CONTAGEM{}".format(erro))


    def pegar_vencimento_cliente(self):
        sql = "select vencimento_licenca from propriedade_tabelas;"
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.cursor()
        return c.execute(sql).fetchall()

    def pegar_todas_mensagens(self):
        sql = "select codigo, mensagem_padrao from mensagens_sistema;"
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.cursor()
        return c.execute(sql).fetchall()


    def pegar_mensagem_padrao(self):
        sql = "select mensagem_padrao from mensagens_sistema order by codigo desc limit 1;"
        conexao = sqlite3.connect(self.caminho_absoluto)
        c = conexao.cursor()
        return c.execute(sql).fetchall()


class Gerencial_SQL:
    def __init__(self, user, passwd, host, port, db):
        USER = user
        PASSWORD_LOCAL = passwd
        HOST_LOCAL = host.split(":")[0]
        PORT = port
        DB_LOCAL = db
        try:
            self.engine = create_engine('mysql://{}:{}@{}:{}/{}'.format(USER,
                                        PASSWORD_LOCAL, HOST_LOCAL, PORT, DB_LOCAL), connect_args={'connect_timeout': 5})
            metadata = MetaData(bind=self.engine)

        except my.OperationalError as erro: print("ERRO CONECTAR NO BANCO DADOS {}".format(erro)); print("ERRO DE CONEXAO COM O BANCO({})".format(erro)); return False
        except my.InternalError as erro: print("ERRO CONECTAR NO BANCO DADOS {}".format(erro)); print("ERRO DE CONEXAO COM O BANCO({})".format(erro)); return False
        except Exception as erro:  print("ERRO EXECUTAR COMANDO {}".format(erro)); print("ERRO DE CONEXAO COM O BANCO({})".format(erro)); return False


    def pegar_codigo_cliente(self):
        sql = "select codigo from CLIENTES order by codigo desc limit 1"
        try: return self.engine.execute(sql).fetchall()[0][0]
        except Exception as erro: print("ERRO EM PEGAR CODIGO ({})".format(erro)); return False


    def verifica_licenca_cliente(self, dados, ativo=3):
        sql = "select situacao from CLIENTES where codigo='{}';".format(dados['codigo'])
        try: return True if(self.engine.execute(sql).fetchall()[0][0] == ativo) else False
        except: return False

    def verifica_licenca_cliente_data(self, dados):
        sql = "select cliente from VENCIMENTO_CLIENTES where cliente='{}' and validade>=curdate();".format(int(dados['cliente']))
        try: return True if(self.engine.execute(sql).fetchall()[0][0] == int(dados['cliente'])) else False
        except Exception as erro: print(erro); return False


    def pegar_data_vencimento_cliente(self, dados):
        sql = "select validade from VENCIMENTO_CLIENTES where cliente='{}' order by codigo desc limit 1;".format(int(dados['cliente']))
        try: return self.engine.execute(sql).fetchall()[0][0]
        except Exception as erro: print(erro); return False


    def pegar_clasula_contrato(self):
        sql = "select clasulas from CONTRATOS_SIS_MANUNTECAOS;"
        try: return self.engine.execute(sql).fetchall()[0][0]
        except Exception as erro: print(erro); return False


    def pegar_custo_contrato(self):
        sql = "select * from CUSTO_SIS_MANUNTECAO;"
        try: return self.engine.execute(sql).fetchall()[0][0]
        except Exception as erro: print(erro); return False


    def inserir_cliente(self, dados):
        usuario = dados['nome'].split(" ")[0] +'@'+ re.sub('[\(|\)|-]', '', dados['telefone'])
        nome = self.limpar_dados(dados['nome'])
        nome_fantasia = self.limpar_dados(dados['nome_fantasia'])
        cidade = self.limpar_dados(dados['cidade'])
        bairro = self.limpar_dados(dados['bairro'])
        numero = self.limpar_dados(dados['numero'])
        rua = self.limpar_dados(dados['rua'])
        email = self.limpar_dados(dados['email'])

        sql = "insert into CLIENTES(nome, usuario, nome_fantasia, telefone, cep, estado, cidade, bairro, rua, numero, email, situacao, computador) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');"\
        .format(nome, usuario, nome_fantasia, dados['telefone'], dados['cep'], dados['estado'], cidade, bairro,  rua, numero, email, dados['situacao'], dados['computador'])
        try: self.engine.execute(sql); return True
        except Exception as erro: print("ERRO EM INSERIR NO BANCO({})".format(erro)); return False


    def alterar_cliente(self, dados):
        usuario = dados['nome'].split(" ")[0] +'@'+ re.sub('[\(|\)|-]', '', dados['telefone'])
        usuario = dados['nome'].split(" ")[0] +'@'+ re.sub('[\(|\)|-]', '', dados['telefone'])
        nome = self.limpar_dados(dados['nome'])
        nome_fantasia = self.limpar_dados(dados['nome_fantasia'])
        cidade = self.limpar_dados(dados['cidade'])
        bairro = self.limpar_dados(dados['bairro'])
        numero = self.limpar_dados(dados['numero'])
        rua = self.limpar_dados(dados['rua'])
        email = self.limpar_dados(dados['email'])

        sql = "update CLIENTES set nome='{}', senha='{}', telefone='{}', cep='{}', estado='{}', cidade='{}', bairro='{}', rua='{}', numero='{}', email='{}', situacao='{}', usuario='{}' where codigo='{}'; "\
        .format(dados['nome'], dados['senha'], dados['telefone'], dados['cep'], dados['estado'], cidade, bairro, rua, numero, email, dados['situacao'], usuario, dados['codigo'])
        try: self.engine.execute(sql); return True
        except: return False


    def pegar_mensagen_padrao(self, dados):
        try:
            sql = "select * from MENSAGEN_PADROES where cliente='{}' and situacao='1'; ".format(dados)
            return self.engine.execute(sql).fetchall()
        except Exception as erro: print("ERRO EM PEGAR MENSAGEM({})".format(erro)); return False


    def alterar_mensagem_vista(self, dados):
        try:
            sql = "update MENSAGEN_PADROES set situacao='0' where cliente='{}'; ".format(dados)
            self.engine.execute(sql)
            return True
        except Exception as erro: print("ERRO EM ALTERAR MENSAGEM({})".format(erro)); return False


    def executar_cmd(self, cmd, retorna=False):
        try:
            saida = self.engine.execute(cmd)
            if(retorna): return saida.fetchall()[0]
            return True
        except: return False


    def gravar_registro(self, dados):
        sql = "insert into LOG_SYS(data_hora, usuario, operacao, tabela, estado_anterior, estado_novo) values(now(), '{}', '{}', '{}', '{}', '{}');".format(dados['usuario'],
                                                                                           dados['operacao'], dados['tabela'], dados['estado_anterior'], dados['estado_novo'])
        try: self.engine.execute(sql); return True
        except Exception as erro:  print("ERRO EM REGISTRAR LOG({})".format(erro)); return False


    def limpar_dados(self, dados):  return dados.replace("\"", "").replace("\'", "").upper()
# print(SQL().alterar_produto_estoque({"quantidade":"10","preco":"1.555","data_entrega":"11/01/2018","produto":"1","descricao":"121212"}))
# print(SQL().pegar_estoque_codigo_tabela('1')[0][3])
# sql = {'eqt_ent_oct': '4', 'data_entrada': '12/07/2019 08:31', 'data_saida': '12/07/2019', 'cliente_oct': '2', 'descricao_oct': 'ertxdfghfdghdfg', 'tecnico_oct': '1', 'valor_oct': 0.0, 'valor_peca': 225.0, 'valor_desconto_oct': 0.0, 'total_servico': 225.0, 'situacao_oct': 9}
# cmd = SQL().inserir_orcamento(sql, False)
# for pr in range(7):
#     if(SQL().alterar_produto_estoque_quantidade({"quantidade": 3, "codigo": pr}, False, cmd) == False): print("erro"); break
#     SQL().inserir_orcamento_produtos({'orcamento': 1, 'produto': pr, 'quantidade': 10}, cmd)
#     SQL().inserir_orcamento_servicos({'orcamento': 1, 'servico': pr, 'quantidade': 10}, cmd)
# SQL().fechar_conexao(cmd)
# SQL().alterar_data_registro({'data_registro':'10/10/2020'})
# print(SQL().pegar_registro())
# print(SQL().pegar_usuario_senha({'usuario':'GREG', 'senha': 135}))
# Gerencial_SQL().gravar_registro({'usuario': 'gregorio', 'operacao': 'entrada no sistema', 'estado_anterior': '', 'estado_novo': ''})
# print(SQL().pegar_cliente_codigo(9))
# print(SQL().pegar_estoque_codigo('2'))
