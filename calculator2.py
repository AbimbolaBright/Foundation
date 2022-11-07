import tkinter as tk

class App(tk.Frame):
    
    DEFAULT_PADY = 2
    
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.config()
        self.grid()
        self.create_widgets()
        
    def config(self):
        self.master.title("x*y")
        
    def create_widgets(self):
        top = self.winfo_toplevel() 
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.result_label = tk.Label(self, text="Input a number: ")
        self.result_label.grid(row=0, column=0, pady=App.DEFAULT_PADY, sticky=tk.W + tk.E + tk.N + tk.S)
        self.number_entry = tk.Entry(self, justify=tk.RIGHT)
        self.number_entry.grid(row=1, column=0, pady=App.DEFAULT_PADY, sticky=tk.W + tk.E + tk.N + tk.S)
        self.show_button = tk.Button(self, text="ok", width=4, command=self.update_result)
        self.show_button.grid(row=2, column=0, pady=App.DEFAULT_PADY, sticky=tk.SE)
        
    def update_result(self):
        self.result_label["text"] = '\n'.join([
            "{x}*{y} = {result}".format(x = int(self.number_entry.get()), 
                                            y = n, result = int(self.number_entry.get())*n) 
                                                for n in range(11)])

if __name__ == '__main__':
    App().mainloop()
 