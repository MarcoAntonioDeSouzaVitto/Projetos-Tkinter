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
    frameLobby = ctk.CTkFrame(janela, fg_color="#541c24", height=125, corner_radius=0)
    frameLobby.place(relx=0.0, rely=0.0, relwidth=1.0, anchor="nw")
    bordaframe = ctk.CTkFrame(janela, fg_color="white", height=2, corner_radius=0)
    bordaframe.place(relx=0.0, y=125, relwidth=1.0, anchor="nw")
    ctk.CTkLabel(frameLobby, text="Grand\n       Jaguar",fg_color="#403f3e", font=("Agency FB", 32, "bold")).place(relx=0.2,rely=0.5,anchor="center")

lobby()
janela.after(0, lambda: janela.state("zoomed"))
janela.mainloop()
