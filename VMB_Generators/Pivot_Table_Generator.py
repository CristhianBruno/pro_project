import pandas as pd
import numpy as np


def PT_Sector(data_frame_base, selected_sector):
    """
    Function to create pivot tables based on a selected sector.
    :param data_frame_base: Base Data Frame.
    :param selected_sector: Selection of sector, part of the GSE column of the main data frame.
    :return: Pivot table including:
            Subindustry
            Companies
            Success Rate
            Last Fund. ($MM avg.)
            Seed Investors
            Angel Investors
    """

    df = data_frame_base
    df_sector = df[df['GSE'] == selected_sector]
    pivot_sector1 = pd.pivot_table(df_sector, values='FUN',
                                   index=(['GSU']),
                                   columns=['STA'],
                                   aggfunc=np.nanmean,
                                   fill_value=0)

    pivot_sector1["Last Fund.\n($MM avg.)"] = \
        round((pivot_sector1["Failed"] + pivot_sector1["Success"]) / 1000000, 2)

    pivot_sector2 = pd.pivot_table(df_sector, values='FUN',
                                   index=(['GSU']),
                                   columns=['STA'],
                                   aggfunc=np.count_nonzero,
                                   fill_value=0)

    pivot_sector2["Companies"] = pivot_sector2["Failed"] + pivot_sector2["Success"]
    pivot_sector2["Success Rate"] = \
        round(pivot_sector2["Success"] /
              (pivot_sector2["Failed"] + pivot_sector2["Success"]) * 100, 2)

    pivot_sector3 = pd.pivot_table(df_sector, values='INS',
                                   index=(['GSU']),
                                   columns=['STA'],
                                   aggfunc=np.sum,
                                   fill_value=0)

    pivot_sector3["Seed Investors"] = pivot_sector3["Failed"] + pivot_sector3["Success"]

    pivot_sector4 = pd.pivot_table(df_sector, values='INA',
                                   index=(['GSU']),
                                   columns=['STA'],
                                   aggfunc=np.sum,
                                   fill_value=0)

    pivot_sector4["Angel Investors"] = pivot_sector4["Failed"] + pivot_sector4["Success"]

    pivot_sector5 = pd.pivot_table(df_sector, values='NAD',
                                   index=(['GSU']),
                                   columns=['STA'],
                                   aggfunc=np.sum,
                                   fill_value=0)

    pivot_sector5["Advisors"] = pivot_sector5["Failed"] + pivot_sector5["Success"]

    df_sector_pt = pivot_sector1.drop(columns=['Failed', 'Success'], axis=1)
    df_sector_pt["Companies"] = pivot_sector2["Companies"]
    df_sector_pt["Success\nRate (%)"] = pivot_sector2["Success Rate"]
    df_sector_pt["Seed\nInvestors"] = pivot_sector3["Seed Investors"]
    df_sector_pt["Angel\nInvestors"] = pivot_sector4["Angel Investors"]
    df_sector_pt["Advisors"] = pivot_sector5["Advisors"]
    df_sector_pt = df_sector_pt.reset_index()
    df_sector_pt.columns.name = None
    df_sector_pt = df_sector_pt[["GSU",
                                 "Companies",
                                 "Success\nRate (%)",
                                 "Last Fund.\n($MM avg.)",
                                 "Seed\nInvestors",
                                 "Angel\nInvestors",
                                 "Advisors"]]
    df_sector_pt.rename(columns={"GSU": "Subindustry"}, inplace=True)

    return df_sector_pt


