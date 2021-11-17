from PyQt5 import uic,QtWidgets
import mysql
from mysql.connector import connection, cursor

def connection():

    conn = mysql.connector.connect (
        host = "localhost",
        user = "root",
        password = "ih, vazei a senha",
        database = "db_freud"
    )

    return conn

def chama_tela():

    usuario = login.lineEdit.text()
    senha = login.lineEdit_2.text()
    login.label_3.setText("")

    conn = connection()

    cursor = conn.cursor()

    try:
        cursor.execute("SELECT senha_login, id_matricula FROM tb_login WHERE email_login = '{}'".format(usuario))
        senha_bd = cursor.fetchall()
        print(senha_bd[0][0])
        print(senha_bd[0][1])

        id_matricula = int(senha_bd[0][1])

        cursor.execute("SELECT id_nivel, nome FROM tb_matricula WHERE id_matricula = '{}'".format(id_matricula))
        id_nivel_banco = cursor.fetchall()

        print(id_nivel_banco[0][0])
        print(id_nivel_banco[0][1])
        cursor.close()
        conn.close()

        id_nivel = int(id_nivel_banco[0][0])
        nome = str(id_nivel_banco[0][1])

        if senha == senha_bd[0][0]:
            login.lineEdit_2.setText("")
            login.label_3.setText("")
            login.close()

            if id_nivel == 1:
                tela_adm.show()
                tela_adm.label_3.setText("{}".format(nome))
            elif id_nivel == 2:
                tela_professor.show()
                tela_professor.label_3.setText("{}".format(nome))
            else:
                tela_aluno.show()
                tela_aluno.label_3.setText("{}".format(nome))

        elif senha != senha_bd[0][0]:

            login.label_3.setText("Login ou senha incorretos!")
    except:
            id_matricula = 0
            login.label_3.setText("Login ou senha incorretos!")

    

    return id_matricula

def cadastrar_usuario():
 
    nome = criar_conta.lineEdit.text()
    cpf = criar_conta.lineEdit_2.text()
    nascimento = criar_conta.lineEdit_3.text()
    endereco = criar_conta.lineEdit_4.text()
    nome_mae = criar_conta.lineEdit_5.text()
    nome_pai = criar_conta.lineEdit_6.text()

    if criar_conta.radioButton.isChecked():

        nivel = 2

    else:

        nivel = 3


    conn = connection()

    cursor = conn.cursor()

    try:
        command_sql = ("INSERT INTO tb_matricula (id_nivel, nome, cpf, nascimento, endereco, nome_mae, nome_pai) values (%s, %s, %s, %s, %s, %s, %s)")
        data = (
            nivel,
            nome,
            cpf,
            nascimento,
            endereco,
            nome_mae,
            nome_pai
        )

        cursor.execute(command_sql, data)
        conn.commit()

        cursor.execute(("SELECT id_matricula, nome FROM tb_matricula WHERE nome = '{}'".format(nome)))
        dados = cursor.fetchall()

        id = dados[0][0]
        nome = nome.lstrip().lower().replace(" ", "")
        
        sql = "INSERT INTO tb_login (id_matricula, email_login, senha_login) values (%s, %s, %s)"
        data = (
            id,
            f"{nome}@freud.com",
            f"{nome}123@"
        )
        cursor.execute(sql, data)
        conn.commit()

        cursor.close()
        conn.close()

        criar_conta.close()
        tela_adm.show()

         
        criar_conta.lineEdit.setText("")
        criar_conta.lineEdit_2.setText("")
        criar_conta.lineEdit_3.setText("")
        criar_conta.lineEdit_4.setText("")
        criar_conta.lineEdit_5.setText("")
        criar_conta.lineEdit_6.setText("")


    except:
        criar_conta.label_6.setText("Erro ao cadastrar!")

def abre_editar_senha():
    login.close()
    editar_senha.show()

def abre_criar_conta_adm():
    tela_adm.close()
    criar_conta.show()

def abre_excluir_conta_adm():
    
    tela_adm.close()
    excluir_conta.show()

def editar_senhas():

    usuario = editar_senha.lineEdit.text()
    nova_senha = editar_senha.lineEdit_2.text()
    confirmar_senha = editar_senha.lineEdit_3.text()

    conn = connection()

    cursor = conn.cursor()

    try:
        cursor.execute("SELECT email_login FROM tb_login WHERE email_login = '{}'".format(usuario))
        confirma_usuario = cursor.fetchall()
    except:
        editar_senha.label_3.setText("E-mail não existe no nosso sistema!")

    if nova_senha == confirmar_senha:

        try:
            cursor.execute("UPDATE tb_login SET senha_login = '{}' WHERE email_login = '{}'".format(nova_senha, usuario))
            conn.commit()
            editar_senha.close()
            login.show()
        except:
            editar_senha.label_3.setText("Erro ao atualizar a senha!")
    else:
        editar_senha.label_3.setText("As senhas não são iguais!")

