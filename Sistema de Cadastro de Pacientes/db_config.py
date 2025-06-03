import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="clinica",
        user="postgres",
        password="sua_senha"
    )
