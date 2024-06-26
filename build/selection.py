# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font
import os
import resultMK2


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd() + r"\assets\selection_img")

name_str = ''
developer_str = ''
rating_str = ''
greater_than = True
less_than = False
tags_lib = {"FANTASY": 0, "DRAMA": 0, "ROMANCE": 0, "SEXUAL_CONTENT": 2, "SCIENCE_FICTION": 0, "COMEDY": 0,
            "MYSTERY": 0, "HORROR": 0, "ACTION": 0}
tags_lib_helper = {'fantasy': "FANTASY", 'drama': 'DRAMA', 'romance': 'ROMANCE', 'eroge': 'SEXUAL_CONTENT',
                   'scifi': 'SCIENCE_FICTION', 'comedy': 'COMEDY', 'mystery': 'MYSTERY', 'horror': 'HORROR',
                   'action': 'ACTION'}

## Currently unusable and broken
# def tags_color(input: str) -> str:
#     tag = tags_lib_helper[input]
#     tag_value = tags_lib[tag]
#     if tag_value % 3 == 0:
#         return input + '.png'
#     if tag_value % 3 == 1:
#         return input + '_green.png'
#     if tag_value % 3 == 2:
#         return input + '_red.png'


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def fgreater_than():
    global greater_than
    greater_than = True
    global less_than
    less_than = False
    print_param()

def fless_than():
    global greater_than
    greater_than = False
    global less_than
    less_than = True
    print_param()

def swap_window(tkwindow: Tk, name: Entry, developer: Entry, rating: Entry) -> None:
    global name_str
    name_str = name.get()
    global developer_str
    developer_str = developer.get()
    global rating_str
    rating_str = rating.get()
    resultMK2.main(tags_lib, name_str, developer_str, rating_str, greater_than, less_than)
    tkwindow.destroy()

def edit_tags(string: str):
    tags_lib[string] = tags_lib[string] + 1
    print_param()

def print_param():
    print('************************************')
    print("fantasy: "  + is_included(tags_lib[tags_lib_helper['fantasy']]))
    print("drama: " + is_included(tags_lib[tags_lib_helper['drama']]))
    print("romance: " + is_included(tags_lib[tags_lib_helper['romance']]))
    print("sci-fi: " + is_included(tags_lib[tags_lib_helper['scifi']]))
    print("comedy: " + is_included(tags_lib[tags_lib_helper['comedy']]))
    print("mystery: " + is_included(tags_lib[tags_lib_helper['mystery']]))
    print("horror: " + is_included(tags_lib[tags_lib_helper['horror']]))
    print("action: " + is_included(tags_lib[tags_lib_helper['action']]))
    print()
    if greater_than == True:
        print("greater than or equal to: " + '\033[32mtrue\033[0m')
        print("less than or equal to: " + '\033[31mfalse\033[0m')
    if less_than == True:
        print("greater than or equal to: " + '\033[31mfalse\033[0m')
        print("less than or equal to: " + '\033[32mtrue\033[0m')
    print("\n\n\n")

def is_included(i: int):
    if i % 3 == 0:
        return 'Neutral'
    if i % 3 == 1:
        return '\033[32mIncluded\033[0m'
    if i % 3 == 2:
        return '\033[31mExcluded\033[0m'


# I've been defeated. You Won. You Win. I Quit. This Ain't it. Screw Tkinter.
# This was pure misery. First and Last time using Tkinter.
# def edit_tags(string: str, button: Button):
#     tags_lib[string] = tags_lib[string] + 1
#     refresh(button)
#
# def refresh(button: Button):
#     button.config(image=PhotoImage(file=relative_to_assets(tags_color('drama'))))
#     button.pack()
#     print(tags_color('drama'))

