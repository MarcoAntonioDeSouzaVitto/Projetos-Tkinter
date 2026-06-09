import sqlite3
import customtkinter as ctk
ctk.set_appearance_mode("dark")
janela = ctk.CTk()
janela.geometry("900x700")
janela.title("Grand Jaguar")

conexao = sqlite3.connect("mkV3060.db")
funcio = conexao.cursor()
funcio.execute("""
    CREATE TABLE IF NOT EXISTS base(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        saldo REAL NOT NULL,
        pp TEXT NOT NULL
)
""")
e = ""
def lobby():
    def accountCreate():
        global warning, e
        try:
            warning.place_forget()
        except:
            pass
        u = username_create.get()
        e = email_create.get()
        p = passwrd_create.get()
        cp = confpasswrd_create.get()
        sd = 0
        profpic = 0
        if not (u and e and p and cp):
            msg = "ALL FIELDS ARE REQUIRED"
        elif not e.endswith(("@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@live.com", "@icloud.com")):
            msg = "INSERT A VALID EMAIL ADDRESS"
        elif len(p) < 6:
            msg = "MINIMUM 6 CHARACTERS"
        elif p != cp:
            msg = "PASSWORDS DO NOT MATCH"
        else:
            funcio.execute(
                "INSERT INTO base(username,email,password, saldo,pp) VALUES(?,?,?,?,?)",
                (u,e,p,sd,profpic)
            )
            conexao.commit()
            game()
            return
        warning = ctk.CTkLabel(frameLogin, text=f"{msg}", text_color="red")
        warning.place(relx = 0.75, rely =0.72, anchor = "center")
    def login():
        global warning, e
        try:
            warning.place_forget()
        except:
            pass
        e = email_login.get()
        p = passwrd_login.get()
        if not (e and p):
            msg = "ALL FIELDS ARE REQUIRED"
        else:
            funcio.execute(
                "SELECT email, password FROM base WHERE email = ? AND password = ?",
                (e,p)
            )
            resultado = funcio.fetchall()
            if resultado:
                game()
                return
            else:
                msg = "INCORRECT PASSWORD OR EMAIL"
        warning = ctk.CTkLabel(frameLogin, text=f"{msg}", text_color="red")
        warning.place(relx = 0.25, rely =0.56, anchor = "center")

    janela.configure(fg_color="#121212")
    go_game = ctk.CTkButton(janela, text="Game",corner_radius=75,width=150,height=150, command=userInfo)
    go_game.place(relx=0.9, rely=0.9, anchor="center")

    frameLogin = ctk.CTkFrame(janela, fg_color="#101c30", width=950,height=650)
    frameLogin.place(relx=0.5,rely=0.5,anchor= "center")
    frameVE = ctk.CTkFrame(frameLogin, fg_color="#ffdc82",width=4,height=600)
    frameVE.place(relx=0.5,rely=0.5, anchor = "center")

    ctk.CTkLabel(frameLogin, text="WELCOME BACK", font=("Arial Regular", 28, "bold")).place(relx=0.25,rely=0.1,anchor="center")
    ctk.CTkLabel(frameLogin, text="E-mail", font=("Arial Regular", 16)).place(relx=0.09, rely=0.27,anchor="center")
    ctk.CTkLabel(frameLogin, text="Password", font=("Arial Regular", 16)).place(relx=0.104, rely=0.422, anchor="center")
    email_login = ctk.CTkEntry(frameLogin,width=350,height=50,placeholder_text="👤 E-mail", font=("Arial Regular",20))
    email_login.place(relx=0.25,rely=0.33,anchor="center")
    passwrd_login = ctk.CTkEntry(frameLogin,width=350,height=50,placeholder_text="🔒 Password", font=("Arial Regular",20))
    passwrd_login.place(relx=0.25,rely=0.48,anchor="center")
    send = ctk.CTkButton(frameLogin,text="ENTER",width=300,height=50, corner_radius=150, font=("Arial Regular",20), command=login)
    send.place(relx=0.25,rely=0.63,anchor="center")

    ctk.CTkLabel(frameLogin, text="NEW HERE?", font=("Arial Regular", 28, "bold")).place(relx=0.75,rely=0.1,anchor="center")
    ctk.CTkLabel(frameLogin, text="Username", font=("Arial Regular", 16)).place(relx=0.75, rely=0.27,anchor="center")
    ctk.CTkLabel(frameLogin, text="E-mail", font=("Arial Regular", 16)).place(relx=0.8, rely=0.27,anchor="center")
    ctk.CTkLabel(frameLogin, text="Password", font=("Arial Regular", 16)).place(relx=0.75, rely=0.422, anchor="center")
    ctk.CTkLabel(frameLogin, text="Confirm Password", font=("Arial Regular", 16)).place(relx=0.8, rely=0.422, anchor="center")
    username_create = ctk.CTkEntry(frameLogin,width=350,height=50,placeholder_text="👤 Username", font=("Arial Regular",20))
    username_create.place(relx=0.75,rely=0.285,anchor="center")
    email_create = ctk.CTkEntry(frameLogin, width=350, height=50, placeholder_text="📩 E-mail",font=("Arial Regular", 20))
    email_create.place(relx=0.75, rely=0.40, anchor="center")
    passwrd_create = ctk.CTkEntry(frameLogin,width=350,height=50,placeholder_text="🔒 Password", font=("Arial Regular",20))
    passwrd_create.place(relx=0.75,rely=0.515,anchor="center")
    confpasswrd_create = ctk.CTkEntry(frameLogin,width=350,height=50,placeholder_text="🔐 Confirm Password", font=("Arial Regular",20))
    confpasswrd_create.place(relx=0.75,rely=0.63,anchor="center")
    send = ctk.CTkButton(frameLogin,text="CREATE ACCOUNT",width=300,height=50, corner_radius=150, font=("Arial Regular",20),command=accountCreate)
    send.place(relx=0.75,rely=0.8,anchor="center")
