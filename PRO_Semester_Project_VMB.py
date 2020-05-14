from tkinter import ttk
from PIL import ImageTk, Image
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandastable import Table, config
from VMB_Generators.Pivot_Table_Generator import *
from VMB_Generators.Button_Generator import *
from VMB_Generators.Graph_Generator import *
from VMB_Generators.KeyFacts_Sector_Generator import *
from VMB_Generators.Industry_Selection import *
from VMB_Generators.Model_Generator import *

matplotlib.use("TkAgg")

# Database:
df_base = pd.read_csv("CAX_Preprocessed_PROG.csv")
df_ind = pd.read_csv("GICS_Industry.csv")
df = df_base.merge(df_ind, on='IND')
df_dict = pd.read_csv("CAX_Summary_Sector.csv", index_col="Sector")

# Fonts:
LARGE_FONT = ("Avenir", 14)
LARGE_FONT_B = ("Avenir", 14, 'bold')
NORMAL_FONT = ("Avenir", 12)
SMALL_FONT = ("Avenir", 10)

options = {'rowheight': 32, 'colheadercolor': '#0087a2', 'font': 'Avenir', 'fontsize': 12, 'grid_color': '#dbfff0',
           'rowselectedcolor': '#9be7da', 'cellbackgr': 'white'}

# Create the program:
root = tk.Tk()
root.title("VMB Venture Capital - Investor Platform")

# Define the geometry of the frames:
width_window = 800
height_window = 800

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coord = (screen_width / 2) - (width_window / 2)
y_coord = (screen_height / 2) - (height_window / 2)

root.geometry("%dx%d+%d+%d" %
              (width_window, height_window, x_coord, y_coord))

# Frames: Main structure
main_page = tk.Frame(root)
dashboard = tk.Frame(root)
table_sector = tk.Frame(root)
main_table = tk.Frame(root)
main_graphs1 = tk.Frame(root)
main_graphs2 = tk.Frame(root)
interactive_analysis1 = tk.Frame(root)
interactive_analysis2 = tk.Frame(root)
vmb_model1 = tk.Frame(root)
vmb_model2 = tk.Frame(root)
vmb_model3 = tk.Frame(root)
vmb_model_results = tk.Frame(root)

# Frames: Main per sector
s_CS_main = tk.Frame(root)
s_IT_main = tk.Frame(root)
s_IN_main = tk.Frame(root)
s_UT_main = tk.Frame(root)
s_CD_main = tk.Frame(root)
s_EN_main = tk.Frame(root)
s_FI_main = tk.Frame(root)
s_HE_main = tk.Frame(root)
s_RE_main = tk.Frame(root)

# Frames: Statistics per sector
s_CS_table = tk.Frame(root)
s_IT_table = tk.Frame(root)
s_IN_table = tk.Frame(root)
s_UT_table = tk.Frame(root)
s_CD_table = tk.Frame(root)
s_EN_table = tk.Frame(root)
s_FI_table = tk.Frame(root)
s_HE_table = tk.Frame(root)
s_RE_table = tk.Frame(root)

for frame in (main_page, dashboard, table_sector, interactive_analysis1,
              interactive_analysis2, main_table, main_graphs1, main_graphs2,
              vmb_model1, vmb_model2, vmb_model3, vmb_model_results,
              s_CS_main, s_IT_main, s_IN_main, s_UT_main,
              s_CD_main, s_EN_main, s_FI_main, s_HE_main, s_RE_main,
              s_CS_table, s_IT_table, s_IN_table, s_UT_table,
              s_CD_table, s_EN_table, s_FI_table, s_HE_table, s_RE_table):
    frame.grid(row=0, column=0, columnspan=10, rowspan=10, sticky='news')


def raise_frame(frame_to_call):
    frame_to_call.tkraise()


# -------------------- Main page --------------------

# Title:
title1 = tk.Label(main_page, text="VMB", font=("Avenir", 40))
title1.grid(row=0, column=3)

title2 = tk.Label(main_page, text="Venture Capital", font=("Avenir", 20))
title2.grid(row=0, column=4, sticky='w')

# Profile presentation:
profile_presentation = "We are a Venture Capital fund aimed to connect..."
profile = tk.Label(main_page, text=profile_presentation, font=NORMAL_FONT)
profile.grid(row=1, column=2, columnspan=4)

# Logo

img_path = "VMB_logo.jpg"

image = Image.open(img_path)
image = image.resize((200, 200))
photo = ImageTk.PhotoImage(image)
label = tk.Label(main_page, image=photo)
label.image = photo
label.grid(row=0, column=0, rowspan=2, columnspan=2)
label.config(width=250, height=250)

# Buttons

dashboard_button(main_page, dashboard, 2, 0)
interactive_analysis_button(main_page, interactive_analysis1, 2, 2)
vmb_model_button(main_page, vmb_model1, 2, 4)
destroyer_button(main_page, main_page, 10, 5)

# Key facts:
nr1 = tk.Label(main_page, text="472", font=("Avenir", 50), fg='dodgerblue', anchor='s')
nr1.grid(row=3, column=0, columnspan=2)
nr1.config(width=8, height=2)
fact1 = tk.Label(main_page, text="Companies", font=("Avenir Bold", 20), fg='black', anchor='n')
fact1.grid(row=4, column=0, columnspan=2)

nr2 = tk.Label(main_page, text="21", font=("Avenir", 50), fg='dodgerblue', anchor='s')
nr2.grid(row=3, column=2, columnspan=2)
nr2.config(width=8, height=2)
fact2 = tk.Label(main_page, text="Countries", font=("Avenir Bold", 20), fg='black', anchor='n')
fact2.grid(row=4, column=2, columnspan=2)

nr3 = tk.Label(main_page, text="19", font=("Avenir", 50), fg='dodgerblue', anchor='s')
nr3.grid(row=3, column=4, columnspan=2)
nr3.config(width=8, height=2)
fact3 = tk.Label(main_page, text="Industries", font=("Avenir Bold", 20), fg='black', anchor='n')
fact3.grid(row=4, column=4, columnspan=2)

nr4 = tk.Label(main_page, text="USD 2bn", font=("Avenir", 40), fg='dodgerblue', anchor='s')
nr4.grid(row=5, column=0, columnspan=2)
nr4.config(width=8, height=2)
fact4 = tk.Label(main_page, text="Last funding\nround amount", font=("Avenir Bold", 20), fg='black', anchor='n')
fact4.grid(row=6, column=0, columnspan=2)

nr5 = tk.Label(main_page, text="654", font=("Avenir", 50), fg='dodgerblue', anchor='s')
nr5.grid(row=5, column=2, columnspan=2)
nr5.config(width=8, height=2)
fact5 = tk.Label(main_page, text="Seed Investors", font=("Avenir Bold", 20), fg='black', anchor='n')
fact5.grid(row=6, column=2, columnspan=2)

nr6 = tk.Label(main_page, text="244", font=("Avenir", 50), fg='dodgerblue', anchor='s')
nr6.grid(row=5, column=4, columnspan=2)
nr6.config(width=8, height=2)
fact6 = tk.Label(main_page, text="Angel and VC\nInvestors", font=("Avenir Bold", 20), fg='black', anchor='n')
fact6.grid(row=6, column=4, columnspan=2)

