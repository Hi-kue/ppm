from tkinter import *
import customtkinter
from colors import colors
import random

# Custom Properties for Application
BG_COLOR = '#16262E'
FG_COLOR = '#FBF7F4'
HOVER_COLOR = '#FFFCF9'
HOVER_TEXTC = '#071013'

HEIGHT = 500
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