def PT_Main(data_frame_base):
    """
    Function to create pivot table for the main data frame.
    :param data_frame_base: Base Data Frame.
    :return: Pivot table including:
            Subindustry
            Companies
            Success Rate
            Last Fund. ($MM avg.)
            Seed Investors
            Angel Investors
    """

    pivot_1 = pd.pivot_table(data_frame_base,
                             values='FUN',
                             index=(['GSE']),
                             columns=['STA'],
                             aggfunc=np.nanmean,
                             fill_value=0)

    pivot_1["Last Fund.\n($MM avg.)"] = \
        round((pivot_1["Failed"] + pivot_1["Success"]) / 1000000, 2)

    pivot_2 = pd.pivot_table(data_frame_base, values='FUN',
                             index=(['GSE']),
                             columns=['STA'],
                             aggfunc=np.count_nonzero,
                             fill_value=0)

    pivot_2["Companies"] = pivot_2["Failed"] + pivot_2["Success"]
    pivot_2["Success Rate"] = round(pivot_2["Success"] / (pivot_2["Failed"] + pivot_2["Success"]) * 100, 2)

    pivot_3 = pd.pivot_table(data_frame_base, values='INS',
                             index=(['GSE']),
                             columns=['STA'],
                             aggfunc=np.sum,
                             fill_value=0)

    pivot_3["Seed Investors"] = pivot_3["Failed"] + pivot_3["Success"]

    pivot_4 = pd.pivot_table(data_frame_base, values='INA',
                             index=(['GSE']),
                             columns=['STA'],
                             aggfunc=np.sum,
                             fill_value=0)

    pivot_4["Angel Investors"] = pivot_4["Failed"] + pivot_4["Success"]

    pivot_5 = pd.pivot_table(data_frame_base, values='NAD',
                             index=(['GSE']),
                             columns=['STA'],
                             aggfunc=np.sum,
                             fill_value=0)

    pivot_5["Advisors"] = pivot_5["Failed"] + pivot_5["Success"]

    df_main_pt = pivot_1.drop(columns=['Failed', 'Success'], axis=1)
    df_main_pt["Companies"] = pivot_2["Companies"]
    df_main_pt["Success\nRate (%)"] = pivot_2["Success Rate"]
    df_main_pt["Seed\nInvestors"] = pivot_3["Seed Investors"]
    df_main_pt["Angel\nInvestors"] = pivot_4["Angel Investors"]
    df_main_pt["Advisors"] = pivot_5["Advisors"]
    df_main_pt = df_main_pt.reset_index()
    df_main_pt.columns.name = None
    df_main_pt = df_main_pt[["GSE",
                             "Companies",
                             "Success\nRate (%)",
                             "Last Fund.\n($MM avg.)",
                             "Seed\nInvestors",
                             "Angel\nInvestors",
                             "Advisors"]]
    df_main_pt.rename(columns={"GSE": "Sector"}, inplace=True)

    return df_main_pt


def PT_RE_sector(data_frame_base, sector='Real Estate'):
    """
    Function to create pivot tables based on a selected sector.
    :param sector: Sector == Real Estate
    :param data_frame_base: Base Data Frame.
    :return: Pivot table including:
            Subindustry
            Companies
            Success Rate
            Last Fund. ($MM avg.)
            Seed Investors
            Angel Investors
    """

    df = data_frame_base
    df_s_re = df[df['GSE'] == sector]
    pivot_s_re1 = pd.pivot_table(df_s_re, values='FUN',
                                 index=(['GSU']),
                                 columns=['STA'],
                                 aggfunc=np.nanmean,
                                 fill_value=0)

    pivot_s_re1["Last Fund.\n($MM avg.)"] = \
        round(pivot_s_re1["Success"] / 1000000, 2)

    pivot_s_re2 = pd.pivot_table(df_s_re, values='FUN',
                                 index=(['GSU']),
                                 columns=['STA'],
                                 aggfunc=np.count_nonzero,
                                 fill_value=0)

    pivot_s_re2["Companies"] = pivot_s_re2["Success"]
    pivot_s_re2["Success Rate"] = \
        round(pivot_s_re2["Success"] /
              pivot_s_re2["Success"] * 100, 2)

    pivot_s_re3 = pd.pivot_table(df_s_re, values='INS',
                                 index=(['GSU']),
                                 columns=['STA'],
                                 aggfunc=np.sum,
                                 fill_value=0)

    pivot_s_re3["Seed Investors"] = pivot_s_re3["Success"]

    pivot_s_re4 = pd.pivot_table(df_s_re, values='INA',
                                 index=(['GSU']),
                                 columns=['STA'],
                                 aggfunc=np.sum,
                                 fill_value=0)

    pivot_s_re4["Angel Investors"] = pivot_s_re4["Success"]

    pivot_s_re5 = pd.pivot_table(df_s_re, values='NAD',
                                 index=(['GSU']),
                                 columns=['STA'],
                                 aggfunc=np.sum,
                                 fill_value=0)

    pivot_s_re5["Advisors"] = pivot_s_re5["Success"]

    df_s_re_pt = pivot_s_re1.drop(columns=['Success'], axis=1)
    df_s_re_pt["Companies"] = pivot_s_re2["Companies"]
    df_s_re_pt["Success\nRate (%)"] = pivot_s_re2["Success Rate"]
    df_s_re_pt["Seed\nInvestors"] = pivot_s_re3["Seed Investors"]
    df_s_re_pt["Angel\nInvestors"] = pivot_s_re4["Angel Investors"]
    df_s_re_pt["Advisors"] = pivot_s_re5["Advisors"]
    df_s_re_pt = df_s_re_pt.reset_index()
    df_s_re_pt.columns.name = None
    df_s_re_pt = df_s_re_pt[["GSU",
                             "Companies",
                             "Success\nRate (%)",
                             "Last Fund.\n($MM avg.)",
                             "Seed\nInvestors",
                             "Angel\nInvestors",
                             "Advisors"]]
    df_s_re_pt.rename(columns={"GSU": "Subindustry"}, inplace=True)

    return df_s_re_pt

