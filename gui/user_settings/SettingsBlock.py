from gui.meta.Fonts import Fonts
import customtkinter as ctk
import tkinter as tk
class SettingsBlock(Fonts):
    def __init__(self, master):
        super().__init__()

        # self.main_label_text = main_label_text
        self.master = master
        self.settings_frame = ctk.CTkFrame(self.master)
        self.settings_frame.pack(fill="x")

    def add_settings_block(self, label_text, callback, callback_command=None, *args):
        block = ctk.CTkFrame(master=self.settings_frame)
        block.pack(fill="x")

        label = ctk.CTkLabel(master=block, text=label_text, font=self.font_base,

                             # bg_color="red"

                             )
        label.pack(side="left",
                   fill="x",
                   # expand=1,

                   )
        widget = callback(block, *args)
        if callback_command:
            widget.configure(command=callback_command)
        widget.pack(side="right", fill="x")
        return widget

    def add_block_label(self, label_text):
        block = ctk.CTkFrame(master=self.settings_frame)
        block.pack(fill="x")
        label = ctk.CTkLabel(master=block, text=label_text, font=self.font_bold)
        label.pack(fill="x", side="left")


