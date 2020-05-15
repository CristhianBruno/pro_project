import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def Graph_Main(data_frame):
    df = data_frame
    STA_Success = df['STA'].value_counts()[0]
    STA_Failed = df['STA'].value_counts()[1]
    STA_list = [STA_Success, STA_Failed]

    figure_STA = plt.Figure(figsize=(7, 5), dpi=100)
    ax_STA = figure_STA.add_subplot(111)
    labels = ['Success', 'Failed']
    colors = ['#005878', '#63ffb3']
    ax_STA.pie(STA_list, labels=labels, autopct='%1.1f%%',
               shadow=True, startangle=290, pctdistance=1.15, labeldistance=1.35,
               colors=colors, textprops={'fontsize': 12, 'fontname': 'DejaVu Sans'})
    ax_STA.axis('equal')
    ax_STA.set_title("Success Rate of Startups", fontname='DejaVu Sans', fontsize=16, fontweight='bold')
    figure_STA.set_tight_layout('tight')

    return figure_STA


def Graph_Main1(data_frame):
    df = data_frame
    # Graph: Stacked Bar: YOF and STA
    yof_list = np.sort(df['YOF'].drop_duplicates())

    pivot_YOFSTA = pd.pivot_table(df, values='GIG', index='YOF', columns='STA',
                                  aggfunc=np.count_nonzero, fill_value=0)
    N = 15
    ind = np.arange(N)

    year_success = np.asarray(pivot_YOFSTA['Success'])
    year_failed = np.asarray(pivot_YOFSTA['Failed'])
    yof_list = np.asarray(np.delete(yof_list, 15), dtype=int)

    plt.style.use('seaborn')
    figure1 = plt.Figure(figsize=(4, 3), dpi=100)
    ax1 = figure1.add_subplot(111)
    p1 = ax1.bar(ind, year_success)
    p2 = ax1.bar(ind, year_failed, bottom=year_success)

    ax1.set_ylabel('Number of companies', fontname='DejaVu Sans', fontsize=8)
    ax1.legend([p1, p2], ['Success', 'Failed'])
    ax1.set_xticks(range(N))
    ax1.set_xticklabels(yof_list, fontname='DejaVu Sans')
    ax1.tick_params(axis='both', labelsize=6)
    ax1.set_title('Status by Year of Foundation', fontname='DejaVu Sans', fontsize=12, fontweight='bold')
    figure1.set_tight_layout('tight')

    return figure1


def Graph_Main2(data_frame):
    df = data_frame
    COU_countries_total = df['COU'].value_counts().index.tolist()
    COU_values_total = df['COU'].value_counts().tolist()
    COU_countries = COU_countries_total[0:7]
    COU_values = COU_values_total[0:7]
    COU_countries.append('Others')
    COU_values.append(sum(COU_values_total[7:22]))

    figure_COU = plt.Figure(figsize=(4, 3), dpi=100)
    ax_COU = figure_COU.add_subplot(111)
    labels = COU_countries
    colors = ['#005878', '#006f8f', '#0087a2', '#009faf',
              '#00b8b8', '#00d0bb', '#11e8b9', '#63ffb3']
    ax_COU.pie(COU_values, labels=labels, autopct='%1.1f%%',
               shadow=True, startangle=15, pctdistance=1.15, labeldistance=1.35,
               colors=colors, textprops={'fontsize': 8, 'fontname': 'DejaVu Sans'})
    ax_COU.axis('equal')
    ax_COU.set_title("Startups per Country", fontname='DejaVu Sans', fontsize=12, fontweight='bold')
    figure_COU.set_tight_layout('tight')

    return figure_COU