# -------------------- Dashboard --------------------

label = tk.Label(dashboard, text="Dashboard", font=('Avenir', 40))
label.grid(row=0, column=0, columnspan=10)

# Buttons:

main_page_button(dashboard, main_page, 1, 0)
interactive_analysis_button(dashboard, interactive_analysis1, 1, 2)
vmb_model_button(dashboard, vmb_model1, 1, 4)
destroyer_button(dashboard, main_page, 10, 8)
main_table_button(dashboard, main_table, 5, 1)
main_graphs_button(dashboard, main_graphs1, 5, 3)

# Graph Main: Pie per GSE
figure_main = Graph_Main(df)
bar_main = FigureCanvasTkAgg(figure_main, dashboard)
bar_main.get_tk_widget().grid(row=4, column=0, columnspan=6)

# -------------------- Main Table --------------------

dashboard_button(main_table, dashboard, 0, 11)
destroyer_button(main_table, main_page, 1, 11)

pt = Table(main_table, dataframe=PT_Main(df), showtoolbar=False,
           showstatusbar=True, editable=False, enable_menus=True)
pt.contractColumns()
pt.sortTable(1, ascending=0)
config.load_options()
config.apply_options(options, pt)
pt.show()

# -------------------- Main Graph 1 --------------------

label = tk.Label(main_graphs1, text="Dashboard", font=('Avenir', 40))
label.grid(row=0, column=2, columnspan=8)

dashboard_button(main_graphs1, dashboard, 0, 0)
destroyer_button(main_graphs1, main_page, 5, 11)
empty_label(main_graphs1, 3, 0)
empty_label(main_graphs1, 4, 0)
graphs2_button(main_graphs1, main_graphs2, 5, 0)

# Graph 1: Status by year of foundation
figure1 = Graph_Main1(df)
bar1 = FigureCanvasTkAgg(figure1, main_graphs1)
bar1.get_tk_widget().grid(row=1, column=0, columnspan=6)

# Graph 2: Countries
figure2 = Graph_Main2(df)
bar2 = FigureCanvasTkAgg(figure2, main_graphs1)
bar2.get_tk_widget().grid(row=1, column=6, columnspan=6)

# Graph 3: Status if worked on top companies
figure3 = Graph_Main3(df)
bar3 = FigureCanvasTkAgg(figure3, main_graphs1)
bar3.get_tk_widget().grid(row=2, column=0, columnspan=6)

# Graph 4: Invested through incubators
figure4 = Graph_Main4(df)
bar4 = FigureCanvasTkAgg(figure4, main_graphs1)
bar4.get_tk_widget().grid(row=2, column=6, columnspan=6)

# -------------------- Main Graph 2 --------------------

label = tk.Label(main_graphs2, text="Dashboard", font=('Avenir', 40))
label.grid(row=0, column=2, columnspan=8)

dashboard_button(main_graphs2, dashboard, 0, 0)
destroyer_button(main_graphs2, main_page, 5, 11)
empty_label(main_graphs2, 3, 0)
empty_label(main_graphs2, 4, 0)
graphs1_button(main_graphs2, main_graphs1, 5, 0)

# Graph 5: Average Experience by Status
figure1 = Graph_Main5(df)
bar1 = FigureCanvasTkAgg(figure1, main_graphs2)
bar1.get_tk_widget().grid(row=1, column=0, columnspan=6)

# Graph 6: Difficulty of obtaining workforce
figure2 = Graph_Main6(df)
bar2 = FigureCanvasTkAgg(figure2, main_graphs2)
bar2.get_tk_widget().grid(row=1, column=6, columnspan=6)

# Graph 7: Barries of entry to industry by status
figure4 = Graph_Main7(df)
bar4 = FigureCanvasTkAgg(figure4, main_graphs2)
bar4.get_tk_widget().grid(row=2, column=0, columnspan=6)

# Graph 8: Funding per number of investors and advisors
figure3 = Graph_Main8(df)
bar3 = FigureCanvasTkAgg(figure3, main_graphs2)
bar3.get_tk_widget().grid(row=2, column=6, columnspan=6)

# -------------------- Analysis per Sector 1 --------------------

label = tk.Label(interactive_analysis1, text="Analysis per Sector", font=('Avenir', 40))
label.grid(row=0, column=0, columnspan=10)

# Buttons:
main_page_button(interactive_analysis1, main_page, 1, 0)
dashboard_button(interactive_analysis1, dashboard, 1, 2)
vmb_model_button(interactive_analysis1, vmb_model1, 1, 4)
destroyer_button(interactive_analysis1, main_page, 5, 7)
graphs2_button(interactive_analysis1, interactive_analysis2, 5, 0)

# Graph Sector 1: Pie chart by GSE

figure_sector_GSE = Graph_Sector_Pie(df)

pie_sector = FigureCanvasTkAgg(figure_sector_GSE, interactive_analysis1)
pie_sector.get_tk_widget().grid(row=2, column=0, columnspan=6)

# -------------------- Analysis per Sector 2 --------------------

label = tk.Label(interactive_analysis2, text="Analysis per Sector", font=('Avenir', 40))
label.grid(row=0, column=0, columnspan=10)

# Buttons:
main_page_button(interactive_analysis2, main_page, 1, 0)
dashboard_button(interactive_analysis2, dashboard, 1, 2)
vmb_model_button(interactive_analysis2, vmb_model1, 1, 4)
destroyer_button(interactive_analysis2, main_page, 8, 8)
graphs1_button(interactive_analysis2, interactive_analysis1, 6, 0)

# Menu to select industry:
OptionList = list(df['GSE'].drop_duplicates().sort_values().iloc[:-1])

label_selector = tk.Label(interactive_analysis2, text="Choose a sector:", font=LARGE_FONT, height=3)
label_selector.grid(column=0, row=3, columnspan=2, sticky='e')

cb_sector = ttk.Combobox(interactive_analysis2, values=OptionList, width=30, state='readonly', font=LARGE_FONT)
cb_sector.grid(column=2, row=3, columnspan=2)
cb_sector.set('Sector')


def getInput():
    selection = cb_sector.get()
    l2.configure(text='Go to sector: \n%s' % selection)
    sector_main_button(interactive_analysis2, sector_selector(), 6, 2)


b = tk.Button(interactive_analysis2, text="Submit", command=getInput)
b.grid(column=4, row=3, columnspan=2, sticky='w')

empty_label(interactive_analysis2, 5, 0)
empty_label(interactive_analysis2, 5, 2)

l2 = tk.Label(interactive_analysis2, text='', font=('Avenir', 14))
l2.grid(column=2, row=4, columnspan=2)


def sector_selector():
    go = dashboard
    selection = str(cb_sector.get())
    if selection == 'Communication Services':
        go = s_CS_main
    elif selection == 'Information Technology':
        go = s_IT_main
    elif selection == 'Industrials':
        go = s_IN_main
    elif selection == 'Utilities':
        go = s_UT_main
    elif selection == 'Consumer Discretionary':
        go = s_CD_main
    elif selection == 'Energy':
        go = s_EN_main
    elif selection == 'Financials':
        go = s_FI_main
    elif selection == 'Health Care':
        go = s_HE_main
    elif selection == 'Real Estate':
        go = s_RE_main
    return go


