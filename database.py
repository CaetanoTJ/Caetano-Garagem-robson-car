import sqlite3

from main import JanelaLogin

def configurar_banco():
    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()
    
   
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS usuarios (
        user TEXT PRIMARY KEY, 
        password TEXT)
    """)
    
   
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
    
  
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estoque (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto TEXT, 
            quantidade INTEGER,
            valor REAL
        )
    """)
    
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
