import tkinter
import customtkinter
import random
from commands import COMMANDS
from colors import colors
import datetime
from tabulate import tabulate

# Custom Properties for Application
HEIGHT = 700
WIDTH = 700

# Button Defaults & Customization Variables
DEFAULT_TEXT = 'EMPTY TEXT'
QUERY_TEXT = 'QUERY'
SUBMIT_TEXT = 'SUBMIT'
HASH_TEXT = 'HASH'

TEXT_COLOR = '#e8e8e8'
HOVER_COLOR = '#7F8487'
BORDER_COLOR = '#474647'
BG_COLOR = '#413F42'
FG_COLOR = '#fafafa'


# Pre Determined Variables for Ease of Modification
LAB_WIDTH = 350
LAB_HEIGHT = 30
T_FONT = 'Candara'
CORNER_RAD = 3

# Random Colour Combinations + Other
colour = '#' + ('%06x' % random.randint(0, 0xFFFFFF))
current_time = datetime.datetime.now()

app = customtkinter.CTk()

# Initial Appearence Using CTK
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")


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

        # LOWER RIGHT FRAME FOR PURPOSE, ETC
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

        # INPUT FOR COLLECTING USER RESPONSE

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

        self.InputEMAIL = customtkinter.CTkEntry(
            master=self.frame_right,
            width=LAB_WIDTH,
            height=LAB_HEIGHT,
            corner_radius=3,
            text_font=(T_FONT, 10),
            justify=tkinter.LEFT,
        )
        self.InputEMAIL.grid(row=1, column=1, pady=5, padx=0)

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
            command=self.submit,
            text=SUBMIT_TEXT,
            text_font='Candara 10 bold',
            text_color=TEXT_COLOR,
            hover=True,
            hover_color=HOVER_COLOR,
            height=40,
            width=120,
            border_width=2,
            corner_radius=5,
            border_color=BORDER_COLOR,
            fg_color=BG_COLOR,
        )

        self.SubmitBUTTON.grid(
            row=0, column=0, columnspan=2, rowspan=2, padx=10, pady=10)

        # BUTTON FOR : HASHING PASSWORDS USER PROVIDED (HASH)
        self.HashBUTTON = customtkinter.CTkButton(
            master=self.frame_left,
            command=COMMANDS.HASH,
            text=HASH_TEXT,
            text_font='Candara 10 bold',
            text_color=TEXT_COLOR,
            hover=True,
            hover_color=HOVER_COLOR,
            height=40,
            width=120,
            border_width=2,
            corner_radius=5,
            border_color=BORDER_COLOR,
            fg_color=BG_COLOR,

        )
        self.HashBUTTON.grid(
            row=3, column=0, columnspan=2, rowspan=2, padx=10, pady=10)

        # BUTTON FOR : QUERYING USER INFORMATION INTO DATABASE (QUERY)
        self.QueryBUTTON = customtkinter.CTkButton(
            master=self.frame_left,
            command=COMMANDS.QUERY,
            text=QUERY_TEXT,
            text_font='Candara 10 bold',
            text_color=TEXT_COLOR,
            hover=True,
            hover_color=HOVER_COLOR,
            height=40,
            width=120,
            border_width=2,
            corner_radius=5,
            border_color=BORDER_COLOR,
            fg_color=BG_COLOR,
        )
        self.QueryBUTTON.grid(
            row=5, column=0, columnspan=2, rowspan=2, padx=10, pady=10)

        # ====================BREAKER======================

        # INPUT FOR : PROVIDING USER CLARIFICATION ON BUTTONS - SUBMIT, QUERY, HASH
        self.InfoINPUT = customtkinter.CTkTextbox(
            master=self.lower_frame_right,
            width=450,
            height=150,
            corner_radius=5,
            text_font=('Segoe UI Symbol', 10),
            text_color=FG_COLOR,
            # justify=tkinter.LEFT,
        )

        self.InfoINPUT.grid(
            row=0, column=0, padx=10, pady=10)

        # SCROLL FOR TEXTBOX : PROVIDES AUTO SCROLLABILITY
        self.InfoSCROLL = customtkinter.CTkScrollbar(
            master=self.InfoINPUT,
            command=self.InfoINPUT.yview,
            scrollbar_hover_color=HOVER_COLOR,
            orientation='vertical',
            hover=True
        )

        self.InfoSCROLL.grid(row=0, column=1, sticky='ns')

    def close_app(self, event=1):
        if event == 1:
            self.destroy()

    # TODO: WORK ON COMMANDS
    def submit(self):
        # Prompted Text Shows Within Textbox Widget -> Provides User Information Submitted

        submit_content = {
            'NUM:': self.InputNUM.get(),
            'EMAIL:': self.InputEMAIL.get(),
            'PASSWORD:': self.InputPASSWORD.get(),
            'TYPE:': self.InputTYPE.get(),
            'NAME:': self.InputNAME.get(),
            # 'INFO:': f'Submitted at {current_time.strftime("%y-%m-%d ~ %H:%M:%S")}'
        }

        self.InfoINPUT.insert(customtkinter.EXTENDED, tabulate(
            submit_content.items(),
            headers=['VALUES', 'USER IN'],
            showindex=True,
            tablefmt='grid',
        ))

        print(tabulate(
            submit_content.items(),
            headers=['VALUES', 'USER IN'],
            showindex=True,
            tablefmt='grid'
        ))

        # Return Button Pressed In Terminal
        print(
            f'{colors.CBOLD}{colors.CVIOLETBG}{colors.CWHITE2}SUBMIT BUTTON PRESSED AT: {current_time.strftime("%y-%m-%d ~ %H:%M:%S")}{colors.ENDC}')

    def hash(self, **kwargs):
        print(
            f'{colors.CBOLD}{colors.CREDBG2}{colors.CBLACK}HASH BUTTON PRESSED AT: {current_time.strftime("%y-%m-%d ~ %H:%M:%S")}{colors.ENDC}')

    def query(self, *args):
        print(
            f'{colors.CBOLD}{colors.CBEIGEBG}{colors.CBLACK}QUERY BUTTON PRESSED AT: {current_time.strftime("%y-%m-%d ~ %H:%M:%S")}{colors.ENDC}')


if __name__ == "__main__":
    app = APP()
    app.mainloop()