def Graph_Main3(data_frame):
    df = data_frame
    pivot_E10STA = pd.pivot_table(df, values='YOF', index='E10', columns='STA',
                                  aggfunc=np.count_nonzero, fill_value=0, margins=True)
    pivot_E10STA['Total'] = pivot_E10STA['Success'] + pivot_E10STA['Failed']
    pivot_E10STA['Success'] = round(pivot_E10STA['Success'] / pivot_E10STA['Total']*100, 2)
    pivot_E10STA['Failed'] = round(pivot_E10STA['Failed'] / pivot_E10STA['Total']*100, 2)
    pivot_E10STA = pivot_E10STA.iloc[:-1].drop(columns=['All', 'Total'])
    pivot_E10STA = pivot_E10STA.reset_index()
    pivot_E10STA.rename(columns={"E10": "Top"}, inplace=True)
    pivot_E10STA['Top'].replace({1.0: 'Yes', 0.0: 'No'}, inplace=True)
    pivot_E10STA.columns.name = None

    figure_E10 = plt.Figure(figsize=(4, 3), dpi=100)
    ax_E10STA = figure_E10.add_subplot(111)
    pivot_E10STA.plot.barh(x='Top', legend=True, ax=ax_E10STA, rot=90)
    ax_E10STA.set_title('Worked on top companies', fontname='DejaVu Sans', fontsize=12, fontweight='bold')
    ax_E10STA.set_ylabel('', fontdict={'size': 8})
    figure_E10.set_tight_layout('tight')

    return figure_E10


def Graph_Main4(data_frame):
    df = data_frame
    pivot_INCSTA = pd.pivot_table(df, values='YOF', index='INC', columns='STA',
                                  aggfunc=np.count_nonzero, fill_value=0, margins=True)
    pivot_INCSTA['Total'] = pivot_INCSTA['Success'] + pivot_INCSTA['Failed']
    pivot_INCSTA['Success'] = round(pivot_INCSTA['Success'] / pivot_INCSTA['Total']*100, 2)
    pivot_INCSTA['Failed'] = round(pivot_INCSTA['Failed'] / pivot_INCSTA['Total']*100, 2)
    pivot_INCSTA = pivot_INCSTA.iloc[:-1].drop(columns=['All', 'Total'])
    pivot_INCSTA = pivot_INCSTA.reset_index()
    pivot_INCSTA.rename(columns={"INC": "Incubator"}, inplace=True)
    pivot_INCSTA.columns.name = None

    figure_INC = plt.Figure(figsize=(4, 3), dpi=100)
    ax_INCSTA = figure_INC.add_subplot(111)
    pivot_INCSTA.plot.barh(x='Incubator', stacked=True, legend=True, ax=ax_INCSTA, rot=90)
    ax_INCSTA.set_title('Invested through global incubator', fontname='DejaVu Sans', fontsize=11, fontweight='bold')
    ax_INCSTA.set_ylabel('', fontdict={'size': 8})
    figure_INC.set_tight_layout('tight')

    return figure_INC


def Graph_Main5(data_frame):
    df = data_frame
    pivot_AYESTA = pd.pivot_table(df, values='YOF', index='AYE', columns='STA',
                                  aggfunc=np.count_nonzero, fill_value=0, margins=True)
    pivot_AYESTA.sort_values(['Success'], inplace=True)
    pivot_AYESTA['Total'] = pivot_AYESTA['Success'] + pivot_AYESTA['Failed']
    pivot_AYESTA['Failed'] = round(pivot_AYESTA['Failed'] / pivot_AYESTA['Total']*100, 2)
    pivot_AYESTA['Success'] = round(pivot_AYESTA['Success'] / (pivot_AYESTA['Total'])*100, 2)
    pivot_AYESTA['Total'] = pivot_AYESTA['Success'] + pivot_AYESTA['Failed']
    pivot_AYESTA = pivot_AYESTA.iloc[:-1].drop(columns=['All', 'Total'])
    pivot_AYESTA = pivot_AYESTA.reset_index()
    pivot_AYESTA.columns.name = None
    pivot_AYESTA.rename(columns={'AYE': 'Experience'},
                        inplace=True)
    figure_AYE = plt.Figure(figsize=(4, 3), dpi=100)
    ax_AYESTA = figure_AYE.add_subplot(111)
    pivot_AYESTA.plot.barh(x='Experience', stacked=True, legend=True, ax=ax_AYESTA, rot=0)
    ax_AYESTA.set_title('Cofounders Relevant Experience', fontname='DejaVu Sans', fontsize=12, fontweight='bold')
    ax_AYESTA.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc='center',
                     ncol=2, mode="expand", borderaxespad=0)
    figure_AYE.set_tight_layout('tight')

    return figure_AYE


