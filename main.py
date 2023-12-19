from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os

ws = Tk()
ws.geometry("400x750")
ws.title("Secret Notes")
ws.config(padx=15, pady=15)

canvas = Canvas(ws, width=200, height=200)
canvas.pack()
img = Image.open('topsecret.png')
resize_img = img.resize((150, 150))
image = ImageTk.PhotoImage(resize_img)
canvas.create_image(110, 90, anchor="center", image=image)

title_label = Label(text="Enter Your Title", font=("Arial", 10, "bold"))
title_label.pack()

title_entry = Entry(width=50)
title_entry.pack()
title_entry.focus()

secret_label = Label(text="Enter Your Secret", font=("Arial", 10, "bold"))
secret_label.pack()

secret_text = Text(height=20, width=40)
secret_text.pack()

master_label = Label(text="Enter Your Master Key", font=("Arial", 10, "bold"))
master_label.pack()

master_entry = Entry(width=50)
master_entry.pack()

secret_input = secret_text.get("1.0", END)


def crypt_text_func(keyw, text):

    encoded = ''.join(chr(ord(i) + keyw) for i in text)

    with open("secretnotes.txt", mode="a") as secret_notes:
        secret_notes.write(f"\nencoding='utf-8'\n{title_entry.get()}\n{encoded}\n")

    secret_text.insert(1.0, encoded)


def decrypt_text_func(keyw, text):

    decoded = ''.join(chr(ord(i) - keyw) for i in text)

    secret_text.insert(1.0, decoded)


def crypt_btn_func():
    key = master_entry.get()
    try:
        return crypt_text_func(int(key), secret_input)
    except ValueError:
        return error_msg()


def decrypt_btn_func():
    key = master_entry.get()
    try:
        return decrypt_text_func(int(key), secret_input)
    except ValueError:
        return error_msg()


def error_msg():
    msg = 'Enter All Items'
    messagebox.showwarning(title='Warning', message=msg)


save_btn = Button(text="Save & Encrypt", command=crypt_btn_func)
save_btn.config(padx=10, pady=10)
save_btn.pack()

dec_btn = Button(text="Decrypt", command=decrypt_btn_func)
save_btn.config(padx=5, pady=5)
dec_btn.pack()


ws.mainloop()
