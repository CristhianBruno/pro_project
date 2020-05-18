""" ## Programing - Final Project - UNIL - MSc. in Finance - May 2020
### Group members: Valeria Medinaceli, Martin Ruilova, and Bruno Ayllon.
---

This scripts is designed to generate all the buttons that connect every frame of the
platform.

"""

# Import external dependencies:
import tkinter as tk
from tkinter.messagebox import askyesno
import webbrowser

# Fonts:
LARGE_FONT = ("DejaVu Sans", 14)
NORMAL_FONT = ("DejaVu Sans", 12)
SMALL_FONT = ("DejaVu Sans", 10)


# -------------------- Button generators --------------------


# Generate the functions for each Button:
def raise_frame(frame_to_call):
    """ Raises the selected frame.

    :param frame_to_call: The name of the frame to be called.
    :return: Raises the selected frame to the main view.
    """
    frame_to_call.tkraise()


def dashboard_button(where, frame, rows, columns):
    """ Button to go to the Dashboard.

    :param where: Frame where the button will be installed.
    :param frame: Dashboard.
    :param rows: Number of the row where the button will be installed.
    :param columns: Number of the column where the button will be installed.
    :return: Creates a widget with the mentioned specifications.
    """

    button_dashboard = tk.Button(where, text="Dashboard",
                                 command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_dashboard.grid(row=rows, column=columns, columnspan=2, sticky='news')
    button_dashboard.config(width=10, height=3)


def interactive_analysis_button(where, frame, rows, columns):
    """ Button to go to the Analysis per sector section.

    :param where: Frame where the button will be installed.
    :param frame: Analysis per sector.
    :param rows: Number of the row where the button will be installed.
    :param columns: Number of the column where the button will be installed.
    :return: Creates a widget with the mentioned specifications.
    """

    button_interactive_analysis = tk.Button(where, text="Analysis\nper Sector",
                                            command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_interactive_analysis.grid(row=rows, column=columns, columnspan=2, sticky='news')
    button_interactive_analysis.config(width=10, height=3)


def vmb_model_button(where, frame, rows, columns):
    """ Button to go to the VMB Model.

    :param where: Frame where the button will be installed.
    :param frame: VMB Model.
    :param rows: Number of the row where the button will be installed.
    :param columns: Number of the column where the button will be installed.
    :return: Creates a widget with the mentioned specifications.
    """

    button_vmb_model = tk.Button(where, text="VMB Model",
                                 command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_vmb_model.grid(row=rows, column=columns, columnspan=2, sticky='news')
    button_vmb_model.config(width=10, height=3)


def main_page_button(where, frame, rows, columns):
    """ Button to go to the Main Page.

    :param where: Frame where the button will be installed.
    :param frame: Main Page.
    :param rows: Number of the row where the button will be installed.
    :param columns: Number of the column where the button will be installed.
    :return: Creates a widget with the mentioned specifications.
    """

    button_main_page = tk.Button(where, text="Main Page",
                                 command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_main_page.grid(row=rows, column=columns, columnspan=2, sticky='news')
    button_main_page.config(width=10, height=3)


def sector_main_button(where, frame, rows, columns):
    """ Button to go to the selected sector's Profile.

    :param where: Frame where the button will be installed.
    :param frame: Profile per sector.
    :param rows: Number of the row where the button will be installed.
    :param columns: Number of the column where the button will be installed.
    :return: Creates a widget with the mentioned specifications.
    """

    button_sector_table = tk.Button(where, text="Profile",
                                    command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_sector_table.grid(row=rows, column=columns, sticky='news', columnspan=2)
    button_sector_table.config(width=10, height=3)


def sector_table_button(where, frame, rows, columns):
    """ Button to go to the Statistics of the selected sector.

    :param where: Frame where the button will be installed.
    :param frame: Statistics per sector.
    :param rows: Number of the row where the button will be installed.
    :param columns: Number of the column where the button will be installed.
    :return: Creates a widget with the mentioned specifications.
    """

    button_sector_table = tk.Button(where, text="Statistics",
                                    command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_sector_table.grid(row=rows, column=columns, sticky='news', columnspan=2)
    button_sector_table.config(width=10, height=3)


def sector_profile_button(where, frame, rows, columns):
    """ Button to go back to the Profile per sector.

    :param where: Frame where the button will be installed.
    :param frame: Profile per sector.
    :param rows: Number of the row where the button will be installed.
    :param columns: Number of the column where the button will be installed.
    :return: Creates a widget with the mentioned specifications.
    """

    button_sector_table = tk.Button(where, text="Back to\n profile",
                                    command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_sector_table.grid(row=rows, column=columns, sticky='new', columnspan=2)
    button_sector_table.config(width=10, height=3)


def main_table_button(where, frame, rows, columns):
    """ Button to go back to the Profile per sector.

    :param where: Frame where the button will be installed.
    :param frame: Profile per sector.
    :param rows: Number of the row where the button will be installed.
    :param columns: Number of the column where the button will be installed.
    :return: Creates a widget with the mentioned specifications.
    """

    button_sector_table = tk.Button(where, text="Statistics",
                                    command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_sector_table.grid(row=rows, column=columns, sticky='news', columnspan=2)
    button_sector_table.config(width=10, height=3)


def main_graphs_button(where, frame, rows, columns):
    """ Button to go to the first page of the Graphs section of Dashboard.

    :param where: Frame where the button will be installed.
    :param frame: Graphs, page 1.
    :param rows: Number of the row where the button will be installed.
    :param columns: Number of the column where the button will be installed.
    :return: Creates a widget with the mentioned specifications.
    """

    button_sector_table = tk.Button(where, text="Graphs",
                                    command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_sector_table.grid(row=rows, column=columns, sticky='news', columnspan=2)
    button_sector_table.config(width=10, height=3)


def graphs2_button(where, frame, rows, columns):
    """ Button to go to the second page of the Graphs section of Dashboard.

    :param where: Frame where the button will be installed.
    :param frame: Graphs, page 2.
    :param rows: Number of the row where the button will be installed.
    :param columns: Number of the column where the button will be installed.
    :return: Creates a widget with the mentioned specifications.
    """

    button_sector_table = tk.Button(where, text="Next page",
                                    command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_sector_table.grid(row=rows, column=columns, sticky='news', columnspan=2)
    button_sector_table.config(width=10, height=3)


def graphs1_button(where, frame, rows, columns):
    """ Button to go back to the first page of the Graphs section of Dashboard.

    :param where: Frame where the button will be installed.
    :param frame: Graphs, page 1.
    :param rows: Number of the row where the button will be installed.
    :param columns: Number of the column where the button will be installed.
    :return: Creates a widget with the mentioned specifications.
    """

    button_sector_table = tk.Button(where, text="Previous page",
                                    command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_sector_table.grid(row=rows, column=columns, sticky='news', columnspan=2)
    button_sector_table.config(width=10, height=3)


def model_continue_button(where, frame, rows, columns):
    """ Button to go to the next page of the VMB Model.

    :param where: Frame where the button will be installed.
    :param frame: VMB Model.
    :param rows: Number of the row where the button will be installed.
    :param columns: Number of the column where the button will be installed.
    :return: Creates a widget with the mentioned specifications.
    """
    button_sector_table = tk.Button(where, text="Continue",
                                    command=lambda: raise_frame(frame), font=LARGE_FONT, cursor="dot")
    button_sector_table.grid(row=rows, column=columns, sticky='news', columnspan=2)
    button_sector_table.config(width=10, height=3)


def destroyer_button(where, frame, rows, columns):
    """ Button to quit the program.

    :param where: Frame where the button will be installed.
    :param rows: Number of the row where the button will be installed.
    :param columns: Number of the column where the button will be installed.
    :return: Creates a widget to quit the program if requested.
    """

    button_destroyer = tk.Button(where, text="EXIT", command=ask_if_quit, font=SMALL_FONT, cursor="dot")
    button_destroyer.grid(row=rows, column=columns, columnspan=1)
    button_destroyer.config(width=5, height=2)


def ask_if_quit():
    """ Button to go ask the user if she is sure to leave the program.
    """

    question = askyesno(title='VMB Venture Capital',
                        message="Thank you for visiting VMB's platform!\n\nAre you sure you want to leave?",
                        icon='warning', default='no')
    if question:
        quit()


def empty_label(where, rows, columns):
    """ Creates an empty label for diagramming.

    :param where: Frame where the label will be installed.
    :param rows: Number of the row where the label will be installed.
    :param columns: Number of the column where the label will be installed.
    :return: Empty label.
    """
    label_empty = tk.Label(where, text=" ", font=LARGE_FONT)
    label_empty.grid(column=columns, row=rows, sticky='news')


def callback(url):
    """  Calls the given url and opens it on a browser.

    :param url: URL of the Explanation of the features.
    :return: Opens the Explanation of the features on the default browser.
    """
    webbrowser.open_new(url)


def link_exp(where, rows, columns):
    """ Creates a button to go to the Explanation of the features.

    :param where: Frame where the button will be installed.
    :param rows: Number of the row where the button will be installed.
    :param columns: Number of the column where the button will be installed.
    :return: A button to open the Explanation of the features document on a browser.
    """
    link = tk.Label(where, text="Feature\nexplanations", fg="blue", cursor="dot", font=SMALL_FONT)
    link.bind("<Button-1>",
              lambda e: callback("https://render.githubusercontent.com/view/pdf?commit=f5502b42dde7a7653d3a42c75ecbb0551a4cfd37&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f43726973746869616e4272756e6f2f70726f5f70726f6a6563742f663535303262343264646537613736353364336134326337356563626230353531613463666433372f4578747261732f466561747572652532304578706c616e6174696f6e732e706466&nwo=CristhianBruno%2Fpro_project&path=Extras%2FFeature+Explanations.pdf&repository_id=264005100&repository_type=Repository#bc595f58-5861-4b32-b4cd-7207682ccf7a"))
    link.grid(columns=columns, row=rows, columnspan=2, sticky='news')


