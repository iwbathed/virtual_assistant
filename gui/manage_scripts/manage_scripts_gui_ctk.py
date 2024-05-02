# import tkinter as tk
# import tkinter as ttk
# from tkinter.constants import BOTH, LEFT, VERTICAL, Y, RIGHT, END

import customtkinter as ctk
from customtkinter import BOTH, LEFT, X, RIGHT, END, TOP


import os
from commands_controller.scripts_controller.scripts_json_crud import load_scripts_info_to_json, \
    scripts_path, edit_script_field_by_script_name_json, delete_script_info_by_name_json, \
    get_script_field_by_key

from commands_controller.scripts_controller.scritps_json_crud_enum import ScriptsInfo
from gui.manage_scripts.RecordActionsDialog import RecordActionsDialog
from gui.manage_scripts.scripts_builder.BuildScript import BuildScriptsGUI
from gui.meta.OneRunner import OneRunner
from gui.meta.Window_meta import Window


class ManageScriptsGUI(Window):
    def __init__(self, master, title_text):
        super().__init__(master, title_text)
        # Left side: list of labels
        # self.label_frame = ctk.CTkFrame(master, width=400, border_width=2)
        # self.label_frame.pack(side="left",
        #                       anchor="nw",
        #                       fill="y",
        #                       expand=1)
        # self.label_frame.pack_configure(expand=1)

        self.record_toplevel, self.builder_toplevel = None, None



        self.movable_labels_frame = ctk.CTkScrollableFrame(self.master)
        self.movable_labels_frame.pack(side="left",
                                       anchor="nw",
                                       fill="both",
                                       expand=1,
                                    )
        self._load_scripts_gui()

        # Right side
        self.right_frame = ctk.CTkFrame(master, border_width=2,
                                        # fg_color="red"
                                        )
        self.right_frame.pack(side="left",
                              anchor="nw",
                              expand=1,
                              fill=BOTH,
                              )

        # buttons
        self.button_frame = ctk.CTkFrame(self.right_frame,
                                         )

        self.button_frame.pack(side=TOP, anchor="nw", fill=BOTH,
                               expand=1
                               )


        self.refresh_button = ctk.CTkButton(self.button_frame, text="Refresh", command=self.handle_refresh_button)
        self.widget_width_multiply(self.refresh_button, 2)
        self.refresh_button.pack(padx=5, pady=5)
        self.record_actions_button = ctk.CTkButton(self.button_frame, text="Record actions", command=self.handle_record_actions_button)
        self.widget_width_multiply(self.record_actions_button, 2)
        self.record_actions_button.pack(padx=5, pady=5)

        self.build_script_button = ctk.CTkButton(self.button_frame, text="Build scrips",
                                                   command=self.handle_build_scripts_button)
        self.widget_width_multiply(self.build_script_button, 2)
        self.build_script_button.pack(padx=5, pady=5)



        # self.update_button = ctk.CTkButton(self.button_frame, text="Update", command=self.handle_update_button,
        #                                    state="disabled")
        # self.update_button.pack(padx=5, pady=5)
        self.delete_button = ctk.CTkButton(self.button_frame, text="Delete", command=self.handle_delete_button,
                                           state="disabled")
        self.widget_width_multiply(self.delete_button, 2)
        self.delete_button.pack(padx=5, pady=5)

        # user_message_frame

        self.user_message_frame = ctk.CTkFrame(self.right_frame)
        self.user_message_frame.pack(side=TOP, anchor="n", fill=X)
        self.save_message_label = ctk.CTkLabel(self.user_message_frame, text=f"")
        self.save_message_label.pack(fill="x")

        # edit frame
        self.edit_frame = ctk.CTkFrame(self.right_frame)
        self.script_command_entry = ctk.CTkEntry(self.edit_frame,
                                                 placeholder_text="Executor (leave empty for *.exe etc)"
                                                 )
        self.widget_width_multiply(self.script_command_entry, 2)
        self.script_command_entry.pack()

        self.script_name_entry = ctk.CTkEntry(self.edit_frame, justify="left",
                                              placeholder_text="File name"
                                              )
        self.widget_width_multiply(self.script_name_entry, 2)
        self.script_name_entry.pack()

        self.script_phrase_entry = ctk.CTkEntry(self.edit_frame,
                                                placeholder_text="Key phrase"
                                                )
        self.widget_width_multiply(self.script_phrase_entry, 2)
        self.script_phrase_entry.pack()

        self.edit_buttons_frame = ctk.CTkFrame(self.edit_frame)
        self.edit_buttons_frame.pack()

        self.save_edited_button = ctk.CTkButton(self.edit_buttons_frame, text="Save",
                                                command=self.handle_save_edited_button)
        self.save_edited_button.pack(side=LEFT)

        self.cancel_edited_button = ctk.CTkButton(self.edit_buttons_frame, text="Cancel",
                                                  command=self.handle_cansel_edited_button)
        self.cancel_edited_button.pack(side=RIGHT)

        self.update_font(self.master, self.font_base)


        # self.edit_frame = ctk.CTkFrame(self.right_frame,
        #                                fg_color="red")
        #
        # self.script_command_entry = ctk.CTkEntry(self.edit_frame)
        # self.script_command_entry.grid(row=0, column=0,
        #                                sticky="nsew"
        #                                )
        #
        # self.script_name_entry = ctk.CTkEntry(self.edit_frame,  justify="left")
        # self.script_name_entry.grid(row=1, column=0,
        #                             sticky="nw"
        #                             )
        #
        # self.script_phrase_entry = ctk.CTkEntry(self.edit_frame)
        # self.script_phrase_entry.grid(row=2, column=0,
        #                               sticky="nsew"
        #                               )
        #
        # self.edit_buttons_frame = ctk.CTkFrame(self.edit_frame)
        # self.edit_buttons_frame.grid(row=3, column=0,
        #                              sticky="se"
        #                              )
        #
        # self.save_edited_button = ctk.CTkButton(self.edit_buttons_frame, text="Save",
        #                                         command=self.handle_save_edited_button)
        # self.save_edited_button.pack(side=LEFT)
        #
        # self.cancel_edited_button = ctk.CTkButton(self.edit_buttons_frame, text="Cancel",
        #                                           command=self.handle_cansel_edited_button)
        # self.cancel_edited_button.pack(side=RIGHT)






    def widget_width_multiply(self, widget, multiply_factor):
        widget.configure(width=widget.cget("width") * multiply_factor)

    def _clear_widget(self, frame):
        for widget in frame.winfo_children():
            print(widget)
            widget.destroy()

    def _load_scripts_gui(self):
        self.labels = []
        self.selected_label: ctk.CTkLabel = None  # Track the currently selected label
        data = load_scripts_info_to_json()
        # print(f"3 {data}")

        self._clear_widget(self.movable_labels_frame)
        for i in range(len(data)):
            # print(item)
            label = ctk.CTkLabel(self.movable_labels_frame,
                                 # name=item[ScriptsInfo.NAME.value],
                                 text=f"{data[i][ScriptsInfo.NAME.value]}\n{data[i][ScriptsInfo.PHRASE.value]}",
                                 justify="left", anchor="nw")

            label.pack(anchor="nw", fill="x", padx=5, pady=2)

            # label.bind("<Button-1>", lambda i=i: self.handle_label_click(label=self.labels[i]))  # Bind click event
            label.bind("<Button-1>", lambda event, clabel=label: self.handle_label_click(label=clabel, event=event))
            self.labels.append(label)
        self.update_font(self.movable_labels_frame, self.font_base)
        # print("!"*10)
        # for j in self.labels:
        #     print(id(j))

        # self._resize_label_canvas()


    def handle_cansel_edited_button(self):
        self.edit_frame.pack_forget()

    def handle_save_edited_button(self):
        prev_script_name, prev_script_phrase = self.selected_label.cget("text").split("\n", 1)
        prev_script_command = get_script_field_by_key(
            prev_script_name, ScriptsInfo.NAME.value, ScriptsInfo.RUN_COMMAND.value)

        new_script_name = self.script_name_entry.get()
        new_script_phrase = self.script_phrase_entry.get()
        new_script_command = self.script_command_entry.get()

        prev_script_path = scripts_path + "\\" + prev_script_name
        new_script_path = scripts_path + "\\" + new_script_name

        message = ""
        change_status = True
        if prev_script_name != new_script_name:

            if not os.path.exists(new_script_path):
                os.rename(src=prev_script_path, dst=new_script_path)
                edit_script_field_by_script_name_json(prev_script_name, ScriptsInfo.NAME.value, new_script_name)


            else:  # if file with this name exist
                change_status = False
                message += "File with such name already exist!\n"

        if change_status:
            if prev_script_phrase != new_script_phrase:
                edit_script_field_by_script_name_json(new_script_name, ScriptsInfo.PHRASE.value, new_script_phrase)
            if prev_script_command != new_script_command:
                edit_script_field_by_script_name_json(new_script_name, ScriptsInfo.RUN_COMMAND.value,
                                                      new_script_command)

            message += "Saved successfully!"

            self.edit_frame.pack_forget()
            self._load_scripts_gui()

        print("save_edited_button")

    def _set_save_edited_message(self, message: str, color: str):
        self.save_message_label.configure(text=message, fg=color)

    # def clear_message_text

    def handle_refresh_button(self):
        self.handle_cansel_edited_button()
        self._load_scripts_gui()
        print("refresh_button")

    def handle_label_click(self, label: ctk.CTkLabel, event):
        start_color = label.cget("fg_color")

        if self.selected_label:
            self.selected_label.configure(fg_color=start_color)

        self.selected_label = label
        self.selected_label.configure(fg_color=("lightblue", "black"))
        # self.update_button.configure(state="normal")
        self.delete_button.configure(state="normal")

        self.handle_update_button()

    def handle_record_actions_button(self):
        if self.record_toplevel is None or not self.record_toplevel.winfo_exists():
            self.record_toplevel = RecordActionsDialog("Enter file name")  # create window if its None or destroyed
            self.record_toplevel.focus()
        else:
            self.record_toplevel.focus()
        # runner = OneRunner()
        # runner.run_tkinter(RecordActionsDialog, "Enter file name")
        # print("Create button clicked!")

    def handle_build_scripts_button(self):
        if self.builder_toplevel is None or not self.builder_toplevel.winfo_exists():
            self.builder_toplevel = BuildScriptsGUI( "Commands builder")  # create window if its None or destroyed
            self.builder_toplevel.focus()
        else:
            self.builder_toplevel.focus()
        # runner = OneRunner()
        # runner.run_tkinter(BuildScriptsGUI, "Commands builder")


    def handle_update_button(self):
        if self.selected_label:
            print(type(self.selected_label))
            script_name, script_phrase = self.selected_label.cget("text").split("\n", 1)
            script_command = \
                get_script_field_by_key(script_name, ScriptsInfo.NAME.value, ScriptsInfo.RUN_COMMAND.value)

            self.script_name_entry.delete(0, END)
            self.script_phrase_entry.delete(0, END)
            self.script_command_entry.delete(0, END)

            self.script_name_entry.insert(0, script_name)
            self.script_phrase_entry.insert(0, script_phrase)
            self.script_command_entry.insert(0, script_command)

            # self.edit_frame.pack(fill="both", expand=True)
            # self.edit_frame.grid(row=2, column=0, sticky="nw")
            self.edit_frame.pack(side=TOP, anchor="nw", fill=BOTH, expand=1
                # side=TOP, anchor="n", fill=BOTH,
            )
            print(f"Update button clicked for label: {self.selected_label.cget('text')}")
        else:
            print("No label selected for update.")

    def handle_delete_button(self):
        if self.selected_label:
            script_name, script_phrase = self.selected_label.cget("text").split("\n", 1)
            self.labels.remove(self.selected_label)
            self.selected_label.destroy()
            self.selected_label = None
            # self.update_button.config(state="disabled")  # Disable update button
            self.delete_button.configure(state="disabled")  # Disable delete button
            os.remove(scripts_path + "\\" + script_name)
            delete_script_info_by_name_json(script_name)
            self._load_scripts_gui()

        else:
            print("No label selected for deletion.")


# root = None
#
# class ManageScriptsGUISingletonRun:
#     def __init__(self, *args):
#         global root
#         if root is None:
#             root = tk.Tk()
#             # root.protocol("WM_DELETE_WINDOW", self.on_quit)
#             ManageScriptsGUI(root)
#             root.mainloop()
#         else:
#             print("Вікно вже відкрите")
#
#     def on_quit(self):
#         global root
#         root.destroy()
#         root = None


if __name__ == "__main__":
    runner = OneRunner()
    runner.run_tkinter(ManageScriptsGUI, "Manage commands")
    # ManageScriptsGUISingletonRun()

    # run_tkinter(ManageScriptsGUI)
