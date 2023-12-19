from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
encoding = "utf-8"


class SecretNotesApp:
    def __init__(self, root):
        self.root = root
        root.geometry("400x750")
        root.title("Secret Notes")
        root.config(padx=15, pady=15)

        self.create_widgets()

    def create_widgets(self):
        self.create_image_widget()
        self.create_input_widgets()

    def create_image_widget(self):
        canvas = Canvas(self.root, width=200, height=200)
        canvas.pack()
        img = Image.open('topsecret.png')
        resize_img = img.resize((150, 150))
        self.image = ImageTk.PhotoImage(resize_img)  # Save reference to avoid garbage collection
        canvas.create_image(110, 90, anchor="center", image=self.image)

    def create_input_widgets(self):
        title_label = Label(text="Enter Your Title", font=("Arial", 10, "bold"))
        title_label.pack()

        self.title_entry = Entry(width=50)
        self.title_entry.pack()
        self.title_entry.focus()

        secret_label = Label(text="Enter Your Secret", font=("Arial", 10, "bold"))
        secret_label.pack()

        self.secret_text = Text(height=20, width=40)
        self.secret_text.pack()

        master_label = Label(text="Enter Your Master Key", font=("Arial", 10, "bold"))
        master_label.pack()

        self.master_entry = Entry(width=50)
        self.master_entry.pack()

        save_btn = Button(text="Save & Encrypt", command=self.crypt_btn_func)
        save_btn.config(padx=10, pady=10)
        save_btn.pack()

        dec_btn = Button(text="Decrypt", command=self.decrypt_btn_func)
        dec_btn.config(padx=5, pady=5)
        dec_btn.pack()

    def crypt_text_func(self, key, text_widget):
        text = text_widget.get("1.0", END)
        encoded = ''.join(chr((ord(i) + key) % 0x110000) for i in text)

        with open("secretnotes.txt", mode="a", encoding="utf-8") as secret_notes:
            secret_notes.write(f"\n{self.title_entry.get()}\n{encoded}\n")

        text_widget.delete("1.0", END)
        text_widget.insert(1.0, encoded)

    def decrypt_text_func(self, key, text_widget):
        text = text_widget.get("1.0", END)
        decoded = ''.join(chr((ord(i) - key) % 0x110000) for i in text)
        text_widget.delete("1.0", END)
        text_widget.insert(1.0, decoded)

    def get_valid_integer(self, input_str):
        try:
            return int(input_str)
        except ValueError:
            return None

    def crypt_btn_func(self):
        key = self.get_valid_integer(self.master_entry.get())
        if key is not None:
            self.crypt_text_func(key, self.secret_text)
        else:
            self.error_msg()

    def decrypt_btn_func(self):
        key = self.get_valid_integer(self.master_entry.get())
        if key is not None:
            self.decrypt_text_func(key, self.secret_text)
        else:
            self.error_msg()

    def error_msg(self):
        msg = 'Enter All Items'
        messagebox.showwarning(title='Warning', message=msg)


if __name__ == "__main__":
    ws = Tk()
    app = SecretNotesApp(ws)
    ws.mainloop()