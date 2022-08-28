from tkinter import *
import customtkinter
from colors import colors
import random

# Custom Properties for Application
BG_COLOR = '#16262E'
FG_COLOR = '#FBF7F4'
HOVER_COLOR = '#FFFCF9'
HOVER_TEXTC = '#071013'

HEIGHT = 600
WIDTH = 800

DEFAULT_TEXT = 'EMPTY TEXT'
QUERY_TEXT = 'QUERY'
SUBMIT_TEXT = 'SUBMIT'
PPM_TEXT = 'The purpose of this application is to store your information,\nplease input all of the information provided in input boxes below.'

# Random Colour Combinations
colour = '#' + ('%06x' % random.randint(0, 0xFFFFFF))

app = customtkinter.CTk()

# Initial Appearence Using CTK
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")


class COMMANDS():
    # Submits the Values Inputted from User
    def SUBMIT():
        pass  # connect.py instance within here.

    def DEFAULT():
        return print(f'{colors.CBOLD}{colors.CVIOLETBG2}{colors.CWHITE2}DEFAULT BUTTON PRESSED.{colors.ENDC}')


class APP(customtkinter.CTk, COMMANDS):
    def __init__(self) -> None:
        super().__init__()

        self.title("PPM - PROTECTED PASSWORD MANAGER")
        self.geometry(f'{WIDTH}x{HEIGHT}')
        self.protocol("WM_DELETE_WINDOW", self.close_app)

        # Icons for Buttons : SUBMIT, QUERY

        # ============Confuguring Grids=============
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # LEFT FRAME FOR BUTTONS
        self.frame_left = customtkinter.CTkFrame(
            master=self,
            width=180,
            corner_radius=5
        )

        self.frame_left.grid(
            row=0,
            column=0,
            sticky="nswe"
        )

        # RIGHT FRAME FOR INFORMATION
        self.frame_right = customtkinter.CTkFrame(master=self)

        self.frame_right.grid(
            row=1,
            column=1,
            sticky="nswe",
            padx=10,
            pady=10
        )

        # UPPER RIGHT FRAME FOR APP INTRODUCTION
        self.upper_frame_right = customtkinter.CTkFrame(
            master=self, fg_color=FG_COLOR, corner_radius=5)

        self.frame_right.grid(
            row=0,
            column=0,
            sticky="nswe",
            padx=10,
            pady=10,
        )

        # ==========Configuring Labels============

        # LABEL For PPM Introduction
        self.LabelPPM = customtkinter.CTkLabel(
            master=self.frame_right,
            text='PPM - PROTECTED PASSWORD MANAGER',
            text_color=FG_COLOR,
            text_font=('Bahnschrift Bold', 11),

        )
        self.LabelPPM.grid(row=1, column=0, pady=0, padx=5)

    def close_app(self, event=1):
        if event == 1:
            self.destroy()


if __name__ == "__main__":
    app = APP()
    app.mainloop()
