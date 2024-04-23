import tkinter
from tkinter import messagebox

class Login :
    USERNAME = "admin"
    PASSWORD = "12345"

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
        self.loginButton.grid(row=2, column=1, sticky="ew", pady=10)

    def showSuccessDialog(self):
        messagebox.showinfo("Berhasil Login", f"Halo! Selamat Datang, {self.USERNAME}!")

    def showErrorDialog(self):
        messagebox.showerror("Gagal Login", "Username/Password Salah")

        # Untuk memanggil ulang main ketika gagal login
        self.window.mainloop()

    def checkLogin(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        if username == self.USERNAME and password == self.PASSWORD:
            self.showSuccessDialog()
        else:
            self.showErrorDialog()

window = tkinter.Tk()
app = Login(window)
window.mainloop()
