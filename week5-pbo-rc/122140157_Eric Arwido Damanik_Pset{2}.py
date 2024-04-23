import tkinter
from tkinter import messagebox

class LoginApp:

    registered_accounts_file = "registrasi_akun.txt"

    def __init__(self, window):
        self.window = window
        self.window.title("Login")
        self.window.minsize(250, 140)

        self.usernameLabel = tkinter.Label(window, text="Username : ")
        self.usernameLabel.grid(row=0, column=0, sticky="ew")

        self.usernameEntry = tkinter.Entry(window)
        self.usernameEntry.grid(row=0, column=1, sticky="ew")

        self.passwordLabel = tkinter.Label(window, text="Password : ")
        self.passwordLabel.grid(row=1, column=0, sticky="ew")

        self.passwordEntry = tkinter.Entry(window, show="*")
        self.passwordEntry.grid(row=1, column=1, sticky="ew")

        self.loginButton = tkinter.Button(window, text="Login", command=self.checkLogin)
        self.loginButton.grid(row=2, column=1, sticky="ew", pady=5)

        self.registButton = tkinter.Button(window, text="Register", command=self.openWinregis)
        self.registButton.grid(row=3, column=1, sticky="ew", pady=5)

    def showSuccessDialog(self, username):
        messagebox.showinfo("Berhasil Login", f"Halo! Selamat Datang, {username}!")

    def showErrorDialog(self):
        messagebox.showerror("Gagal Login", "Username/Password Salah")

    def checkLogin(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        if self.authenticate(username, password):
            self.showSuccessDialog(username)
        else:
            self.showErrorDialog()

    def openWinregis(self):
        register_window = RegistApp(self.window)

    def authenticate(self, username, password):
        with open(LoginApp.registered_accounts_file, "r") as file:
            for line in file:
                if ":" in line:
                    stored_username, stored_password = line.strip().split(":")
                    if username == stored_username and password == stored_password:
                        return True
        return False

class RegistApp:

    registered_accounts_file = "registrasi_akun.txt"

    def __init__(self, window):

        self.WinregWindow = tkinter.Toplevel(window)
        self.WinregWindow.title("Register")
        self.WinregWindow.minsize(250, 140)

        self.usernameLabel = tkinter.Label(self.WinregWindow, text="Username : ")
        self.usernameLabel.grid(row=0, column=0, sticky="ew")

        self.usernameEntry = tkinter.Entry(self.WinregWindow)
        self.usernameEntry.grid(row=0, column=1, sticky="ew")

        self.passwordLabel = tkinter.Label(self.WinregWindow, text="Password : ")
        self.passwordLabel.grid(row=1, column=0, sticky="ew")

        self.passwordEntry = tkinter.Entry(self.WinregWindow, show="*")
        self.passwordEntry.grid(row=1, column=1, sticky="ew")

        self.registerButton = tkinter.Button(self.WinregWindow, text="Register", command=self.registerAccount)
        self.registerButton.grid(row=2, column=1, sticky="ew", pady=5)

    def registerAccount(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        with open(RegistApp.registered_accounts_file, "a") as file:
            file.write(f"{username}:{password}\n")
        messagebox.showinfo("Berhasil Registrasi", "Akun sudah teregistrasi!")
        self.WinregWindow.destroy()

# Mengecek apakah file akun terdaftar sudah ada, jika tidak maka akan dibuat.
try:
    with open(LoginApp.registered_accounts_file, "x"):
        pass
except FileExistsError:
    pass

window = tkinter.Tk()
app = LoginApp(window)
window.mainloop()
