import customtkinter as ctk
import sqlite3
from tkinter import ttk
import shutil  
import os      
import json
import os


def carregar_config():
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
    
        return {"nome_oficina": "Garagem Robson'Car", "cor_destaque": "blue"}


dados = carregar_config()


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def configurar_banco():
    
    if os.path.exists('usuarios.db'):
        try:
            shutil.copy2('usuarios.db', 'backup_garagem.db')
        except Exception as e:
            print(f"Erro ao criar backup: {e}")

    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    
    
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (user TEXT PRIMARY KEY, password TEXT)")
    
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS servicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT,
            veiculo TEXT,
            placa TEXT,
            descricao TEXT,
            valor REAL,
            status TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estoque (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto TEXT,
            quantidade INTEGER
        )
    """)
    
    conn.commit()
    conn.close()
    print("Banco de dados e tabelas configurados com sucesso!")

class JanelaCadastro(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.title("Novo Cadastro")
        self.geometry("400x400")
        self.grab_set() 

        ctk.CTkLabel(self, text="Criar Novo Acesso", font=("Roboto", 20, "bold")).pack(pady=20)
        self.novo_u = ctk.CTkEntry(self, placeholder_text="Usuário", width=200)
        self.novo_u.pack(pady=10)
        self.nova_s = ctk.CTkEntry(self, placeholder_text="Senha", width=200, show="*")
        self.nova_s.pack(pady=10)
        
        ctk.CTkButton(self, text="Salvar", fg_color="green", command=self.registrar).pack(pady=20)

    def registrar(self):
        u, s = self.novo_u.get(), self.nova_s.get()
        if u and s:
            try:
                conn = sqlite3.connect('usuarios.db')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO usuarios (user, password) VALUES (?, ?)", (u, s))
                conn.commit()
                conn.close()
                self.destroy()
            except:
                print("Erro: Usuário já existe.")


class JanelaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(f"{dados['nome_oficina']} - Gestão Profissional")
        self.geometry("1100x650")
        
        
        style = ttk.Style()
        style.theme_use("default")
        
        
        style.configure("Treeview", 
                        background="#2a2a2a", 
                        foreground="white", 
                        rowheight=20, 
                        fieldbackground="#2a2a2a", 
                        borderwidth=0,
                        font=("Segoe UI", 14)) 

        style.map("Treeview", background=[('selected', '#1f538d')])

        
        style.configure("Treeview.Heading", 
                        background="#333", 
                        foreground="white", 
                        relief="flat",
                        font=("Segoe UI", 16, "bold")) 
        
        
        self.menu_lateral = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.menu_lateral.pack(side="left", fill="y")
        ctk.CTkLabel(self.menu_lateral, text=dados['nome_oficina'].upper(), font=("Roboto", 22, "bold")).pack(pady=30)

       

        ctk.CTkButton(self.menu_lateral, text="🏠 Home", fg_color=dados['cor_destaque'], command=self.mostrar_home).pack(pady=10, padx=20)
        ctk.CTkButton(self.menu_lateral, text="🚗 Nova O.S.", fg_color=dados['cor_destaque'], command=self.tela_os).pack(pady=10, padx=20)
        ctk.CTkButton(self.menu_lateral, text="📋 Listar Serviços", fg_color=dados['cor_destaque'], command=self.listar_os).pack(pady=10, padx=20)
        ctk.CTkButton(self.menu_lateral, text="📦 Estoque", fg_color=dados['cor_destaque'], command=self.tela_estoque).pack(pady=10, padx=20)
        ctk.CTkButton(self.menu_lateral, text="💰 Financeiro", fg_color=dados['cor_destaque'], command=self.tela_vendas).pack(pady=10, padx=20)
        ctk.CTkButton(self.menu_lateral, text="🚪 Sair", fg_color="#911", command=self.quit).pack(side="bottom", pady=20)

        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(side="right", fill="both", expand=True, padx=20, pady=20)
        self.mostrar_home()

    def limpar_tela(self):
        for w in self.container.winfo_children(): w.destroy()

    def mostrar_home(self):
        self.limpar_tela()
        ctk.CTkLabel(self.container, text="Bem-vindo, Robson!\nSistema de Funilaria e Pintura", font=("Roboto", 26)).pack(pady=150)
    
    
    def tela_os(self):
        self.limpar_tela()
        ctk.CTkLabel(self.container, text="Nova Ordem de Serviço", font=("Roboto", 24, "bold")).pack(pady=20)
        
        
        self.ent_cli = ctk.CTkEntry(self.container, font=("Segoe UI", 18, "bold"), corner_radius=10, placeholder_text="Nome do Cliente", width=450)
        self.ent_cli.pack(pady=10)
        
        
        self.ent_vei = ctk.CTkEntry(self.container, font=("Segoe UI", 18, "bold"), corner_radius=10, placeholder_text="Veículo (Ex: Gol Prata)", width=450)
        self.ent_vei.pack(pady=10)
        
        
        self.ent_pla = ctk.CTkEntry(self.container, font=("Segoe UI", 18, "bold"), corner_radius=10, placeholder_text="Placa", width=450)
        self.ent_pla.pack(pady=10)
        
        
        self.ent_des = ctk.CTkEntry(self.container, font=("Segoe UI", 18, "bold"), corner_radius=10, placeholder_text="Descrição do Serviço", width=450)
        self.ent_des.pack(pady=10)
        
        
        self.ent_valor = ctk.CTkEntry(self.container, font=("Segoe UI", 18, "bold"), corner_radius=10, placeholder_text="Valor (Ex: 500,00)", width=450)
        self.ent_valor.pack(pady=10)
        self.ent_valor.insert(0, "0,00") 
        
      
        self.ent_valor.bind("<Return>", lambda _: self.salvar_os())
        
      
        ctk.CTkButton(self.container, text="Gravar O.S.", fg_color="green", font=("Roboto", 18, "bold"), width=200, height=45, command=self.salvar_os).pack(pady=30)

    def salvar_os(self):
        try:
            val = float(self.ent_valor.get().replace(',', '.'))
            conn = sqlite3.connect('usuarios.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO servicos (cliente, veiculo, placa, descricao, valor, status) VALUES (?,?,?,?,?,?)",
                           (self.ent_cli.get(), self.ent_vei.get(), self.ent_pla.get(), self.ent_des.get(), val, "Aguardando"))
            conn.commit(); conn.close()
            self.mostrar_home()
        
        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Erro", f"Não foi possível salvar: {e}")    

    def listar_os(self):
        self.limpar_tela()
        ctk.CTkLabel(self.container, text="Serviços na Oficina", font=("Segoe UI", 18, "bold")).pack(pady=10)
        colunas = ("ID", "Cliente", "Veículo", "Placa", "Status")
        self.tabela = ttk.Treeview(self.container, columns=colunas, show="headings")
        for col in colunas: self.tabela.heading(col, text=col)
        self.tabela.pack(fill="both", expand=True, padx=10, pady=10)
        
        btn_f = ctk.CTkFrame(self.container, fg_color="transparent")
        btn_f.pack(pady=10)
        ctk.CTkButton(btn_f, text="✅ Concluir", fg_color="blue", command=self.concluir_os).pack(side="left", padx=10)
        ctk.CTkButton(btn_f, text="❌ Excluir", fg_color="#911", command=self.deletar_os).pack(side="left", padx=10)
        self.atualizar_tabela_dados()

    def atualizar_tabela_dados(self):
        for i in self.tabela.get_children(): self.tabela.delete(i)
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, cliente, veiculo, placa, status FROM servicos")
        for l in cursor.fetchall(): self.tabela.insert("", "end", values=l)
        conn.close()

    def concluir_os(self):
        sel = self.tabela.selection()
        if sel:
            id_os = self.tabela.item(sel)['values'][0]
            conn = sqlite3.connect('usuarios.db')
            conn.execute("UPDATE servicos SET status = 'Concluído' WHERE id = ?", (id_os,))
            conn.commit(); conn.close(); self.atualizar_tabela_dados()

    def deletar_os(self):
        sel = self.tabela.selection()
        if sel:
            id_os = self.tabela.item(sel)['values'][0]
            conn = sqlite3.connect('usuarios.db')
            conn.execute("DELETE FROM servicos WHERE id = ?", (id_os,))
            conn.commit(); conn.close(); self.atualizar_tabela_dados()

    
    def tela_estoque(self):
        self.limpar_tela()
        ctk.CTkLabel(self.container, text="📦 Controle de Estoque", font=("Segoe UI", 18, "bold")).pack(pady=10)
        
        f_add = ctk.CTkFrame(self.container)
        f_add.pack(fill="x", padx=20, pady=10)
        self.e_prod = ctk.CTkEntry(f_add, font=("Segoe UI", 18, "bold"), placeholder_text="Produto", width=250); self.e_prod.pack(side="left", padx=10, pady=15)
        self.e_qtd = ctk.CTkEntry(f_add, font=("Segoe UI", 18, "bold"), placeholder_text="Qtd", width=80); self.e_qtd.pack(side="left", padx=5)
        ctk.CTkButton(f_add, text="➕ Add", fg_color="green", command=self.salvar_prod).pack(side="left", padx=10)

        col = ("ID", "Produto", "Quantidade")
        self.tabela_est = ttk.Treeview(self.container, columns=col, show="headings")
        for c in col: self.tabela_est.heading(c, text=c)
        self.tabela_est.pack(fill="both", expand=True, padx=20, pady=10)

        f_baixa = ctk.CTkFrame(self.container, fg_color="transparent")
        f_baixa.pack(pady=10)
        ctk.CTkLabel(f_baixa, text="Qtd para retirar:").pack(side="left", padx=5)
        self.ent_baixa = ctk.CTkEntry(f_baixa, width=60); self.ent_baixa.insert(0, "1"); self.ent_baixa.pack(side="left", padx=5)
        ctk.CTkButton(f_baixa, text="📉 Dar Baixa", fg_color="#76ba08", command=self.dar_baixa).pack(side="left", padx=10)
        ctk.CTkButton(self.container, text="limpa estoque", command=self.limpa_estoque).pack()
        self.atualizar_tabela_est()
        
    def limpa_estoque(self):
        from tkinter import messagebox  
        confirmar = messagebox.askyesno("Atenção Robson", "Deseja apagar TODOS os itens do estoque?") 
        
        if confirmar:
            try:
                conn = sqlite3.connect('usuarios.db')
                cursor = conn.cursor()
                
                cursor.execute("CREATE TABLE IF NOT EXISTS estoque (id INTEGER PRIMARY KEY AUTOINCREMENT, produto TEXT, quantidade INTEGER)")
                
                cursor.execute("DELETE FROM estoque")
                
                conn.commit()
                conn.close()
                
                for item in self.tabela_est.get_children():
                    self.tabela_est.delete(item)
                messagebox.showinfo("Sucesso", "O estoque foi zerado!")
               
            except Exception as e:
                messagebox.showerror("erro", f"Não consegui limpar o banco: {e}")    
    def salvar_prod(self):
        conn = sqlite3.connect('usuarios.db')
        conn.execute("INSERT INTO estoque (produto, quantidade) VALUES (?,?)", (self.e_prod.get(), int(self.e_qtd.get())))
        conn.commit(); conn.close(); self.atualizar_tabela_est()

    def dar_baixa(self):
        sel = self.tabela_est.selection()
        if sel:
            try:
                qtd_r = int(self.ent_baixa.get())
                item = self.tabela_est.item(sel)['values']
                id_p, qtd_at = item[0], int(item[2])
                if qtd_at >= qtd_r:
                    conn = sqlite3.connect('usuarios.db')
                    conn.execute("UPDATE estoque SET quantidade = ? WHERE id = ?", (qtd_at - qtd_r, id_p))
                conn.commit()
                conn.close(); self.atualizar_tabela_est()
            except: print("Erro na baixa")

    def atualizar_tabela_est(self):
        for i in self.tabela_est.get_children(): 
            self.tabela_est.delete(i)
        
        conn = sqlite3.connect('usuarios.db')
        
        for l in conn.execute("SELECT id, produto, quantidade FROM estoque"): self.tabela_est.insert("", "end", values=l)
        conn.close()

    
    def tela_vendas(self):
        self.limpar_tela()
        conn = sqlite3.connect('usuarios.db')
        total = conn.execute("SELECT SUM(valor) FROM servicos WHERE status = 'Concluído'").fetchone()[0] or 0.0
        qtd = conn.execute("SELECT COUNT(*) FROM servicos WHERE status = 'Concluído'").fetchone()[0]
        conn.close()
        ctk.CTkLabel(self.container, text=f"Faturamento: R$ {total:.2f}", font=("Roboto", 30, "bold"), text_color="#2ecc71").pack(pady=50)
        ctk.CTkLabel(self.container, text=f"Serviços Entregues: {qtd}", font=("Roboto", 18)).pack()


class JanelaLogin(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login - Garagem Robson'Car")
        self.geometry("400x450")
        self.resizable(False, False)

        
        ctk.CTkLabel(self, text="Acesso Restrito", font=("Roboto", 24, "bold")).pack(pady=40)

       
        self.u = ctk.CTkEntry(self, placeholder_text="Usuário", width=250, height=35)
        self.u.pack(pady=10)

        
        self.s = ctk.CTkEntry(self, placeholder_text="Senha", width=250, height=35, show="*")
        self.s.pack(pady=10)

      
        self.u.bind("<Return>", lambda event: self.logar())
        self.s.bind("<Return>", lambda event: self.logar())
        

     
        self.btn_entrar = ctk.CTkButton(self, text="Entrar", width=250, height=40, 
                                        font=("Roboto", 16, "bold"), command=self.logar)
        self.btn_entrar.pack(pady=20)

       
        ctk.CTkButton(self, text="Cadastrar Novo Acesso", fg_color="transparent", 
                      text_color="gray", hover_color="#333", 
                      command=lambda: JanelaCadastro(self)).pack(pady=10)

    def logar(self):
        usuario = self.u.get()
        senha = self.s.get()

        if not usuario or not senha:
            print("Preencha todos os campos!")
            return

        conn = sqlite3.connect('usuarios.db')
       
        user_data = conn.execute("SELECT * FROM usuarios WHERE user=? AND password=?", 
                                 (usuario, senha)).fetchone()
        conn.close()

        if user_data:
            print(f"✅ Bem-vindo, {usuario}!")
            self.destroy()  
            app = JanelaPrincipal()  
            app.mainloop()
        else:
            print("❌ Login Inválido! Verifique usuário e senha.")


if __name__ == "__main__":
    configurar_banco()
    app = JanelaLogin()
    app.mainloop()
