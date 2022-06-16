#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from pathlib import Path
from moviepy.editor import VideoFileClip


class ChosenVideo:
    def __init__(self, path=None, lang=None):
        self._path = path
        self._lang = lang
        self._duration = self._get_duration(path)

    def _get_duration(self, path):
        clip = VideoFileClip(path)
        return clip.duration

    def dump_info(self):
        pass


"""
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x250')
        self.title('Menubutton Demo')

        # Menubutton variable
        self.selected_lang = tk.StringVar()
        self.selected_lang.trace("w", self.menu_item_selected)

        # create the menu button
        self.create_menu_button()
        self.create_menu_button()

    def menu_item_selected(self, *args):
        
        # self.config(bg=self.selected_lang.get())
        print(f"SELECTED {self.selected_lang.get()}")

    def create_menu_button(self):
        
        # menu variable
        langs = ('Italian', 'English')

        # create the Menubutton
        menu_button = ttk.Menubutton(
            self,
            text='Select a lang')

        # create a new menu instance
        menu = tk.Menu(menu_button, tearoff=0)

        for lang in langs:
            menu.add_radiobutton(
                label=lang,
                value=lang,
                variable=self.selected_lang)

        # associate menu with the Menubutton
        menu_button["menu"] = menu

        menu_button.pack(expand=True)
"""


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('640x480')
        self.title('App Configurator')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        PUSH1 = tk.Label(
            self,
            text="PUSH 1",
            bg="green",
            fg="white"
        )

        """
        PUSH1.pack(
            ipadx=10,
            ipady=10,
            fill='both',
            expand=True,
            side='left'
        )"""

        PUSH1.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        # box 2
        PUSH2 = tk.Label(
            self,
            text="PUSH 2",
            bg="red",
            fg="white"
        )

        """
        PUSH2.pack(
            ipadx=10,
            ipady=10,
            fill='both',
            expand=True,
            side='right'
        )"""

        PUSH2.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        self.langs = ('Italian', 'English')
        self.lang1_var = tk.StringVar(self)
        self.lang2_var = tk.StringVar(self)

        self.create_lang_menu(PUSH1, self.lang1_var, 0)
        self.create_lang_menu(PUSH2, self.lang2_var, 1)

    def create_lang_menu(self, container, var, col):
        # padding for widgets using the grid layout
        paddings = {'padx': 5, 'pady': 5}
        # label
        label = ttk.Label(
            container,  text='Select video language:')
        label.grid(column=0, row=0, sticky=tk.W, **paddings)

        # option menu
        option_menu = ttk.OptionMenu(
            self,
            var,
            self.langs[0],
            *self.langs,
            command=self.option_changed)

        option_menu.grid(column=1, row=col, sticky=tk.W, **paddings)

        # output label
        self.output_label = ttk.Label(self, foreground='red')
        self.output_label.grid(column=0, row=1, sticky=tk.W, **paddings)

    def option_changed(self, *args):
        self.output_label['text'] = f'You selected'


if __name__ == "__main__":
    app = App()

    #root.attributes('-fullscreen', False)
    app.mainloop()