def Graph_Main6(data_frame):
    df = data_frame
    pivot_DWFSTA = pd.pivot_table(df, values='YOF', index='DWF', columns='STA',
                                  aggfunc=np.count_nonzero, fill_value=0, margins=True)
    pivot_DWFSTA.sort_values(['All'], inplace=True)
    pivot_DWFSTA['Total'] = pivot_DWFSTA['Success'] + pivot_DWFSTA['Failed']
    pivot_DWFSTA['Failed'] = round(pivot_DWFSTA['Failed'] / pivot_DWFSTA['Total']*100, 2)
    pivot_DWFSTA['Success'] = round(pivot_DWFSTA['Success'] / (pivot_DWFSTA['Total'])*100, 2)
    pivot_DWFSTA['Total'] = pivot_DWFSTA['Success'] + pivot_DWFSTA['Failed']
    pivot_DWFSTA = pivot_DWFSTA.iloc[:-1].drop(columns=['All', 'Total'])
    pivot_DWFSTA = pivot_DWFSTA.reset_index()
    pivot_DWFSTA.columns.name = None
    pivot_DWFSTA.rename(columns={'DWF': 'Difficulty'},
                        inplace=True)

    figure_DWF = plt.Figure(figsize=(4, 3), dpi=100)
    ax_DWFSTA = figure_DWF.add_subplot(111)
    pivot_DWFSTA.plot.area(x='Difficulty', stacked=True, legend=True, ax=ax_DWFSTA, rot=0)
    ax_DWFSTA.set_title('Difficulty to find workforce (%)', fontname='DejaVu Sans', fontsize=12, fontweight='bold')
    ax_DWFSTA.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc='center',
                     ncol=2, mode="expand", borderaxespad=0)
    figure_DWF.set_tight_layout('tight')

    return figure_DWF


def Graph_Main7(data_frame):
    df = data_frame
    pivot_BARSTA = pd.pivot_table(df, values='YOF', index='BAR', columns='STA',
                                  aggfunc=np.count_nonzero, fill_value=0, margins=True)
    pivot_BARSTA.sort_values(['All'], inplace=True)
    pivot_BARSTA = pivot_BARSTA.iloc[:-1].drop(columns=['All'])
    pivot_BARSTA = pivot_BARSTA.reset_index()
    pivot_BARSTA.columns.name = None
    pivot_BARSTA.rename(columns={'BAR': 'Barriers'},
                        inplace=True)

    no_failed = pivot_BARSTA.iloc[0]['Failed']
    no_success = pivot_BARSTA.iloc[0]['Success']
    yes_failed = pivot_BARSTA.iloc[1]['Failed']
    yes_success = pivot_BARSTA.iloc[1]['Success']
    total = no_failed + no_success + yes_failed + yes_success

    no_f = no_failed / total
    yes_f = yes_failed / total
    no_s = no_success / total
    yes_s = yes_success / total

    # Make data:
    group_names=['Failed', 'Success']
    group_size=[(no_failed + yes_failed), (no_success + yes_success)]
    subgroup_names=['YES', 'NO', 'YES', 'NO']
    subgroup_size=[yes_f, no_f, yes_s, no_s]

    # Create colors:
    a, c = [plt.cm.Blues, plt.cm.Greens]

    # First Ring (outside):
    figure_BAR = plt.Figure(figsize=(4, 3), dpi=100)
    ax_BARSTA = figure_BAR.add_subplot(111)

    ax_BARSTA.axis('equal')
    mypie, _ = ax_BARSTA.pie(group_size, radius=1.3,
                             labels=group_names, colors=[a(0.7), c(0.7)],
                             textprops={'fontsize': 10, 'fontname': 'DejaVu Sans'}, startangle=350)
    plt.setp( mypie, width=0.3, edgecolor='white')

    # Second Ring (Inside):
    mypie2, _ = ax_BARSTA.pie(subgroup_size, radius=1.3-0.3,
                              labels=subgroup_names, labeldistance=0.7, colors=[a(0.6), a(0.3), c(0.6), c(0.3)],
                              textprops={'fontsize': 8, 'fontname': 'DejaVu Sans'}, startangle=350)
    plt.setp(mypie2, width=0.4, edgecolor='white')
    ax_BARSTA.set_title('Barriers to entry to industry by status', fontname='DejaVu Sans', fontsize=11,
                        fontweight='bold')
    figure_BAR.set_tight_layout('tight')

    return figure_BAR


