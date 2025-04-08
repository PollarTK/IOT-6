import mysql.connector

class Banco:
    def connectar(self):

        return mysql.connector.connect(
            host = "paparella.com.br",
            user = "paparell_aluno_9",
            password = "@Senai2025",
            database = "paparell_python"
        )
    def criar_tabela(self):
        conexao = self.connectar()
        cursor = conexao.cursor()

        query = ('''
        create table if not exists leds(id int auto_increment primary key,
        aluno varchar(255) not null,estado varchar(255) not null) ''')
        cursor.execute(query)
        conexao.commit()
        cursor.close()
        conexao.close()
    def inserir_ou_atualizar(self, aluno, led, estado):
        #verifica o aluno
        conexao = self.connectar()
        cursor = conexao.cursor()
        query = "SELECT id FROM leds WHERE aluno=%s"
        cursor.execute(query, (aluno,))
        id = cursor.fetchone()
        if id:
            # atualiza os dados
            query = "UPDATE leds set estado = %s WHERE id=%s"
            cursor.execute(query, (estado, id[0]))
            print(f"Estado do LED do Aluno: {aluno}, atualizado com Sucesso!")
        else:
            query = "INSERT INTO leds(aluno, led, estado) values (%s,%s,%s)"
            cursor.execute(query,(aluno,led,estado))
            print(f"Estado do LED do Aluno {aluno}, Criado com sucesso!")
        conexao.commit()
        cursor.close()
        conexao.close()

    def lista_estados(self):
        conexao = self.connectar()
        cursor = conexao.cursor()
        query = "SELECT * FROM leds"
        cursor.execute(query)
        leds = cursor.fetchall()
        if not leds:
            print("leds nao encontrados!")
        else:
            for led in leds:
                print(f"ID: {led[0]} | Aluno: {led[1]} |LED: {led[2]}| Estado: {led[3]}")

        conexao.commit()
        cursor.close()
        conexao.close()
    def ler_estados(self, aluno):
        conexao = self.connectar()
        cursor = conexao.cursor()

        query = "SELECT estado FROM leds WHERE aluno =%s"
        cursor.execute(query, (aluno,))
        estado = cursor.fetchone()
        return estado[0]