# Graph Sector 2: Barh of funding (FUN) per GSE

figure_sector_FUN = Graph_Sector_Barh(df)

barh_FUN = FigureCanvasTkAgg(figure_sector_FUN, interactive_analysis2)
barh_FUN.get_tk_widget().grid(row=2, column=0, columnspan=6)

# -------------------- Profile sector s_CS --------------------

sector_CS = "Communication Services"

label = tk.Label(s_CS_main, text="Sector: %s" % sector_CS, font=('Avenir', 40))
label.grid(row=0, column=0, columnspan=10)

interactive_analysis_button(s_CS_main, interactive_analysis2, 8, 1)
sector_table_button(s_CS_main, s_CS_table, 8, 3)
destroyer_button(s_CS_main, main_page, 8, 8)
empty_label(s_CS_main, 7, 1)

# Graph Sector: Funding per subindustry

figure_sector_CS = Graph_Sector_1(df, sector_CS)

barh_sector_CS = FigureCanvasTkAgg(figure_sector_CS, s_CS_main)
barh_sector_CS.get_tk_widget().grid(row=1, column=0, columnspan=6)

# Key facts:

KeyFacts_Sector(sector_CS, df_dict, s_CS_main)

# -------------------- Table sector s_CS --------------------

interactive_analysis_button(s_CS_table, interactive_analysis2, 0, 11)
sector_profile_button(s_CS_table, s_CS_main, 1, 11)
destroyer_button(s_CS_table, main_page, 2, 11)

pt = Table(s_CS_table, dataframe=PT_Sector(df, sector_CS), height=100, showtoolbar=False,
           showstatusbar=True, editable=False, enable_menus=True)
pt.contractColumns()
pt.sortTable(1, ascending=0)
config.load_options()
config.apply_options(options, pt)
pt.show()

# -------------------- Profile sector s_IT --------------------

sector_IT = "Information Technology"

label = tk.Label(s_IT_main, text="Sector: %s" % sector_IT, font=('Avenir', 40))
label.grid(row=0, column=0, columnspan=10)

interactive_analysis_button(s_IT_main, interactive_analysis2, 8, 1)
sector_table_button(s_IT_main, s_IT_table, 8, 3)
destroyer_button(s_IT_main, main_page, 8, 8)
empty_label(s_IT_main, 7, 1)

# Graph Sector: Funding per subindustry

figure_sector_IT = Graph_Sector_1(df, sector_IT)

barh_sector_IT = FigureCanvasTkAgg(figure_sector_IT, s_IT_main)
barh_sector_IT.get_tk_widget().grid(row=1, column=0, columnspan=6)

# Key facts:

KeyFacts_Sector(sector_IT, df_dict, s_IT_main)

# -------------------- Table sector s_IT --------------------

interactive_analysis_button(s_IT_table, interactive_analysis2, 0, 11)
sector_profile_button(s_IT_table, s_IT_main, 1, 11)
destroyer_button(s_IT_table, main_page, 2, 11)

pt = Table(s_IT_table, dataframe=PT_Sector(df, sector_IT), showtoolbar=False,
           showstatusbar=True, editable=False, enable_menus=True)
pt.contractColumns()
pt.sortTable(1, ascending=0)
config.load_options()
config.apply_options(options, pt)
pt.show()

# -------------------- Profile sector s_IN --------------------

sector_IN = 'Industrials'

label = tk.Label(s_IN_main, text="Sector: %s" % sector_IN, font=('Avenir', 40))
label.grid(row=0, column=0, columnspan=10)

interactive_analysis_button(s_IN_main, interactive_analysis2, 8, 1)
sector_table_button(s_IN_main, s_IN_table, 8, 3)
destroyer_button(s_IN_main, main_page, 8, 8)
empty_label(s_IN_main, 7, 1)

# Graph Sector: Funding per subindustry

figure_sector_IN = Graph_Sector_1(df, sector_IN)

barh_sector_IN = FigureCanvasTkAgg(figure_sector_IN, s_IN_main)
barh_sector_IN.get_tk_widget().grid(row=1, column=0, columnspan=6)

# Key facts:

KeyFacts_Sector(sector_IN, df_dict, s_IN_main)

# -------------------- Table sector s_IN --------------------

interactive_analysis_button(s_IN_table, interactive_analysis2, 0, 11)
sector_profile_button(s_IN_table, s_IN_main, 1, 11)
destroyer_button(s_IN_table, main_page, 2, 11)

pt = Table(s_IN_table, dataframe=PT_Sector(df, sector_IN), showtoolbar=False,
           showstatusbar=True, editable=False, enable_menus=True)
pt.contractColumns()
pt.sortTable(1, ascending=0)
config.load_options()
config.apply_options(options, pt)
pt.show()

# -------------------- Profile sector s_UT --------------------

sector_UT = 'Utilities'

label = tk.Label(s_UT_main, text="Sector: %s" % sector_UT, font=('Avenir', 40))
label.grid(row=0, column=0, columnspan=10)

interactive_analysis_button(s_UT_main, interactive_analysis2, 8, 1)
sector_table_button(s_UT_main, s_UT_table, 8, 3)
destroyer_button(s_UT_main, main_page, 8, 8)
empty_label(s_UT_main, 7, 1)

# Graph Sector: Funding per subindustry

figure_sector_UT = Graph_Sector_1(df, sector_UT)

barh_sector_UT = FigureCanvasTkAgg(figure_sector_UT, s_UT_main)
barh_sector_UT.get_tk_widget().grid(row=1, column=0, columnspan=6)

# Key facts:

KeyFacts_Sector(sector_UT, df_dict, s_UT_main)

# -------------------- Table sector s_UT --------------------

interactive_analysis_button(s_UT_table, interactive_analysis2, 0, 11)
sector_profile_button(s_UT_table, s_UT_main, 1, 11)
destroyer_button(s_UT_table, main_page, 2, 11)

pt = Table(s_UT_table, dataframe=PT_Sector(df, sector_UT), showtoolbar=False,
           showstatusbar=True, editable=False, enable_menus=True)
pt.contractColumns()
pt.sortTable(1, ascending=0)
config.load_options()
config.apply_options(options, pt)
pt.show()

# -------------------- Profile sector s_CD --------------------

sector_CD = 'Consumer Discretionary'

label = tk.Label(s_CD_main, text="Sector: %s" % sector_CD, font=('Avenir', 40))
label.grid(row=0, column=0, columnspan=10)

interactive_analysis_button(s_CD_main, interactive_analysis2, 8, 1)
sector_table_button(s_CD_main, s_CD_table, 8, 3)
destroyer_button(s_CD_main, main_page, 8, 8)
empty_label(s_CD_main, 7, 1)

# Graph Sector: Funding per subindustry

figure_sector_CD = Graph_Sector_1(df, sector_CD)

