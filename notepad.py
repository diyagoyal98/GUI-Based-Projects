from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file=None
    TextArea.delete(1.0,END) #1.0->Fist line and 0th character

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))      
            f.close()
            root.title(os.path.basename(file)+" - Notepad")
            print("File Sved")
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()        

def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad","Notepad by Diya")


def createWidgets():
    # Add text area
    global TextArea
    TextArea=Text(root,font="lucida 13")
    TextArea.pack(expand=True,fill=BOTH)
    #Let's create a menu bar
    MenuBar=Menu(root)
    root.config(menu=MenuBar)
    FileMenu=Menu(MenuBar,tearoff=0)
    #To open new file
    FileMenu.add_command(label="New",command=newFile)

    #To open already existing file 
    FileMenu.add_command(label="Open",command=openFile)

    #To save the current file
    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    MenuBar.add_cascade(label="File",menu=FileMenu)

    #Edit menu start
    EditMenu=Menu(MenuBar,tearoff=0)
    #To give the feature of cut,copy,paste
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)

    MenuBar.add_cascade(label="Edit",menu=EditMenu)

    #Help menue
    HelpMenu=Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about)

    MenuBar.add_cascade(label="Help",menu=HelpMenu)

    root.config(menu=MenuBar)


    #Adding scroll bar
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    



root=Tk()
root.geometry("644x700")
root.title("Untitled - NOTEPAD")
file=None # Till nowno file opened (but it will point to that file which we will open)

createWidgets()
root.mainloop()

    