def Graph_Main8(data_frame):
    df = data_frame
    df_FUNINV = df[['FUN', 'INS', 'INA', 'NAD']]
    pivot_FUNINV = pd.pivot_table(df_FUNINV, values=['INS', 'INA', 'NAD'], index='FUN',
                                  aggfunc=np.sum, fill_value=0, margins=True)
    pivot_FUNINV['INV'] = pivot_FUNINV['INS'] + pivot_FUNINV['INA'] + pivot_FUNINV['NAD']
    pivot_FUNINV = pivot_FUNINV.iloc[:-1]
    pivot_FUNINV = pivot_FUNINV.reset_index().drop(columns=['INS', 'INA', 'NAD'])
    pivot_FUNINV.columns.name = None
    pivot_FUNINV['FUN'] = round(pivot_FUNINV['FUN']/1000000, 2)

    figure_INV = plt.Figure(figsize=(4, 3), dpi=100)
    ax_FUNINV = figure_INV.add_subplot(111)
    pivot_FUNINV.plot.scatter(x='FUN', y='INV', ax=ax_FUNINV, c='#005878')
    ax_FUNINV.set_title('Funding per number of\ninvestors and advisors', fontname='DejaVu Sans',
                        fontsize=12, fontweight='bold')
    ax_FUNINV.set_ylabel('Investors and advisors', fontdict={'size': 8, 'fontname': 'DejaVu Sans'})
    ax_FUNINV.set_xlabel('Funding in USD MM.', fontdict={'size': 8, 'fontname': 'DejaVu Sans'})
    figure_INV.set_tight_layout('tight')

    return figure_INV


def Graph_Sector_Pie(data_frame):
    df = data_frame
    # Graph 2: Pie chart by GSE
    pivot_GSESTA = pd.pivot_table(df, values='YOF', index='GSE', columns='STA',
                                  aggfunc=np.count_nonzero, fill_value=0, margins=True)
    pivot_GSESTA = pivot_GSESTA.iloc[:-1].sort_values(by='All')

    figure_sector = plt.Figure(figsize=(7, 5), dpi=100)
    ax_sector = figure_sector.add_subplot(111)
    labels = list(pivot_GSESTA.index)
    colors = ['#f1f1f1', '#63ffb3', '#00e4b7', '#00c8b7', '#00abb0',
              '#008fa3', '#007390', '#005878', '#003f5c']
    ax_sector.pie(pivot_GSESTA['All'], labels=labels, autopct='%1.1f%%',
                  shadow=True, startangle=0, pctdistance=1.15, labeldistance=1.3,
                  colors=colors, textprops={'fontsize': 8})
    ax_sector.set_title('Startups by sector', fontname='DejaVu Sans', fontsize=11, fontweight='bold')
    ax_sector.axis('equal')
    figure_sector.set_tight_layout('tight')

    return figure_sector


def Graph_Sector_Barh(data_frame):
    df = data_frame
    pivot_FUNSTA = pd.pivot_table(df, values='FUN', index='GSE', columns='STA',
                                  aggfunc=np.nanmean, fill_value=0, margins=True)
    pivot_FUNSTA['Total'] = pivot_FUNSTA['Success'] + pivot_FUNSTA['Failed']
    pivot_FUNSTA.sort_values(['Total'], inplace=True)
    pivot_FUNSTA = pivot_FUNSTA.reset_index()
    pivot_FUNSTA['Failed'] = round(pivot_FUNSTA['Failed']/1000000, 2)
    pivot_FUNSTA['Success'] = round(pivot_FUNSTA['Success']/1000000, 2)
    pivot_FUNSTA = pivot_FUNSTA.drop(columns=['All', 'Total'])
    pivot_FUNSTA.rename(columns={'GSE': 'Sector'},
                        inplace=True)
    pivot_FUNSTA['Sector'].replace({'Information Technology': 'Inf. Tech.',
                                    'Consumer Discretionary': 'Consumer D.',
                                    'Communication Services': 'Com. Serv.'}, inplace=True)
    pivot_FUNSTA.columns.name = None

    figure_FUN = plt.Figure(figsize=(7, 4), dpi=100)
    ax_FUNSTA = figure_FUN.add_subplot(111)
    pivot_FUNSTA.plot.barh(x='Sector', stacked=False, subplots=False, legend=True, ax=ax_FUNSTA, rot=45)
    ax_FUNSTA.set_title('Avg. Funding Amount by Sector (USD MM)', fontname='DejaVu Sans', fontsize=11,
                        fontweight='bold')
    ax_FUNSTA.legend(loc='lower right')
    ax_FUNSTA.set_yticklabels(pivot_FUNSTA['Sector'].tolist(), fontdict={'size': 6})
    ax_FUNSTA.set_ylabel('', fontdict={'size': 8})
    figure_FUN.set_tight_layout('tight')

    return figure_FUN


