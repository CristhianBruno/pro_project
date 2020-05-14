import tkinter as tk
from tkinter.messagebox import askyesno
import webbrowser

# Fonts:
LARGE_FONT = ("Avenir", 14)
NORMAL_FONT = ("Avenir", 12)
SMALL_FONT = ("Avenir", 10)


# -------------------- Button generators --------------------


def raise_frame(frame_to_call):
    frame_to_call.tkraise()


def dashboard_button(where, frame, rows, columns):
    button_dashboard = tk.Button(where, text="Dashboard",
                                 command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_dashboard.grid(row=rows, column=columns, columnspan=2, sticky='news')
    button_dashboard.config(width=10, height=3)


def interactive_analysis_button(where, frame, rows, columns):
    button_interactive_analysis = tk.Button(where, text="Analysis\nper Sector",
                                            command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_interactive_analysis.grid(row=rows, column=columns, columnspan=2, sticky='news')
    button_interactive_analysis.config(width=10, height=3)


def vmb_model_button(where, frame, rows, columns):
    button_vmb_model = tk.Button(where, text="VMB Model",
                                 command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_vmb_model.grid(row=rows, column=columns, columnspan=2, sticky='news')
    button_vmb_model.config(width=10, height=3)


def main_page_button(where, frame, rows, columns):
    button_main_page = tk.Button(where, text="Main Page",
                                 command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_main_page.grid(row=rows, column=columns, columnspan=2, sticky='news')
    button_main_page.config(width=10, height=3)


def sector_main_button(where, frame, rows, columns):
    button_sector_table = tk.Button(where, text="Profile",
                                    command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_sector_table.grid(row=rows, column=columns, sticky='news', columnspan=2)
    button_sector_table.config(width=10, height=3)


def sector_table_button(where, frame, rows, columns):
    button_sector_table = tk.Button(where, text="Statistics",
                                    command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_sector_table.grid(row=rows, column=columns, sticky='news', columnspan=2)
    button_sector_table.config(width=10, height=3)


def sector_profile_button(where, frame, rows, columns):
    button_sector_table = tk.Button(where, text="Back to\n profile",
                                    command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_sector_table.grid(row=rows, column=columns, sticky='new', columnspan=2)
    button_sector_table.config(width=10, height=3)


def main_table_button(where, frame, rows, columns):
    button_sector_table = tk.Button(where, text="Statistics",
                                    command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_sector_table.grid(row=rows, column=columns, sticky='news', columnspan=2)
    button_sector_table.config(width=10, height=3)


def main_graphs_button(where, frame, rows, columns):
    button_sector_table = tk.Button(where, text="Graphs",
                                    command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_sector_table.grid(row=rows, column=columns, sticky='news', columnspan=2)
    button_sector_table.config(width=10, height=3)


def graphs2_button(where, frame, rows, columns):
    button_sector_table = tk.Button(where, text="Next page",
                                    command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_sector_table.grid(row=rows, column=columns, sticky='news', columnspan=2)
    button_sector_table.config(width=10, height=3)


def graphs1_button(where, frame, rows, columns):
    button_sector_table = tk.Button(where, text="Previous page",
                                    command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_sector_table.grid(row=rows, column=columns, sticky='news', columnspan=2)
    button_sector_table.config(width=10, height=3)


def model_continue_button(where, frame, rows, columns):
    button_sector_table = tk.Button(where, text="Continue",
                                    command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_sector_table.grid(row=rows, column=columns, sticky='news', columnspan=2)
    button_sector_table.config(width=10, height=3)


def destroyer_button(where, frame, rows, columns):
    button_destroyer = tk.Button(where, text="EXIT", command=ask_if_quit, font=SMALL_FONT, cursor="dot")
    button_destroyer.grid(row=rows, column=columns, columnspan=1)
    button_destroyer.config(width=5, height=2)


def ask_if_quit():
    question = askyesno(title='VMB Venture Capital',
                        message="Thank you for visiting VMB's platform!\n\nAre you sure you want to leave?",
                        icon='warning', default='no')
    if question:
        quit()


def empty_label(where, rows, columns):
    label_empty = tk.Label(where, text=" ", font=LARGE_FONT)
    label_empty.grid(column=columns, row=rows, sticky='news')


def callback(url):
    webbrowser.open_new(url)


def link_exp(where, rows, columns):
    link = tk.Label(where, text="Feature\nexplanations", fg="blue", cursor="dot", font=SMALL_FONT)
    link.bind("<Button-1>",
              lambda e: callback("https://www.dropbox.com/s/jluw9n9rm34y4ap/Feature%20Explanations.pdf?dl=0"))
    link.grid(columns=columns, row=rows, columnspan=2, sticky='news')


