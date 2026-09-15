import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "12345":
        messagebox.showinfo("Login Berhasil", "Selamat datang!")
    else:
        messagebox.showerror("Login Gagal", "Username atau password salah.")

root = tk.Tk()
root.title("Login")
root.geometry("400x450")
root.resizable(False, False)
root.configure(bg="#FCE4EC")

# Judul
tk.Label(
    root,
    text="Welcome ♡",
    font=("Arial", 26, "bold"),
    bg="#FCE4EC",
    fg="#C2185B"
).pack(pady=(60, 10))

tk.Label(
    root,
    text="Silakan login untuk melanjutkan",
    font=("Arial", 10),
    bg="#FCE4EC",
    fg="#777777"
).pack(pady=(0, 35))

# Username
tk.Label(
    root,
    text="Username",
    font=("Arial", 11, "bold"),
    bg="#FCE4EC",
    fg="#AD1457"
).pack(anchor="w", padx=55)

username_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=30,
    relief="flat",
    bg="white"
)
username_entry.pack(pady=(8, 20), ipady=8)

# Password
tk.Label(
    root,
    text="Password",
    font=("Arial", 11, "bold"),
    bg="#FCE4EC",
    fg="#AD1457"
).pack(anchor="w", padx=55)

password_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=30,
    show="*",
    relief="flat",
    bg="white"
)
password_entry.pack(pady=(8, 30), ipady=8)

# Tombol Login
tk.Button(
    root,
    text="LOGIN",
    command=login,
    font=("Arial", 11, "bold"),
    bg="#EC407A",
    fg="white",
    activebackground="#D81B60",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    width=25
).pack(ipady=8)

tk.Label(
    root,
    text="♡ Have a nice day ♡",
    font=("Arial", 9),
    bg="#FCE4EC",
    fg="#999999"
).pack(pady=35)

root.mainloop()
