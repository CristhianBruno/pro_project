""" ## Programing - Final Project - UNIL - MSc. in Finance - May 2020
### Group members: Valeria Medinaceli, Martin Ruilova, and Bruno Ayllon.
---

This scripts is designed to display the key facts of each sector on the platform.

"""

# Import external dependencies:
import tkinter as tk
import numpy as np


# Create the generator function:
def KeyFacts_Sector(sector, data_frame, frame):
    """
    Creates the labels that displays the key facts of the selected sector (GSE).
    Parameters
    ----------
    sector: GSE variable selected by the user.
    data_frame: Data frame generated by the pre-processing.
    frame: Frame where the labels will be created.

    Returns
    -------
    Displays the labels according to the sector selected by the user.
    """

    df_dict = data_frame
    companies = int(np.asarray(df_dict.loc[[sector], ['Companies']]))
    countries = int(np.asarray(df_dict.loc[[sector], ['Countries']]))
    success_rate = round(float(np.asarray(df_dict.loc[[sector], ['Success rate']])) * 100, 2)
    funding = round(float(np.asarray(df_dict.loc[[sector], ['Avg. amount of funding raised']])), 2)
    investors = int(np.asarray(df_dict.loc[[sector], ['Avg. investors']]))
    advisors = int(np.asarray(df_dict.loc[[sector], ['Avg. advisors']]))

    nr1 = tk.Label(frame, text=companies, font=("DejaVu Sans", 40), fg='dodgerblue', anchor='s')
    nr1.grid(row=3, column=0, columnspan=2)
    nr1.config(width=8, height=1)
    fact1 = tk.Label(frame, text="Companies", font=("DejaVu Sans Bold", 16), fg='black', anchor='n')
    fact1.grid(row=4, column=0, columnspan=2)

    nr2 = tk.Label(frame, text=countries, font=("DejaVu Sans", 40), fg='dodgerblue', anchor='s')
    nr2.grid(row=3, column=2, columnspan=2)
    nr2.config(width=8, height=1)
    fact2 = tk.Label(frame, text="Countries", font=("DejaVu Sans Bold", 16), fg='black', anchor='n')
    fact2.grid(row=4, column=2, columnspan=2)

    nr3 = tk.Label(frame, text="%.2f%%" % success_rate, font=("DejaVu Sans", 40), fg='dodgerblue', anchor='s')
    nr3.grid(row=3, column=4, columnspan=2)
    nr3.config(width=8, height=1)
    fact3 = tk.Label(frame, text="Success rate", font=("DejaVu Sans Bold", 16), fg='black', anchor='n')
    fact3.grid(row=4, column=4, columnspan=2)

    nr4 = tk.Label(frame, text="USD %.2f" % funding, font=("DejaVu Sans", 40), fg='dodgerblue', anchor='s')
    nr4.grid(row=5, column=0, columnspan=2)
    nr4.config(width=8, height=1)
    fact4 = tk.Label(frame, text="Avg. funding in millions", font=("DejaVu Sans Bold", 16), fg='black', anchor='n')
    fact4.grid(row=6, column=0, columnspan=2)

    nr5 = tk.Label(frame, text=investors, font=("DejaVu Sans", 40), fg='dodgerblue', anchor='s')
    nr5.grid(row=5, column=2, columnspan=2)
    nr5.config(width=8, height=1)
    fact5 = tk.Label(frame, text="Avg. investors", font=("DejaVu Sans Bold", 16), fg='black', anchor='n')
    fact5.grid(row=6, column=2, columnspan=2)

    nr6 = tk.Label(frame, text=advisors, font=("DejaVu Sans", 40), fg='dodgerblue', anchor='s')
    nr6.grid(row=5, column=4, columnspan=2)
    nr6.config(width=8, height=1)
    fact6 = tk.Label(frame, text="Avg. advisors", font=("DejaVu Sans Bold", 16), fg='black', anchor='n')
    fact6.grid(row=6, column=4, columnspan=2)