def excluir_contas():

    usuario = excluir_conta.lineEdit.text()

    conn = connection()

    cursor = conn.cursor()

    try:

        cursor.execute("SELECT id_matricula FROM tb_login WHERE email_login = '{}'".format(usuario))
        id_excluir = cursor.fetchall()
        excluir = int(id_excluir[0][0])
        print(excluir)

        cursor.execute("DELETE FROM tb_login WHERE email_login = '{}'".format(usuario))
        conn.commit()

        cursor.execute("DELETE FROM tb_matricula WHERE id_matricula = '{}'".format(excluir))
        conn.commit()

        tela_adm.show()
        excluir_conta.close()
    except:
            excluir_conta.label_5.setText("Erro ao deletar usuário!")

def logout_adm():
    tela_adm.close()
    login.label_3.setText("")
    login.show()

def logout_professor():
    tela_professor.close()
    login.label_3.setText("")
    login.show()

def logout_aluno():
    tela_aluno.close()
    login.label_3.setText("")
    login.show()

def fecha_perfil_aluno():

    tela_aluno.show()
    perfil_aluno.close()

def fechar_perfil_professor():

    tela_professor.show()
    perfil_professor.close()

def fechar_criar_conta():

    tela_adm.show()
    criar_conta.close()

def meu_perfil_aluno():

    tela_aluno.close()
    perfil_aluno.show()

    id_matri = chama_tela()

    conn = connection()

    cursor = conn.cursor()

    try:
        cursor.execute("SELECT nome, cpf, nascimento, endereco, nome_mae, nome_pai FROM tb_matricula WHERE id_matricula = '{}'".format(id_matri))
        dados = cursor.fetchall()

        perfil_aluno.label_3.setText("{}".format(dados[0][0]))
        perfil_aluno.label_10.setText("{}".format(dados[0][1]))
        perfil_aluno.label_5.setText("{}".format(dados[0][2]))
        perfil_aluno.label_9.setText("{}".format(dados[0][3]))
        perfil_aluno.label_7.setText("{}".format(dados[0][4]))
        perfil_aluno.label_8.setText("{}".format(dados[0][5]))

        cursor.close()
        conn.close()

    except:

        print("erro")

def meu_perfil_professor():

    tela_professor.close()
    perfil_professor.show()

    id_matri = chama_tela()

    conn = connection()

    cursor = conn.cursor()

    try:
        cursor.execute("SELECT nome, cpf, nascimento, endereco, nome_mae, nome_pai FROM tb_matricula WHERE id_matricula = '{}'".format(id_matri))
        dados = cursor.fetchall()

        perfil_aluno.label_3.setText("{}".format(dados[0][0]))
        perfil_aluno.label_10.setText("{}".format(dados[0][1]))
        perfil_aluno.label_5.setText("{}".format(dados[0][2]))
        perfil_aluno.label_9.setText("{}".format(dados[0][3]))
        perfil_aluno.label_7.setText("{}".format(dados[0][4]))
        perfil_aluno.label_8.setText("{}".format(dados[0][5]))

        cursor.close()
        conn.close()

    except:

        print("erro")

app = QtWidgets.QApplication([])
login = uic.loadUi("sources/login.ui")
tela_adm = uic.loadUi("sources/tela_ADM.ui")
tela_aluno = uic.loadUi("sources/tela_aluno.ui")
tela_professor = uic.loadUi("sources/tela_professor.ui")
editar_senha = uic.loadUi("sources/editar_senha.ui")
criar_conta = uic.loadUi("sources/criarConta_adm.ui")
excluir_conta = uic.loadUi("sources/excluirConta_adm.ui")
perfil_aluno = uic.loadUi("sources/meuPerfil_alunos.ui")
perfil_professor =uic.loadUi("sources/meuPerfil_professor.ui")


tela_adm.pushButton.clicked.connect(logout_adm)
tela_professor.pushButton.clicked.connect(logout_professor)
tela_aluno.pushButton.clicked.connect(logout_aluno)
login.pushButton_2.clicked.connect(chama_tela)
login.pushButton.clicked.connect(abre_editar_senha)
editar_senha.pushButton_2.clicked.connect(editar_senhas)
tela_adm.pushButton_2.clicked.connect(abre_criar_conta_adm)
tela_adm.pushButton_4.clicked.connect(abre_excluir_conta_adm)
criar_conta.pushButton_2.clicked.connect(cadastrar_usuario)
excluir_conta.pushButton_4.clicked.connect(excluir_contas)
tela_aluno.pushButton_3.clicked.connect(meu_perfil_aluno)
tela_professor.pushButton_3.clicked.connect(meu_perfil_professor)
perfil_aluno.pushButton.clicked.connect(fecha_perfil_aluno)
perfil_professor.pushButton.clicked.connect(fechar_perfil_professor)

criar_conta.pushButton.clicked.connect(fechar_criar_conta)

login.show()
app.exec()