barh_sector_CD = FigureCanvasTkAgg(figure_sector_CD, s_CD_main)
barh_sector_CD.get_tk_widget().grid(row=1, column=0, columnspan=6)

# Key facts:

KeyFacts_Sector(sector_CD, df_dict, s_CD_main)

# -------------------- Table sector s_CD --------------------

interactive_analysis_button(s_CD_table, interactive_analysis2, 0, 10)
sector_profile_button(s_CD_table, s_CD_main, 1, 11)
destroyer_button(s_CD_table, main_page, 2, 11)

pt = Table(s_CD_table, dataframe=PT_Sector(df, sector_CD), showtoolbar=False,
           showstatusbar=True, editable=False, enable_menus=True)
pt.contractColumns()
pt.sortTable(1, ascending=0)
config.load_options()
config.apply_options(options, pt)
pt.show()

# -------------------- Profile sector s_EN --------------------

sector_EN = 'Energy'

label = tk.Label(s_EN_main, text="Sector: %s" % sector_EN, font=('Avenir', 40))
label.grid(row=0, column=0, columnspan=10)

interactive_analysis_button(s_EN_main, interactive_analysis2, 8, 1)
sector_table_button(s_EN_main, s_EN_table, 8, 3)
destroyer_button(s_EN_main, main_page, 8, 8)
empty_label(s_EN_main, 7, 1)

# Graph Sector: Funding per subindustry

figure_sector_EN = Graph_Sector_1(df, sector_EN)

barh_sector_EN = FigureCanvasTkAgg(figure_sector_EN, s_EN_main)
barh_sector_EN.get_tk_widget().grid(row=1, column=0, columnspan=6)

# Key facts:

KeyFacts_Sector(sector_EN, df_dict, s_EN_main)

# -------------------- Table sector s_EN --------------------

interactive_analysis_button(s_EN_table, interactive_analysis2, 0, 11)
sector_profile_button(s_EN_table, s_EN_main, 1, 11)
destroyer_button(s_EN_table, main_page, 2, 11)

pt = Table(s_EN_table, dataframe=PT_Sector(df, sector_EN), showtoolbar=False,
           showstatusbar=True, editable=False, enable_menus=True)
pt.contractColumns()
pt.sortTable(1, ascending=0)
config.load_options()
config.apply_options(options, pt)
pt.show()

# -------------------- Profile sector s_FI --------------------

sector_FI = 'Financials'

label = tk.Label(s_FI_main, text="Sector: %s" % sector_FI, font=('Avenir', 40))
label.grid(row=0, column=0, columnspan=10)

interactive_analysis_button(s_FI_main, interactive_analysis2, 8, 1)
sector_table_button(s_FI_main, s_FI_table, 8, 3)
destroyer_button(s_FI_main, main_page, 8, 8)
empty_label(s_FI_main, 7, 1)

# Graph Sector: Funding per subindustry

figure_sector_FI = Graph_Sector_1(df, sector_FI)

barh_sector_FI = FigureCanvasTkAgg(figure_sector_FI, s_FI_main)
barh_sector_FI.get_tk_widget().grid(row=1, column=0, columnspan=6)

# Key facts:

KeyFacts_Sector(sector_FI, df_dict, s_FI_main)

# -------------------- Table sector s_FI --------------------

interactive_analysis_button(s_FI_table, interactive_analysis2, 0, 11)
sector_profile_button(s_FI_table, s_FI_main, 1, 11)
destroyer_button(s_FI_table, main_page, 2, 11)

sector_FI = 'Financials'

pt = Table(s_FI_table, dataframe=PT_Sector(df, sector_FI), showtoolbar=False,
           showstatusbar=True, editable=False, enable_menus=True)
pt.contractColumns()
pt.sortTable(1, ascending=0)
config.load_options()
config.apply_options(options, pt)
pt.show()

# -------------------- Profile sector s_HE --------------------

sector_HE = 'Health Care'

label = tk.Label(s_HE_main, text="Sector: %s" % sector_HE, font=('Avenir', 40))
label.grid(row=0, column=0, columnspan=10)

interactive_analysis_button(s_HE_main, interactive_analysis2, 8, 1)
sector_table_button(s_HE_main, s_HE_table, 8, 3)
destroyer_button(s_HE_main, main_page, 8, 8)
empty_label(s_HE_main, 7, 1)

# Graph Sector: Funding per subindustry

figure_sector_HE = Graph_Sector_1(df, sector_HE)

barh_sector_HE = FigureCanvasTkAgg(figure_sector_HE, s_HE_main)
barh_sector_HE.get_tk_widget().grid(row=1, column=0, columnspan=6)

# Key facts:

KeyFacts_Sector(sector_HE, df_dict, s_HE_main)

# -------------------- Table sector s_HE --------------------

interactive_analysis_button(s_HE_table, interactive_analysis2, 0, 11)
sector_profile_button(s_HE_table, s_HE_main, 1, 11)
destroyer_button(s_HE_table, main_page, 2, 11)

pt = Table(s_HE_table, dataframe=PT_Sector(df, sector_HE), showtoolbar=False,
           showstatusbar=True, editable=False, enable_menus=True)
pt.contractColumns()
pt.sortTable(1, ascending=0)
config.load_options()
config.apply_options(options, pt)
pt.show()

# -------------------- Profile sector s_RE --------------------

sector_RE = 'Real Estate'

label = tk.Label(s_RE_main, text="Sector: %s" % sector_RE, font=('Avenir', 40))
label.grid(row=0, column=0, columnspan=10)

interactive_analysis_button(s_RE_main, interactive_analysis2, 8, 1)
sector_table_button(s_RE_main, s_RE_table, 8, 3)
destroyer_button(s_RE_main, main_page, 8, 8)
empty_label(s_RE_main, 7, 1)

# Graph Sector: Funding per subindustry

figure_sector_RE = Graph_Sector_RE(df, sector_RE)

barh_sector_RE = FigureCanvasTkAgg(figure_sector_RE, s_RE_main)
barh_sector_RE.get_tk_widget().grid(row=1, column=0, columnspan=6)

# Key facts:

KeyFacts_Sector(sector_RE, df_dict, s_RE_main)

# -------------------- Table sector s_RE --------------------

interactive_analysis_button(s_RE_table, interactive_analysis2, 0, 11)
sector_profile_button(s_RE_table, s_RE_main, 1, 11)
destroyer_button(s_RE_table, main_page, 2, 11)

pt = Table(s_RE_table, dataframe=PT_RE_sector(df, sector_RE), showtoolbar=False,
           showstatusbar=True, editable=False, enable_menus=True)
pt.contractColumns()
pt.sortTable(1, ascending=0)
config.load_options()
config.apply_options(options, pt)
pt.show()

# -------------------- VMB Model Page 1 --------------------
label = tk.Label(vmb_model1, text="VMB Model", font=('Avenir', 40))
label.grid(row=0, column=0, columnspan=10)

# Buttons:

main_page_button(vmb_model1, main_page, 1, 0)
dashboard_button(vmb_model1, dashboard, 1, 4)
interactive_analysis_button(vmb_model1, interactive_analysis1, 1, 8)
destroyer_button(vmb_model1, main_page, 11, 11)
link_exp(vmb_model1, 11, 1)

