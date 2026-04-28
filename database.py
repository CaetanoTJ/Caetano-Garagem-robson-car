import sqlite3

from main import JanelaLogin

def configurar_banco():
    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()
    
    # 1. CRIA A TABELA DE USUÁRIOS (Faltava isso!)
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS usuarios (
        user TEXT PRIMARY KEY, 
        password TEXT)
    """)
    
    # 2. CRIA A TABELA DE SERVIÇOS (Corrigida)
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS servicos (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        cliente TEXT, 
        veiculo TEXT, 
        placa TEXT, 
        descricao TEXT, 
        valor REAL, 
        status TEXT)
    """)
    
    # Tabela 3: ESTOQUE!)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estoque (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto TEXT, 
            quantidade INTEGER,
            valor REAL
        )
    """)
    
    # 4. CRIA O ACESSO INICIAL
    try:
        cursor.execute("INSERT INTO usuarios (user, password) VALUES (?, ?)", ("admin", "1234"))
        conexao.commit()
        print("Sucesso: Tabela de usuários pronta e 'admin' criado!")
    except:
        print("Aviso: Banco já possui o usuário admin.") 
    
    conexao.close()
    
    if __name__ == "__main__":
      configurar_banco() 
      app = JanelaLogin()
      app.mainloop()