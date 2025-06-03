from flask import Flask, request, jsonify
from db_config import get_connection

app = Flask(__name__)

@app.route('/pacientes', methods=['POST'])
def adicionar_paciente():
    dados = request.json
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
        INSERT INTO pacientes (nome, data_nascimento, cpf, telefone, endereco)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (
        dados['nome'],
        dados['data_nascimento'],
        dados['cpf'],
        dados['telefone'],
        dados['endereco']
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensagem': 'Paciente adicionado com sucesso'}), 201

@app.route('/pacientes', methods=['GET'])
def listar_pacientes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pacientes")
    colunas = [desc[0] for desc in cursor.description]
    pacientes = [dict(zip(colunas, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return jsonify(pacientes)

@app.route('/pacientes/<int:id>', methods=['PUT'])
def atualizar_paciente(id):
    dados = request.json
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
        UPDATE pacientes
        SET nome=%s, data_nascimento=%s, cpf=%s, telefone=%s, endereco=%s
        WHERE id=%s
    """
    cursor.execute(sql, (
        dados['nome'],
        dados['data_nascimento'],
        dados['cpf'],
        dados['telefone'],
        dados['endereco'],
        id
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensagem': 'Paciente atualizado com sucesso'})

@app.route('/pacientes/<int:id>', methods=['DELETE'])
def deletar_paciente(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pacientes WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensagem': 'Paciente deletado com sucesso'})

if __name__ == '__main__':
    app.run(debug=True)
