from tkinter import *
from PIL import ImageTk, Image

ws = Tk()
ws.geometry("400x750")
ws.title("Secret Notes")

canvas = Canvas(ws, width=200, height=200)
canvas.pack()
img = Image.open('topsecret.png')
resize_img = img.resize((150, 150))
image = ImageTk.PhotoImage(resize_img)
canvas.create_image(110, 90, anchor="center", image=image)

title_label = Label(text="Enter Your Title")
title_label.pack()

title_entry = Entry(width=50)
title_entry.pack()
title_entry.focus()

secret_label = Label(text="Enter Your Secret")
secret_label.pack()

secret_text = Text(height=20, width=40)
secret_text.pack()

master_label = Label(text="Enter Your Master Key")
master_label.pack()

master_entry = Entry(width=50)
master_entry.pack()

save_btn = Button(text="Save & Encrypt")
save_btn.pack()

dec_btn = Button(text="Decrypt")
dec_btn.pack()


def crypt_text_func(text, keyw):
    crypt_text = ''.join(chr(ord(i) + keyw) for i in text)
    return crypt_text


secret_input = secret_text.get(1.0, END)
key = master_entry.get()
crypt_text = crypt_text_func(secret_input, key)


def decrypt_text_func(text, keyw):
    decrypt_text = ''.join(chr(ord(i) - keyw) for i in text)
    return decrypt_text


secret_input2 = secret_text.get(1.0, END)
decrypt_text = decrypt_text_func(secret_input2, key)

ws.mainloop()
