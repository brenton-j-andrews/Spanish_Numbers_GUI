import pyttsx3
import random
from tkinter import *


# ---------------------------- Constants, globals and engine init ------------------------------- #
spanish_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
english_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
BACKGROUND_COLOR = "#808080"
GREEN = '#2B5329'
RED = '#9E1A1A'
WHITE = '#FFFFFF'
rand_number = 0
right_int = 0
wrong_int = 0

engine = pyttsx3.init()


# ---------------------------- Functions ------------------------------- #
def generate_int():
    global rand_number
    start_range = int(range_input_start.get())
    end_range = int(range_input_finish.get())
    engine.setProperty('voice', spanish_voice_id)
    rand_number = random.randrange(start_range, end_range)
    engine.say(f"{rand_number}")
    engine.runAndWait()


def repeat_rand_number():
    engine.say(f"{rand_number}")
    engine.runAndWait()


def check_answer():
    engine.setProperty('voice', english_voice_id)
    global rand_number, right_int, wrong_int
    user_answer = int(input_box.get())
    if user_answer == rand_number:
        right_int += 1
        correct_label.config(text=f'Correct Answers:\n\n {right_int}')
        engine.say(f'Correct!')
        engine.runAndWait()
    else:
        wrong_int += 1
        incorrect_label.config(text=f'Incorrect Answers:\n\n {wrong_int}')
        engine.say(f"Incorrect answer. The correct number was {rand_number}")
        engine.runAndWait()
    input_box.delete(0, END)
    generate_int()


# ---------------------------- UI Configuration ------------------------------- #
window = Tk()
window.title('Type the number.')
window.geometry('500x500')
window.config(padx=25, pady=25, bg=BACKGROUND_COLOR)

start_button = Button(text='Start', width=15, command=generate_int)
start_button.grid(pady=25, column=0, row=0)

stop_button = Button(text='Stop', width=15, command=exit)
stop_button.grid(padx=25, pady=25, column=2, row=0)


# Number range inputs.
range_label = Label(window, text='Range of numbers to study:')
range_label.grid(pady=25, column=0, row=1)

range_input_start = Entry(master=window)
range_input_start.insert(END, '1')
range_input_start.grid(padx=10, column=1, row=1)

range_input_finish = Entry(master=window)
range_input_finish.insert(END, '10')
range_input_finish.grid(padx=10, column=2, row=1)


# Language / speed settings and dropdown menus.
lang_label = Label(window, text="Study Language:")
lang_label.grid(column=0, row=2)
lang_options = ['Spanish', 'Mandarin', 'German']
lang_click = StringVar()
lang_click.set("Spanish")
lang_dropdown = OptionMenu(window, lang_click, *lang_options)
lang_dropdown.grid(pady=10, column=0, row=3)

speed_label = Label(window, text="Speed:")
speed_label.grid(column=2, row=2)
speed_options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
speed_click = IntVar()
speed_click.set("1")
speed_dropdown = OptionMenu(window, speed_click, *speed_options)
speed_dropdown.grid(pady=10, column=2, row=3)


# Answer and submission widgets.
input_label = Label(window, text='ANSWER: ')
input_label.grid(column=1, row=4)

input_box = Entry(master=window)
input_box.grid(padx=10, pady=10, column=1, row=5)

repeat_button = Button(text='Repeat', command=repeat_rand_number)
repeat_button.grid(column=2, row=5)

submit_button = Button(text='Check Answer', command=check_answer)
submit_button.grid(column=1, row=6)


# Score Counters.
correct_label = Label(window, bg=GREEN, pady=5, fg=WHITE, text=f'Correct Answers:\n\n {right_int}')
correct_label.grid(column=0, row=7)

incorrect_label = Label(window, bg=RED, pady=5, fg=WHITE, text=f'Incorrect Answers:\n\n {wrong_int}')
incorrect_label.grid(column=2, row=7)

window.mainloop()
