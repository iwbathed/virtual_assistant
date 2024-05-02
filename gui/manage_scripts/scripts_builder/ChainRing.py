import os

from gui.meta.Fonts import Fonts
import customtkinter as ctk
import tkinter as tk
from PIL import Image

from project_settings import base_dir
from user_settings.settings_handler import settings_handler

# current_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# icons_path = os.path.join(current_dir_path, "..\\icons")
# base_dir

icons_path = os.path.join(base_dir, "gui", "icons")

# print(current_dir_path)
# print(base_dir)
# print(icons_path)
class ChainRing(Fonts):
    def __init__(self, master):
        super().__init__()
        self.rings = []
        self.master = master
        # self.ring = ctk.CTkFrame(self.master)
        # self.ring.pack(fill="x", padx=5, pady=5)
        self.font_size = settings_handler.font_size

    # def get_ring(self):
    #     return self.ring

    def add_command(self, widget_to_add: tk.Widget, ring:ctk.CTkFrame):
        widget_to_add.pack(side="left", anchor="w", expand=1, fill="both")
        # command_frame.pack(side="left", anchor="n")
        arrows_size = self.font_size/4
        close_size = self.font_size
        buttons_frame = ctk.CTkFrame(master=ring)
        buttons_frame.pack(side="right", anchor="e")


        arrows_frame = ctk.CTkFrame(master=buttons_frame)
        arrows_frame.pack(side="left")
        # foto = tk.PhotoImage(master=arrows_frame, file=os.path.join(icons_path, r"arrow_up.png"))
        arrow_up_icon = ctk.CTkImage(light_image=Image.open(os.path.join(icons_path, r"arrow_up.png")),
                                          dark_image=Image.open(os.path.join(icons_path, r"arrow_up.png")),
                                          size=(close_size,
                                                close_size))
        button_move_up = ctk.CTkButton(master=arrows_frame,
                                       image=arrow_up_icon,
                                       # image=foto,

                                       text="",
                                       width=close_size, height=arrows_size,
                                       command=lambda: self.move_up(ring))
        button_move_up.pack(side="top")


        arrow_up_icon = ctk.CTkImage(light_image=Image.open(os.path.join(icons_path, "arrow_down.png")),
                                          dark_image=Image.open(os.path.join(icons_path, "arrow_down.png")),
                                          size=(close_size,
                                                close_size))
        button_move_down = ctk.CTkButton(master=arrows_frame, image=arrow_up_icon, text="",
                                         width=close_size, height=arrows_size,
                                         command=lambda: self.move_down(ring))
        button_move_down.pack(side="bottom")

        arrow_up_icon = ctk.CTkImage(light_image=Image.open(os.path.join(icons_path, "close.png")),
                                          dark_image=Image.open(os.path.join(icons_path, "close.png")),
                                          size=(close_size,
                                                close_size))
        button_delete = ctk.CTkButton(master=buttons_frame, image=arrow_up_icon, text="",
                                      width=close_size, height=close_size,
                                      command= lambda: self.delete_ring(ring))
        button_delete.pack(side="right", fill="y")


    def add_ring(self, callback, *args):
        ring = ctk.CTkFrame(self.master)
        ring.pack(fill="x", padx=5, pady=5)
        widget = callback(ring, *args)
        self.add_command(widget, ring)
        self.rings.append(ring)

    def delete_ring(self, ring: ctk.CTkFrame):
        ring.pack_forget()
        self.rings.remove(ring)


    def move_up(self, ring):
        pos = self.rings.index(ring)
        if pos != 0:
            temp = self.rings[pos - 1]
            self.rings[pos] = temp
            self.rings[pos-1] = ring
            self.rebuild_chain()

    def move_down(self, ring):
        pos = self.rings.index(ring)
        if pos != len(self.rings) - 1:
            temp = self.rings[pos + 1]
            self.rings[pos] = temp
            self.rings[pos + 1] = ring
            self.rebuild_chain()

    def rebuild_chain(self):
        for ring in self.rings:
            ring.pack_forget()
            ring.pack(fill="x", padx=5, pady=5)







