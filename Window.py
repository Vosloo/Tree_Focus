from tkinter import *

class App():
    def __init__(self, window_name, size='1024x768'):
        self.window = Tk()
        self.window.title(window_name)
        self.window.geometry(size)

        self.label = Label(self.window, text="Hello there", font=('Ariel', 14))
        self.label.grid(row=0, column=0)

        self.button = Button(self.window, text="Click me!", command=self.clicked_button)
        self.button.grid(row=0, column=1)

        self.quit = Button(self.window, text="Quit", command=self.window.destroy)
        self.quit.grid(row=1, column=1)
    
    def clicked_button(self):
        self.label.configure(text='Button clicked!')
    
    def run(self):
        self.window.mainloop()

app = App("Focus tree")
app.run()