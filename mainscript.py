import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title ('Hello world')

        tk.Label(self, text = 'This is your first GUI. (high five)').pack()
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()
