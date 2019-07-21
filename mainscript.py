import tkinter as tk
import subprocess



class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title ('Hello world')

        self.master.resizable(False, False)
        tk.Button(self, text = 'OK', default = 'active', command = self.click_ok).pack(side = 'right')
        #self.master.tk_setPallete(background = '#ececec')

        #x = (self.master.winfo_screenwidth()-self.master.winfo_reqwidth())/2
        #y = (self.master.winfo_screenheight()-self.master.winfo_reqheight())/3
        #self.master.winfo.geometry('+{}+{}'.format(x,y))
        #self.master.config(menu=tk.Menu(self.master))

        tk.Label(self, text = 'This is your first GUI. (high five)').pack()
if __name__ == '__main__':
#    subprocess.cell(['/user/bin/osascript', '-e', 'tell app "Finder" to set fromntmost of subprocess 'Python' to true'])
    root = tk.Tk()
    app = App(root)
    app.mainloop()
