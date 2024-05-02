import tkinter as tk

import customtkinter as ctk

from user_settings.settings_handler import settings_handler


class Fonts:
    def __init__(self):
        # print(settings_handler.font_family)
        # print(settings_handler.font_size)
        self.font_base = ctk.CTkFont(family=settings_handler.font_family, size=int(settings_handler.font_size))

        self.font_bold = ctk.CTkFont(family=settings_handler.font_family, size=int(settings_handler.font_size),
                                     weight="bold")

    # def update_font(self, widget: tk.Widget, font:ctk.CTkFont):
    #     widget.configure(font=font)
