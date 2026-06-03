import sqlite3
import customtkinter as ctk
ctk.set_appearance_mode("dark")
janela = ctk.CTk()
janela.geometry("900x700")
janela.title("Grand Jaguar")
def lobby():
    janela.configure(fg_color="#121212")
    frameLobby = ctk.CTkFrame(janela, fg_color="red", width=3000,height=125, corner_radius=0)
    frameLobby.place(relx=0.5, rely=0.05, anchor="center")
    ctk.CTkLabel(frameLobby, text="Grand Jaguar",fg_color="red", font=("Agency FB", 42, "bold")).place(relx=0.5,rely=0.5,anchor="center")
    go_game = ctk.CTkButton(janela, text="Game",corner_radius=75,width=150,height=150, command=game)
    go_game.place(relx=0.5, rely=0.5, anchor="center")
def game():
    for elemento in janela.winfo_children():
        elemento.destroy()
    janela.configure(fg_color="#141c24")
    frameLobby = ctk.CTkFrame(janela, fg_color="#141c24", height=125, corner_radius=0)
    frameLobby.place(relx=0.0, rely=0.0, relwidth=1.0, anchor="nw")
    bordaframeHO = ctk.CTkFrame(janela, fg_color="white", height=2, corner_radius=0)
    bordaframeHO.place(relx=0.0, y=125, relwidth=1.0, anchor="nw")
    bordaframeVE = ctk.CTkFrame(janela, fg_color="white", height=1200, corner_radius=0)
    bordaframeVE.place(relx=0.1, rely= 0.125, relwidth=0.001, anchor="nw")
    botao3traco = ctk.CTkButton(frameLobby,fg_color="#141c24", text="≡", font=("Agency FB", 73, "bold"), hover_color="#141c24")
    botao3traco.place(relx=0.03,rely=0.45,anchor="center")
    ctk.CTkLabel(frameLobby, text="Grand\n       Jaguar",fg_color="#141c24", font=("Agency FB", 38, "bold")).place(relx=0.12,rely=0.5,anchor="center")
    ctk.CTkLabel(frameLobby, text="🐯", text_color="Orange", fg_color="#141c24", font=("Agency FB", 46, "bold")).place(relx=0.08, rely=0.5, anchor="center")

lobby()
janela.after(0, lambda: janela.state("zoomed"))
janela.mainloop()
