# 🚗 Garagem Robson'Car - Sistema de Gestão de Oficina

Sistema desktop desenvolvido em **Python** para o gerenciamento de ordens de serviço, controle de estoque e acompanhamento financeiro de oficinas mecânicas e de funilaria.

---

## 💻 Tecnologias Utilizadas

* **Python** (Linguagem principal)
* **CustomTkinter** (Interface gráfica moderna e estilizada)
* **SQLite3** (Banco de dados relacional embarcado)
* **Tkinter / ttk.Treeview** (Tabelas de dados e componentes nativos)
* **Shutil / OS / JSON** (Gerenciamento de arquivos, backups automáticos e configurações)

---

## ⚙️ Funcionalidades do Sistema

1. **🔒 Sistema de Login e Cadastro:**
   * Autenticação de usuários integrada ao banco de dados SQLite.
   * Janela dedicada para criação de novos acessos de forma segura.

2. **🛠️ Gestão de Ordens de Serviço (O.S.):**
   * Cadastro completo contendo cliente, veículo, placa, descrição do serviço e valor.
   * Listagem de serviços ativos na oficina em formato de tabela dinâmica.
   * Gestão de status: marcação de serviços como "Concluídos" ou exclusão de registros.

3. **📦 Controle de Estoque:**
   * Cadastro e listagem de produtos com controle de quantidade.
   * Funcionalidade de "Dar Baixa" dinâmica no estoque.
   * Ferramenta de limpeza geral do estoque com alerta de confirmação.

4. **💰 Módulo Financeiro:**
   * Cálculo automático do faturamento total baseado nos serviços concluídos.
   * Indicador da quantidade total de serviços entregues pela oficina.

5. **🛡️ Segurança de Dados:**
   * Backup automático do banco de dados (`usuarios.db`) toda vez que o sistema é inicializado (`shutil.copy2`).
   * Arquivo de configuração externa (`config.json`) para personalização do nome da oficina e temas visuais.

---

## 🚀 Como Executar o Projeto

1. Certifique-se de ter o **Python** instalado na sua máquina.
2. Instale a biblioteca do CustomTkinter abrindo o terminal e digitando:
   ```bash
   pip install customtkinter
