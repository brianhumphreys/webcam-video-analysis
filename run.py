from tkinter import *


class Application(Frame):
    def capture(self):
        print("turn camera on")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack()

        self.START = Button(self, width=30, height=2, bg='#111', fg='green')
        self.START["text"] = "START CAPTURE",
        self.START["command"] = self.capture

        self.START.pack(side=LEFT)  #{"side": "bottom"}


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
