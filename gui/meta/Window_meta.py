import _tkinter

from constants.constants import logo_icon_path_ico
from gui.meta.Fonts import Fonts
from user_settings.settings_handler import settings_handler
import customtkinter as ctk

from ctypes import windll, c_int, byref, sizeof
class Window(Fonts):
    def __init__(self, master, title_text):
        super().__init__()
        self.settings = settings_handler
        if self.settings.settings_json_exist():
            self.settings.set_settings(self.settings.read_json())

        self.master: ctk.CTk = master
        self.master.iconbitmap(logo_icon_path_ico)
        self.master.title(title_text)


    def update_font(self, widget, font):
        all_widgets = self.all_children(widget)
        for widget in all_widgets:
            # widget.configure(font=self.font_bold)
            try:
                widget.configure(font=font)
            except (ValueError, _tkinter.TclError) as e:
                continue

    def all_children(self, widget, finList=[]):
        _list = widget.winfo_children()
        for item in _list:
            finList.append(item)
            self.all_children(item, finList)
        return finList