feature_explanation = '  VMB Venture Capital developed a tool to forecast if a startup is to be successful based on' \
                      'a series of features. The model takes 12 features\n' \
                      '  divided in four categories: Industry, Experience of the cofounders team, Market ' \
                      'characteristics, and Business model.\n' \
                      '  A deeper explanation of the features in provided in the link at the bottom of the page.' \
                      '  This model is meant to connect investors and potentially successful startups, and finally ' \
                      'generate a more efficient capital allocation.\n' \
                      '  For the entrepreneur: We invite you to submit your information to receive the forecast. ' \
                      'This way you can see in which topics you must focus\n' \
                      '  on and improve your chance of success! Keep on because your next investor may be watching!'

exp_features = tk.Label(vmb_model1, text=feature_explanation, font=NORMAL_FONT, justify='left', anchor='nw')
exp_features.grid(row=2, column=0, columnspan=10, sticky='nsew')
exp_features.config(width=60, height=5)

title_sector = tk.Label(vmb_model1, text="Model features: Industry", font=('Avenir', 20, 'bold'))
title_sector.grid(row=3, column=0, columnspan=10, sticky='nsew')
title_sector.config(width=60, height=2)

list_sectors = ['Communication Services', 'Information Technology', 'Industrials', 'Utilities',
                'Consumer Discretionary', 'Energy', 'Financials', 'Health Care', 'Real Estate']


def vmb_model_inputs_sector(*args):
    cb_input_subindustry.config(values=Get_Subindustry(cb_input_sector.get()))


def vmb_model_inputs_subindustry(*args):
    cb_input_activity.config(values=Get_Activities(cb_input_subindustry.get()))


def vmb_model_inputs_activity(*args):
    sector = cb_input_sector.get()
    subindustry = cb_input_subindustry.get()
    activity = cb_input_activity.get()
    if sector == 'Sector' or subindustry == 'Subindustry' or activity == 'Activity':
        label_inputs_activity1.configure(text='Please submit your')
        label_inputs_activity2.configure(text='information correctly')
    else:
        label_inputs_activity1.configure(text='Sector:\n'
                                              'Subindustry:\n'
                                              'Activity:')
        label_inputs_activity2.configure(text='%s\n'
                                              '%s\n'
                                              '%s' %
                                              (sector, subindustry, activity))
        model_continue_button(vmb_model1, vmb_model2, 11, 4)


# Selector: Sector
label_sector_selector = tk.Label(vmb_model1, text="Choose a sector: ", font=LARGE_FONT, height=3)
label_sector_selector.grid(column=1, row=4, columnspan=2, sticky='e')

cb_input_sector = ttk.Combobox(vmb_model1, values=list_sectors, width=30, state='readonly', font=LARGE_FONT)
cb_input_sector.grid(column=3, row=4, columnspan=6, sticky='ew')
cb_input_sector.bind("<<ComboboxSelected>>", vmb_model_inputs_sector)
cb_input_sector.set('Sector')

# Selector: Subindustry
list_subindustry = Get_Subindustry(cb_input_sector.get())

label_subindustry_selector = tk.Label(vmb_model1, text="Choose a subindustry: ", font=LARGE_FONT, height=3)
label_subindustry_selector.grid(column=1, row=5, columnspan=2, sticky='e')

cb_input_subindustry = ttk.Combobox(vmb_model1, values=list_subindustry, width=30, state='readonly', font=LARGE_FONT)
cb_input_subindustry.grid(column=3, row=5, columnspan=6, sticky='ew')
cb_input_subindustry.bind("<<ComboboxSelected>>", vmb_model_inputs_subindustry)
cb_input_subindustry.set('Subindustry')

# Selector: Activity (var4 - IND)
list_activities = Get_Activities(cb_input_subindustry.get())

label_activities_selector = tk.Label(vmb_model1, text="Choose an activity: ", font=LARGE_FONT, height=3)
label_activities_selector.grid(column=1, row=6, columnspan=2, sticky='e')

cb_input_activity = ttk.Combobox(vmb_model1, values=list_activities, width=30, state='readonly', font=LARGE_FONT)
cb_input_activity.grid(column=3, row=6, columnspan=6, sticky='ew')
cb_input_activity.set('Activity')

submit_activity = tk.Button(vmb_model1, text="Submit", command=vmb_model_inputs_activity)
submit_activity.grid(column=4, row=8, columnspan=2)

label_inputs_activity1 = tk.Label(vmb_model1, text='', font=LARGE_FONT, justify='right')
label_inputs_activity1.grid(column=0, row=10, columnspan=5, sticky='e')

label_inputs_activity2 = tk.Label(vmb_model1, text='', font=LARGE_FONT_B, justify='left')
label_inputs_activity2.grid(column=5, row=10, columnspan=5, sticky='w')

empty_space = tk.Label(vmb_model1, text="-", fg='white')
empty_space.grid(row=12, column=0, columnspan=10, sticky='nsew')
empty_space.config(width=60, height=2)


# -------------------- VMB Model Page 2 --------------------
label = tk.Label(vmb_model2, text="VMB Model", font=('Avenir', 40))
label.grid(row=0, column=0, columnspan=10)

# Buttons:

main_page_button(vmb_model2, main_page, 1, 0)
dashboard_button(vmb_model2, dashboard, 1, 4)
interactive_analysis_button(vmb_model2, interactive_analysis1, 1, 8)
destroyer_button(vmb_model2, main_page, 14, 12)
link_exp(vmb_model2, 14, 1)

title_team = tk.Label(vmb_model2, text="Model features: Experience of the team", font=('Avenir', 20, 'bold'))
title_team.grid(row=3, column=0, columnspan=10, sticky='nsew')
title_team.config(width=60, height=2)

rb_AYE = tk.StringVar(vmb_model2)
rb_BIG = tk.StringVar(vmb_model2)
rb_SUR = tk.StringVar(vmb_model2)
rb_INC = tk.StringVar(vmb_model2)

dict_AYE = {'High': 0, 'Medium': 2, 'Low': 1}
keys_AYE = list(dict_AYE.keys())
values_AYE = list(dict_AYE.values())

dict_BIG = {'Yes': 1, 'No': 0}
keys_BIG = list(dict_BIG.keys())
values_BIG = list(dict_BIG.values())

dict_SUR = {'Yes': 2, 'No': 0, 'Not Applicable': 1}
keys_SUR = list(dict_SUR.keys())
values_SUR = list(dict_SUR.values())

dict_INC = {'Yes': 1, 'No': 0}
keys_INC = list(dict_INC.keys())
values_INC = list(dict_INC.values())

dict_REC = {'Low (0 to 150)': 0, 'Medium (150 to 300)': 1, 'High (300 to 450)': 2, 'Highest (more than 450)': 3}
keys_REC = list(dict_REC.keys())
values_REC = list(dict_REC.values())


def get_AYE(*args):
    input_AYE = rb_AYE.get()
    return input_AYE


def get_BIG(*args):
    input_BIG = rb_BIG.get()
    return input_BIG


