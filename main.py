import os
import time
from datetime import datetime

SPLIT_SYMBOL = "-"
INDEX = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', '/', ' ']
BG = " "
CHAR = "o"
COLOUR = 'K'
BACKGROUND = " "*len(COLOUR)
MAPPER = {BG: BACKGROUND, CHAR : COLOUR}

class Graphics():
    r"""This class load a bunch of strings and let them print as numbers
    The standard used is 20 columns by 12 rows.
    ```
                 ____________________
                |        oooo        |
                |     oooooooooo     |
                |    oooo    oooo    |
                |   oooo      oooo   |
                |    oooo    oooo    |
                |      oooooooo      |
                |    oooo    oooo    |
                |  oooo        oooo  |
                |  oooo        oooo  |
                |   oooo      oooo   |
                |    oooooooooooo    |
                |       oooooo       |
                 --------------------
    ```

    """
    def __init__(self):
        self.numbers: dict = {}

        self.load_numbers()

    
    def load_numbers(self):
        with open("numbers_strip.txt", mode = "r", encoding = "utf-8") as fp:
            for idx, char in enumerate(fp, 0):
                # print(idx, number)
                for key in MAPPER:
                    char = char.replace(key, MAPPER[key])
                self.numbers[INDEX[idx]] = char

    def print_number(self, idx: int | str):
        for line in self.numbers[idx].split(SPLIT_SYMBOL):
            print(line)

    def sync_printing(self, indexes: list):
        line = ""
        for reading_line_num in range(12):
            for i in indexes:
                    line += str(self.numbers[i].split(SPLIT_SYMBOL)[reading_line_num])
            line += "\n"
        print(line, flush = True)
        

def clock_terminal() -> None:
    clock = Graphics()
    while True:
        now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        chars = []
        for char in now:
            chars.append(char)
        clock.sync_printing(chars)
        time.sleep(1)



if __name__ == "__main__":
    clock_terminal()