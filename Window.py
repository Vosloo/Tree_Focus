from tkinter import *
from tkinter import messagebox

class App(Frame):
    def __init__(self, root, window_name, size='1024x768'):
        super().__init__(root)

        self.root = root
        self.root.title(window_name)

        self._center_window(size)
        self._create_menu()

        self.quit = Button(self.root, text='Quit!', command=self.root.destroy, font=('Arial', 16))
        self.quit.pack(side='top')

        self.root.bind('<Leave>', self.popup_warning)
        self.root.bind('<Key-Escape>', self.quit_app)
        
    def quit_app(self, event):
        self.root.destroy()

    def popup_warning(self, event):
        messagebox.showwarning('Warning', 'App left!')

    def hello(self):
        print('yo yo')

    def _center_window(self, size):
        screen_height = self.root.winfo_screenheight()
        screen_width = self.root.winfo_screenwidth()
        window_width, window_height = [int(x) for x in size.split('x')]
        
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        geometry = str(window_width) + 'x' + str(window_height) + '+' + str(x) + '+' + str(y)
        self.root.geometry(geometry)

    def _create_menu(self):
        self.menubar = Menu(self.root)

        # create a pulldown menu, and add it to the menu bar
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.hello)
        self.filemenu.add_command(label="Save", command=self.hello)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        # create more pulldown menus
        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Cut", command=self.hello)
        self.editmenu.add_command(label="Copy", command=self.hello)
        self.editmenu.add_command(label="Paste", command=self.hello)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.hello)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        # display the menu
        self.root.config(menu=self.menubar)    


root = Tk()
app = App(root=root, window_name="Focus tree")
app.mainloop()