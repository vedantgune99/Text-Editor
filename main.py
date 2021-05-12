from tkinter import *
from tkinter import Menu
from tkinter import colorchooser
from tkinter.messagebox import askokcancel
from tkinter.filedialog import askopenfilename, asksaveasfilename
from pathlib import Path


# All Functions Here...


def do_nothing():
    pass


def new():
    # New File Function
    global file
    file = None
    root.title("Untitled - Editor")
    textarea.delete(1.0, END)


def new_Shortcut(event):
    # New File Function
    global file
    file = None
    root.title("Untitled - Editor")
    textarea.delete(1.0, END)


def openfile():
    # Open File Function
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = None

    else:
        textarea.delete(1.0, END)
        root.title(Path(file).name + "- Editor")
        with open(file, 'r') as f:
            textarea.insert(1.0, f.read())


def openfile_Shortcut(event):
    # Open File Function
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = None

    else:
        textarea.delete(1.0, END)
        root.title(Path(file).name + "- Editor")
        with open(file, 'r') as f:
            textarea.insert(1.0, f.read())


def savefile():
    # File Save Function
    global file
    if file == None:
        file = asksaveasfilename(defaultextension=".txt", initialfile="Untitled.txt",
                                 filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None

        else:
            with open(file, 'w') as f:
                f.write(textarea.get(1.0, END))
                root.title(Path(file).name + "- Editor")
    else:
        with open(file, 'w') as f:
            f.write(textarea.get(1.0, END))
            root.title(Path(file).name + "- Editor")


def savefile_Shortcut(event):
    # File Save Function
    global file
    if file == None:
        file = asksaveasfilename(defaultextension=".txt", initialfile="Untitled.txt",
                                 filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None

        else:
            with open(file, 'w') as f:
                f.write(textarea.get(1.0, END))
                root.title(Path(file).name + "- Editor")
    else:
        with open(file, 'w') as f:
            f.write(textarea.get(1.0, END))
            root.title(Path(file).name + "- Editor")

def engaged(event):
    # textarea active status change function
    sbar['text'] = "Status : Writing..."


def free(event):
    # textarea inactive status change function
    sbar['text'] = "Status : Ready..."


def fullscreen(event):
    root.attributes('-fullscreen', True)


def reset_win(event):
    root.attributes('-fullscreen', False)


def darkTheme():
    textarea['bg'] = 'black'
    textarea['fg'] = 'white'
    textarea['insertbackground'] = 'red'
    textarea['cursor'] = 'dotbox'
    sbar['bg'] = 'light gray'


def sunTheme():
    textarea['bg'] = 'wheat'
    textarea['fg'] = 'brown'
    textarea['insertbackground'] = 'black'
    textarea['cursor'] = 'pirate'
    font = "Helvetica"
    textarea['font'] = f'{font} {size} italic'
    sbar['bg'] = 'brown'
    sbar['fg'] = 'wheat'


def lightTheme():
    textarea['bg'] = 'light gray'
    textarea['fg'] = 'black'
    textarea['insertbackground'] = 'cyan'
    font = "Helvetica"
    textarea['font'] = f"{font} {size} bold"
    sbar['bg'] = "sky blue"
    sbar['fg'] = "white"


def default():
    textarea['bg'] = 'white'
    textarea['fg'] = 'black'
    font = "Helvetica"
    textarea['font'] = f'{font} {size}'
    textarea['insertbackground'] = 'black'
    textarea['cursor'] = 'arrow'
    root.config(bg='white')
    sbar['bg'] = 'light gray'


def cut():
    textarea.event_generate('<<Cut>>')
    sbar['text'] = 'Status : Cut Text Successfully!'


def copy():
    textarea.event_generate('<<Copy>>')
    sbar['text'] = 'Status : Copied Text Successfully!'


def paste():
    textarea.event_generate('<<Paste>>')
    sbar['text'] = 'Status : Pasted Text Successfully!'


def key_cut(event):
    sbar['text'] = 'Status : Cut Text Successfully!'
    textarea.event_generate('<<Cut>>')


def key_copy(event):
    sbar['text'] = 'Status : Copied Text Successfully!'
    textarea.event_generate('<<Copy>>')


def key_paste(event):
    sbar['text'] = 'Status : Pasted Text Successfully!'
    textarea.event_generate('<<Paste>>')


def font_color():
    textarea['fg'] = colorchooser.askcolor(title="Pick Font Color")[1]


def background():
    textarea['bg'] = colorchooser.askcolor(title="Pick Background Color")[1]


def cursor_color():
    textarea['insertbackground'] = colorchooser.askcolor(title="Pick Cursor Color")[1]


def sbar_color():
    sbar['bg'] = colorchooser.askcolor(title="Pick Status Bar Color")[1]


def window_color():
    color = colorchooser.askcolor(title="Pick Window Color")[1]
    root.config(bg=color)


def about():
    askokcancel("About Editor", "Editor Version: 1.0,\n"
                                "Origin: India,\n"
                                "Developer: Vedant Gune.")


def get_help():
    with open('README.md', 'r') as info:
        askokcancel("Information By Editor", info.read())


def increase_font():
    global size, font
    size += 2
    textarea['font'] = f"{font} {size}"


def decrease_font():
    global size, font
    size -= 2
    textarea['font'] = f"{font} {size}"


def font_inc(event):
    global size, font
    size += 2
    textarea['font'] = f"{font} {size}"


def font_dec(event):
    global size, font
    size -= 2
    textarea['font'] = f"{font} {size}"


def bold(event):
    textarea['font'] += " bold"


def italic(event):
    textarea['font'] += " italic"


def underline(event):
    textarea['font'] += " underline"


# Initialization and Customizations...
root = Tk()
size = 18
font = "Helvetica"
file = None
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
root.geometry(f"{width}x{height}")
root.title("Text Editor")

# Tool bar or Menubar...
menubar = Menu(root, bg="black")
filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label='New (Ctrl + N)', command=new)
filemenu.add_command(label='Open (Ctrl + O)', command=openfile)
filemenu.add_separator()
filemenu.add_command(label='Save (Ctrl + S )', command=savefile)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=quit)
menubar.add_cascade(label='File', menu=filemenu)

