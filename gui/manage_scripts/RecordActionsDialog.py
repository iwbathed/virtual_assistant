import os.path

import customtkinter as ctk
import keyboard

from commands_controller.action_recorder.record import pickle_file_exist, record
from gui.meta.Toplevel_meta import ToplevelWindow

from gui.meta.OneRunner import OneRunner


current_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# scripts_path = os.path.join(current_dir_path, "scripts")

class RecordActionsDialog(ToplevelWindow,
                          # Window
                          ):
    def __init__(self,  title_text):
        super().__init__( title_text)
        pady, padx = 5, 5
        # self.master.attributes("-topmost", True)
        self.dialog_frame = ctk.CTkFrame(self)
        self.dialog_frame.pack(fill="both", expand=1)
        # self.label = ctk.CTkLabel(master=self.dialog_frame, text="Enter file name"
        #                           )
        # self.label.grid(row=0, column=0,
        #                 pady=pady, padx=padx
        #                 )



        self.file_name_frame = ctk.CTkFrame(master=self.dialog_frame)
        self.file_name_frame.pack(fill="x", expand=1
                             )

        self.entry_name = ctk.CTkEntry(master=self.file_name_frame,
                                       placeholder_text="My record",)
        self.entry_name.pack(fill="x", expand=1)

        self.escape_label = ctk.CTkLabel(master=self.file_name_frame, text="Enter file name:")
        self.escape_label.pack(fill="x", expand=1)

        escape_buttons: list = ["esc", "ctrl", "alt", "ctrl+alt"]
        self.escape_frame = ctk.CTkFrame(master=self.dialog_frame)
        self.escape_frame.pack(fill="x", expand=1
                             )
        self.escape_label = ctk.CTkLabel(master= self.escape_frame, text="Stop record button:")
        self.escape_label.pack(fill="x", expand=1)

        self.escape_combo = ctk.CTkComboBox(master=self.escape_frame,
                                values=escape_buttons,
                                )
        self.escape_combo.pack(fill="x", expand=1
                             )

        # self.switch_var = ctk.StringVar(value="on")
        #
        # self.switch = ctk.CTkSwitch(master=self.dialog_frame, text="Minimise windows",
        #                        variable=self.switch_var, onvalue="on", offvalue="off")
        # self.switch.grid(row=1, column=0,
        #             # pady=pady, padx=padx
        #                  )

        self.button_start_recording = ctk.CTkButton(master=self.dialog_frame,
                                                    text="Start recording",
                                                    command=self.handle_ok_button_click)
        self.button_start_recording.pack(


                                         )


        # resizeble
        # self.master.grid_columnconfigure(0, weight=1)
        # self.master.grid_rowconfigure(0, weight=1)
        #
        # self.file_name_frame.grid_columnconfigure(0, weight=1)
        # self.file_name_frame.grid_rowconfigure(0, weight=1)
        # self.file_name_frame


    def handle_ok_button_click(self):

        escape_keys=self.escape_combo.get()
        file_name = self.entry_name.get()
        if not self.check_keys_are_legal(escape_keys):
            print("incorrect keys sequence")
        else:
            if file_name:
                if not pickle_file_exist(file_name):

                    record(file_name=file_name, escape_key=escape_keys)

                else:
                    print(f"file with name {file_name} already exist")
            else:
                print("File name can not be empty")


        # print(keyboard._canonical_names.canonical_names.values())
        escape_keys_list = self.escape_combo.get()

        # print(self.switch._check_state)
        # print(self.entry_name.get())
        # print(self.escape_combo.get())



    def check_keys_are_legal(self, escape_keys:str):
        escape_keys_list = [x.strip() for x in escape_keys.split("+")]
        return not any(x not in keyboard._canonical_names.canonical_names.values() for x in escape_keys_list)


if __name__ == "__main__":
    print(current_dir_path)
    runner = OneRunner()
    runner.run_tkinter(RecordActionsDialog, "Enter file name:")

    # print(keyboard._canonical_names.canonical_names.values())
    # escape_keys = "ctrl+0+esc"
    #
    # escape_keys_list = [x.strip() for x in escape_keys.split("+")]
    # if not any(x not in keyboard._canonical_names.canonical_names.values() for x in escape_keys_list) :
    #     print("ok")
    # else:
    #     print("error")

    # print(1)
    # keyboard.wait("ctrl ")
    # print(2)