def get_SUR(*args):
    input_SUR = rb_SUR.get()
    return input_SUR


def get_INC(*args):
    input_INC = rb_INC.get()
    return input_INC


def get_REC(*args):
    input_REC = cb_REC.get()
    return input_REC


def vmb_model_inputs_team(*args):
    REC = cb_REC.get()
    if REC == 'Recognitions':
        label_inputs_team1.configure(text='Please submit your ')
        label_inputs_team2.configure(text='information correctly')
    else:
        try:
            AYE = keys_AYE[int(rb_AYE.get())]
            BIG = keys_BIG[int(rb_BIG.get())]
            SUR = keys_SUR[int(rb_SUR.get())]
            INC = keys_INC[int(rb_INC.get())]
            label_inputs_team1.configure(text='Level of experience:\n'
                                         'Experience on Big 5:\n'
                                         'Survived a recession:\n'
                                         'Invested through incubator:\n'
                                         'Number of recognitions:')
            label_inputs_team2.configure(text='%s\n'
                                              '%s\n'
                                              '%s\n'
                                              '%s\n'
                                              '%s' % (AYE, BIG, SUR, INC, REC))
            model_continue_button(vmb_model2, vmb_model3, 14, 4)
        except ValueError:
            label_inputs_team1.configure(text='Please submit your ')
            label_inputs_team2.configure(text='information correctly')


# Selector: Range of years of experience of cofounders (var1 - AYE)
label_AYE = tk.Label(vmb_model2, text="Level of relevant\n experience of cofounders", font=LARGE_FONT, height=3)
label_AYE.grid(column=0, row=4, columnspan=2, rowspan=3, sticky='nsew')

rb_AYE1 = tk.Radiobutton(vmb_model2, text=keys_AYE[0], variable=rb_AYE, value=0, command=get_AYE)
rb_AYE2 = tk.Radiobutton(vmb_model2, text=keys_AYE[1], variable=rb_AYE, value=1, command=get_AYE)
rb_AYE3 = tk.Radiobutton(vmb_model2, text=keys_AYE[2], variable=rb_AYE, value=2, command=get_AYE)
rb_AYE1.grid(row=4, column=3, sticky='w')
rb_AYE2.grid(row=5, column=3, sticky='w')
rb_AYE3.grid(row=6, column=3, sticky='w')

# Selector: Experience on Big 5 Consulting Firms (var2 - BIG)
label_BIG = tk.Label(vmb_model2, text="Cofounders have previous\nexperience on one of \nBig 5 Consulting firms?",
                     font=LARGE_FONT, height=3)
label_BIG.grid(column=6, row=4, columnspan=2, rowspan=2, sticky='nsew')

rb_BIG1 = tk.Radiobutton(vmb_model2, text=keys_BIG[0], variable=rb_BIG, value=0, command=get_BIG)
rb_BIG2 = tk.Radiobutton(vmb_model2, text=keys_BIG[1], variable=rb_BIG, value=1, command=get_BIG)
rb_BIG1.grid(row=4, column=9, sticky='w')
rb_BIG2.grid(row=5, column=9, sticky='w')

empty_space = tk.Label(vmb_model2, text="-", fg='white')
empty_space.grid(row=7, column=0, columnspan=10, sticky='nsew')
empty_space.config(width=60, height=2)

# Selector: Previous startup had survived recession period (var9 - SUR)
label_SUR = tk.Label(vmb_model2, text="Its previous startup\nhad survived a recession\nperiod?",
                     font=LARGE_FONT, height=3)
label_SUR.grid(column=6, row=8, columnspan=2, rowspan=3, sticky='nsew')

rb_SUR1 = tk.Radiobutton(vmb_model2, text=keys_SUR[0], variable=rb_SUR, value=0, command=get_SUR)
rb_SUR2 = tk.Radiobutton(vmb_model2, text=keys_SUR[1], variable=rb_SUR, value=1, command=get_SUR)
rb_SUR3 = tk.Radiobutton(vmb_model2, text=keys_SUR[2], variable=rb_SUR, value=2, command=get_SUR)
rb_SUR1.grid(row=8, column=9, sticky='w')
rb_SUR2.grid(row=9, column=9, sticky='w')
rb_SUR3.grid(row=10, column=9, sticky='w')


# Selector: Invested through global incubator competition (var11 - INC)
label_INC = tk.Label(vmb_model2, text="Startup received\ninvestments through an\nincubator competition?",
                     font=LARGE_FONT, height=3)
label_INC.grid(column=0, row=8, columnspan=2, rowspan=2, sticky='nsew')

rb_INC1 = tk.Radiobutton(vmb_model2, text=keys_INC[0], variable=rb_INC, value=0, command=get_INC)
rb_INC2 = tk.Radiobutton(vmb_model2, text=keys_INC[1], variable=rb_INC, value=1, command=get_INC)
rb_INC1.grid(row=8, column=3, sticky='w')
rb_INC2.grid(row=9, column=3, sticky='w')


# Selector: Number of recognitions to cofounders (var8 - REC)
label_REC = tk.Label(vmb_model2, text="Number of recognitions\nto cofounders", font=LARGE_FONT, height=3)
label_REC.grid(column=2, row=11, columnspan=2, sticky='nse')

cb_REC = ttk.Combobox(vmb_model2, values=keys_REC, width=30, state='readonly', font=LARGE_FONT)
cb_REC.grid(column=4, row=11, columnspan=6)
cb_REC.set('Recognitions')

submit_team = tk.Button(vmb_model2, text="Submit", command=vmb_model_inputs_team)
submit_team.grid(column=4, row=12, columnspan=2)

label_inputs_team1 = tk.Label(vmb_model2, text='', font=LARGE_FONT, justify='right')
label_inputs_team1.grid(column=0, row=13, columnspan=5, sticky='e')

label_inputs_team2 = tk.Label(vmb_model2, text='', font=LARGE_FONT_B, justify='left')
label_inputs_team2.grid(column=5, row=13, columnspan=5, sticky='w')


# -------------------- VMB Model Page 3 --------------------
label = tk.Label(vmb_model3, text="VMB Model", font=('Avenir', 40))
label.grid(row=0, column=0, columnspan=10)

# Buttons:

main_page_button(vmb_model3, main_page, 1, 0)
dashboard_button(vmb_model3, dashboard, 1, 4)
interactive_analysis_button(vmb_model3, interactive_analysis1, 1, 8)
destroyer_button(vmb_model3, main_page, 14, 9)
link_exp(vmb_model3, 14, 1)

title_market = tk.Label(vmb_model3, text="Model features: Market characteristics", font=('Avenir', 20, 'bold'))
title_market.grid(row=2, column=0, columnspan=10, sticky='nsew')
title_market.config(width=60, height=2)

title_bm = tk.Label(vmb_model3, text="Model features: Business Model", font=('Avenir', 20, 'bold'))
title_bm.grid(row=7, column=0, columnspan=10, sticky='nsew')
title_bm.config(width=60, height=2)