def Graph_Sector_1(data_frame, selected_sector):
    df = data_frame
    df_sector = df[df['GSE'] == selected_sector]
    pivot_FUNGSU = pd.pivot_table(df_sector, values='FUN', index='GSU', columns='STA',
                                  aggfunc=np.nanmean, fill_value=0, margins=True)
    pivot_FUNGSU = pivot_FUNGSU.iloc[:-1]
    pivot_FUNGSU['Total'] = pivot_FUNGSU['Success'] + pivot_FUNGSU['Failed']
    pivot_FUNGSU.sort_values(['Total'], inplace=True)
    pivot_FUNGSU = pivot_FUNGSU.reset_index()
    pivot_FUNGSU['Failed'] = round(pivot_FUNGSU['Failed'] / 1000000, 2)
    pivot_FUNGSU['Success'] = round(pivot_FUNGSU['Success'] / 1000000, 2)
    pivot_FUNGSU = pivot_FUNGSU.drop(columns=['All', 'Total'])
    pivot_FUNGSU.rename(columns={'GSU': 'Subindustry'},
                        inplace=True)
    pivot_FUNGSU.columns.name = None

    figure_FUNGSU = plt.Figure(figsize=(7, 4), dpi=100)
    ax_FUNGSU = figure_FUNGSU.add_subplot(111)
    pivot_FUNGSU.plot.barh(x='Subindustry', stacked=False, subplots=False, legend=True, ax=ax_FUNGSU, rot=45)
    ax_FUNGSU.set_title('Avg. Funding Amount by Subindustry (USD MM)', fontname='DejaVu Sans', fontsize=11,
                        fontweight='bold')
    ax_FUNGSU.legend(loc='lower right')
    ax_FUNGSU.set_yticklabels(pivot_FUNGSU['Subindustry'].tolist(), fontdict={'size': 8})
    ax_FUNGSU.set_ylabel('', fontdict={'size': 8})
    figure_FUNGSU.set_tight_layout('tight')

    return figure_FUNGSU


def Graph_Sector_RE(data_frame, selected_sector):
    df = data_frame
    df_sector = df[df['GSE'] == selected_sector]
    pivot_FUNGSU = pd.pivot_table(df_sector, values='FUN', index='GSU', columns='STA',
                                      aggfunc=np.nanmean, fill_value=0, margins=True)
    pivot_FUNGSU = pivot_FUNGSU.iloc[:-1]
    pivot_FUNGSU = pivot_FUNGSU.reset_index()
    pivot_FUNGSU['Failed'] = round(pivot_FUNGSU['Success'] *0, 2)
    pivot_FUNGSU['Success'] = round(pivot_FUNGSU['Success'] / 1000000, 2)
    pivot_FUNGSU = pivot_FUNGSU.drop(columns=['All'])
    pivot_FUNGSU = pivot_FUNGSU[['GSU', 'Failed', 'Success']]
    pivot_FUNGSU.rename(columns={'GSU': 'Subindustry'},
                        inplace=True)
    pivot_FUNGSU.columns.name = None

    figure_FUNGSU = plt.Figure(figsize=(7, 4), dpi=100)
    ax_FUNGSU = figure_FUNGSU.add_subplot(111)
    pivot_FUNGSU.plot.barh(x='Subindustry', stacked=False, subplots=False, legend=True, ax=ax_FUNGSU, rot=45)
    ax_FUNGSU.set_title('Avg. Funding Amount by Subindustry (USD MM)', fontname='DejaVu Sans', fontsize=11,
                        fontweight='bold')
    ax_FUNGSU.legend(loc='lower right')
    ax_FUNGSU.set_yticklabels(pivot_FUNGSU['Subindustry'].tolist(), fontdict={'size': 8})
    ax_FUNGSU.set_ylabel('', fontdict={'size': 8})
    figure_FUNGSU.set_tight_layout('tight')

    return figure_FUNGSU