def userInfo():
    for elemento in janela.winfo_children():
        elemento.destroy()
    janela.configure(fg_color="#121212")
    funcio.execute(
        "SELECT username, saldo, pp FROM base WHERE email = ?",
        (e,)
    )
    data = funcio.fetchone()
    canvas = ctk.CTkCanvas(janela, width=500, height=500, bg="#121212", highlightthickness=0)
    canvas.place(relx=0.2, rely=0.45, anchor="center")
    canvas.create_oval(10, 10, 300, 300, fill="#2d3030", outline="orange", width=5)
    frameLobbys = ctk.CTkFrame(janela, fg_color="black", height=125, corner_radius=0)
    frameLobbys.place(relx=0.0, rely=0.0, relwidth=1.0, anchor="nw")
    botao3traco = ctk.CTkButton(frameLobbys,fg_color="black", text="≡", font=("Agency FB", 73, "bold"), hover_color="black")
    botao3traco.place(relx=0.03,rely=0.40,anchor="center")
    ctk.CTkLabel(frameLobbys, text="Grand\n       Jaguar",fg_color="black", font=("Agency FB", 35, "bold")).place(relx=0.12,rely=0.45,anchor="center")
    ctk.CTkButton(frameLobbys, text="🐯", text_color="Orange", fg_color="black",command= game, hover_color="black",width=40, font=("Agency FB", 43, "bold")).place(relx=0.08, rely=0.45, anchor="center")
    ctk.CTkLabel(janela, text="data[2]",fg_color="#2d3030", font=("Arial Regular", 80, "bold")).place(relx=0.15,rely=0.35,anchor = "center")
    ctk.CTkLabel(janela, text="data[0]", font=("Arial Regular", 24, "bold")).place(relx=0.15, rely=0.57, anchor="center")
    ctk.CTkFrame(janela,fg_color="#121212", border_color="#d9c25b",border_width=3, width=380,height=200).place(relx=0.15,rely=0.75,anchor="center")
    ctk.CTkLabel(janela, text="Saldo: ", font=("Microsoft Sans Serif", 24), text_color="white").place(relx=0.15, rely=0.68,anchor="center")
    saldo = ctk.CTkLabel(janela,text=f"R$data[1]:.2f",text_color="#d9c25b", font=("Microsoft Sans Serif", 38))
    saldo.place(relx=0.15, rely=0.765, anchor="center")
    ctk.CTkFrame(janela,fg_color="#1a1a1a", width=500,height=650, corner_radius=0, border_color="#7ad470",border_width=3).place(relx=0.55,rely=0.5,anchor="center")
    ctk.CTkLabel(janela, text="Deposit",fg_color="#1a1a1a",text_color="white", font=("Arial Rounded MT Bold", 28)).place(relx=0.472, rely=0.3, anchor="center")
    ctk.CTkLabel(janela, text="Add cash💸", fg_color="#1a1a1a", text_color="green",font=("Arial Regular", 32)).place(relx=0.55, rely=0.22, anchor="center")
    def validar(texto):
        if texto in ("", "🪙Ex: 34.50"): return True
        if not texto.replace(".", "", 1).isdigit(): return False
        return "." not in texto or len(texto.split(".")[-1]) <= 2
    vcmd = (janela.register(validar), "%P")
    deposito = ctk.CTkEntry(janela, placeholder_text="🪙Ex: 34.50", font=("Arial Regular", 28), width=400,height=75, validate ="key", validatecommand=vcmd)
    deposito.place(relx =0.55, rely=0.37, anchor = "center")
    sendDeposit = ctk.CTkButton(janela,text="DEPOSIT", text_color="#1a1a1a", fg_color="#2fc91e", width=300,height=85, corner_radius=50, hover_color="#0dd62b")
    sendDeposit.place(relx=0.55,rely=0.7,anchor="center")