def main() -> None:
    window = Tk()

    window.geometry("1280x720")
    window.configure(bg="#FFFFFF")
    global tags_lib
    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        640.0,
        360.0,
        image=image_image_1
    )

    canvas.create_text(
        32.0,
        21.0,
        anchor="nw",
        text="Visual Novel Name:",
        fill="#D0D0D0",
        font=("ABeeZee Regular", 46 * -1)
    )

    canvas.create_text(
        748.0,
        33.0,
        anchor="nw",
        text="*All Tags Are Optional",
        fill="#D0D0D0",
        font=("ABeeZee Regular", 46 * -1)
    )

    canvas.create_text(
        15.0,
        320.0,
        anchor="nw",
        text="Ranking Filter (10 is Lowest, 100 is Highest):",
        fill="#D0D0D0",
        font=("ABeeZee Regular", 46 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        446.0,
        126.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        font=('ABeeZee_Regular 40'),
        bd=0,
        bg="#D0D0D0",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=47.0,
        y=89.0,
        width=798.0,
        height=73.0
    )

    canvas.create_text(
        22.0,
        168.0,
        anchor="nw",
        text="Developer Name:",
        fill="#D0D0D0",
        font=("ABeeZee Regular", 46 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        446.0,
        268.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        font=('ABeeZee_Regular 40'),
        bd=0,
        bg="#D0D0D0",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=47.0,
        y=231.0,
        width=798.0,
        height=73.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        332.0,
        419.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        font=('ABeeZee_Regular 40'),
        bd=0,
        bg="#D0D0D0",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=262.0,
        y=382.0,
        width=140.0,
        height=73.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fless_than(),
        relief="flat"
    )
    button_1.place(
        x=132.0,
        y=382.0,
        width=75.0,
        height=75.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fgreater_than(),
        relief="flat"
    )
    button_2.place(
        x=28.0,
        y=382.0,
        width=75.0,
        height=75.0
    )

    canvas.create_text(
        10.0,
        463.0,
        anchor="nw",
        text="Genre (Green = Included, Red = Excluded, Click to Change):",
        fill="#D0D0D0",
        font=("ABeeZee Regular", 46 * -1)
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("drama.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: edit_tags("DRAMA"),
        relief="flat"
    )
    button_3.place(
        x=260.0,
        y=522.0,
        width=200.0,
        height=75.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("scifi.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: edit_tags("SCIENCE_FICTION"),
        relief="flat"
    )
    button_4.place(
        x=736.0,
        y=522.0,
        width=200.0,
        height=75.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("romance.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: edit_tags("ROMANCE"),
        relief="flat"
    )
    button_5.place(
        x=498.0,
        y=522.0,
        width=200.0,
        height=75.0
    )

# REMOVES EROGE FUNCTIONALITY. AUTOMATICALLY EXCLUDED
    # button_image_6 = PhotoImage(
    #     file=relative_to_assets("eroge.png"))
    # button_6 = Button(
    #     image=button_image_6,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: edit_tags("SEXUAL_CONTENT"),
    #     relief="flat"
    # )
    # button_6.place(
    #     x=956.0,
    #     y=580.0,
    #     width=200.0,
    #     height=75.0
    # )

    button_image_7 = PhotoImage(
        file=relative_to_assets("fantasy.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: edit_tags("FANTASY"),
        relief="flat"
    )
    button_7.place(
        x=22.0,
        y=522.0,
        width=200.0,
        height=75.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("mystery.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: edit_tags("MYSTERY"),
        relief="flat"
    )
    button_8.place(
        x=253.0,
        y=624.0,
        width=200.0,
        height=75.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("action.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: edit_tags("ACTION"),
        relief="flat"
    )
    button_9.place(
        x=736.0,
        y=625.0,
        width=200.0,
        height=75.0
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("horror.png"))
    button_10 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: edit_tags("HORROR"),
        relief="flat"
    )
    button_10.place(
        x=498.0,
        y=625.0,
        width=200.0,
        height=75.0
    )

    button_image_11 = PhotoImage(
        file=relative_to_assets("comedy.png"))
    button_11 = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: edit_tags("COMEDY"),
        relief="flat"
    )
    button_11.place(
        x=22.0,
        y=625.0,
        width=200.0,
        height=75.0
    )

    # Buttons 12 and 13 were removed due to redundancy

    button_image_14 = PhotoImage(
        file=relative_to_assets("button_14.png"))
    button_14 = Button(
        image=button_image_14,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: swap_window(window, entry_1, entry_2, entry_3),
        relief="flat"
    )
    button_14.place(
        x=946.0,
        y=401.0,
        width=268.0,
        height=62.0
    )
    window.resizable(False, False)
    window.mainloop()


if __name__ == '__main__':
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n') # terminal issues. This must be done
    main()
