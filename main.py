import customtkinter
from PIL import Image, ImageTk
import os
import sys
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import messagebox


def verificar_login(username, password):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username=? AND password=?", (username, password))
    resultado = cursor.fetchone()
    conexao.close()
    return resultado is not None

def tentar_login(root, janela_login, usuario, senha):
    if verificar_login(usuario, senha):
        messagebox.showinfo("Login", "Login bem-sucedido!")
        janela_login.destroy()
        JanelaMain(root)
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos.")
        # Pode mostrar uma CTkMessageBox ou CTkLabel com erro


def recuperar_senha(username):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT email FROM usuarios WHERE username=?", (username,))
    resultado = cursor.fetchone()
    conexao.close()

    if resultado is None:
        messagebox.showerror("Erro", "Usuário não encontrado.")
        return
    
    email_destino = resultado[0]

    remetente = "" # e-mail remetente
    senha_email = ""  # senhaapp do seu email

    # Buscar a senha do usuário
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT password FROM usuarios WHERE username=?", (username,))
    resultado_senha = cursor.fetchone()
    conexao.close()

    if resultado_senha is None:
        messagebox.showerror("Erro", "Senha do usuário não encontrada.")
        return

    senha_usuario = resultado_senha[0]

    assunto = "Recuperação de Senha"
    corpo = f"Olá {username},\n\nSua senha é: {senha_usuario}\n\nAtenciosamente,\nEquipe de Suporte"

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = email_destino
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo, 'plain'))

    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remetente, senha_email)
        servidor.sendmail(remetente, email_destino, msg.as_string())
        servidor.quit()
        messagebox.showinfo("Sucesso", "Senha enviada para o e-mail.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao enviar email: {e}")


# TELA DE LOGIN
def login_page(root):
    Janelalogin = customtkinter.CTkToplevel()
    Janelalogin.title("Login")
    Janelalogin.geometry("300x300")

    label = customtkinter.CTkLabel(Janelalogin, text="Welcome to the Login Page")
    label.pack(pady=20)

    login_entry = customtkinter.CTkEntry(Janelalogin, placeholder_text="Username")
    login_entry.pack(pady=10)
    password_entry = customtkinter.CTkEntry(Janelalogin, placeholder_text="Password", show="*")
    password_entry.pack(pady=10)

    login_btn = customtkinter.CTkButton(
        Janelalogin,
        text="Login",
        command=lambda: tentar_login(root, Janelalogin, login_entry.get(), password_entry.get())
    )
    login_btn.pack(pady=10)

    label_esqueceu_senha = customtkinter.CTkLabel(Janelalogin, text="forgot password?")
    label_esqueceu_senha.pack(pady=10)
    esqueceu_btn = customtkinter.CTkButton(Janelalogin, text="recover password", command=lambda: recuperar_senha(login_entry.get()))
    esqueceu_btn.pack(pady=2)

    # ENCERRA O PROGRAMA AO FECHAR A JANELA DE LOGIN
    def fechar_janela():
        Janelalogin.destroy()
        sys.exit()
    Janelalogin.protocol("WM_DELETE_WINDOW", fechar_janela)

def fechar_janelalogin(root, Janelalogin):
    Janelalogin.destroy()
    JanelaMain(root)


def JanelaMain(root):
    JanelaPrincipal = customtkinter.CTkToplevel()
    JanelaPrincipal.title("Main Window")
    JanelaPrincipal.geometry("700x500")

    label = customtkinter.CTkLabel(JanelaPrincipal, text="Welcome to the Main Window")
    label.pack(pady=20)

    def fechar_janela():
        JanelaPrincipal.destroy()
        sys.exit()
    JanelaPrincipal.protocol("WM_DELETE_WINDOW", fechar_janela)



root = customtkinter.CTk()
root.withdraw()  # Oculta a janela principal

login_page(root)

# Mantém o app rodando
root.mainloop()