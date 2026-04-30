import psycopg2
from psycopg2 import Error

def conectar_banco():
    try:
        # Configurações de conexão (ajuste conforme seu banco)
        conexao = psycopg2.connect(
            host='localhost',
            database='escola',   # O banco deve existir ou ser criado
            user='postgres',     # Usuário padrão
            password='aluno', # Sua senha do PostgreSQL
            port= 5432           # Porta padrão do PostgreSQL
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None

def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            data_nascimento VARCHAR(10),
            cpf VARCHAR(14) UNIQUE
        )
    """)
    conexao.commit()

def cadastrar_aluno():
    conn = conectar_banco()
    if conn:
        criar_tabela(conn)
        cursor = conn.cursor()

        print("--- Cadastro de Aluno no Banco de Dados ---")
        nome = input("Nome: ").strip()
        data_nasc = input("Data de Nascimento (DD/MM/AAAA): ").strip()
        cpf = input("CPF (apenas números): ").strip()

        # Comando SQL para inserção
        sql = "INSERT INTO alunos (nome, data_nascimento, cpf) VALUES (%s, %s, %s)"
        valores = (nome, data_nasc, cpf)

        try:
            cursor.execute(sql, valores)
            conn.commit() # Salva as alterações
            print(f"\nSucesso! {cursor.rowcount} registro(s) inserido(s).")
        except Error as e:
            print(f"Erro ao inserir dados: {e}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    cadastrar_aluno()