rb_BAR = tk.StringVar(vmb_model3)
rb_DWF = tk.StringVar(vmb_model3)
rb_PST = tk.StringVar(vmb_model3)
rb_CDA = tk.StringVar(vmb_model3)
rb_MLB = tk.StringVar(vmb_model3)

dict_BAR = {'Yes': 1, 'No': 0}
keys_BAR = list(dict_BAR.keys())
values_BAR = list(dict_BAR.values())

dict_DWF = {'High': 0, 'Medium': 2, 'Low': 1}
keys_DWF = list(dict_DWF.keys())
values_DWF = list(dict_DWF.values())

dict_PST = {'Yes': 1, 'No': 0}
keys_PST = list(dict_PST.keys())
values_PST = list(dict_PST.values())

dict_CDA = {'Yes': 1, 'No': 0}
keys_CDA = list(dict_CDA.keys())
values_CDA = list(dict_CDA.values())

dict_MLB = {'Yes': 1, 'No': 0}
keys_MLB = list(dict_MLB.keys())
values_MLB = list(dict_MLB.values())

dict_CPB = {'Platform': 3, 'Cloud': 1, 'Both': 0, 'None': 2}
keys_CPB = list(dict_CPB.keys())
values_CPB = list(dict_CPB.values())


def get_BAR(*args):
    input_BAR = rb_BAR.get()
    return input_BAR


def get_DWF(*args):
    input_DWF = rb_DWF.get()
    return input_DWF


def get_PST(*args):
    input_PST = rb_PST.get()
    return input_PST


def get_CDA(*args):
    input_CDA = rb_CDA.get()
    return input_CDA


def get_MLB(*args):
    input_MLB = rb_MLB.get()
    return input_MLB


def get_CPB(*args):
    input_CPB = cb_CPB.get()
    return input_CPB


def vmb_model_inputs_business(*args):
    CPB = cb_CPB.get()
    if CPB == 'Base':
        label_inputs_business1.configure(text='Please submit your ')
        label_inputs_business2.configure(text='information correctly')
    else:
        try:
            BAR = keys_BAR[int(rb_BAR.get())]
            DWF = keys_DWF[int(rb_DWF.get())]
            PST = keys_PST[int(rb_PST.get())]
            CDA = keys_CDA[int(rb_CDA.get())]
            MLB = keys_MLB[int(rb_MLB.get())]
            label_inputs_business1.configure(text='Barriers of entry:\n'
                                             'Difficulty of obtaining workforce:\n'
                                             'Pricing strategy:\n'
                                             'Focus on consumer data:\n'
                                             'Machine Learning based:\n'
                                             'Cloud or platform based:')
            label_inputs_business2.configure(text='%s\n'
                                                  '%s\n'
                                                  '%s\n'
                                                  '%s\n'
                                                  '%s\n'
                                                  '%s' %
                                                  (BAR, DWF, PST, CDA, MLB, CPB))
            model_continue_button(vmb_model3, vmb_model_results, 13, 4)
        except ValueError:
            label_inputs_business1.configure(text='Please submit your ')
            label_inputs_business2.configure(text='information correctly')


# Selector: Barriers of entry for the competitors (var3 - BAR)
label_BAR = tk.Label(vmb_model3, text="Barriers of entry \nfor the competitors",
                     font=LARGE_FONT, height=3)
label_BAR.grid(column=1, row=3, columnspan=2, rowspan=2, sticky='nsew')

rb_BAR1 = tk.Radiobutton(vmb_model3, text=keys_BAR[0], variable=rb_BAR, value=0, command=get_BAR)
rb_BAR2 = tk.Radiobutton(vmb_model3, text=keys_BAR[1], variable=rb_BAR, value=1, command=get_BAR)
rb_BAR1.grid(row=3, column=3, sticky='w')
rb_BAR2.grid(row=4, column=3, sticky='w')

# Selector: Difficulty of obtaining work force (var5 - DWF)
label_DWF = tk.Label(vmb_model3, text="Difficulty of\nobtaining\nworkforce",
                     font=LARGE_FONT, height=3)
label_DWF.grid(column=6, row=3, columnspan=2, rowspan=2, sticky='nsew')

rb_DWF1 = tk.Radiobutton(vmb_model3, text=keys_DWF[0], variable=rb_DWF, value=0, command=get_DWF)
rb_DWF2 = tk.Radiobutton(vmb_model3, text=keys_DWF[1], variable=rb_DWF, value=1, command=get_DWF)
rb_DWF3 = tk.Radiobutton(vmb_model3, text=keys_DWF[2], variable=rb_DWF, value=2, command=get_DWF)
rb_DWF1.grid(row=3, column=8, sticky='w')
rb_DWF2.grid(row=4, column=8, sticky='w')
rb_DWF3.grid(row=5, column=8, sticky='w')

# Selector: Pricing strategy (var6 - PST)
label_PST = tk.Label(vmb_model3, text="Pricing\nstrategy",
                     font=LARGE_FONT, height=3)
label_PST.grid(column=0, row=8, columnspan=2, rowspan=2, sticky='nsew')

rb_PST1 = tk.Radiobutton(vmb_model3, text=keys_PST[0], variable=rb_PST, value=0, command=get_PST)
rb_PST2 = tk.Radiobutton(vmb_model3, text=keys_PST[1], variable=rb_PST, value=1, command=get_PST)
rb_PST1.grid(row=8, column=2, sticky='w')
rb_PST2.grid(row=9, column=2, sticky='w')

# Selector: Focus on consumer data (var10 - CDA)
label_CDA = tk.Label(vmb_model3, text="Startup is focused\non consumer data?",
                     font=LARGE_FONT, height=3)
label_CDA.grid(column=3, row=8, columnspan=3, rowspan=2, sticky='nsew')

rb_CDA1 = tk.Radiobutton(vmb_model3, text=keys_CDA[0], variable=rb_CDA, value=0, command=get_CDA)
rb_CDA2 = tk.Radiobutton(vmb_model3, text=keys_CDA[1], variable=rb_CDA, value=1, command=get_CDA)
rb_CDA1.grid(row=8, column=6, sticky='w')
rb_CDA2.grid(row=9, column=6, sticky='w')

# Selector: Machine Learning based business (var12 - MLB)
label_MLB = tk.Label(vmb_model3, text="Is a Machine Learning\nbased business?",
                     font=LARGE_FONT, height=3)
label_MLB.grid(column=7, row=8, columnspan=2, rowspan=2, sticky='nsew')

rb_MLB1 = tk.Radiobutton(vmb_model3, text=keys_MLB[0], variable=rb_MLB, value=0, command=get_MLB)
rb_MLB2 = tk.Radiobutton(vmb_model3, text=keys_MLB[1], variable=rb_MLB, value=1, command=get_MLB)
rb_MLB1.grid(row=8, column=9, sticky='w')
rb_MLB2.grid(row=9, column=9, sticky='w')

# Selector: Cloud or platform based service or product (var7 - CPB)
label_CPB = tk.Label(vmb_model3, text="Is a cloud or platform\nbased service or product?", font=LARGE_FONT, height=3)
label_CPB.grid(column=1, row=10, columnspan=3, sticky='nse')

