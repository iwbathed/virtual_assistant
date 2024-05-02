import customtkinter as ctk

from gui.meta.Window_meta import Window
from gui.meta.Singleton import SingletonMeta



class OneRunner(metaclass=SingletonMeta):
    def __init__(self):
        self.callbacks_id = {}

    def run_tkinter(self, callback: Window, title):

        if id(callback) not in self.callbacks_id :

            root = ctk.CTk()
            root.protocol("WM_DELETE_WINDOW", lambda : self._on_quit(id(callback)))
            self.callbacks_id[id(callback)] = root
            callback(root, title)
            root.mainloop()

        else:
            # lead to Fatal Python error
            # root = self.callbacks_id[id(callback)]
            # root.attributes("-topmost", True)
            # root.attributes("-topmost", False)

            print("Вікно вже відкрите")

    def _on_quit(self, call_id):
        root = self.callbacks_id[call_id]
        root.destroy()
        self.callbacks_id.pop(call_id)

    def destroy_all(self):
        print(self.callbacks_id)
        for k in self.callbacks_id.keys():
            root = self.callbacks_id[k]
            root.destroy()
        self.callbacks_id.clear()
# root = None
# def run_tkinter(callback):
#     global root
#     if root is None:
#         root = tk.Tk()
#         root.protocol("WM_DELETE_WINDOW", _on_quit)
#         callback(root)
#         root.mainloop()
#     else:
#         print("Вікно вже відкрите")
#
# def _on_quit():
#     global root
#     root.destroy()
#     root = None

# class OneRunner:
#     def __init__(self):
#         self.root = None
#
#     def run_tkinter(self, callback):
#
#         if self.root is None:
#             self.root = tk.Tk()
#             self.root.protocol("WM_DELETE_WINDOW", self._on_quit)
#             callback(self.root)
#             self.root.mainloop()
#         else:
#             print("Вікно вже відкрите")
#
#     def _on_quit(self):
#
#         self.root.destroy()
#         self.root = None