from ctypes import windll, c_int, byref, sizeof
from tkinter import PhotoImage, Toplevel, Menu

import customtkinter as ctk
from customtkinter import AppearanceModeTracker

from constants.constants import logo_icon_path_ico, logo_icon_path_png

from PIL import ImageTk, Image


from gui.meta.Fonts import Fonts
from gui.meta.Singleton import SingletonMeta





class ToplevelWindow(Toplevel,
                     Fonts
                     ):
    def __init__(self, title, *args, **kwargs):

        Toplevel.__init__(self, *args, **kwargs)

        Fonts.__init__(self)  # Initialize the Fonts class
        # self.geometry("1000x1000")

        # ico=PhotoImage(file=logo_icon_path_png)


        # AppearanceModeTracker.init_appearance_mode()
        # AppearanceModeTracker.set_appearance_mode("dark")
        # ctk.set_appearance_mode("dark")  # default

        # ico = ImageTk.PhotoImage(Image.open(logo_icon_path_png))
        # self.iconphoto(False, ico)


        self.title(title)
        self.iconbitmap(logo_icon_path_png)  # Assuming logo_icon_path_ico is a valid path



        print(self)
        print(logo_icon_path_ico)


    # def _set_top_var_color(self):
    #     HWND = windll.user32.GetParent(self.winfo_id())
    #     white_color = 0xffffffff
    #     black_color = 0x000000FF
    #     print(HWND)
    #     # if ctk.get_appearance_mode() == "Light":
    #     #     bar_color = white_color
    #     #     print("Light")
    #     #
    #     # elif ctk.get_appearance_mode() == "Dark":
    #     #     bar_color = black_color
    #     #     print("Dark")
    #     windll.dwmapi.DwmSetWindowAttribute(
    #         HWND,
    #         35,
    #         byref(c_int(black_color)),
    #         sizeof(c_int)
    #     )




# class ToplevelWindow(ctk.CTkToplevel,
#                      # Fonts
#                      ):
#     def __init__(self, title,  *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         self.iconbitmap(r"D:\programing\my_projects\python\bachelor\speech_recognition_v2\gui\icons\logo_fox_64x64.ico")
#         # self.iconbitmap(logo_icon_path_ico)
#         self.title(title)
#         print(self)

        # self.geometry("400x300")
        # print(type(self))
        # self.label = ctk.CTkLabel( self, text="ToplevelWindow")
        # self.label.pack(padx=20, pady=20)






# class App(ctk.CTk):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.geometry("500x400")
#
#         self.button_1 = ctk.CTkButton(self, text="open toplevel", command=self.open_toplevel)
#         self.button_1.pack(side="top", padx=20, pady=20)
#
#         self.toplevel_window = None
#
#     def open_toplevel(self):
#         if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
#             self.toplevel_window = ToplevelWindow(self, "toptop")  # create window if its None or destroyed
#         else:
#             self.toplevel_window.focus()  # if window exists focus it






# if __name__ == "__main__":
#     app = App()
#     app.mainloop()