cb_CPB = ttk.Combobox(vmb_model3, values=keys_CPB, width=30, state='readonly', font=LARGE_FONT)
cb_CPB.grid(column=4, row=10, columnspan=6, sticky='w')
cb_CPB.set('Base')

submit_business = tk.Button(vmb_model3, text="Submit", command=vmb_model_inputs_business)
submit_business.grid(column=4, row=11, columnspan=2)

label_inputs_business1 = tk.Label(vmb_model3, text='', font=LARGE_FONT, justify='right')
label_inputs_business1.grid(column=0, row=12, columnspan=5, sticky='e')

label_inputs_business2 = tk.Label(vmb_model3, text='', font=LARGE_FONT_B, justify='left')
label_inputs_business2.grid(column=5, row=12, columnspan=5, sticky='w')


# -------------------- VMB Model Page Results --------------------
label = tk.Label(vmb_model_results, text="VMB Model", font=('Avenir', 40))
label.grid(row=0, column=0, columnspan=10)

# Buttons:

main_page_button(vmb_model_results, main_page, 1, 0)
dashboard_button(vmb_model_results, dashboard, 1, 4)
interactive_analysis_button(vmb_model_results, interactive_analysis1, 1, 8)
destroyer_button(vmb_model_results, main_page, 12, 12)

title_results = tk.Label(vmb_model_results, text="VMB Model Results", font=('Avenir', 20, 'bold'))
title_results.grid(row=2, column=0, columnspan=10, sticky='nsew')
title_results.config(width=60, height=2)


def charge_inputs():
    sector = cb_input_sector.get()
    subindustry = cb_input_subindustry.get()
    activity = cb_input_activity.get()
    REC = cb_REC.get()
    AYE = keys_AYE[int(rb_AYE.get())]
    BIG = keys_BIG[int(rb_BIG.get())]
    SUR = keys_SUR[int(rb_SUR.get())]
    INC = keys_INC[int(rb_INC.get())]
    CPB = cb_CPB.get()
    BAR = keys_BAR[int(rb_BAR.get())]
    DWF = keys_DWF[int(rb_DWF.get())]
    PST = keys_PST[int(rb_PST.get())]
    CDA = keys_CDA[int(rb_CDA.get())]
    MLB = keys_MLB[int(rb_MLB.get())]

    label_inputs_results1.configure(text='Sector:\n'
                                         'Subindustry:\n'
                                         'Activity:\n'
                                         'Level of experience:\n'
                                         'Experience on Big 5:\n'
                                         'Survived a recession:\n'
                                         'Invested through incubator:\n'
                                         'Number of recognitions:\n'
                                         'Barriers of entry:\n'
                                         'Difficulty of obtaining workforce:\n'
                                         'Pricing strategy:\n'
                                         'Focus on consumer data:\n'
                                         'Machine Learning based:\n'
                                         'Cloud or platform based:')
    label_inputs_results2.configure(text='%s\n'
                                         '%s\n'
                                         '%s\n'
                                         '%s\n'
                                         '%s\n'
                                         '%s\n'
                                         '%s\n'
                                         '%s\n'
                                         '%s\n'
                                         '%s\n'
                                         '%s\n'
                                         '%s\n'
                                         '%s\n'
                                         '%s' %
                                         (sector, subindustry, activity, AYE, BIG, SUR, INC,
                                          REC, BAR, DWF, PST, CDA, MLB, CPB))
    submit_results = tk.Button(vmb_model_results, text="Get\nResults", command=vmb_model, font=LARGE_FONT)
    submit_results.grid(column=1, row=7, columnspan=2, rowspan=2, sticky='news')
    submit_results.config(width=10, height=4)


ending_text = '\n  Thank you for using VMB Venture Capital tool to get our forecast about your startup. The tool was ' \
              'developed by\n ' \
              '  our data scientists to provide what determinants entrepreneurs like you have to focus on to succeed, ' \
              'and to\n' \
              '  convince the policy makers on what they have to work on to make our ecosystem to flourish.\n' \
              '  The model used is Random Forest with a hyper parameter tuning, trained by the CAX_Startup database ' \
              'available\n' \
              '  on Kaggle.\n' \
              '  For more information about the model reliability and validation, please contact the following ' \
              'direction:\n' \
              '  simon.scheidegger@unil.ch or attend to his Advanced Data Analytics class at UNIL every Wednesday ' \
              'from 08:30\n' \
              '  to 12:00 (pre-corona schedule or remotely after-corona).'


def vmb_model():
    IND = Get_Activity_Value(cb_input_activity.get())
    REC = dict_REC.get(cb_REC.get())
    AYE = values_AYE[int(rb_AYE.get())]
    BIG = values_BIG[int(rb_BIG.get())]
    SUR = values_SUR[int(rb_SUR.get())]
    INC = values_INC[int(rb_INC.get())]
    CPB = dict_CPB.get(cb_CPB.get())
    BAR = values_BAR[int(rb_BAR.get())]
    DWF = values_DWF[int(rb_DWF.get())]
    PST = values_PST[int(rb_PST.get())]
    CDA = values_CDA[int(rb_CDA.get())]
    MLB = values_MLB[int(rb_MLB.get())]

    values = [AYE, BIG, BAR, IND, DWF, PST, CPB, REC, SUR, CDA, INC, MLB]
    values = np.reshape(np.array(values), (1, 12))

    forecast_nr, precision = get_classification(values)
    forecast = ''
    if forecast_nr == 0:
        forecast = 'Failed'
    elif forecast_nr == 1:
        forecast = 'Successful'
    label_results1.configure(text='Forecast =\n'
                                  'Precision =')
    label_results2.configure(text='%s\n'
                                  '%.2f%%' % (forecast, (precision * 100)))
    final_label.configure(text=ending_text)


button_charge_inputs = tk.Button(vmb_model_results, text="Charge\nInputs", command=charge_inputs, font=LARGE_FONT)
button_charge_inputs.grid(column=1, row=3, columnspan=2, rowspan=2, sticky='news')
button_charge_inputs.config(width=10, height=4)

label_inputs_results1 = tk.Label(vmb_model_results, text='', font=LARGE_FONT, justify='right')
label_inputs_results1.grid(column=3, row=3, columnspan=4, rowspan=4, sticky='e')

label_inputs_results2 = tk.Label(vmb_model_results, text='', font=LARGE_FONT_B, justify='left')
label_inputs_results2.grid(column=7, row=3, columnspan=4, rowspan=4, sticky='w')

label_results1 = tk.Label(vmb_model_results, text='', font=('Avenir', 20), justify='right')
label_results1.grid(column=3, row=7, columnspan=4, rowspan=4, sticky='e')

label_results2 = tk.Label(vmb_model_results, text='', font=('Avenir', 20, 'bold'), justify='left')
label_results2.grid(column=7, row=7, columnspan=4, rowspan=4, sticky='w')

final_label = tk.Label(vmb_model_results, text='', font=LARGE_FONT, justify='left', anchor='nw')
final_label.grid(row=11, column=0, columnspan=10, sticky='nsew')
final_label.config(width=60, height=9)


raise_frame(main_page)
root.mainloop()

# The end
