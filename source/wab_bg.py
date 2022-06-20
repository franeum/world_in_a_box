"""
background manager
"""

import tkinter as tk
import tkinter.font as tkFont
import time


def draw_bg():
    """
    draw background with countdown
    """
    root = tk.Tk()
    root.configure(bg='black', cursor='none')
    root.attributes('-fullscreen', True)

    win = tk.Label(root, text="", background="#000", foreground="#fff",
                   font=tkFont.Font(family='Helvetica', size=72, weight='bold'))

    for i in range(3, 0, -1):
        win['text'] = str(i)
        win.pack(ipadx=10, ipady=300)
        root.update()
        time.sleep(0.75)

    win.destroy()
    root.update()
