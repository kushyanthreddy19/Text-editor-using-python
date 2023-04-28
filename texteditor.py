import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def _init_(self, master):
        self.master = master
        self.master.title("Text Editor")
        self.textarea = tk.Text(self.master, font=('Arial', 12))
        self.textarea.pack(fill='both', expand=True)

        menubar = tk.Menu(self.master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exit_app)
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cut", command=self.cut)
        editmenu.add_command(label="Copy", command=self.copy)
        editmenu.add_command(label="Paste", command=self.paste)
        menubar.add_cascade(label="Edit", menu=editmenu)

        self.master.config(menu=menubar)

    def new_file(self):
        self.textarea.delete('1.0', tk.END)

    def open_file(self):
        file = filedialog.askopenfile(defaultextension=".txt", filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
        if file is not None:
            self.textarea.delete('1.0', tk.END)
            contents = file.read()
            self.textarea.insert('1.0', contents)
            file.close()

    def save_file(self):
        file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
        if file is not None:
            file.write(self.textarea.get('1.0', tk.END))
            file.close()

    def exit_app(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.master.destroy()

    def cut(self):
        self.textarea.event_generate("<<Cut>>")

    def copy(self):
        self.textarea.event_generate("<<Copy>>")

    def paste(self):
        self.textarea.event_generate("<<Paste>>")

if _name_ == '_main_':
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()