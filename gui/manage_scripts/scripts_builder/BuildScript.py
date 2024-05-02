import keyboard
from typing import List

from commands_controller.scrips_builder.builder_json_crud import create_json
from gui.meta.Toplevel_meta import ToplevelWindow
from gui.meta.Window_meta import Window
from gui.manage_scripts.scripts_builder.ChainRing import ChainRing

from gui.meta.OneRunner import OneRunner
import customtkinter as ctk


class BuildScriptsGUI(ToplevelWindow):
    def __init__(self, title_text):
        super().__init__(title_text)

        self.main_frame = ctk.CTkFrame(master=self)
        self.main_frame.pack(fill="both", expand=1)


        self.available_commands_frame = ctk.CTkScrollableFrame(master=self.main_frame)
        self.available_commands_frame.pack(side="left", expand=1, fill="both")

        self._add_option(master=self.available_commands_frame,
                         callback=self.execute_ring,
                         button_text="Execute")

        self._add_option(master=self.available_commands_frame,
                         callback=self.keyboard_ring,
                         button_text="Keyboard")

        self._add_option(master=self.available_commands_frame,
                         callback=self.mouse_click_ring,
                         button_text="Mouse click")

        self._add_option(master=self.available_commands_frame,
                         callback=self.mouse_move_ring,
                         button_text="Mouse move")


        self.script_frame = ctk.CTkScrollableFrame(master=self.main_frame)
        self.script_frame.pack(side="right", expand=1, fill="both")
        self.chain = ChainRing(self.script_frame)

        self.save_frame = ctk.CTkFrame(master=self)
        self.save_frame.pack(fill="x")
        self.file_name_entry = ctk.CTkEntry(self.save_frame)
        self.file_name_entry.pack(side="left", fill="x", expand=1)
        self.save_button = ctk.CTkButton(self.save_frame, text="Save",
                                         command=lambda : self.handle_save_button())
        self.save_button.pack(side="right")


        # self.chain.add_ring(self.ring_with_label, "r1")
        # self.chain.add_ring(self.keyboard_ring)
        # self.chain.add_ring(self.execute_ring, "Execute")
        #
        # self.chain.add_ring(self.mouse_move_ring)
        # self.chain.add_ring(self.mouse_click_ring)

    def handle_save_button(self):
        file_name = self.file_name_entry.get()
        print(file_name)

        actions=[]
        frames: List[ctk.CTkFrame] = self.chain.rings
        for frame in frames:
            text = frame.winfo_children()[0].winfo_children()[0].cget("text")
            data = self._get_data_by_ring_label(text, frame.winfo_children()[0])
            actions.append(data)
            # print(data)
        res = create_json(actions, file_name)
        if not res:
            print("File from builder NOT saved")
        else:
            print("Actions from builder Saved!")


    def _get_data_by_ring_label(self, text, frame):
        if text == "Execute":
            return self._get_execute_ring_data(frame)
        if text == "Keyboard":
            return self._get_keyboard_ring_data(frame)
        if text == "Mouse click":
            return self._get_mouse_click_ring_data(frame)
        if text == "Mouse move":
            return self._get_mouse_move_ring_data(frame)












    def _add_option(self, master, callback, button_text:str=None):
        button = ctk.CTkButton(master=master, text=button_text,
                               command=lambda : self.chain.add_ring(callback, button_text))
        button.pack(fill="x")

    def _add_label(self, master, label_text):
        label = ctk.CTkLabel(master=master, text=label_text)
        label.pack(fill="x")

    def execute_ring(self, ring: ctk.CTkFrame, label_text: str = None):
        frame = ctk.CTkFrame(master=ring)
        if label_text:
            self._add_label(frame, label_text)
        executor_entry = ctk.CTkEntry(master=frame,
                                      placeholder_text="Executor (leave empty for *.exe, *.lnk etc. )")
        executor_entry.pack(fill="x")
        file_name_entry = ctk.CTkEntry(master=frame,
                                       placeholder_text="Absolute path to file")
        file_name_entry.pack(fill="x")
        return frame

    def _get_execute_ring_data(self, frame: ctk.CTkFrame):
        widgets_list = frame.winfo_children()
        data = {"command_name":widgets_list[0].cget("text"),
                "executor": widgets_list[1].get(),
                "path": widgets_list[2].get()
                }
        return data

    def keyboard_ring(self, ring: ctk.CTkFrame, label_text: str = None):
        frame = ctk.CTkFrame(master=ring)
        if label_text:
            self._add_label(frame, label_text)
        keys_combo = ctk.CTkComboBox(master=frame,
                                     values=list(keyboard._canonical_names.canonical_names.values()))
        keys_combo.pack(fill="x")

        keyboard_actions = ["Press", "Release", "Press and release"]
        keyboard_actions_combo = ctk.CTkComboBox(master=frame,
                                                 values=keyboard_actions)
        keyboard_actions_combo.pack(fill="x")

        # def radiobutton_event():
        #     print("radiobutton toggled, current value:", keyboard_action_radio_var.get())
        #
        # keyboard_action_radio_var = tk.IntVar(value=0)
        # press_radio = ctk.CTkRadioButton(master=frame, text="Press",
        #                                              command=radiobutton_event,
        #                                    variable=keyboard_action_radio_var, value=1)
        # press_radio.pack()
        #
        #
        #
        # release_radio = ctk.CTkRadioButton(master=frame, text="Release",
        #                                              command=radiobutton_event,
        #                                    variable=keyboard_action_radio_var, value=2)
        # release_radio.pack()
        # press_and__release_radio = ctk.CTkRadioButton(master=frame, text="Press and release",
        #                                    command=radiobutton_event,
        #                                    variable=keyboard_action_radio_var, value=3)
        # press_and__release_radio.pack()
        return frame

    def _get_keyboard_ring_data(self, frame:ctk.CTkFrame):
        widgets_list = frame.winfo_children()
        data= {"command_name":widgets_list[0].cget("text"),
               "button": widgets_list[1].get(),
               "action": widgets_list[2].get()
        }
        return data

    def mouse_click_ring(self, ring: ctk.CTkFrame, label_text: str = None):
        frame = ctk.CTkFrame(master=ring)
        if label_text:
            self._add_label(frame, label_text)
        mouse_buttons = ["left button click", "right button click", "middle button click"]
        mouse_buttons_combo = ctk.CTkComboBox(master=frame, values=mouse_buttons)
        mouse_buttons_combo.pack(fill="x")
        click_options = ["single click", "double click"]
        click_options_combo = ctk.CTkComboBox(master=frame, values=click_options)
        click_options_combo.pack(fill="x")

        return frame

    def _get_mouse_click_ring_data(self, frame:ctk.CTkFrame):
        widgets_list = frame.winfo_children()
        data = {"command_name":widgets_list[0].cget("text"),
                "button": widgets_list[1].get(),
                "click_type": widgets_list[2].get()
        }
        return data

    def mouse_move_ring(self, ring: ctk.CTkFrame, label_text: str = None):
        frame = ctk.CTkFrame(master=ring)
        if label_text:
            self._add_label(frame, label_text)

        def on_action_select(event):
            # print(event)
            # print(mouse_action_combo.get())
            if mouse_action_combo.get() == "move":
                print(event)
                x_start_entry.configure(state="disabled")
                y_start_entry.configure(state="disabled")
            elif mouse_action_combo.get() == "drag":
                x_start_entry.configure(state="normal")
                y_start_entry.configure(state="normal")
            else:
                print("none")
                print(mouse_action_combo.get())
        mouse_action = ["move", "drag"]
        mouse_action_combo = ctk.CTkComboBox(master=frame, values=mouse_action, command= lambda event: on_action_select(event))
        mouse_action_combo.pack(fill="x")


        # combobox_event = ctk.EventType("<<TComboboxSelected>>")
        # combobox_event.register(combobox_callback)
        # mouse_action_combo.bind("<<TComboboxSelected>>", on_action_select)

        def validate_numeric_entry_callback(P, min_value: int = 0, max_value: int = 2000):
            min_value = int(min_value)
            max_value = int(max_value)
            if P == "" or (str.isdigit(P) and min_value <= int(P) <= max_value):
                return True
            return False

        duration_min, duration_max = 0, 5
        vcmd = (ring.register(validate_numeric_entry_callback))
        duration_entry = ctk.CTkEntry(master=frame,
                                      placeholder_text=f"Duration second ({duration_min, duration_max})",
                                      validatecommand=(vcmd, '%P', duration_min, duration_max)
                                      )
        duration_entry.pack(fill="x")

        x_coordinate_min, x_coordinate_max = 0, 7680  # 8k resolution
        y_coordinate_min, y_coordinate_max = 0, 4320
        x_end_entry = ctk.CTkEntry(master=frame,
                                   placeholder_text="Move to X coordinate",
                                   validatecommand=(vcmd, '%P', x_coordinate_min, x_coordinate_max)
                                                     )
        x_end_entry.pack(fill="x")

        y_end_entry = ctk.CTkEntry(master=frame,
                                   placeholder_text="Move to Y coordinate",
                                   validatecommand=(vcmd, '%P', y_coordinate_min, y_coordinate_max)
                                   )
        y_end_entry.pack(fill="x")

        x_start_entry = ctk.CTkEntry(master=frame,
                                     placeholder_text="Start from X coordinate",
                                     validatecommand=(vcmd, '%P', x_coordinate_min, x_coordinate_max),
                                     state="disabled"
                                     )
        x_start_entry.pack(fill="x")


        y_start_entry = ctk.CTkEntry(master=frame,
                                     placeholder_text="Start from Y coordinate",
                                     validatecommand=(vcmd, '%P', y_coordinate_min, y_coordinate_max),
                                     state="disabled"
                                     )
        y_start_entry.pack(fill="x")



        # click_options = ["single click", "double click"]
        # click_options_combo = ctk.CTkComboBox(master=frame, values=click_options)
        # click_options_combo.pack()

        return frame

    def _get_mouse_move_ring_data(self, frame:ctk.CTkFrame):
        widgets_list = frame.winfo_children()
        data = {"command_name":widgets_list[0].cget("text"),
                "move_type": widgets_list[1].get(),
                "duration": widgets_list[2].get(),
                "x_end": widgets_list[3].get(),
                "y_end": widgets_list[4].get(),
                "x_start": widgets_list[5].get(),
                "y_start": widgets_list[6].get(),

        }
        return data



    # def ring_with_label(self, ring: ctk.CTkFrame, text: str):
    #     frame = ctk.CTkFrame(master=ring)
    #     label = ctk.CTkLabel(master=frame,
    #                               text=text)
    #     label.pack(fill="x")
    #     return frame

    # def ring_type2(self, ring: ctk.CTkFrame):
    #     frame = ctk.CTkFrame(master=ring)
    #     label = ctk.CTkLabel(master=frame,
    #                               text="temp2")
    #     label.pack(side="left")
    #     return frame







    # def load_available_commads_gui(self):
    #     self.commads_frame






    # def run_program_label




if __name__ == "__main__":
    runner = OneRunner()
    runner.run_tkinter(BuildScriptsGUI, "Commands builder")
