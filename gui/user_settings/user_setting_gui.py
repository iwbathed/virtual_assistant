# import tkinter as tk
# import tkinter.ttk as ttk
from tkinter import font, END
import customtkinter as ctk

from gui.meta.OneRunner import OneRunner

from gui.meta.Window_meta import Window
from gui.user_settings.SettingsBlock import SettingsBlock
from main_folder.device_id import input_devices
from main_folder.stt_models_info import get_languages, get_models_by_lang

from models.tts.silero_tts import lang


class UserSettingsGUI(Window):
    def __init__(self, master, title_text):
        super().__init__(master, title_text)


        # self.settings_frame = ctk.CTkFrame(self.master)
        # #
        # self.settings_frame.grid()
        self.settings_block = SettingsBlock(self.master)
        #
        # stt model
        self._settings_stt_model_create()

        # tts model
        self._setting_tts_model_create()
        # input device
        self._settings_input_devices_create()
        #
        self._settings_font_create()

        self._settings_recognition_confidence_percentage()

        self._add_save_button()

    #     self._resize_widgets()
    # def _resize_widgets(self):
    #     widgets = self.master.winfo_children()
    #     max_width=0
    #     for widget in widgets:
    #         current_widget_width = widget.winfo_width()
    #         if current_widget_width > max_width:
    #             max_width = current_widget_width
    #
    #     for widget in widgets:
    #         widget.

    def _add_save_button(self):
        # settings_save_button_block = SettingsBlock(self.settings_frame)


        block = ctk.CTkFrame(master=self.settings_block.settings_frame)
        block.pack(fill="x")


        self.save_settings_button = ctk.CTkButton(master=block,
                                                  text="Save",
                                                  command=lambda: self.on_save_button_click(),
                                                  )

        self.save_settings_button.pack(fill="x")

        # self.settings_block.add_single_settings_block(block, self.save_settings_button)

    def _settings_recognition_confidence_percentage(self):




        self.settings_block.add_block_label("Recognition confidence")


        min_wwd_percent, max_wwd_percent = 1, 100
        self.wwd_recognition_entry = self.settings_block.add_settings_block(f"WWD confidence percentage ({min_wwd_percent} - {max_wwd_percent})%:",
                                               self._add_numeric_input, None,
                                               self.settings.wwd_recognition_percentage,
                                               min_wwd_percent, max_wwd_percent
                                               )

        # self.wwd_recognition_entry = self._add_numeric_input(parent=self.settings_block.settings_frame,
        #                                                      start_value=self.settings.wwd_recognition_percentage,
        #                                                      min_value=min_wwd_percent, max_value=max_wwd_percent)
        # self.settings_block.add_settings_block(self.wwd_recognition_entry,
        #                                        f"WWD confidence percentage ({min_wwd_percent} - {max_wwd_percent})%:")


        min_stt_percent, max_stt_percent = 1, 100
        self.stt_recognition_entry = self.settings_block.add_settings_block(f"WWD confidence percentage ({min_wwd_percent} - {max_wwd_percent})%:",
                                               self._add_numeric_input, None,
                                               self.settings.stt_recognition_percentage,
                                               min_stt_percent, max_stt_percent
                                               )




        # self.stt_recognition_entry = self._add_numeric_input(parent=self.settings_block.settings_frame,
        #                                                      start_value=self.settings.stt_recognition_percentage,
        #                                                      min_value=min_stt_percent, max_value=max_stt_percent)
        # self.settings_block.add_settings_block(self.stt_recognition_entry,
        #                                        f"STT confidence percentage ({min_stt_percent} - {max_stt_percent})%:")

    def validate_numeric_entry_callback(self, P, min_value: int = 0, max_value: int = 2000):
        min_value = int(min_value)
        max_value = int(max_value)
        if P == "" or (str.isdigit(P) and min_value <= int(P) <= max_value):
            return True
        return False

    def _add_numeric_input(self, parent, start_value: int, min_value: int = 0, max_value: int = 10_000):
        vcmd = (parent.register(self.validate_numeric_entry_callback))
        entry = ctk.CTkEntry(master=parent, textvariable=ctk.StringVar(),
                             validate='key',
                             validatecommand=(vcmd, '%P', min_value, max_value),
                             )
        entry.delete(0, END)
        entry.insert(0, start_value)
        return entry

    def _settings_font_create(self):
        fonts = font.families()

        # settings_font_block = SettingsBlock(self.master, )

        self.settings_block.add_block_label("Font")

        self.font_family_combo = self.settings_block.add_settings_block("Font family", self._create_setting_combobox_list,
                                                                        None,  list(fonts),
                                                                        self.settings.font_family)



        # self.font_family_combo = self._create_setting_combobox_list(
        #     parent=self.settings_block.settings_frame,
        #     list_content=list(fonts),
        #     chosen_option_text=self.settings.font_family,
        # )
        # self.settings_block.add_settings_block(self.font_family_combo, "Font family")

        min_font_size = 1
        max_font_size = 40
        self.font_size_entry = self.settings_block.add_settings_block(f"Font_size ({min_font_size} - {max_font_size}):",
                                               self._add_numeric_input,
                                               None, self.settings.font_size,
                                                       min_font_size, max_font_size,)


        # self.font_size_entry = self._add_numeric_input(parent=self.settings_block.settings_frame,
        #                                                start_value=self.settings.font_size,
        #                                                min_value=min_font_size, max_value=max_font_size,
        #                                                )
        # # self.font_size_entry.s
        # self.settings_block.add_settings_block(self.font_size_entry,
        #                                        f"Font_size ({min_font_size} - {max_font_size}):")

        # fonts = ctk.CTkFont
        # self.font_frame, self.font_label, self.font_combo = self._add_setting_combobox_list(
        #     self.settings_frame, "Font: ", list(fonts),
        #     chosen_option_text=self.settings.font_family)

    def _settings_input_devices_create(self):
        input_device_info = input_devices()
        input_device_names = [f"{info['name']}; Channels {info['maxInputChannels']}" for info in input_device_info]

        # settings_input_devise_block = SettingsBlock(self.settings_frame, "Input device")
        self.settings_block.add_block_label("Devices")



        self.input_device_combo = self.settings_block.add_settings_block("Input device", self._create_setting_combobox_list,
                                               lambda e: self.on_stt_language_choose(),
                                               list(input_device_names),
                                               self.settings.input_device,
                                               )

        # self.input_device_combo = self._create_setting_combobox_list(
        #     parent=self.settings_block.settings_frame,
        #     list_content=list(input_device_names),
        #     chosen_option_text=self.settings.input_device,
        # )
        # self.stt_language_combo.configure(command=lambda e: self.on_stt_language_choose())
        # self.settings_block.add_settings_block(self.input_device_combo, "Input device")






    def _create_setting_combobox_list(self, parent, list_content: list, chosen_option_text: str = None) \
            -> ctk.CTkComboBox:
        # current_width = max([len(info) for info in list_content])
        combo = ctk.CTkComboBox(parent,
                                values=list_content,
                                # width=current_width
                                )
        try:
            combo.set(chosen_option_text)
        except ValueError:
            combo.set(combo["values"][0])
            print(f"Item '{chosen_option_text}' not found in ComboBox options.")
        # combo.pack(side="right")
        return combo

    def _settings_stt_model_create(self):
        # settings_stt_model_block = SettingsBlock(self.settings_frame, "Stt model")
        self.settings_block.add_block_label("Stt model")
        # lang
        stt_languages = get_languages()

        self.stt_language_combo = self.settings_block.add_settings_block("Language: ",
                                               self._create_setting_combobox_list,
                                               lambda e: self.on_stt_language_choose(),
                                               list(stt_languages),
                                               self.settings.stt_model_settings["language"],
                                               )


        # self.stt_language_combo = self._create_setting_combobox_list(
        #     parent=self.settings_block.settings_frame,
        #     list_content=list(stt_languages),
        #     chosen_option_text=self.settings.stt_model_settings["language"],
        # )
        # self.stt_language_combo.configure(command=lambda e: self.on_stt_language_choose())
        # self.settings_block.add_settings_block(self.stt_language_combo, "Language: ")


        # model
        stt_models = get_models_by_lang(self.settings.stt_model_settings["language"])

        self.stt_model_combo = self.settings_block.add_settings_block("Model: ",
                                                                      self._create_setting_combobox_list, None,
                                                                      list(stt_models),
                                                                      self.settings.stt_model_settings["model_name"]
                                                                      )


        # self.stt_model_combo = \
        #     self._create_setting_combobox_list(
        #         parent=self.settings_block.settings_frame,
        #         list_content=list(stt_models),
        #         chosen_option_text=self.settings.stt_model_settings["model_name"])
        # self.settings_block.add_settings_block(self.stt_model_combo, "Model: ")

        min_time, max_time = 0, 60
        self.stt_active_time_entry = \
            self.settings_block.add_settings_block(f"Listening time  ({min_time} - {max_time}s)",
                                                   self._add_numeric_input, None,
                                                   self.settings.stt_listening_time,
                                                   min_time, max_time
                                                   )

        # self.stt_active_time_entry = self._add_numeric_input(parent=self.settings_block.settings_frame,
        #                                                      start_value=self.settings.stt_listening_time,
        #                                                      min_value=min_time, max_value=max_time
        #                                                      )
        #
        # self.settings_block.add_settings_block(self.stt_active_time_entry,
        #                                        f"Listening time  ({min_time} - {max_time}s)")

    def _setting_tts_model_create(self):
        # settings_tts_model_block = SettingsBlock(self.settings_frame, "Tts model")
        self.settings_block.add_block_label("Tts model")

        # lang
        languages = lang.keys()

        self.tts_language_combo = self.settings_block.add_settings_block("Language: ",
                                                                         self._create_setting_combobox_list,
                                                                         lambda e: self.on_tts_language_choose(),
                                                                         list(languages),
                                                                         self.settings.tts_model_settings["language"]
                                                                         )

        # self.tts_language_combo = \
        #     self._create_setting_combobox_list(parent=self.settings_block.settings_frame,
        #                                        list_content=list(languages),
        #                                        chosen_option_text=self.settings.tts_model_settings["language"]
        #                                        )
        # self.tts_language_combo.configure(command=lambda e: self.on_tts_language_choose())
        # self.settings_block.add_settings_block(self.tts_language_combo, "Language: ")
        selected_lang = self.tts_language_combo.get()



        # model
        models_for_selected_languages = lang[selected_lang].keys()

        self.tts_model_combo = self.settings_block.add_settings_block("Models: ",
                                                                      self._create_setting_combobox_list,
                                                                      None,
                                                                      list(models_for_selected_languages),
                                                                      self.settings.tts_model_settings["model_id"]
                                                                      )

        # self.tts_model_combo = \
        #     self._create_setting_combobox_list(parent=self.settings_block.settings_frame,
        #                                        list_content=list(models_for_selected_languages),
        #                                        chosen_option_text=self.settings.tts_model_settings["model_id"])
        #
        # self.tts_model_combo.configure(command=lambda e: self.on_tts_model_choose(self.tts_language_combo.get()))
        #
        # self.settings_block.add_settings_block(self.tts_model_combo, "Models: ")
        selected_model = self.tts_model_combo.get()




        # speakers
        speakers_for_selected_models = lang[selected_lang][selected_model]
        self.tts_speaker_combo = self.settings_block.add_settings_block("Speaker: ",
                                                                        self._create_setting_combobox_list,
                                                                        None,
                                                                        list(speakers_for_selected_models),
                                                                        self.settings.tts_model_settings["speaker"]
                                                                        )


        # self.tts_speaker_combo = \
        #     self._create_setting_combobox_list(parent=self.settings_block.settings_frame,
        #                                        list_content=list(speakers_for_selected_models),
        #                                        chosen_option_text=self.settings.tts_model_settings["speaker"]
        #                                        )
        # self.settings_block.add_settings_block(self.tts_speaker_combo, "Speaker: ")

    def on_stt_language_choose(self):
        selected_lang = self.stt_language_combo.get()
        models_for_selected_languages = get_models_by_lang(selected_lang)
        print(models_for_selected_languages)
        self.stt_model_combo.configure(values=list(models_for_selected_languages))
        self.stt_model_combo.set(self.stt_model_combo.cget('values')[0])

    def on_tts_language_choose(self):
        selected_lang = self.tts_language_combo.get()
        models_for_selected_languages = lang[selected_lang].keys()
        self.tts_model_combo.configure(values=list(models_for_selected_languages))
        self.tts_model_combo.set(self.tts_model_combo.cget('values')[0])

        self.on_tts_model_choose(selected_lang)

    def on_tts_model_choose(self, selected_lang):
        selected_model = self.tts_model_combo.get()
        speakers_for_selected_models = lang[selected_lang][selected_model]
        self.tts_speaker_combo.configure(values=list(speakers_for_selected_models))
        self.tts_speaker_combo.set(self.tts_speaker_combo.cget('values')[0])

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # def _settings_background_color_create(self):
    #     self.bg_color_frame = ctk.CTkFrame(self.settings_frame, bg=self.settings.bg_color)
    #     self.bg_color_frame.pack(anchor="nw", fill="y", expand=True)
    #
    #     self.bg_color_label = ctk.CTkLabel(self.bg_color_frame, text=f"Background color",
    #                                    fg=self.settings.font_color, bg=self.settings.bg_color)
    #     self.bg_color_label.pack(side="left", fill="x")
    #
    #     self.bg_color_button = ctk.CTkButton(self.bg_color_frame, highlightthickness=2,
    #                                      highlightbackground=self.settings.font_color, bg=self.settings.bg_color)
    #     self.bg_color_button.configure(command=lambda: self.choose_color(self.bg_color_button),
    #                                    width=self.bg_color_button.winfo_reqheight())
    #     self.bg_color_button.pack(side="right")
    #
    #
    # def _settings_font_color_create(self):
    #     self.font_color_frame = ctk.CTkFrame(self.settings_frame, bg=self.settings.bg_color)
    #     self.font_color_frame.pack(anchor="nw", fill="y", expand=True)
    #     self.font_color_label = ctk.CTkLabel(self.font_color_frame, text=f"Font color",
    #                                      fg=self.settings.font_color, bg=self.settings.bg_color)
    #     self.font_color_label.pack(side="left", fill="x")
    #     self.font_color_button = ctk.CTkButton(self.font_color_frame, bg=self.settings.font_color)
    #     self.font_color_button.configure(command=lambda: self.choose_color(self.font_color_button),
    #                                      width=self.font_color_button.winfo_reqheight())
    #     self.font_color_button.pack(side="right")
    #
    #
    #
    # def _settings_font_family_create(self):
    #     fonts = font.families()
    #     # fonts = ctk.CTkFont
    #     self.font_frame, self.font_label, self.font_combo = self._add_setting_combobox_list(
    #         self.settings_frame, "Font: ", list(fonts),
    #     chosen_option_text=self.settings.font_family)
    #
    # def _settings_mouse_speed_create(self, min_speed, max_speed):
    #     self.mouse_speed_frame, self.mouse_speed_label, self.mouse_speed_entry = \
    #         self._add_numeric_input(self.settings_frame, f"Mouse speed ({min_speed} - {max_speed}): ",
    #                                 min_speed, max_speed)
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # def choose_color(self, color_widget):
    #     color = tkcolorpicker.askcolor(parent=self.settings_frame)
    #     if color[1]:
    #         color_widget.configure(bg=color[1])

    def on_save_button_click(self):
        setting_dict = self.settings.get_settings_dict()

        setting_dict["input_device"] = self.input_device_combo.get()
        setting_dict["stt_model_settings"]["language"] = self.stt_language_combo.get()
        setting_dict["stt_model_settings"]["model_name"] = self.stt_model_combo.get()
        setting_dict["tts_model_settings"]["language"] = self.tts_language_combo.get()
        setting_dict["tts_model_settings"]["model_id"] = self.tts_model_combo.get()
        setting_dict["tts_model_settings"]["speaker"] = self.tts_speaker_combo.get()
        setting_dict["font_family"] = self.font_family_combo.get()
        setting_dict["font_size"] = int(self.font_size_entry.get())
        setting_dict["wwd_recognition_percentage"] = int(self.wwd_recognition_entry.get())
        setting_dict["stt_recognition_percentage"] = int(self.stt_recognition_entry.get())
        setting_dict["stt_listening_time"] = int(self.stt_active_time_entry.get())
        self.settings.create_json(setting_dict)


if __name__ == "__main__":
    # run_tkinter(UserSettingsGUI)

    runner = OneRunner()
    runner.run_tkinter(UserSettingsGUI, "Settings")

    # run_tkinter(UserSettingsGUI)
    # UserSettingsGUISingletonRun()