editmenu = Menu(menubar, tearoff=False)
editmenu.add_command(label='Cut (Ctrl + X)', command=cut)
editmenu.add_command(label='Copy (Ctrl + C)', command=copy)
editmenu.add_command(label='Paste (Ctrl + V)', command=paste)
editmenu.add_command(label='Increase Font Size ▲', command=increase_font)
editmenu.add_command(label='Decrease Font Size ▼', command=decrease_font)
menubar.add_cascade(label="Edit", menu=editmenu)

colormenu = Menu(menubar, tearoff=False)
colormenu.add_command(label='Sun Theme', command=sunTheme)
colormenu.add_command(label='Dark Theme', command=darkTheme)
colormenu.add_command(label='Light Theme', command=lightTheme)
colormenu.add_separator()
colormenu.add_command(label='Default Theme', command=default)
menubar.add_cascade(label="Themes", menu=colormenu)

custommenu = Menu(menubar, tearoff=False)
custommenu.add_command(label='background', command=background)
custommenu.add_command(label='font color', command=font_color)
custommenu.add_command(label='statusbar color', command=sbar_color)
custommenu.add_command(label='cursor color', command=cursor_color)
custommenu.add_command(label='window color', command=window_color)
menubar.add_cascade(label="Custom Colors", menu=custommenu)

helpmenu = Menu(menubar, tearoff=False)
helpmenu.add_command(label='About Editor', command=about)
helpmenu.add_command(label='Help', command=get_help)
menubar.add_cascade(label="More...", menu=helpmenu)

# Status Bar
sbar = Label(root, text="Status : Ready...", anchor=W, relief=SUNKEN)
sbar.pack(side=BOTTOM, fill=X)

# Textarea to write...
textarea = Text(root, font=f"{font} {size}")
textarea.pack(fill=BOTH, expand=True, padx=7, pady=7)

# Adding Vertical ScrollBar...
vscroll = Scrollbar(textarea)
vscroll.pack(fill=Y, side=RIGHT)
vscroll.config(command=textarea.yview)
textarea.config(yscrollcommand=vscroll.set)

# Key Bindings...
textarea.bind('<Control-x>', key_cut)
textarea.bind('<Control-c>', key_copy)
textarea.bind('<Control-v>', key_paste)
textarea.bind('<KeyPress>', engaged)
textarea.bind('<KeyRelease>', free)
textarea.bind('<Control-f>', fullscreen)
textarea.bind('<Control-z>', reset_win)
textarea.bind('<Up>', font_inc)
textarea.bind('<Down>', font_dec)
textarea.bind('<Control-b>', bold)
textarea.bind('<Control-i>', italic)
textarea.bind('<Control-u>', underline)
textarea.bind('<Control-o>', openfile_Shortcut)
textarea.bind('<Control-n>', new_Shortcut)
textarea.bind('<Control-s>', savefile_Shortcut)

# Root Configuration and Mainloop...
root.config(menu=menubar)
root.mainloop()
