import tkinter as tk
import sqlite3

conexao = sqlite3.connect("usuario.db")
funcio = conexao.cursor()
funcio.execute("""
    CREATE TABLE IF NOT EXISTS cadastro1(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
)
""")

janela = tk.Tk()
janela.minsize(width=900, height=700)
janela.title("Banana")
def pg3():
    for elemento in janela.winfo_children():
        elemento.destroy()
    tk.Button(janela, text="VOLTAR", command=pg1).place(relx=0.8, rely=0.7, anchor="center")
    tk.Label(janela, text="3").pack(pady=50)
def pg2():
    for elemento in janela.winfo_children():
        elemento.destroy()
    tk.Label(janela, text="Página de Cadastro",bg="#121414",fg="white", font=("Arial", 18, "bold")).pack(pady=10)
    def pegar_all_dados():
        global aviso
        try:
            aviso.place_forget()
        except:
            pass
        u = entrada_username.get().strip()
        e = entrada_email.get().strip()
        s = entrada_senha.get().strip()
        cs = entrada_conf_senha.get().strip()
        msg = ""
        if u == "" or e == "" or s == "" or cs == "":
            msg = "PREENCHA TODOS OS CAMPOS!"
        elif not e.endswith(("@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com")):
            msg = "INSIRA EMAIL VÁLIDO!"
        elif s != cs:
            msg = "SENHAS NÂO COINCIDEM"
        elif len(s) < 6:
            msg = "SENHA INVÀLIDA"
        if msg == "":
            funcio.execute("SELECT email FROM cadastro1 WHERE email = ?", (e,))
            search = funcio.fetchone()
            if not search is None:
                msg = "EMAIL JÁ CADASTRADO NO SISTEMA!"
        if msg != "":
            aviso = tk.Label(frame_1, text=msg, fg="red", bg="lightblue", font=("Arial", 12, "bold"))
        else:
            aviso = tk.Label(frame_1, text="LOGIN FEITO COM SUCESSO!", fg="green", bg="lightblue",
                             font=("Arial", 12, "bold"))
            funcio.execute("INSERT INTO cadastro1(username,email,password) VALUES(?,?,?)", (u, e, s))
            conexao.commit()
            print(f"Sucesso: {u}, {e}, {s}")
        aviso.place(relx=0.5, rely=0.73, anchor="center")

    # Frame =======================
    frame_1 = tk.Frame(janela, bd=4, bg="lightblue", highlightbackground="darkblue", highlightthickness=2)
    frame_1.place(relx=0.5, rely=0.45, relwidth=0.5, relheight=0.7, anchor="center")
    # =======================

    # Username =======================
    nome = tk.Label(frame_1, text="Username: ", bg="lightblue")
    nome.config(font=("Georgia", 10))
    nome.place(relx=0.1, rely=0.2, anchor="w")

    entrada_username = tk.Entry(frame_1, highlightbackground="black", highlightthickness=1)
    entrada_username.place(relx=0.65, rely=0.2, anchor="center", relwidth=0.5, relheight=0.05)
    # =======================

    # Email =======================
    email = tk.Label(frame_1, text="Email: ", bg="lightblue")
    email.config(font=("Georgia", 10))
    email.place(relx=0.1, rely=0.3, anchor="w")
    entrada_email = tk.Entry(frame_1, highlightbackground="black", highlightthickness=1)
    entrada_email.place(relx=0.65, rely=0.3, anchor="center", relwidth=0.5, relheight=0.05)
    # =======================

    # Senha =======================
    Password = tk.Label(frame_1, text="Password: ", bg="lightblue")
    Password.config(font=("Georgia", 10))
    Password.place(relx=0.1, rely=0.4, anchor="w")
    entrada_senha = tk.Entry(frame_1, highlightbackground="black", highlightthickness=1)
    entrada_senha.place(relx=0.65, rely=0.4, anchor="center", relwidth=0.5, relheight=0.05)
    # =======================

    # Confirmação Senha =======================
    Password_conf = tk.Label(frame_1, text="Password Confirm: ", bg="lightblue")
    Password_conf.config(font=("Georgia", 10))
    Password_conf.place(relx=0.1, rely=0.5, anchor="w")
    entrada_conf_senha = tk.Entry(frame_1, highlightbackground="black", highlightthickness=1)
    entrada_conf_senha.place(relx=0.65, rely=0.5, anchor="center", relwidth=0.5, relheight=0.05)

    # =======================

    def close_pagina():
        conexao.close()
        janela.destroy()

    close = tk.Button(frame_1, text="Close", command=close_pagina)
    close.place(relx=0.9, rely=0.9, anchor="center")
    enviar = tk.Button(frame_1, text="Enviar", command=pegar_all_dados)
    enviar.place(relx=0.5, rely=0.65, relwidth=0.3, relheight=0.07, anchor="center")

    tk.Button(janela, text="VOLTAR", command=pg1).place(relx=0.9, rely=0.95, anchor="center", relwidth=0.08,relheight=0.05)

def pg1():
    for elemento in janela.winfo_children():
        elemento.destroy()
    janela.config(bg="#121414")
    tk.Label(janela, text="Sistema de Login radical",fg="white", bg="#121414", font=("Trebuchet MS", 24, "bold")).place(relx=0.5,rely=0.05,anchor="center")
    tk.Button(janela,text="LOGIN", command=pg3).place(relx=0.5,rely=0.40, anchor="center", relwidth=0.2,relheight=0.1)
    tk.Button(janela,text="CADASTRO", command=pg2).place(relx=0.5, rely=0.55, anchor="center", relwidth=0.2,relheight=0.1)
pg1()
janela.mainloop()
