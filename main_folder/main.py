from infi.systray import SysTrayIcon
from constants.constants import logo_icon_path_ico
from gui.meta.OneRunner import OneRunner


from gui.manage_scripts.manage_scripts_gui_ctk import ManageScriptsGUI
from gui.user_settings.user_setting_gui import UserSettingsGUI

# from main_folder.va_assistant import stop_listener, play_listener

if __name__ == "__main__":


    # run_va_title = "Run"
    # stop_va_title = "Stop"
    # run_va = (run_va_title, None, lambda play: play_listener())
    # stop_va = (stop_va_title, None, lambda stop: stop_listener())


    manage_scripts_title = "Manage commands"
    manage_scripts = (manage_scripts_title, None, lambda run: OneRunner().
                      run_tkinter(ManageScriptsGUI, manage_scripts_title))

    settings_title = "Settings"
    settings = (settings_title, None, lambda run: OneRunner().
                run_tkinter(UserSettingsGUI, settings_title))

    menu_options = (
        # run_va, stop_va,
        manage_scripts, settings)


    def on_quit_callback(systray: SysTrayIcon):
        OneRunner().destroy_all()
        # exit()


    tray = SysTrayIcon(logo_icon_path_ico, "Fox-fix", menu_options,
                       on_quit=on_quit_callback
                       )
    tray.start()




# menu_options = (("Say Hello", None, say_hello),)
#
# systray = SysTrayIcon(logo_icon_path_ico, "Fox-fix", menu_options)
# systray.start()