def game():
    for elemento in janela.winfo_children():
        elemento.destroy()
    dados = funcio.execute(
        "SELECT username, pp FROM base WHERE email = ? ",
        (e,)
    )
    data = funcio.fetchone()
    janela.configure(fg_color="#141c24")
    frameLobby = ctk.CTkFrame(janela, fg_color="#141c24", height=125, corner_radius=0)
    frameLobby.place(relx=0.0, rely=0.0, relwidth=1.0, anchor="nw")

    bordaframeHO = ctk.CTkFrame(janela, fg_color="white", height=2, corner_radius=0)
    bordaframeHO.place(relx=0.0, y=105, relwidth=1.0, anchor="nw")
    bordaframeVE = ctk.CTkFrame(janela, fg_color="white", height=1200, corner_radius=0)
    bordaframeVE.place(relx=0.1, rely= 0.105, relwidth=0.001, anchor="nw")

    botao3traco = ctk.CTkButton(frameLobby,fg_color="#141c24", text="≡", font=("Agency FB", 73, "bold"), hover_color="#141c24")
    botao3traco.place(relx=0.03,rely=0.40,anchor="center")
    ctk.CTkLabel(frameLobby, text="Grand\n       Jaguar",fg_color="#141c24", font=("Agency FB", 35, "bold")).place(relx=0.12,rely=0.45,anchor="center")
    ctk.CTkLabel(frameLobby, text="🐯", text_color="Orange", fg_color="#141c24", font=("Agency FB", 43, "bold")).place(relx=0.08, rely=0.45, anchor="center")

    botao_casino = ctk.CTkButton(frameLobby, text="♠cassino",font=("Lucida Sans", 21, "bold"), text_color="#c9c9c9", fg_color="#141c24",hover_color="#d60222")
    botao_casino.place(relx=0.3,rely=0.50,anchor="center")
    botao_esporte = ctk.CTkButton(frameLobby, text="🏀esportes",font=("Lucida Sans", 21, "bold"), text_color="#c9c9c9", fg_color="#141c24",hover_color="#d60222")
    botao_esporte.place(relx=0.38,rely=0.50,anchor="center")

    profilepicture = ctk.CTkButton(frameLobby,text=f"{data[1]}",font=("Arial Regular",50, "bold"), fg_color="#141c24",hover_color="#141c24",command=userInfo)
    profile = ctk.CTkButton(frameLobby, text=f"Welcome, {data[0]}!",font=("Arial Regular",20), fg_color="#141c24",hover_color="#141c24",command=userInfo)
    profilepicture.place(relx=0.83,rely=0.5,anchor = "center")
    profile.place(relx=0.9,rely=0.5,anchor = "center")

    frameAdd = ctk.CTkFrame(janela,fg_color="orange", height=300, corner_radius=10)
    frameAdd.place(relx = 0.55, rely= 0.3, relwidth = 0.8, anchor = "center")
    ctk.CTkLabel(frameAdd, text="Primeiro cassino\n honesto\n do Brasil!", font=("Arial Black", 38   )).place(relx=0.15, rely = 0.5, anchor = "center")
    ctk.CTkLabel(janela, text="Populares", font=("Century Gothic", 28, "bold")).place(relx=0.15, rely = 0.54, anchor = "center")
    ctk.CTkButton(janela,text=f"{"\n"*8}Caça-Níquel",command=niquel,width=300,height=380,font=("Lucida Sans", 32, "bold"),fg_color="#d4374f", hover_color="#d4374f").place(relx=0.2,rely=0.78,anchor = "center")
    ctk.CTkButton(janela, text="🎰", font=("Century Gothic", 60, "bold"),fg_color="#d4374f", text_color="white",hover_color="#d4374f",command=niquel, corner_radius=0).place(relx=0.2, rely=0.78, anchor="center")
    ctk.CTkButton(janela, text=f"{"\n" * 8}Cavalinhos", width=300, height=380, font=("Lucida Sans", 32, "bold"),fg_color="#37d444", hover_color="#37d444",command=cavalo).place(relx=0.38, rely=0.78, anchor="center")
    ctk.CTkButton(janela, text="🎠", font=("Century Gothic", 60), fg_color="#37d444", text_color="#61360e",corner_radius=0,hover_color="#37d444",command=cavalo).place(relx=0.38, rely=0.78, anchor="center")
