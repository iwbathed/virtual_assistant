from enum import Enum

class ScriptsInfo(Enum):
    NAME: str = "script_name"
    PHRASE: str = "key_phrase"
    RUN_COMMAND: str = "run_command"


if __name__ == "__main__":
    print(ScriptsInfo.NAME.value)
