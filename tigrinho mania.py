import tkinter as tk
import sqlite3
janela = tk.Tk()
janela.title("GRANDE_ONÇÃO")
janela.minsize(width=900, height=700)
def menu():
    for elementos in janela.winfo_children():
        elementos.destroy()
    janela.config(bg="#121212")
    # =====~Frame~===========----------
    frame_menu = tk.Frame(janela, bg="#cc1212").place(relx=0.5,rely=0.1,relwidth=1,relheight=0.2,anchor="center")
    # =====~Title~===========----------
    tk.Label(frame_menu,text="GRANDE ONÇÃO🐆🎲",font=("Palatino Linotype", 24, "bold"), bg="#cc1212",fg="#F5F5F7").place(relx=0.5,rely=0.1,anchor="center")
    #=====~Login~===========----------
    login_button = tk.Button(janela,text="LOGIN",bg="#FFCE00", font=("Georgia", 12),command= login)
    login_button.place(relx=0.5,rely=0.4,relwidth=0.2,relheight=0.075, anchor="center")
    #=====~Register~===========----------
    register_button = tk.Button(janela,text="REGISTER",bg="#12E06A", font=("Georgia", 12), command=cadastro)
    register_button.place(relx=0.5,rely=0.6,relwidth=0.2,relheight=0.075, anchor="center")
    # =====~Selo~===========----------
    tk.Label(janela, text="⋈ SELO DE HONESTIDADE DA O.N.U ⋈", bg="#121212", fg="#F5F5F7", font=("Arial", 10, "bold")).place(relx=0.02,rely=0.95)
def login():
    for elementos in janela.winfo_children():
        elementos.destroy()
    janela.config(bg="#403f3e")
    # =====~Frame~===========----------
    frame_menu = tk.Frame(janela, bg="#222626").place(relx=0.73,rely=0.5,relwidth=0.5,relheight=0.95,anchor="center")
    # =====~Email~===========----------
    emailLogin = tk.Label(frame_menu, text="Email", bg ="#222626", fg="white" )
    emailLogin.place(relx=0.55, rely=0.25, anchor="center")
    email_entry = tk.Entry(frame_menu, highlightbackground="black", highlightthickness=2, font=("Arial", 14))
    email_entry.place(relx=0.73,rely=0.3,relwidth=0.4,relheight=0.08,anchor="center")
    # =====~Password~===========----------
    passwordLogin = tk.Label(frame_menu, text="Password", bg ="#222626", fg="white" )
    passwordLogin.place(relx=0.56, rely=0.45, anchor="center")
    password_entry= tk.Entry(frame_menu, highlightbackground="black", highlightthickness=2, font=("Arial", 14), show="*")
    password_entry.place(relx=0.73,rely=0.5,relwidth=0.4,relheight=0.08,anchor="center")
def cadastro():
    for elementos in janela.winfo_children():
        elementos.destroy()
    janela.config(bg="#403f3e")
def lets_go_gambling():
    for elementos in janela.winfo_children():
        elementos.destroy()
    janela.config(bg="#403f3e")
menu()
janela.mainloop()