def niquel():
    for elemento in janela.winfo_children():
        elemento.destroy()
    janela.configure(fg_color="#141c24")
    frameLobby = ctk.CTkFrame(janela, fg_color="#141c24", height=125, corner_radius=0)
    frameLobby.place(relx=0.0, rely=0.0, relwidth=1.0, anchor="nw")

    bordaframeHO = ctk.CTkFrame(janela, fg_color="white", height=2, corner_radius=0)
    bordaframeHO.place(relx=0.0, y=105, relwidth=1.0, anchor="nw")

    botao3traco = ctk.CTkButton(frameLobby, fg_color="#141c24", text="≡", font=("Agency FB", 73, "bold"),hover_color="#141c24")
    botao3traco.place(relx=0.03, rely=0.40, anchor="center")
    ctk.CTkLabel(frameLobby, text="Grand\n       Jaguar", fg_color="#141c24", font=("Agency FB", 35, "bold")).place(relx=0.12, rely=0.45, anchor="center")
    ctk.CTkButton(frameLobby, text="🐯", text_color="Orange", fg_color="#141c24",command= game, hover_color="#141c24",width=40, font=("Agency FB", 43, "bold")).place(relx=0.08, rely=0.45, anchor="center")

    botao_casino = ctk.CTkButton(frameLobby, text="♠cassino", font=("Lucida Sans", 21, "bold"), text_color="#c9c9c9",fg_color="#141c24", hover_color="#d60222")
    botao_casino.place(relx=0.3, rely=0.50, anchor="center")
    botao_esporte = ctk.CTkButton(frameLobby, text="🏀esportes", font=("Lucida Sans", 21, "bold"), text_color="#c9c9c9",fg_color="#141c24", hover_color="#d60222")
    botao_esporte.place(relx=0.38, rely=0.50, anchor="center")

    principal = ctk.CTkFrame(janela, fg_color="#910109", width=550, height=940, corner_radius=0)
    principal.place(relx=0.5, rely=0.574,anchor = "center")
    wpp = ctk.CTkFrame(principal,fg_color="#c21502", width=550, height=660)
    wpp.place(relx=0.5,rely=0.4,anchor="center")
    slots = ctk.CTkFrame(janela, fg_color="#d4bfa3",width=500, height=550,corner_radius=0)
    slots.place(relx=0.5,rely=0.45,anchor="center")
    barra1 = ctk.CTkFrame(slots,fg_color="#ffd900", border_color="#ff9500", border_width=3, corner_radius=0,width=8,height=550)
    barra1.place(relx=0.333,rely=0.5,anchor="center")
    barra2 = ctk.CTkFrame(slots,fg_color="#ffd900", border_color="#ff9500", border_width=3, corner_radius=0,width=8,height=550)
    barra2.place(relx=0.6659,rely=0.5,anchor="center")

    play = ctk.CTkButton(principal,text="↺",fg_color="#4da616", corner_radius=40,width=80,height=80, font=("Times New Roman", 70), text_color="#ffc800",hover_color="#66c928")
    play.place(relx=0.5,rely=0.85,anchor="center")
