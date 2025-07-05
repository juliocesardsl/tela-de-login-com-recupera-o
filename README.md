# 💻 Sistema de Login com CustomTkinter + SQLite + SMTP

Este projeto é uma interface de autenticação desenvolvida em Python usando:

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) para interface gráfica moderna;
- SQLite como banco de dados local;
- SMTP para envio de e-mails de recuperação de senha.

---

## 🚀 Funcionalidades

- [x] Tela de login estilizada
- [x] Validação de usuário e senha via SQLite
- [x] Recuperação de senha por e-mail
- [x] Encerramento seguro do aplicativo

---

## 🧠 Requisitos

- Python 3.8+
- Pacotes:
  ```bash
  pip install customtkinter Pillow

  🛠️ Como usar
Clone o repositório ou copie os arquivos.

Crie o banco banco.db com a tabela usuarios:
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
);

Adicione manualmente alguns usuários para teste:
INSERT INTO usuarios (username, password, email)
VALUES ('admin', '1234', 'seuemail@gmail.com');

No código, preencha os campos de envio de e-mail:
remetente = "seuemail@gmail.com"
senha_email = "senha_app_do_gmail"

*Lembre-se: use uma senha de aplicativo criada nas configurações de segurança do Gmail.*

![image](https://github.com/user-attachments/assets/ee81dcab-776a-4f5a-a5f1-84a80f462ef5)
![image](https://github.com/user-attachments/assets/6deb4a1a-5061-4e5a-8e50-df1e06e0ee43)
![image](https://github.com/user-attachments/assets/f3f366db-6a08-4dc7-a741-f7e87c55385e)
![image](https://github.com/user-attachments/assets/33d6ab34-d596-4cdd-81d1-dc9fcb49e917)



