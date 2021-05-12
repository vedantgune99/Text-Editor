from tkinter import *


def show_bindings():
    screen = Tk()
    screen.geometry('300x400')
    screen.title("Editor KeyBindings (Shortcuts)")
    Label(screen, text=" - Keyboard Shortcuts - ", fg="sky blue").pack(padx=30, pady=10)

    # Key Bindings Labels...
    Label(screen, text='CUT   :  Control-x', font="Helvetica 8").pack(padx=5)
    Label(screen, text='COPY  :  Control-c', font="Helvetica 8").pack(padx=5)
    Label(screen, text='PASTE :  Control-v', font="Helvetica 8").pack(padx=5)

    Label(screen, text='FULLSCREEN   : Control-f', font="Helvetica 8").pack(padx=5)
    Label(screen, text='NORMALSCREEN : Control-z', font="Helvetica 8").pack(padx=5)

    Label(screen, text='INCREASE FONT SIZE : Up', font="Helvetica 8").pack(padx=5)
    Label(screen, text='DECREASE FONT SIZE : Down', font="Helvetica 8").pack(padx=5)

    Label(screen, text='BOLD FONT       : Control-b', font="Helvetica 8").pack(padx=5)
    Label(screen, text='ITALIC FONT     : Control-i', font="Helvetica 8").pack(padx=5)
    Label(screen, text='UNDERLINED FONT : Control-u', font="Helvetica 8").pack(padx=5)

    Label(screen, text='OPEN FILE : Control-o', font="Helvetica 8").pack(padx=5)
    Label(screen, text='NEW FILE  : Control-n', font="Helvetica 8").pack(padx=5)
    Label(screen, text='SAVE FILE : Control-s', font="Helvetica 8").pack(padx=5)
    screen.mainloop()