def cavalo():
    for elemento in janela.winfo_children():
        elemento.destroy()
    for elemento in janela.winfo_children():
        elemento.destroy()
    janela.configure(fg_color="#141c24")
    frameLobby = ctk.CTkFrame(janela, fg_color="#141c24", height=125, corner_radius=0)
    frameLobby.place(relx=0.0, rely=0.0, relwidth=1.0, anchor="nw")

    bordaframeHO = ctk.CTkFrame(janela, fg_color="white", height=2, corner_radius=0)
    bordaframeHO.place(relx=0.0, y=105, relwidth=1.0, anchor="nw")

    botao3traco = ctk.CTkButton(frameLobby, fg_color="#141c24", text="≡", font=("Agency FB", 73, "bold"),hover_color="#141c24")
    botao3traco.place(relx=0.03, rely=0.40, anchor="center")
    ctk.CTkLabel(frameLobby, text="Grand\n       Jaguar", fg_color="#141c24", font=("Agency FB", 35, "bold")).place(relx=0.12, rely=0.45, anchor="center")
    ctk.CTkButton(frameLobby, text="🐯", text_color="Orange", fg_color="#141c24",command= game, hover_color="#141c24",width=40, font=("Agency FB", 43, "bold")).place(relx=0.08, rely=0.45, anchor="center")

    botao_casino = ctk.CTkButton(frameLobby, text="♠cassino", font=("Lucida Sans", 21, "bold"), text_color="#c9c9c9",fg_color="#141c24", hover_color="#d60222")
    botao_casino.place(relx=0.3, rely=0.50, anchor="center")
    botao_esporte = ctk.CTkButton(frameLobby, text="🏀esportes", font=("Lucida Sans", 21, "bold"), text_color="#c9c9c9",fg_color="#141c24", hover_color="#d60222")
    botao_esporte.place(relx=0.38, rely=0.50, anchor="center")

    principal = ctk.CTkFrame(janela, fg_color="#24282b", width=900, height=700)
    principal.place(relx=0.5, rely=0.5, anchor="center")
    apostaframe = ctk.CTkFrame(janela,fg_color="#24282b",width=900,height=700)
    apostaframe.place(relx=0.5,rely=0.5,anchor="center")

    corredor_escolhido = ctk.StringVar(value="- - -")

    lbl_escolha = ctk.CTkLabel(
        apostaframe,
        text="Escolha o Cavalinho:",
        font=("Arial", 12, "bold"),
        corner_radius=0
    )
    lbl_escolha.place(relx=0.25, rely=0.05, anchor="w")

    menu_corredores = ctk.CTkOptionMenu(
        apostaframe,
        corner_radius=0,
        button_hover_color="#24282b",
        variable=corredor_escolhido,
        values=["Gordiço ", "Felipe", "Omni-man","Putrefação das trevas","Bob"]
    )
    menu_corredores.place(relx=0.4, rely=0.05, anchor="w")

    pista = ctk.CTkFrame(janela, fg_color="#1a1a1a", height=350)
    pista.place(relx=0.5, rely=0.5, relwidth=0.425, anchor="center")
    pista.pack_propagate(False)

    c1 = ctk.CTkButton(pista, text="🐴", fg_color= "red", width=40, height=40, corner_radius=20, font=("Arial", 24, "bold"))
    c1._canvas.config(width=40, height=40)
    c1.place(x=20, y=20)

    c2 = ctk.CTkButton(pista, text="🐴", fg_color="blue", width=40, height=40, corner_radius=20, font=("Arial", 24, "bold"))
    c2._canvas.config(width=40, height=40)
    c2.place(x=20, y=80)

    c3 = ctk.CTkButton(pista, text="🐴", fg_color="darkred", width=40, height=40, corner_radius=20, font=("Arial", 24, "bold"))
    c3._canvas.config(width=40, height=40)
    c3.place(x=20, y=140)

    c4 = ctk.CTkButton(pista, text="🐴", fg_color="green", width=40, height=40, corner_radius=20, font=("Arial", 24, "bold"))
    c4._canvas.config(width=40, height=40)
    c4.place(x=20, y=200)

    c5 = ctk.CTkButton(pista, text="🐴", fg_color="brown", width=40, height=40, corner_radius=20, font=("Arial", 24, "bold"))
    c5._canvas.config(width=40, height=40)
    c5.place(x=20, y=260)

    btn_iniciar = ctk.CTkButton(janela, text="CORRER! 🏁", font=("Arial", 16, "bold"), fg_color="#4da616",hover_color="#3d8512")
    btn_iniciar.place(relx=0.5, rely= 0.8, anchor = "center")

lobby()
janela.after(0, lambda: janela.state("zoomed"))
janela.mainloop()
