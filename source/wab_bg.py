import tkinter as tk
import tkinter.font as tkFont
import time

def draw_bg():
    root = tk.Tk()
    root.configure(bg='black', cursor='none')
    root.attributes('-fullscreen', True)
    
    for i in range(3,0,-1):
        win = tk.Label(root, text=str(i), background="#000", foreground="#fff",
            font=tkFont.Font(family='Helvetica', size=72, weight='bold'))
        win.pack(ipadx=10, ipady=300)
        root.update()
        time.sleep(1)
        win.destroy()
        root.update()
        time.sleep(0.5)

    root.update()
