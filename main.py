from tkinter import *
from tkinter import ttk

import pyjokes

def generate_joke(*args):
    gen_joke = pyjokes.get_joke()
    joke.set(gen_joke)

root = Tk()
root.title("Joke Generator")

mainframe = ttk.Frame(root, padding="10 10 175 15")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

joke = StringVar()
ttk.Label(mainframe, wraplength=400, textvariable=joke).grid(column=0, row=0, columnspan=3, sticky=(W, E), pady=5)
ttk.Button(mainframe, text="Generate Joke", command=generate_joke).grid(column=0, row=1, columnspan=2, sticky=W)

root.bind("<Return>", generate_joke)
root.mainloop()