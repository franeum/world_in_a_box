#!/usr/bin/env python3

import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()

    # place a label on the root window
    message = tk.Label(root, text="Hello, World!")
    message.pack()

    # keep the window displaying
    root.mainloop()
