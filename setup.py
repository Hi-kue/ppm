import tkinter
from tkinter import *
import customtkinter
from colors import colors
import random

# Custom Properties for Application
BG_COLOR = '#16262E'
FG_COLOR = '#FBF7F4'
HOVER_COLOR = '#FFFCF9'
HOVER_TEXTC = '#071013'

HEIGHT = 700
WIDTH = 735

DEFAULT_TEXT = 'EMPTY TEXT'
QUERY_TEXT = 'QUERY'
SUBMIT_TEXT = 'SUBMIT'
HASH_TEXT = 'HASH'

# Pre Determined Variables for Ease of Modification
LAB_WIDTH = 350
LAB_HEIGHT = 30
T_FONT = 'Candara'
CORNER_RAD = 3

# Random Colour Combinations
colour = '#' + ('%06x' % random.randint(0, 0xFFFFFF))

app = customtkinter.CTk()

# Initial Appearence Using CTK
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")


class COMMANDS():
    # Submits the Values Inputted from User
    def SUBMIT():
        return print(f'{colors.CBOLD}{colors.CVIOLETBG}{colors.CWHITE2}SUBMIT BUTTON PRESSED.{colors.ENDC}')

    def DEFAULT():
        return print(f'{colors.CBOLD}{colors.CVIOLETBG}{colors.CWHITE2}DEFAULT BUTTON PRESSED.{colors.ENDC}')


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
            corner_radius=5
        )

        self.frame_left.grid(
            row=0,
            column=0,
            sticky="nswe",
            pady=10
        )

        # UPPER RIGHT FRAME FOR APP INTRODUCTION
        self.upper_frame_right = customtkinter.CTkFrame(
            master=self,
            width=100,
            height=100,
            corner_radius=5
        )

        # UPPER RIGHT FRAME FOR PURPOSE, ETC
        self.upper_frame_right.grid(
            row=0,
            column=1,
            sticky="nswe",
            padx=10,
            pady=10
        )

        # RIGHT UPPER FRAME CONFIGURATION
        self.upper_frame_right.grid_rowconfigure(1, weight=1)
        self.upper_frame_right.grid_columnconfigure(1, weight=1)

        # RIGHT FRAME FOR USER INFORMATION
        self.frame_right = customtkinter.CTkFrame(
            master=self.upper_frame_right,
            corner_radius=5
        )

        self.frame_right.grid(row=2, column=2, columnspan=6,
                              rowspan=6, pady=10, padx=10, sticky="nswe")

        # LOWER FRAME RIGHT FOR DISPLAYING USER INPUT
        self.lower_frame_right = customtkinter.CTkFrame(
            master=self.frame_right,
            corner_radius=5
        )

        # UPPER RIGHT FRAME FOR PURPOSE, ETC
        self.lower_frame_right.grid(
            row=6,
            column=0,
            columnspan=10,
            sticky="nswe",
            padx=10,
            pady=10
        )

        # RIGHT UPPER FRAME CONFIGURATION
        self.lower_frame_right.grid_rowconfigure(1, weight=1)
        self.lower_frame_right.grid_columnconfigure(1, weight=1)

        # ==========Configuring Labels============

        # LABEL For PPM Introduction
        self.LabelPPM = customtkinter.CTkLabel(
            master=self.upper_frame_right,
            text='''
            PPM - PROTECTED PASSWORD MANAGER
                Purpose: 
                    The purpose of PPM is to obtain, hash, and return passwords provided 
                    by the user. This software obtains passwords while hashing them 
                    through a series of hashes (MD5, SHA-1, SHA-2, NTLM, and LANMAN)
                    in order to provide the user upmost protection for fair use. Use
                    This software to your liking!
                    
                Warning ⚠️:
                    The password manager will not be able to complete an entry if there
                    is an empty input field. If it does not follow a specific format it
                    will also prompt an error.
            ''',
            text_color=FG_COLOR,
            text_font=('Candara Bold', 10),
            justify=tkinter.LEFT,
        )
        self.LabelPPM.grid(row=0, column=1, columnspan=4,  pady=5, padx=5)

        # ====================BREAKER======================

        # LABEL & INPUT FOR : NUM
        self.LabelNUM = customtkinter.CTkLabel(
            master=self.frame_right,
            text='ENTER NUM :',
            text_color=FG_COLOR,
            text_font=(T_FONT, 10),
            justify=tkinter.CENTER,
        )
        self.LabelNUM.grid(row=0, column=0, pady=5, padx=0)

        self.InputNUM = customtkinter.CTkEntry(
            master=self.frame_right,
            width=LAB_WIDTH,
            height=LAB_HEIGHT,
            corner_radius=3,
            text_font=(T_FONT, 10),
            justify=tkinter.LEFT,
        )
        self.InputNUM.grid(row=0, column=1, pady=5, padx=0)

        # ====================BREAKER======================

        # LABEL & INPUT FOR : EMAIL
        self.LabelEMAIL = customtkinter.CTkLabel(
            master=self.frame_right,
            text='ENTER EMAIL :',
            text_color=FG_COLOR,
            text_font=(T_FONT, 10),
            justify=tkinter.CENTER,
        )
        self.LabelEMAIL.grid(row=1, column=0, pady=5, padx=0)

        self.InputNUM = customtkinter.CTkEntry(
            master=self.frame_right,
            width=LAB_WIDTH,
            height=LAB_HEIGHT,
            corner_radius=3,
            text_font=(T_FONT, 10),
            justify=tkinter.LEFT,
        )
        self.InputNUM.grid(row=1, column=1, pady=5, padx=0)

        # ====================BREAKER======================

        # LABEL & INPUT FOR : PASSWORD *
        self.LabelPASSWORD = customtkinter.CTkLabel(
            master=self.frame_right,
            text='ENTER PASSWORD :',
            text_color=FG_COLOR,
            text_font=(T_FONT, 10),
            justify=tkinter.CENTER,
        )
        self.LabelPASSWORD.grid(row=2, column=0, pady=5, padx=0)

        self.InputPASSWORD = customtkinter.CTkEntry(
            master=self.frame_right,
            width=LAB_WIDTH,
            height=LAB_HEIGHT,
            corner_radius=3,
            text_font=(T_FONT, 10),
            justify=tkinter.LEFT,
        )
        self.InputPASSWORD.grid(row=2, column=1, pady=5, padx=0)

        # ====================BREAKER======================

        # LABEL & INPUT FOR : TYPE *
        self.LabelTYPE = customtkinter.CTkLabel(
            master=self.frame_right,
            text='ENTER TYPE :',
            text_color=FG_COLOR,
            text_font=(T_FONT, 10),
            justify=tkinter.CENTER,
        )
        self.LabelTYPE.grid(row=3, column=0, pady=5, padx=0)

        self.InputTYPE = customtkinter.CTkEntry(
            master=self.frame_right,
            width=LAB_WIDTH,
            height=LAB_HEIGHT,
            corner_radius=3,
            text_font=(T_FONT, 10),
            justify=tkinter.LEFT,
        )
        self.InputTYPE.grid(row=3, column=1, pady=5, padx=0)

        # ====================BREAKER======================

        # LABEL & INPUT FOR : NAME (OPTIONAL)
        self.LabelNAME = customtkinter.CTkLabel(
            master=self.frame_right,
            text='ENTER NAME (O) :',
            text_color=FG_COLOR,
            text_font=(T_FONT, 10),
            justify=tkinter.CENTER,
        )
        self.LabelNAME.grid(row=4, column=0, pady=5, padx=0)

        self.InputNAME = customtkinter.CTkEntry(
            master=self.frame_right,
            width=LAB_WIDTH,
            height=LAB_HEIGHT,
            corner_radius=3,
            text_font=(T_FONT, 10),
            justify=tkinter.LEFT,
        )
        self.InputNAME.grid(row=4, column=1, pady=5, padx=0)

        # ====================BREAKER======================

        # BUTTON FOR : SUBMITTING USER INFORMATION (SUBMIT)
        self.SubmitBUTTON = customtkinter.CTkButton(
            master=self.frame_left,
            text=SUBMIT_TEXT,
            text_font=(T_FONT, 10),
            border_width=2,
            border_color=str(colour),
            command=COMMANDS.DEFAULT
        )
        self.SubmitBUTTON.grid(
            row=0, column=0, columnspan=2, rowspan=2, padx=10, pady=10)

        # BUTTON FOR : HASHING PASSWORDS USER PROVIDED (HASH)
        self.hashBUTTON = customtkinter.CTkButton(
            master=self.frame_left,
            text=HASH_TEXT,
            text_font=(T_FONT, 10),
            border_width=2,
            border_color=str(colour),
            command=COMMANDS.DEFAULT

        )
        self.hashBUTTON.grid(
            row=3, column=0, columnspan=2, rowspan=2, padx=10, pady=10)

        # BUTTON FOR : QUERYING USER INFORMATION INTO DATABASE (QUERY)
        self.queryBUTTON = customtkinter.CTkButton(
            master=self.frame_left,
            text=QUERY_TEXT,
            text_font=(T_FONT, 10),
            border_width=2,
            border_color=str(colour),
            command=COMMANDS.DEFAULT
        )
        self.queryBUTTON.grid(
            row=5, column=0, columnspan=2, rowspan=2, padx=10, pady=10)

        # ====================BREAKER======================

    def close_app(self, event=1):
        if event == 1:
            self.destroy()


if __name__ == "__main__":
    app = APP()
    app.mainloop()
