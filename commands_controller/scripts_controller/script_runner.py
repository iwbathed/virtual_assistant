import os
import subprocess
import sys


def run_script(path_to_script, execution_command=None):
    print(path_to_script)
    if not execution_command:
        # subprocess.call([path_to_script])
        os.startfile(path_to_script)
        # subprocess.Popen(path_to_script, execution_command=sys.executable)
    else:
        subprocess.call([execution_command, path_to_script])



if __name__ == "__main__":
    run_script(r"C:\Users\user\Desktop\run_telegram.py", "python")